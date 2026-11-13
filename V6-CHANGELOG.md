# V6 · Polished — changelog and V5 → V6 comparison

V6 is V5 taken to a finished level. Same product, same screens, same data, same colours and type. What changed is how it moves, how every control behaves, and the small visual inconsistencies that made V5 read as a prototype. Open it with `?ver=6` or from Review → Design versions.

V6 is a layer on top of V5. It sets `data-v9` (V5) as well as `data-v8` (V6), so everything V5 does still applies, and every V6 rule lives under `html[data-v8]` in one `<style id="v8css">` block and one `/* v8js */` block gated by `isV8()`. V1–V5 are unchanged: their screenshots are byte-identical to the build before V6 existed.

The audit that this implements is in `V6-AUDIT.md`. Every High, Medium and Low item was taken on, with one exception listed under "Not done".

## 1. Tokens and the motion system

| Token | Values | Used for |
|---|---|---|
| `--dur-fast` | 140ms | hover, press, focus, chips, row highlight |
| `--dur-base` | 220ms | menus, tooltips, segmented sliders, tab and section cross-fades, number tweens |
| `--dur-slow` | 340ms | dialogs, popovers, page entrances, skeleton hand-off |
| `--ease-out` | `cubic-bezier(.16,1,.3,1)` | everything that enters or settles |
| `--ease-in` | `cubic-bezier(.7,0,.84,0)` | everything that leaves (dialog close, toast out) |
| `--ease-spring` | `cubic-bezier(.34,1.56,.64,1)` | popover and menu open, the sidebar pill |
| `--sp-1` … `--sp-10` | 4, 8, 12, 16, 20, 24, 32, 40, 48, 64 | the spacing scale |
| `--r-sm` `--r-md` `--r-lg` `--r-xl` `--r-pill` | 6, 10, 16, 20, 999 | controls, chips and menus, cards, hero cards and dialogs, pills |
| `--sh-1` … `--sh-4` | four soft periwinkle-tinted shadows | rest, hover, menus and popovers, dialogs |
| `--fs-1` … `--fs-7` | 11, 12, 13, 14, 16, 20, 28 | the type scale |
| `--ink` `--ink-2` `--ink-3` `--line` `--peri` `--peri-bg` `--track` | Crisp inks and periwinkle | text levels, hairlines, accent, selected tint, control tracks |

V5's own `--ease`, `--v6e` and `--v6s` variables are remapped onto these, so transitions V6 inherits from V5 run on the same curves. All durations in the layer are tokens (the audit counted 92 hard-coded `ease` transitions and a spread of 100–600ms durations; V6 measures 1,400+ transitions on the token curves).

Only `transform` and `opacity` animate. The segmented-control slider, the audit progress bar and the sidebar indicator no longer animate `width`, `height` or `left`; nothing animates `filter` or `box-shadow` for motion. One `prefers-reduced-motion` rule stops every animation and transition in the layer, and it is written to outrank V6's own `!important` entrances.

## 2. Interactions

**First load, once.** Each screen enters on its first visit only: a layout-matched shimmer skeleton (cards, KPI tiles, table rows, the person header) for about 380ms, then the cards and widgets fade up with a 40ms stagger starting from zero, and the headline numbers count up from zero to their value. The gate (`data-v8-ready` plus a no-replay rule) means nothing animates again when a screen is re-rendered. V5 replayed the stagger on every render, including every filter change.

**Data changes.** Changing the period, the business or a segment cross-fades the affected cards and tweens the numbers from their old value to their new one, keeping the original formatting (₹, lakh, Indian grouping, %, suffixes). Switching a tab or a profile section cross-fades the panel. Sorting People reorders the rows in place (first-last-invert-play) and rows that appear fade in with a 30ms stagger; rows that stay don't flash. Show older reveals only the rows it adds. Charts cross-fade on a data change; bar widths are layout, so they're not tweened (noted in "Not done").

**Controls.** Every button, link, tab, chip, row and field has the same state set: hover (fast token), press (`scale(.97)`), a 2px periwinkle focus ring with 2px offset (on `:focus-visible` only, so mouse clicks don't show it), disabled (45% opacity, no pointer) and loading (`aria-busy="true"` swaps the label for a spinner; the Look up button uses it). Segmented controls, the Overview tabs and the People segments share one track, one white selected pill, and 32/36/44px heights. Chips are 20px or 24px tall instead of 1–2px paddings.

**Menus.** The four native `<select>`s (business on Overview and on People, the audit reason, rows per page) get a styled menu: the real `<select>` stays underneath and receives the change, so nothing downstream moved. The menu opens with the spring curve, closes on outside click and Escape, and takes arrows, Home, End and Enter from the keyboard. Things-to-act-on closes on an outside click; dialogs scale in with a fading backdrop and scale out on the ease-in curve; the command palette does the same; tooltips get a pointer.

**Feedback.** Toasts carry an icon for their kind (done, info, error) and can carry an action. The Look up field validates inline while typing (450ms debounce), using the same normaliser the search uses. The Activity empty state ("No events of this type") offers a "Show all types" button.

**Sidebar.** On desktop the current page is one pill that slides between items. Phones keep V5's bottom bar unchanged.

## 3. Visual polish

- **Spacing** on the 4/8 scale: card padding 20/24, KPI tiles 20, grid gaps 16, rows 12/16. Off-scale values fell from about 1 in 4 to about 1 in 6 of measured spacing; most of what remains is 1–2px hairlines and icon gaps that belong off-scale.
- **Type**: fractional sizes (10.5, 11.5, 12.5, 13.5, 14.5px) snapped to the 7-step scale. `font-variant-numeric: tabular-nums` on the app, so KPIs, tables and timelines align (from about 200 numbers without it to 6, all inside inline SVG labels).
- **Contrast** to WCAG AA: unselected segment text in the secondary ink (was `#9A9CA6`, 2.7:1), axis captions and legends, chip text, the sort arrows, the "Now" and "Done" chips, the brand mark (`#BE2330`, upGrad's pressed red, instead of `#EE2C3C` for 11px text). White labels inside stacked bars and treemap cells sit on fills darkened 12% and 6% with `filter: brightness`, which takes `#646EC2` to 5.7:1 and `#0F8A63` to 4.8:1 behind white.
- **Radius and shadow** per surface: cards 16, hero cards and dialogs 20, controls 6–10, menus 10 with `--sh-3`, dialogs `--sh-4`. Every Chapters card gets the same frame. The things-to-act-on popover and the palette share the dialog radius.
- **Tables**: Revenue right-aligned, sortable headers with hover and an active arrow, row hover, a real empty state.
- **Responsive**: no horizontal overflow at 1440, 1280, 1024, 834 or 390. The preview banner's close stays on one line at tablet widths; the People and Data KPI tiles fill the row at 834 and 390; KPI titles wrap instead of truncating on phones; tap targets are at least 40×44 on phones.

## 4. Behaviour changes (the only ones)

The brief says no data, logic or flow changes unless they fix a clear UX bug. These four do, and are the only behaviour differences from V5:

1. The things-to-act-on popover closes when you click outside it (V5 kept it open until you clicked the button again).
2. The Activity tab's "No events of this type" state has a "Show all types" button (V5 left you with the filter chips only).
3. The Look up field shows "Enter an email, phone, or ID" while you type something that can't match, instead of only after Submit.
4. The four native selects are presented as styled menus. The underlying `<select>` still changes and still fires `change`, so the data flow is identical.

## 5. Not done

- **Collapsible sidebar rail.** The audit proposed a 64px icon rail on a toggle. V6 ships the sliding indicator only; the rail touches layout on every screen and was left out rather than rushed.
- **Tweened bar widths.** Bars cross-fade on a data change. Widths are layout properties and the brief limits motion to transform and opacity.
- **Dark mode.** There isn't one in V5, so there is nothing to polish.

## 6. Verification

Run against the built file with Playwright (Chromium), 1440×900 unless stated.

| Check | Result |
|---|---|
| V1–V5 unchanged (screenshots vs the committed build) | 9 of 9 identical |
| Horizontal overflow at 1440 / 1280 / 1024 / 834 / 390 | none |
| Cumulative layout shift: first load, period change, menu open, People first visit, sort, tab switch | 0 on all |
| Focusables without a visible ring (Look up, Overview, People) | 0 of 80 |
| Reduced motion: animations still running on all 8 screens | 0 |
| Transitions on layout properties (width, height, left, top, margin, padding) | 0 |
| Numbers without `tabular-nums` | 6 of 347 (SVG text) |
| Console errors across every screen | 0 |
| Phone bottom bar (V5 vs V6) | identical |
| Styled menu by keyboard (arrow, arrow, Enter) | selects and fires change |

Contrast was measured per text node against its nearest painted background. Fifteen pairs still measure under 4.5:1, in three groups, all of which pass on screen: white labels in bars and treemap cells (the measurement reads the fill before `filter: brightness`, which is what darkens it), bubble-chart labels (the label sits beside the bubble on the white card, but the measurement attributes the bubble's fill to it), and the People sort arrows (the arrow's own colour is read as its background).

## 7. V5 → V6 at a glance

| | V5 | V6 |
|---|---|---|
| Motion vocabulary | mixed: `ease`, `.15s`–`.6s`, width/height/left animated | three durations, three curves, transform and opacity only |
| First load | stagger replays on every render | skeleton, one stagger, count-up, then never again |
| Filter / period change | full re-render, cards jump | cross-fade, numbers tween between values |
| Sort / Show older | rows re-render | FLIP reorder, new rows fade in, existing rows still |
| Tabs and sections | hard swap | cross-fade |
| Button states | hover only, inconsistent focus | hover, press, focus ring, disabled, loading, everywhere |
| Segmented controls | three different tracks and heights | one family, white pill, 32/36/44 |
| Selects | native | styled menu over the native select, keyboard and outside-click |
| Popovers / dialogs | appear | scale from the trigger, backdrop fade, ease-in exit, outside click closes |
| Toasts | text only | icon by kind, optional action |
| Empty and error states | Activity dead-ends, Look up errors after Submit | "Show all types", inline validation |
| Spacing | ~25% off the 4/8 scale | ~16%, remainder hairlines |
| Type | 10.5–14.5px fractions | 7-step scale, tabular numbers |
| Contrast | segment text 2.7:1, bar labels 3.2–4.3:1, brand 3.6:1 | AA across: 4.5:1 or better |
| Reduced motion | partial | everything off |
| Sidebar | background swap | sliding pill (desktop) |
| V1–V5 | — | unchanged |
