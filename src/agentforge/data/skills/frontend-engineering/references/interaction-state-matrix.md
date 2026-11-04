# Frontend interaction state matrix

Use this template for any meaningful page, form, widget, or async operation.

| State | User sees | Available actions | Focus/announcement | Data behavior |
|---|---|---|---|---|
| Initial | | | | |
| Loading | | | | |
| Loaded | | | | |
| Empty | | | | |
| Validation error | | | | |
| Recoverable failure | | | | |
| Terminal failure | | | | |
| Submitting | | | | |
| Success | | | | |
| Refreshing/stale | | | | |
| Offline | | | | |

## Review questions

- Can the user understand what is happening?
- Is the next action clear?
- Can repeated clicks create duplicate mutations?
- Is stale async data prevented from overwriting newer data?
- Is input preserved on recoverable failure?
- Is focus still predictable after a result or error?
- Are statuses available without relying on color?
- Does the layout still work with long text, localization, zoom, and narrow viewports?
