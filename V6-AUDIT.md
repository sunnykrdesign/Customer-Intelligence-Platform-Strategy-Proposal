# V6 audit — V5 taken to a finished level

**Status: for approval.** Nothing below is implemented yet. V6 exists as an exact copy of V5 (`?ver=6`, internal code 8), verified pixel-identical across 24 screen/width pairs with no console errors.

## How V6 is organised

The app is one file; versions are codes inside it, not folders. V6 follows the same convention as V5:

| | V5 | V6 |
|---|---|---|
| URL | `?ver=5` | `?ver=6` |
| Internal code | 9 | 8 (the old V8 was retired and nothing referenced it) |
| `<html>` attributes | `data-v7 data-v9` | `data-v7 data-v9 data-v8` |
| CSS scope | `html[data-v9] …` | `html[data-v8] …` |
| JS check | `isV9()` | `isV8()` (and `isV9()` stays true) |

V6 sets `data-v9` as well, so every V5 rule applies to it. All V6 work goes under `data-v8` / `isV8()`, so V1–V5 can't change. "Shared files" here are the shared CSS/JS blocks; where a V6 refinement needs one, it is overridden under `data-v8`, never edited in place.

**Verification:** V5 vs V6 screenshots of Overview, People, Identity, Data and two people × four tabs, at 1440 and 390: 24 of 24 pairs byte-identical; 0 errors. Switcher, share link (`ver=6`), command palette and localStorage all resolve V6.

## How the audit was done

- Measured V6 at 1440, 1280, 1024, 834 and 390, with and without `prefers-reduced-motion`: overflow, every transition's property, running animations, focus rings, tap targets, text contrast, tabular numerals, and the spacing/radius/shadow/type/easing/duration vocabulary in use.
- Probed behaviour: first load, filter changes, tab and section switches, Show older, sorting, empty states, the command palette, the share dialog, the things-to-act-on popover, toasts, loading.
- Reviewed screenshots by eye at each width.

What's already good and stays: no horizontal overflow at any width; reduced motion stops every animation on every screen; 17 focus-visible rules cover almost everything; the command palette traps focus and closes on Esc/outside click; the share dialog is a native `<dialog>` (focus trap, Esc, outside click all work); `transition: all` is never used; a shimmer skeleton exists for Look up; People has a proper empty state with a clear action; a KPI count-up (`rollIn`) exists.

---

## 1. Motion system

| # | Finding | Rating |
|---|---|---|
| 1.1 | **No motion tokens.** Ten distinct durations in use (.15, .2, .25, .3, .35, .4, .45, .55, .9s…) and five easings; `ease` (symmetric, not ease-out) is the most common at 267 uses. The only tokens are `--ease` and `--v6e`. Durations don't map to fast/base/slow and exits aren't ease-in. | High |
| 1.2 | **Everything replays on every render.** The whole page runs `v6page` (fade + rise + blur) and 36 cards run `rise` with delays stepping 0.9s → 1.26s, not just on first load but again when you switch Prospects → Learners, change the period, change the business, or sort People. Every filter change looks like a page load, and the stagger starts almost a second late. | High |
| 1.3 | **40 keyframe sets, many duplicates.** `rise`/`v6rise`/`a6in`/`v6fade`/`v5fade`/`v6secin` all do "fade up"; `lift`/`lift2`, `wipe`/`v6wipe`, `j6pop`/`v6pop`/`ov8pop`. Each screen animates in a slightly different way. | Medium |
| 1.4 | **Layout properties animate.** Segmented-control sliders (`.slider`) transition `width`; the Identity progress bar transitions `width`; four rules transition `left`, two `max-width`, three `filter` (blur, expensive). Should be transform/opacity only (slider via `scaleX` or translate with measured width set instantly). | Medium |
| 1.5 | **Tab panels switch with no transition** (`#panel` has none), while the Activity panel's children animate in and Insights' don't — inconsistent between tabs. Profile sections fade from 35% (`v6secin`) which reads as a flicker. | Medium |
| 1.6 | **Popover origin is wrong.** Things-to-act-on uses `rise` from a centre origin rather than scaling from its trigger; it does not close on outside click (Esc works). | Medium |
| 1.7 | **Native `<dialog>` has no enter/exit** (share dialog, sign-in): no scale/fade, backdrop appears instantly. | Medium |
| 1.8 | **Count-up only on the Overview headline;** the people/data KPIs, and every number on a period change, just swap. | Low |
| 1.9 | Reduced motion: coverage is complete (0 animations run), but it's 28 scattered `@media` blocks; V6 should hang off one rule plus the motion tokens. | Low |

## 2. Interactions

| # | Finding | Rating |
|---|---|---|
| 2.1 | **Controls mostly have no states.** On Overview, 5 of 37 controls have a press scale (three different values: .95/.96/.97) and only 6 of 37 have any transition at all. Hover colour changes snap. No loading state exists on any button. | High |
| 2.2 | **Skeletons only on Look up.** Overview, People, Identity and Data render in one shot; the Look up skeleton doesn't match the real card layout (72px avatar + 3 bars vs the actual header + facts row + tabs). | High |
| 2.3 | **Sort and filter re-render instead of transitioning.** Sorting People re-runs the rise animation on the rows; Show older appends rows with no reveal; changing the Overview period redraws every chart from zero (full draw-in again) instead of transitioning values. `aria-sort` stays `none` after sorting. | High |
| 2.4 | **Four native `<select>`s** in the app (All businesses on Overview and People, audit Reason, page size, share team): OS-styled popups, no motion, don't match the pill controls next to them. | Medium |
| 2.5 | **Chart tooltips** are a single shared `data-tip` node with no pointer/arrow, no delay, and the same style for every chart; Life-stage bars cut the pointer text at 834. | Medium |
| 2.6 | **Toasts** exist (bottom-centre, 200ms) but have no `role="status"`/`aria-live`, no icon or action (e.g. "Copied" with no undo/open), and stack by replacing. | Medium |
| 2.7 | **Empty states**: People's is good; Activity's "No events of this type for this business." and the Insights "Not computed" lines have no recovery action (clear filter / choose a type). The Look up no-match state should be checked on phone. | Medium |
| 2.8 | **Validation feedback**: the Look up field has no inline error for a malformed email/phone; the sign-in flow shows errors only after submit. | Low |
| 2.9 | **Keyboard**: one focusable without a ring (Look up search input). Sort headers are focusable `div`s with `role=columnheader` but Enter/Space handling should be re-checked after re-render. | Low |
| 2.10 | **Sidebar**: the active item swaps instantly (no sliding indicator), and there's no collapsed state on desktop. | Low |

## 3. Visual polish

| # | Finding | Rating |
|---|---|---|
| 3.1 | **Spacing is off a 4/8 scale in ~600 places.** 12 and 8 dominate (good), but 14px ×88, 10px ×59, 18px ×53, 6px ×93, 5px ×122, 22/26/30px also appear. Visible effects: card headers sit 14px from the top on some cards and 16/20 on others; row paddings vary 10/12/14 between People, Data and Activity lists. | High |
| 3.2 | **Type scale has 20 sizes**, including 10.5, 11.5, 12.5, 13.5 and 14.5px, and four weights. Meta text is set at 11.5, 12 or 12.5 depending on the screen; values at 13/13.5/14. Numbers lack `tabular-nums` in most places (Data 95 of 146, Overview 47 of 98, Activity 23 of 27), so columns of values and dates don't align. | High |
| 3.3 | **Contrast (WCAG AA) — 47 failures at 1440**, in three families: (a) unselected segmented text `#6E7078` on `#ECEEF6` = 4.26 (every "30 days / 12 months / Table / Learners" control); (b) white 11.5px labels inside mid-periwinkle bars = 4.26; (c) the brand mark `upGrad Intelligence` on the lavender sidebar = 3.6/3.9; sort arrows 2.8. Status also relies on colour alone in the Life-stage bars (no labels on slivers). | High |
| 3.4 | **Radius and shadow vocabulary is too wide**: 9 radii in use (3, 4, 6, 8, 10, 12, 14, 16, 22px + pills) and 25 distinct box-shadows. Cards use 16/20/22, inner tiles 10/12/14, chips 6 vs pill. | Medium |
| 3.5 | **Responsive squeezes** (no overflow, but): at 834 the preview banner's close × wraps to a second line; Life-stage bar labels overlap ("12%20%") and slivers have no label; People's KPI mini-bars overlap the "37% of profiles" caption; the five People tiles leave an empty slot (3+2). At 390 the KPI titles truncate with an ellipsis ("90-day conversi…", "Median days to …"). At 1024 the Overview headline tiles get tight. | Medium |
| 3.6 | **Alignment on the person card**: the five fact tiles have uneven content heights ("Known since" carries a second line, Businesses carries two rows), and column widths differ; the section-pager row ("1 of 6 · Personal ›") hangs below very tall sections. | Medium |
| 3.7 | **Hierarchy gaps**: the "Everyone 30" selected segment on People keeps a focus-ring-like outline permanently; the Activity "Details" affordance is an underlined word; the "Today" chapter card has a border the others lack; Chart/Table toggles are 28px tall while the period control next to them is 32. | Medium |
| 3.8 | **Tap targets at 390**: Chart/Table toggles 54×28, period buttons 74×32, P0/P1/T0 pills 37–40px wide, avatar 32px, Details 37px wide. (Height is ≥44 for most; width isn't.) | Medium |
| 3.9 | **Table hierarchy**: People has no hover row state and the Revenue column isn't right-aligned; Data dictionary stacks three filter rows with three pill styles. | Low |
| 3.10 | Dark mode: none exists (only the Ink sidebar). Nothing to polish; not proposing one. | — |

## 4. Tokens

| # | Finding | Rating |
|---|---|---|
| 4.1 | Crisp colour tokens (`--cr-*`) exist but hundreds of rules still hardcode `#15161C`, `#6E7078`, `#E2E3EA`, `#4F57A8`, `#F3F4FB` etc.; shadows, radii, durations and easings have no tokens at all. V6 should add `--r-*`, `--sh-*`, `--dur-*`, `--ease-*`, `--sp-*` under `data-v8` and consolidate the V6 layer onto them. | High |

---

## Proposals (bigger, optional — say which you want)

- **P1 · One control family.** Unify the four pill/segment styles (main tabs, section tabs, period/chart toggles, filter chips) into one segmented control and one chip, with one sliding indicator built on transform. Visual identity unchanged (same periwinkle/white), but one set of sizes (32/36/44), one radius, one state set.
- **P2 · Custom dropdown.** Replace the four native `<select>`s with a styled menu (scale/fade from the trigger, keyboard, Esc/outside click) matching the pills.
- **P3 · Smooth data changes.** On period/business change, keep the cards in place: numbers count to the new value, bars and lines tween (transform/opacity), the insight sentence cross-fades. Draw-in happens once, on first load. Sorting People uses a FLIP reorder instead of re-animating.
- **P4 · Loading layer.** Layout-matched skeletons with shimmer for Overview, People, Data and the person header; button loading states.
- **P5 · Sidebar.** Sliding active indicator and a collapsible rail on desktop (1024–1279 collapses by default).
- **P6 · Toast system.** `role=status`, icon, optional action (Undo / Open), stacking, 3 variants (neutral/success/error) using the existing status colours.

## What I'd implement on approval (no proposals needed)

Everything rated High and Medium in sections 1–4, plus the Lows, as V6-only CSS/JS under `data-v8`:

1. Motion tokens (`--dur-fast 140ms`, `--dur-base 220ms`, `--dur-slow 340ms`; `--ease-out`, `--ease-in`, `--ease-spring`) and one reduced-motion rule; retire the duplicate keyframes for V6; move slider/progress/left/filter transitions to transform/opacity.
2. First-load-only stagger (40ms steps from 0ms, cards and widgets), no replay on filter/sort/tab; tab panels cross-fade; sections fade from 0; popover scales from its trigger and closes on outside click; `<dialog>` enter/exit with backdrop fade.
3. Hover/press (0.97)/focus-visible/disabled/loading for every button and control; row hover on People and Data; `aria-sort` kept in sync.
4. Spacing onto the 4/8 scale, a 7-step type scale (11/12/13/14/16/20/28 with 500/600 only where hierarchy needs it), `tabular-nums` on every number, 4 radii, 4 shadows.
5. Contrast fixes: unselected segment text → `#5F616B` on a slightly lighter track; in-bar labels → 12px semibold with the darker bar shades; brand mark ink; sort arrows; labels on bar slivers via the tooltip/table.
6. Responsive: banner close stays on one line; Life-stage labels hide under 40px width and surface in the tooltip; People tiles 3+2 → 5 in a row at ≥1024 and 2+2+1 centred below; KPI titles wrap instead of truncating; 44px tap targets on phone.

No data, logic or flow changes are planned. One thing I'd flag if approved: closing the things-to-act-on popover on outside click is a small behaviour change (a UX bug fix).
