# Mobile engineering rules

- Treat Android and iOS as distinct environments; verify platform support, lifecycle, permissions, storage, and release constraints separately.
- Handle foreground, background, process termination, restoration, and interrupted network operations.
- Do not assume background execution or push delivery is guaranteed.
- Store credentials in platform-protected secure storage; never in plain preferences, URLs, logs, or analytics.
- Request permissions at the moment of need and handle denial, restriction, and revocation.
- Use deep links and notification payloads as untrusted input; validate parameters and fetch authoritative server state.
- Retry mutations only with idempotency/deduplication; distinguish queued offline work from server-confirmed completion.
- Support dynamic text, screen readers, keyboard/external input where relevant, safe areas, orientation, and reduced motion.
- Test minimum supported and current OS versions, representative device classes, poor connectivity, account switching, and upgrade paths.
- Never commit signing keys, provisioning secrets, or production user data.
