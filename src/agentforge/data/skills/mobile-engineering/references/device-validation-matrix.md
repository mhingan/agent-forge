# Mobile device validation matrix

Use representative device/OS coverage rather than assuming one emulator represents the platform.

| Dimension | Minimum coverage | Result/notes |
|---|---|---|
| OS | Minimum supported and current supported versions | |
| Device class | Small/low-memory, mainstream, large/tablet/foldable if supported | |
| Orientation | Portrait and landscape if supported | |
| Text | Default and large/dynamic text | |
| Appearance | Light/dark and high-contrast where available | |
| Input | Touch, keyboard, external input where relevant | |
| Lifecycle | Foreground/background/termination/restore | |
| Network | Wi-Fi, cellular, slow, offline, reconnect | |
| Permissions | Grant, deny, later revoke, restricted | |
| Navigation | Back gesture/button, deep link, notification route | |
| Accessibility | Screen reader, focus order, labels, reduced motion | |
| Upgrade | Fresh install, upgrade with local data, logout/account switch | |
| Release | Debug/release flavor, signing, production config | |

## Evidence
Record device model, OS, build number, test scenario, expected/actual, screenshot/log reference, and defect ID. Never include tokens or private account data in evidence.
