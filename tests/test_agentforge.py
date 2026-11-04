from __future__ import annotations

import json
import sys
import tempfile
import unittest
try:
    import tomllib  # Python 3.11+
except ImportError:  # pragma: no cover - exercised by the Python 3.10 CI job
    tomllib = None
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))

from agentforge.adapters import render_agent  # noqa: E402
from agentforge.core import install, uninstall, validate_repository, _parse_agents  # noqa: E402


class ValidationTests(unittest.TestCase):
    def test_repository_validates(self):
        self.assertEqual(validate_repository(REPO, strict=True), [])

    def test_every_skill_has_metadata(self):
        skills = sorted((REPO / "skills").glob("*/SKILL.md"))
        self.assertGreaterEqual(len(skills), 10)
        for skill in skills:
            text = skill.read_text(encoding="utf-8")
            self.assertTrue(text.startswith("---\n"), skill)
            self.assertIn("name:", text.split("---", 2)[1], skill)
            self.assertIn("description:", text.split("---", 2)[1], skill)


class AdapterTests(unittest.TestCase):
    def test_renders_all_native_agent_formats(self):
        source = REPO / "agents" / "code-reviewer.md"
        expected = {
            "claude": "code-reviewer.md",
            "codex": "code-reviewer.toml",
            "copilot": "code-reviewer.agent.md",
            "gemini": "code-reviewer.md",
            "antigravity": "code-reviewer.md",
            "antigravity-cli": "code-reviewer.md",
        }
        for target, filename in expected.items():
            with self.subTest(target=target):
                actual_name, content = render_agent(target, source)
                self.assertEqual(actual_name, filename)
                self.assertIn("review", content.lower())
                self.assertTrue(content.strip())
                if target == "codex":
                    if tomllib is not None:
                        parsed = tomllib.loads(content)
                        self.assertEqual(parsed["name"], "code-reviewer")
                        self.assertIn("developer_instructions", parsed)
                    else:
                        self.assertIn('name = "code-reviewer"', content)
                        self.assertIn("developer_instructions =", content)


class InstallTests(unittest.TestCase):
    def test_empty_agent_selection_is_a_clean_error(self):
        with self.assertRaisesRegex(ValueError, "Select at least one target"):
            _parse_agents("")

    def test_shared_skills_install_once_and_tracks_both_targets(self):
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp)
            messages = install(
                root=destination,
                agent_arg="codex,gemini,antigravity",
                scope="project",
                skills=["code-review"],
                components=["skills"],
                destination=destination,
            )
            skill_path = destination / ".agents" / "skills" / "code-review" / "SKILL.md"
            self.assertTrue(skill_path.is_file())
            manifest = json.loads((destination / ".agentforge" / "install-manifest.json").read_text())
            references = [x for x in manifest["installations"] if x["path"].endswith(".agents/skills/code-review")]
            self.assertEqual({x["target"] for x in references}, {"codex", "gemini", "antigravity"})

    def test_uninstall_preserves_modified_content(self):
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp)
            install(
                root=destination,
                agent_arg="claude",
                scope="project",
                skills=["code-review"],
                components=["skills"],
                destination=destination,
            )
            skill_path = destination / ".claude" / "skills" / "code-review" / "SKILL.md"
            skill_path.write_text(skill_path.read_text() + "\n# Local customization\n")
            messages = uninstall(agent_arg="claude", scope="project", destination=destination)
            self.assertTrue(skill_path.exists())
            self.assertTrue(any("KEEP modified path" in message for message in messages))

    def test_uninstall_selected_skill_leaves_other_components(self):
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp)
            install(
                root=destination,
                agent_arg="claude",
                scope="project",
                skills=["code-review", "debugging"],
                components=["skills", "agents", "rules", "workflows"],
                destination=destination,
            )
            uninstall(agent_arg="claude", scope="project", skills=["code-review"], destination=destination)
            self.assertFalse((destination / ".claude/skills/code-review").exists())
            self.assertTrue((destination / ".claude/skills/debugging/SKILL.md").exists())
            self.assertTrue((destination / ".claude/agents/code-reviewer.md").exists())
            self.assertTrue((destination / ".agentforge/rules/universal.md").exists())

    def test_full_project_install_generates_native_layouts(self):
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp)
            install(
                root=destination,
                agent_arg="all",
                scope="project",
                components=["skills", "agents", "rules", "workflows"],
                destination=destination,
            )
            self.assertTrue((destination / ".claude/skills/backend-engineering/SKILL.md").exists())
            self.assertTrue((destination / ".agents/skills/backend-engineering/SKILL.md").exists())
            self.assertTrue((destination / ".github/skills/backend-engineering/SKILL.md").exists())
            self.assertTrue((destination / ".claude/agents/architect.md").exists())
            self.assertTrue((destination / ".codex/agents/architect.toml").exists())
            self.assertTrue((destination / ".github/agents/architect.agent.md").exists())
            self.assertIn("tools:", (destination / ".claude/agents/code-reviewer.md").read_text())
            self.assertIn("read, search", (destination / ".github/agents/code-reviewer.agent.md").read_text())
            self.assertTrue((destination / ".gemini/agents/architect.md").exists())
            antigravity_agent = destination / ".agents/agents/architect.md"
            self.assertTrue(antigravity_agent.exists())
            self.assertIn("subagent: true", antigravity_agent.read_text())
            antigravity_rule = destination / ".agents/rules/security.md"
            self.assertTrue(antigravity_rule.exists())
            self.assertIn("trigger: always_on", antigravity_rule.read_text())
            self.assertTrue((destination / "AGENTS.md").exists())
            self.assertTrue((destination / "CLAUDE.md").exists())
            self.assertTrue((destination / "GEMINI.md").exists())
            self.assertTrue((destination / ".github/copilot-instructions.md").exists())
            self.assertTrue((destination / ".agentforge/workflows/feature-development.md").exists())

    def test_does_not_overwrite_unmanaged_destination(self):
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp)
            preexisting = destination / ".claude" / "skills" / "code-review"
            preexisting.mkdir(parents=True)
            (preexisting / "SKILL.md").write_text("user-owned\n")
            install(
                root=destination,
                agent_arg="claude",
                scope="project",
                skills=["code-review"],
                components=["skills"],
                destination=destination,
                force=True,
            )
            self.assertEqual((preexisting / "SKILL.md").read_text(), "user-owned\n")


if __name__ == "__main__":
    unittest.main()
