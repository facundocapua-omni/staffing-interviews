# Candidate Take-Home Review — "Recent Orders & Reorder" Widget

**Candidate:** Jhon Garces Montes
**Scaffold:** `0ea560c` (Initial commit) → **Submission:** `2a3d8ee` ("solution to challenge")
**Verified via:** full read of all 22 changed/added files, `tsc --noEmit`, `next build`, `jest` (12/12 pass), and live manual testing in a real browser (Playwright) — including waiting out two full 90s access-token TTLs to force a real expiry/refresh cycle.

## What's done well

- **State boundary is correct and well-argued.** React Query owns server state (promo content, paginated orders); Redux Toolkit owns only the cart. `ARCHITECTURE.md:5-15` explains this crisply, and the code matches the claim exactly — [store.ts](../src/store/store.ts) only registers `cart`, nothing server-derived leaks into Redux.
- **Auth layer is genuinely solid.** [authClient.ts](../src/features/auth/authClient.ts) proactively refreshes 5s before expiry, reactively recovers from a 401 with request de-duplication (`sessionRequest` singleton) so a burst of concurrent requests only triggers one refresh call, and avoids double-rotating the refresh token (`recoverFromUnauthorized`, line 72-77). I verified this isn't just well-tested in isolation — I loaded `/account` in a browser, waited >180s (two full TTLs), and clicked "Load more": the request succeeded with zero console errors, confirming the refresh is transparent to the UI exactly as claimed.
- **Data normalization is thorough and defensive**, not just for the two documented edge cases but genuinely for "whatever you find": unknown statuses, dual date formats with impossible-date rejection (`02/30/2026` → null, verified via test and code trace at [ordersApi.ts:39-65](../src/features/orders/ordersApi.ts#L39-L65)), null/partial item arrays, and total recomputation when the server total is missing/invalid.
- **Partial-page failure handling matches the brief precisely.** I drove this live: loading page 3 (the deliberate 500) leaves pages 1-2 fully intact, surfaces an inline retryable alert, and a subsequent click recovers page 3 without ever blanking the widget.
- **Cart merge logic is correct**: reordering the same order twice sums quantities, reordering a different order appends rather than replaces, and it's a defensive copy (verified in [cartSlice.test.ts](../src/features/cart/cartSlice.test.ts) and live in-browser: staged 2 orders → "3 items staged, $18.25 from 2 orders").
- **Accessibility is genuinely considered**, not bolted on: `aria-live` announcements on reorder, `aria-describedby` linking disabled-reorder buttons to their reason text, `role="alert"` on error states, UTC-pinned date formatting, focus-visible outlines in `globals.css`.
- **Tests target real risk, not padding** — auth race/dedup, date/status/item normalization, cart merge, partial-page failure — and `ARCHITECTURE.md` explicitly states what was skipped (route-handler fixtures, visual) and why. This is exactly the judgment the brief asked for in requirement 7.

## Findings

### 1. CTA URL sanitizer has a real bypass — the claimed protection doesn't fully hold (confirmed)

`ARCHITECTURE.md:32-33` claims: *"AEM-authored CTA links are restricted to internal paths and `https://`, so authored content can't inject a `javascript:` URL."* The implementation in [contentApi.ts:39-44](../src/features/content/contentApi.ts#L39-L44):

```js
const isInternalPath = url.startsWith("/") && !url.startsWith("//");
return isInternalPath || url.startsWith("https://") ? url : "/rewards";
```

This does block `javascript:` and bare `//protocol-relative.com`. But it does **not** block a single leading backslash. I reproduced this live: with `ctaUrl = "/\\evil.example.com/phish"`, the sanitizer classifies it as an internal path (starts with `/`, not `//`) and passes it through unchanged. I then rendered that exact string as an `<a href>` in a live browser page (via Playwright's `browser_evaluate`, not just Node) and confirmed the resolved link is `http://evil.example.com/phish` — because browsers normalize backslashes to forward slashes for special schemes per the WHATWG URL spec, so `/\evil.example.com` *is* `//evil.example.com` by the time it's a real link.

**Scenario:** an AEM content author (or anyone who can write to that content-fragment field) sets the CTA URL to `/\attacker.example/phish`; guests clicking "See rewards" land on an attacker-controlled origin, not `/rewards`.

**Coverage gap that let it through:** the candidate's own test ([contentApi.test.ts:11](../src/features/content/contentApi.test.ts#L11)) does test a bypass attempt (`"//untrusted.example/offer"`) and correctly asserts it falls back — but that's the one case the `!startsWith("//")` check already catches. The test never exercises the backslash variant, so the sanitizer's incompleteness never surfaced. This is a good example of testing "a" bypass without testing "the" bypass space.

**Severity:** low-likelihood in this exercise's scope (needs a malicious/compromised content author), but it's precisely the class of bug the brief flagged as high-value to get right, and the write-up asserts protection that isn't actually complete.

### 2. Minor: fallback order-id derivation isn't globally unique across pages (theoretical)

[ordersApi.ts:145](../src/features/orders/ordersApi.ts#L145) computes a synthetic id via `(page - 1) * values.length + index` when the API omits an order id. Since `values.length` is the *current page's* size rather than a fixed page size, this can produce colliding synthetic ids across pages of different lengths (e.g., a short last page). Only affects React list `key`s / dedup in the pathological case of multiple id-less orders across pages — never triggered by the mock data, and not something I could observe going wrong in practice. Flagging as theoretical, not a real defect at current scope.

## Minor notes

- `ARCHITECTURE.md` is 64 lines against the brief's requested 10-15 — the content is genuinely useful and not padded, but it noticeably overshoots the stated deliverable constraint.
- The "can't reorder" screen-reader reason text ("item details are unavailable") is reused verbatim for a legitimately empty order (0 valid items but not literally `null`) — slightly inaccurate wording, not a functional bug.
- `authClient.test.ts` covers the concurrent-401 recovery path well but doesn't separately exercise the proactive 5s-buffer refresh path (I verified that path myself live in-browser instead).
- No ESLint config exists in either the scaffold or the submission — inherited from the scaffold, not a candidate gap.

## Requirements checklist (against TASK.md)

| # | Requirement | Status | Evidence |
|---|---|---|---|
| 1 | Fetch/render AEM promo banner | Done | [contentApi.ts](../src/features/content/contentApi.ts), `PromoBanner` in [AccountDashboard.tsx](../src/features/account/AccountDashboard.tsx) |
| 2 | Fetch/render order history, most recent first | Done | [ordersApi.ts](../src/features/orders/ordersApi.ts) `fetchOrdersPage` + `newestFirst` |
| 3 | Handle malformed/undocumented data gracefully | Done | `normalizeOrder`, `normalizeStatus`, `parseOrderDate`, `normalizeItem` |
| 4 | "Reorder" stages items into app-wide cart | Done | [cartSlice.ts](../src/features/cart/cartSlice.ts) |
| 5 | State-boundary decision + rationale | Done | `ARCHITECTURE.md` §"Where state lives" |
| 6 | Auth: token issuance + refresh survives UI | Done (verified live) | [authClient.ts](../src/features/auth/authClient.ts) |
| 7 | Tests for highest-risk parts + rationale for skips | Done | 5 test files + `ARCHITECTURE.md` §"Tests" |
| 8 | Accessibility + loading/error states | Done | aria-live, aria-describedby, skeletons, retryable errors |

Nothing in scope was skipped. "Not evaluated" items (pixel-perfect design, full coverage, checkout) were correctly left alone.

## Conclusion

This is a strong submission. The state-boundary reasoning, the auth/refresh coordination, and the messy-data normalization are all handled with a level of care — and correctly matched between the write-up and the code — that's uncommon in a 4-hour exercise. The one real finding (the CTA sanitizer bypass) is a legitimate, reproducible security gap, but it's notable more for what it reveals about test-completeness discipline (testing *a* bypass vs. reasoning about the bypass space) than as evidence of weak engineering overall — everything else claimed in the architecture doc, I was able to independently reproduce.

**Suggested follow-up interview questions:**
1. Walk me through `safeCtaUrl`. What's it trying to prevent, and can you think of any string that passes the `isInternalPath` check but wouldn't actually stay on-site once rendered in an `<a href>`?
2. Your architecture doc mentions de-duplicating concurrent refreshes. What would happen if a component called `authenticatedFetch` for a *third* request while the first refresh from a 401 was already in flight, and that request happened to come in with an access token that was already replaced by a still-earlier refresh?
3. `ARCHITECTURE.md` was longer than the brief's 10-15 line guidance — was that a deliberate trade-off under the time box, and what would you have cut to hit the target?
