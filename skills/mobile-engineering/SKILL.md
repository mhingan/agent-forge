---
name: mobile-engineering
description: Design, implement, test, and release cross-platform or native mobile applications, including Flutter and React Native. Use for mobile UI, app lifecycle, offline behavior, navigation, permissions, push notifications, performance, and store readiness.
license: MIT
---

# Mobile application engineering

## Mission

Deliver mobile applications that behave correctly across devices, operating systems, network conditions, app lifecycle transitions, and accessibility settings. A mobile feature is not complete merely because it works in one emulator session.

## 1. Discover target platforms

Establish:
- Framework/runtime and supported versions.
- Android/iOS minimum and target OS versions.
- Device classes, screen sizes, orientation, foldables/tablets, and hardware requirements.
- Navigation model, deep links, universal/app links, notifications, and authentication flow.
- Offline expectations, data synchronization, background execution, and storage constraints.
- Permission requirements, privacy disclosures, analytics, crash reporting, and release process.
- Existing app architecture, design system, state management, networking, and tests.

Inspect project manifests, build configuration, signing setup, environment files, and native platform folders. Do not assume the same capability is available on iOS and Android.

## 2. App architecture and lifecycle

Separate presentation, domain/use-case logic, persistence, and platform services. Keep UI state explicit and avoid coupling business logic to widget lifecycle or platform-specific APIs.

Handle lifecycle transitions: foreground, background, inactive, resumed, process termination, and restoration. Persist only the minimum state required to restore a useful experience. Do not assume background work can run indefinitely.

For Flutter, follow established widget/state conventions, dispose controllers/subscriptions, isolate platform channels behind services, and keep expensive computation off the UI isolate when necessary. For React Native, understand the JS/native boundary, navigation lifecycle, and native module constraints. For native apps, use platform lifecycle and concurrency patterns.

## 3. Navigation and interaction

Define route ownership, back behavior, deep-link parsing, authentication gates, and restoration. Validate deep-link parameters and require authorization at the backend. Make navigation usable with system back gestures and assistive technologies.

Design for safe areas, keyboard appearance, large text, screen rotation, different pixel densities, and system appearance. Use touch targets and spacing appropriate to mobile. Avoid fixed dimensions that clip on small screens.

## 4. Networking and offline behavior

Use explicit request timeouts, cancellation, bounded retry, and idempotency for mutations. Handle flaky connectivity, captive portals, DNS failures, server errors, and slow responses. Communicate offline/stale state clearly.

If offline-first behavior is required, define:
- Local source of truth and sync direction.
- Conflict resolution and merge rules.
- Queueing and replay of pending mutations.
- Idempotency and deduplication.
- Encryption and local retention.
- Behavior on logout, account switch, and device sharing.
- Recovery after app termination during sync.

Never silently treat a queued offline action as confirmed by the server.

## 5. Secure storage and permissions

Store secrets and sensitive credentials using platform-protected storage. Do not store auth tokens in plain preferences, logs, crash breadcrumbs, URLs, or analytics. Encrypt sensitive local data when required and define logout/device reset deletion behavior.

Request permissions at the moment they are needed, explain the user benefit, handle denial/revocation, and provide a useful fallback. Do not request broad permissions preemptively. Handle camera, location, contacts, notifications, files, and biometrics under least privilege and platform policy.

## 6. Push and background tasks

Assume push notifications can be delayed, duplicated, collapsed, or absent. Treat notifications as hints to refresh authoritative server state, not as guaranteed transaction delivery. Define token registration, rotation, logout cleanup, notification routing, user preference, and privacy-safe payload content.

Background tasks must respect platform scheduling and execution limits. Persist checkpoints and make tasks idempotent. Do not rely on permanent background execution for critical business logic.

## 7. Performance, battery, and resource use

Measure cold/warm launch, frame time, memory, network, battery, startup dependencies, image decoding, and list rendering. Avoid repeated polling when push or bounded refresh is more appropriate. Cache with explicit freshness/invalidation rules. Release resources and subscriptions. Test on representative low-end devices, not only flagship hardware.

## 8. Accessibility and localization

Support dynamic type/font scaling, screen readers, semantic labels, focus order, contrast, reduced motion, right-to-left layout where applicable, and large touch targets. Avoid embedding text in images. Use localization resources for all user-facing text, dates, numbers, and currency; never construct localized strings by concatenating fragments.

## 9. Testing matrix

Cover:
- Supported OS versions and device sizes.
- Fresh install, upgrade, logout, account switch, and process restore.
- Offline/online transitions and interrupted requests.
- Permission grant, denial, later revocation, and restricted settings.
- Deep links, notifications, and navigation/back behavior.
- Keyboard, large text, screen reader, dark/light mode, and orientation.
- Low memory, background/foreground, and battery constraints.
- Release signing, build flavors, and production configuration.

Use unit/widget/component tests for logic and UI, integration tests for platform bridges, and end-to-end tests for critical journeys. Keep real store submission separate from local build verification.

## 10. Release readiness

Verify application ID/bundle ID, version/build number, signing identity, provisioning, target API/SDK, privacy manifests/disclosures, permissions, store screenshots/metadata, crash-free baseline, staged rollout, and rollback path. Never commit signing keys or provisioning secrets.

## Definition of done

The feature works across required devices/platforms, handles lifecycle and network failure, enforces server-side authorization, manages permissions safely, is accessible, has meaningful tests, and has documented release implications.

## Completion report

State platforms/devices tested, build configuration, lifecycle/offline cases, accessibility checks, tests, signing/release status, and unverified device-specific behavior.
