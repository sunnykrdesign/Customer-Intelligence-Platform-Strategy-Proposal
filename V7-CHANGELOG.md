# V7 · Atmosphere — changelog and V6 → V7 comparison

V7 is V6's content in a new look. Every screen, number, label and flow is the one V6 shows; what changed is the surface it sits on and the way it moves. Open it with `?ver=7` or from Review → Design versions.

Like V6, V7 is a layer: it sets V5's and V6's flags as well as its own (`data-v10`), so everything they do still applies, and every V7 rule lives under `html[data-v10]` in one `<style id="v10css">` block and one `/* v10js */` block gated by `isV10()`. V1–V6 are unchanged: their screenshots are byte-identical to the build before V7 existed.

The references were the shared dashboard video (coloured figure tiles, pill tabs, charts that draw in, a floating frame on a gradient) and five Figma frames (a frosted "Tickets" layout with an icon rail, Iconly's gradient chart card and pill bottom bar with filled active icons, Intellecta's floating round rail buttons on a lavender gradient, and a soft feature-card grid).

## 1. The look

- **Atmosphere.** The page is a still, soft periwinkle → lavender → peach gradient seen through a frosted white layer (78% white, 40px blur). Nothing in it moves: an earlier draft drifted three blurred blobs and leaned the backdrop with the pointer, which read as jitter behind the data and was removed. The app is full-bleed on every width (an earlier draft floated it in a rounded frame; that was dropped for desktop).
- **The sidebar.** It reads as its own panel: a hairline edge and a soft shadow separate it from the content, whatever the shade. Two layouts, chosen in Review → V7 sidebar layout or with the chevron on the sidebar's edge, remembered per browser. **Expanded** (the default, 276px): the upGrad Intelligence wordmark, a full-width search pill, five rows of a 40px icon circle plus a 14px label, the current page as a white row with a filled periwinkle icon, the audit count as a rose badge at the row's end, and the user's name and team at the bottom. **Rail** (104px): the red upGrad mark, a round search button and five round white icon buttons; the current page is a filled periwinkle circle with a white duotone icon; the audit count sits on the icon's corner; labels, the search shortcut and the user's name stay as tooltips and accessible names. Tablets (821–1100px) always use the rail; phones keep a floating frosted pill bar with the same filled active icon. Four shades, chosen in Review → V7 sidebar shade (the row V4 used for its sidebar; every option now does something in V7): **Frosted** (default: white glass with a hairline, soft periwinkle current row), **Tinted** (solid periwinkle panel, white controls and current row), **Dark** (deep indigo, light text, the current icon glows periwinkle) and **Ink** (near-black, grey text, a white bar marks the current page). The dark shades keep a white keyboard focus ring.
- **Type.** Headlines in Figtree at 38px (30px on phones), tight tracking; section titles 24px; figures 34px with tabular numbers (inherited from V6).
- **Figure tiles.** On Overview, People and Data dictionary the first tile is solid periwinkle, the second soft periwinkle, the third coral, the rest white; the fifth People/Data tile is ink. Gradients run dark → light from the top-left corner so the labels sit on the darker end. Icons, deltas and sparklines inside coloured tiles turn white. Tiles lift on hover.
- **Surfaces.** Cards lose their borders and get 24px corners and one soft, periwinkle-tinted shadow; inner tiles (summary figures, chapter cards, insight tiles) sit on a pale well. The Directory card gets its own padding; the audit hero on UG learning journey is a navy gradient with white stat tiles; the Look up head card is frosted glass on a soft gradient cover; the sticky bands behind the Look up search and section chips are frosted glass rather than the page colour.
- **Controls.** Segmented controls and chips share one family: a pale track, pills, and a black pill for the selected state (the sliding pill in the People, Activity and Data controls is black too). The profile tabs become text tabs with a rose underline that slides. Primary buttons are black pills with a soft highlight that follows the pointer. Secondary buttons, the search fields, the styled menus and the Key button are white pills with a soft shadow. Menus open as rounded white sheets; tooltips are black bubbles with larger corners.
- **Charts.** Stacked-bar segments and horizontal bars get 10px corners and a 3px gap; treemap cells 16px; bubbles a white ring; sparklines in coloured tiles are white.
- **Tables and lists.** Column headers are small caps; rows get 16px corners and a pale hover; avatars are 40px squircles; activity icons 40px tiles.

## 2. Motion

- **Entrance, once per screen.** V6's skeleton stays. When a screen first appears, its cards spring up (26px rise with a slight scale, 850ms, soft spring curve, 70ms stagger), bars grow from their baseline (scaleX or scaleY only), sparklines, trend lines and rings draw themselves along their length (Web Animations on `stroke-dashoffset`), and the headline numbers count up (V6). None of it replays on a re-render: V6's no-replay gate still applies.
- **Navigation.** The rail's active icon pops in with a spring when the route changes; a page revisit slides up and fades in over 400ms.
- **Tabs.** When a Look up tab opens for the first time, the charts and bars in that panel draw in the same way.
- **Backdrop.** Still. (The drift and pointer lean from the first draft are gone.)
- **Reduced motion.** V6's rule stops every animation and transition in the layer; V7's JavaScript checks the same preference before drawing charts in or moving the backdrop.

## 3. Review notes (second pass)

- Desktop is full-bleed: the rounded floating frame was removed; the atmosphere stays behind a frosted layer.
- The sidebar has an expanded mode (default) and a rail, with a chevron on its edge and a Review → V7 sidebar option, so the labels are readable at 14px.
- The wordmark is back as "upGrad Intelligence" in the expanded sidebar; the rail shows only the red mark.
- The Activity feed's "Details" buttons and "Show older" are quiet white pills; only primary actions are black.
- The Data dictionary groups inside "All items" get a hairline frame so they read as groups on the white card.
- The Credentials card no longer has a gap under its title.

## 3b. Review notes (third pass, with motion on)

The earlier passes were checked with motion off, which hid two of these. Everything below was reproduced in the browser before and after the fix.

- **People figure tiles showed a stack of digits** ("0123456789…"): V6's count-up was also feeding the odometer tiles, which animate themselves. The count-up now leaves odometers alone (a V6 change; V6 looked right only because its odometers were 28px and the stack never broke out of the tile).
- **A second focus ring inside the search pills** (People filter, Look up field): the inner input's own ring is gone; the pill shows one ring.
- **Rows showing through the stuck chip bar** on Look up: the three sticky bands (search, head, section chips) are 94% white with a blur and extend to the main column's edges, so scrolling content passes under them.
- **The 12-month figure ran under its delta chip** ("13,83,163 ↑4.2%"): V5 reuses the `.kv` class for the Data dictionary's two-column rows, which turned the Overview figure into a 120px grid. V7 makes it a plain block, so a long figure wraps the chip beneath it. (Latent in V5 and V6, visible there only on the longest figures.)
- **The People table overlapped its own columns** at 1280 with the expanded sidebar and at 1024 with the rail (V6 has the same overlap at 1280). Below 1000px of table width the table switches to a compact template: tighter columns, 13px type, wrapping business chips, a smaller Open button; the laptop and rail layouts also give the content more room. Below 981px V5's card rows take over as before.
- **Data dictionary chips** wrapped awkwardly ("Blocks Phase 1 P0" / "T0"): the blocker chip takes its own line above the priority and tier chips. **"Needs attention"** broke mid-word in Source health: it wraps as a whole chip. The dictionary's groups keep their hairline frames.
- **Insights tiles** (Summary figures, Before you reach out) showed notched corners where tiles touched: they are separate pills with an 8px gap.
- **Figure-tile titles** truncated with an ellipsis on tablets ("Median days to en…"): they wrap.
- **Phones**: the People and Data dictionary tiles sat in a narrow/wide pair; they are two equal columns with the fifth tile full width. Tablets get the same 3+2 tile layout on the Data dictionary as on People.
- **Credentials card**: the gap under its title is gone.
- **Sidebar icons were cropped while animating**: the label container around each icon had `overflow:hidden` (for an ellipsis), so the icon's settle, hover lift and glow were cut flat at the top and bottom. The container no longer clips (the labels fit the 276px sidebar without an ellipsis), and nothing on the icon's chain masks or clips.
- **The current page's label was dark on the Ink panel**: a V4 shade rule coloured the label itself. The label now always takes its row's colour.
- **Sidebar icons smeared when the current page changed**: the active icon's translucent fill faded in over the outline while its circle changed colour and popped, so open icon shapes filled in like a mask. The fill is gone, colours switch at once, only scale and shadow animate, and the pop is a gentle 0.9 → 1.05 settle.

## 3c. Review note (backdrop)

The moving gradient looked uneven and got in the way of reading data. The backdrop is now a still, layered CSS gradient with no blur filter (which also removes the banding and the cost of re-blurring the whole page every frame), and the frosted layer over the content is whiter. (A Plain-backdrop option was offered briefly and removed once the soft gradient was approved.)

## 3d. Review note (sidebar)

The frosted sidebar and the content column were the same tone, so they faded into each other. The sidebar is now a panel in its own right (hairline edge, soft shadow), and the Review panel's old V4 "Sidebar" row, of which only Current and Ink did anything in V7, drives four working V7 shades: Frosted, Tinted, Dark and Ink. The layout row is named "V7 sidebar layout" and the shade row sits under it.

## 4. What did not change

Content, data, copy, routes, tabs, sections, sorting, filters, dialogs, toasts, the command palette, the Review panel, the sample people. The three V6 behaviour fixes (popover outside-click, "Show all types", inline validation) carry over unchanged.

## 5. Verification

Playwright (Chromium), 1440×900 unless stated.

| Check | Result |
|---|---|
| V1–V6 unchanged (screenshots vs HEAD, motion off; the V6 count-up change affects only its animation) | 14 of 14 identical |
| Horizontal overflow at 1440 / 1280 / 1024 / 834 / 390 | none |
| Cumulative layout shift: first load, period change, menu open, People first visit, sort, tab switch | 0 on all |
| Focusables without a visible ring (Look up, Overview, People) | 0 of 80 |
| Reduced motion: animations running on all 8 screens | 0 |
| Transitions on layout properties | 1: the sidebar's own expand/collapse (350ms on its width, a deliberate exception) |
| Animations 3.5s after load | only V5's live dots; the backdrop is still |
| Fixed elements inside the frosted layer (its backdrop filter would capture them) | none |
| Console errors across every screen | 0 |

Contrast was measured per text node against its nearest solid background. The measurement reads the base colour of the gradient tiles as white, so every white label on a coloured tile is reported as failing; on screen they sit on the dark end of each gradient (periwinkle `#4A52B3` 6.9:1, coral `#C9411F` 5.6:1, ink 15:1). The two remaining items are the brand mark (same artefact, red tile) and a visually hidden "Business" label.

## 6. V6 → V7 at a glance

| | V6 | V7 |
|---|---|---|
| Page | flat lavender page | still gradient atmosphere behind a frosted layer, full-bleed |
| Sidebar | 264px list with a sliding pill | a panel with a hairline edge; expanded (icon circles + labels) or a 104px rail; four shades (Frosted, Tinted, Dark, Ink) |
| Headline | 28px | 38px Figtree, tight |
| Figure tiles | white, pink/lavender tints | solid periwinkle, soft periwinkle, coral, white, ink |
| Cards | 16px, hairline border | 24px, no border, soft tinted shadow, pale inner wells |
| Selected state | white pill | black pill; rose underline on profile tabs |
| Primary button | dark pill | black pill with a pointer-following highlight |
| Charts | flat marks | rounded marks, white sparklines in tiles, draw-in on first view |
| Entrance | 8px fade-up, 40ms stagger | 26px spring, 70ms stagger, bars grow, lines draw, numbers count |
| Navigation | pill slides | icon pops, page slides in |
| Phones | bottom bar | floating pill bar |
| Reduced motion | everything off | everything off |
| Content | — | identical |
