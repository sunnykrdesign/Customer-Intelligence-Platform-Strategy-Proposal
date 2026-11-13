# upGrad Customer Intelligence: Phase 1 dashboard design

Design prototype for the Phase 1 of the Customer Intelligence Platform: identity resolution and the unified user database across Unacademy, Internshala and Working Professionals.

**Working dashboard (GitHub Pages):** https://sunnykrdesign.github.io/Customer-Intelligence-Platform-Strategy-Proposal/

**Design canvas:** https://claude.ai/artifact/5uSQYgSmss3X2D4Zu1XahK

The working dashboard is a single self-contained file, `docs/index.html` (plain HTML, CSS and JavaScript, no build step or dependencies apart from the Inter web font). Open it in any browser, host it on any static site, or embed it in an `<iframe>`. Screens are linked by URL: `#/overview`, `#/lookup`, `#/identity`.

All numbers, names and people in the screens are sample data for design review.

## Sign-in flow

The working dashboard starts at sign-in and walks through the full journey:

1. **Sign in** with Google or a work email. Only `@upgrad.com`, `@unacademy.com` and `@internshala.com` addresses are accepted.
2. **Check your email** for a 6-digit code (in the prototype, any 6 digits work).
3. **Choose your team.** The central data team sees Overview, person lookup and identity audits. Counseling teams (Internshala, Working Professionals, Unacademy) only see person lookup.
4. **Before you start.** A one-time agreement to the data-use rules: contact details are hidden until a purpose is given, consent is checked before contact, and data on minors is restricted.
5. **Dashboard.** You land on your team's home screen. Counselors from a business the learner hasn't consented to are told not to contact them, and the link to the owning business's CRM is hidden.

Authentication is simulated in the browser for the prototype; there is no real login or backend. The session lasts until the tab is closed or you sign out.

## Preview and share

- **Preview without signing in** (link under the sign-in panel) opens the dashboard as a guest, seen as the central data team. A dark bar at the top says it's a preview, with **Share** and **Sign in**.
- **Share** (in the sidebar, the preview bar and under the sign-in panel) opens a sheet that builds a link:
  - **Skip sign-in:** the link opens straight into preview mode.
  - **See it as:** central data team, or an Internshala, Working Professionals or Unacademy counselor.
  - **Open on this screen:** the link lands on the screen you're on (or that team's home screen, if they can't see it).
  - **Copy link**, **Open preview**, the device's own share menu where available, and **Embed on a website** (copyable `<iframe>` code).

Preview links look like this:

- Central team overview: `…/?preview=1#/overview`
- Working Professionals counselor on the lookup screen: `…/?preview=1&team=wp#/lookup`

`team` can be `central`, `internshala`, `wp` or `unacademy`.

## Review panel

A **Review** button in the bottom-right corner opens the review controls. They're for design review only, not part of the product. The controls sit in groups: **Version**, **V4 options**, **Look up a person**, **Motion** and **Sharing and access**. A group's title hides when none of its controls apply to the version on screen.

- **Share this view:** **Copy link** gives a link that opens exactly what you're looking at: the design version, the profile layout, the pinned search bar, the sidebar menu items you've left on, the screen you're on and, on Look up a person, the person who's open. It skips sign-in and hides the Review panel, so the person you send it to sees only that view. For example: `…/?preview=1&ver=1&card=top&tabs=left&bar=high&pin=1&nav=overview,people,lookup&p=ananya&review=0#/lookup`
- **Design version:** five versions, named in order. A note under the switcher says which one is on screen. Links use `?ver=1` to `?ver=5`, and older links with the previous numbers still open the right version. Retired drafts, and old links or saved choices for them, open V4. Switching away from V4 puts every colour it changed back, so its theme never shows in another version. A V3 or V4 link also keeps the trend style, for example `&tr=stack`, and a V4 link keeps the theme, for example `&t=ocean`.
- **Sign in:** **Skip** or **Show** (default). Skip opens the prototype straight into the app as Demo User on the Central data team, which can see every page: no sign in, sign up, code, team choice or notice, and no preview bar. Show keeps the full flow. The choice is remembered in this browser, and a link keeps Skip with `&auth=off`.
  - **V1 · Classic** (previously V3)
  - **V2 · Learner 360** (previously V4)
  - **V3 · Master** (previously V6)
  - **V4 · Crisp** (previously V7): the default for new visitors.
  - **V5 · Learner 360 data**: the latest. V4 Crisp with the PM's sample people (see Design versions). Switching into or out of V5 reloads the page, because V5 loads different people.
- **Theme (V4 options):** **Crisp** (default) or **Ocean**. Shown only in V4. A saved or linked Bold or Vivid theme opens as Crisp.
- **Overview:** **New** (default) or **Current**. Shown only in V4 with the Crisp theme. New is the Overview from the shared design, which that design called "Insights". Its content comes from that design; its look follows the Crisp Overview design in Figma (Customer Intelligence Platform file, node 48:12213). The data is laid out to be read at a glance. All figures are sample data.
  - **Look:** Figtree on the Crisp lavender page (#F3F4FB), white 16px cards with no border and 28px padding, 20px card titles. Controls are pills on #ECEEF6 with a white selected pill. Marks are periwinkle (#646EC2) for the one that matters, lavender tints for the rest, ink (#182230) and rose (#D03A70). Takeaways sit in a lavender tint panel. Businesses use periwinkle (WP), rose (SA), olive (KH), violet (International), amber (LC) and blue (Internshala); neighbours were checked for colour-blind separation. Life stage runs light to dark rose for students and light periwinkle to deep indigo for working people.
  - **Header:** the title, the design's "Updated today, 09:00" pill with a lime dot, and the period and business. The **Prospects** and **Learners** switch is a pill on the right. Below it, what the tab counts, the time range (30 days, 90 days, 12 months) and a Business filter, which rescale every figure.
  - **Headline:** the design's pastel KPI tiles, pink to lavender: a white icon circle (the app's Fluent icons, or periwinkle with Colour icons), the period, the value with a white change chip (periwinkle when good, rose when not) and a 12-month sparkline with a soft wash.
  - **Reading aids:**
    - Every card opens with its takeaway in one line (for example "Generative AI interest more than doubled").
    - The bar that matters is in periwinkle and the rest are muted.
    - Dense charts became simpler ones: momentum rows for rising and falling interests, a butterfly chart for Study Abroad destinations (ruled out in rose, first choice in periwinkle), one funnel plus an enrolment-rate ranking instead of six funnels, ranked bars instead of the two heatmaps, year-ago-to-now dots for channel mix, quadrant labels on channel quality, routes for crossover, and a 49% callout for why learners leave.
    - **Rising and falling interests:** one row per interest with its 12-month trend as a wide area line, the share a year ago and now, and the change as a chip. Rises are periwinkle (the biggest in full colour, on a tint), falls are rose. The trend's height has a floor of half the interest's level, so a flat interest stays flat. The lines draw in from the left.
    - **Crossover:** three summary tiles (people who moved, where most went, the biggest source), then every route from one business's people to another, largest first. Each route shows a from pill and a to pill in the business colours, dots that run along the arrow in the destination's colour (faster for bigger routes), a bar for its size, the count and its share. The bars grow in. Narrow cards and phones stack each route onto two or three lines. With reduce motion turned on, the dots become a dashed line and nothing animates.
    - Cards side by side end level: in a shorter card the chart grows into the spare height and lists spread out. The experience charts add three summary tiles in the design's style (Students, 1 to 8 years and 8 years plus for prospects; Students, 3 to 8 years and 8 years plus for learners).
    - Funnels are the design's gradient columns with a white pill for the share that passed each step; the step that loses the most is a rose pill. In narrow cards and on phones the columns become rows.
  - **Exact figures:** hover any mark for a tooltip, or switch any card from **Chart** to **Table**.
  - **No repeated charts:** each chart appears once. Life stage by business, experience, and value by channel are shown on Prospects only; Learners no longer repeats them (value by channel is the bubble size in Channel quality). Top employers and Time to a second purchase take the full width instead.
  - **Crossover sits high:** on both tabs it has its own section right after the first one (Who they are, Who learns with us), instead of at the end.
  - **Current:** keeps Phase 1 progress and Paid leads. A link keeps Current with `&ov=current`.
- **Icons:** **Mono** (default) or **Colour**. Shown only in V4 with the Crisp theme. Colour fills the same icons with the theme's gradients: the figure cards run pink to periwinkle along each row, the sidebar runs rose to periwinkle, and profile sections get gradient discs with white icons. A link keeps the choice with `&ic=color`.
- **Activity icons (V4 and V5):** the Activity tab uses the People outline set. Each timeline event, and each event in By business, shows an ink outline icon in a white circle with a hairline ring, the same as the People KPI tiles. There's no coloured circle per event type, with Mono or Colour icons. Each icon names the activity, not the category: WhatsApp, SMS, email, webinar, call, counselling meeting, new lead or contact, first touch, deal won, application, job application, payment, deferral, extension, refund, employer-paid, enrolment, assignment, progress milestone, certificate, rating, referral, consent and web visit. Icons are chosen from the event's title and type, never its detail line.
- **Tab icons:** **On** (default) or **Off**. Shown only in V4 with the Crisp theme. It shows or hides the icons on the profile section tabs (Identity, Personal, Education, Career, Aspiration, Financial, Consent) so you can compare both. A link keeps Off with `&ti=off`.
- **Section icons:** **Line** (default) or **Circle**. Shown only in V4 with the Crisp theme. Line shows each profile section's icon on its own, with no tinted circle behind it, at 24px and drawn a little bolder, in the section's colour (with Mono or Colour icons). Circle keeps the icon inside a tinted circle, or a gradient one with Colour icons. A link keeps Circle with `&si=circle`.
- **Sidebar:** **Current** (default), **Darker** or **Darkest**. Shown only in V4 with the Crisp theme, on desktop. Current is the soft lavender #E5E3F0. Darker is the deep lavender-indigo #2C2850 with light text and a lighter upGrad red in the logo. On Current and Darker the current page is a see-through white pill (60% white), so the sidebar shade shows through; hover is 30% white. Darkest is the near-black #1B1B1B (the same as the Darkest person card), with light grey text and the current page shown as white text on a faint fill with a white bar at the sidebar's edge. Every shade keeps sidebar text at 4.5:1 or better. On Darker and Darkest the menu icons follow the text colour, even with Colour icons, because the gradient glyphs lose contrast on dark shades. A link keeps the choice with `&sb=darker` or `&sb=darkest`.
- **Person card:** **Current** (default, white), **Darker** or **Darkest**, the same two dark shades as the sidebar. Shown only in V4 with the Crisp theme, in every Look up layout. Darker is the deep lavender-indigo #2C2850 with light text. Darkest is the near-black #1B1B1B (the same as the Darkest sidebar) with light grey text. Both have translucent chips, Show contact and tabs, white fact glyphs (with Mono icons), and a white Open in CRM so it stays the main action. A link keeps the choice with `&pc=darker` or `&pc=darkest`.
- **Person card layout:** **Current** (default) or **Centred**. Shown only in V4 with the Crisp theme, in every Look up layout, on screens wider than 820px; phones keep the current card. Compact, Split and Stats were removed; older links with those open with Current.
  - **Centred** follows the Figma frame "07 · Compact horizontal cards" (Customer Intelligence Platform file, node 77:223):
    - **Header:** a gradient band (#E8E6FC to #F5F1FC to #F9E1ED, radius 20). The 72px photo, the name (28px), the headline and the meta row (known for, the ID chip, Synced with a lime dot) are centred.
    - **Corners:** the five contact channels sit in the top-left corner as white 28px circles. Show contact, the things-to-act-on flag (when there is one) and Open in CRM sit in the top-right corner.
    - **Tabs:** they follow the header, in a #E8E5F2 pill, with Find in profile beside them.
    - **Fact cards:** they sit under the tabs, in one row of five 80px cards. Life stage, Age band and City are white, each with a line icon. Owned by is pink and shows the business's short code (WP, IS). Fields filled is lavender, with the share, a bar and the date it was updated. Between 821px and 1199px wide they wrap into three columns.
    - **Folding header:** the header sits in the frame's soft #F5F4FC panel and folds into the usual slim bar. The things-to-act-on popover opens over the tabs and cards.
    - **Fonts and icons:** the app's own font (Figtree) and Fluent icons. The design's icon files couldn't be downloaded from figma.com in this environment.
  - A link keeps Centred with `&pl=centre`.
- **Search bar:** **Compact** (default) or **Current**. Shown only in V4 with the Crisp theme. Compact puts the Look up field beside "Who's on the line?" instead of under it: 40px tall instead of 56px, up to 440px wide instead of the full page width, with 14px text and a smaller Look up button. With a person open, the row above their card drops from 95px to 40px, and a pinned search bar drops from 119px to 64px. On a phone the heading sits above a 52px full-width field with a 44px arrow button. Current keeps the full-width bar. A link keeps Current with `&sr=current`.
- **Value dates:** **On** (default) or **Off**. Shown only in V4 with the Crisp theme. It shows when information was added and when it was last verified:
  - **Profile values:** in every section, "Added 7 Jun 2024" sits under each value's sources, and "Verified 7 Sep 2026" sits in the row's top-right corner as plain quiet text, in the same style as the Linked and Since dates. There is no tick icon. Rule-derived values say "Derived" and "Rechecked".
  - **Education and career entries:** the same plain "Verified" date, inline after the added date.
  - **Linked records and owners:** "Linked" or "Since" with a date, lined up in a column.
  - **Person card facts:** no dates, except "Updated" under Fields filled.
  - **Sample dates:** they stay the same for each person and field, fall between when upGrad first knew the person and today, and the check never comes before the capture.
  - A link keeps Off with `&dt=off`.
- **Insights:** **Simple** (default), **Call brief** or **Current**. Shown only in V4 with the Crisp theme.
  - **Simple:** a plain read of the person in one clean panel, with no calling advice, reach or contact counts:
    - **Summary:** two or three sentences on who they are, how long upGrad has known them, their current or past programmes and a good next fit, then three figures: lifetime value, programmes and learning.
    - **With upGrad:** a card for each business they're known to, with its stage, since when and the course they took there.
    - **Key details:** status, first seen, last active, intent, re-acquired and next programme.
    - **Activity over time:** events in each of the last six months as a bar chart, with the change from the quarter before. These are sample figures, steady for each person and nudged up by their real events.
    - **Interest by area:** up to three areas, worked out from the words in their courses, goals, headline, skills and activity.
    - Another business without cross-business consent sees only its own relationship. Lifetime value shows "Owner only" to every other business.
  - **Call brief:** the previous default. It shows a verdict, talking points and the best next step, then every signal.
  - **Current:** Before you call as a list, with the signals behind a Show more.
  - A link keeps a choice with `&ins=brief` or `&ins=current`.
- **Spacing:** **Compact** (default) or **Current**. Shown only in V4 with the Crisp theme. Compact tightens vertical spacing across V4:
  - **Person card:** less room above it (the space above the photo drops from 61px to 29px in the Folding header layout), with the person header about 60px shorter.
  - **Pages:** less room at the top of every page and between sections, and slimmer padding in cards, figure tiles and profile rows.
  - A link keeps Current with `&sp=current`.
- **Fact icons:** **On** (default) or **Off**. Shown only in V4 with the Crisp theme. Each fact on the person card (life stage, age band, city, owner, fields filled) gets an icon tile from the design-system set: a briefcase, or a graduation cap for students, then a calendar with a person, a location pin, a team and a pie. With Icons on Mono the tiles are ink on soft lavender; on Colour each fact gets its own pastel tile and tinted glyph. A link keeps Off with `&fi=off`.
- **Look up a person · layout** (all versions): pick where the **person card** sits (Left panel or Top header) and where the **section tabs** sit (Top, Left or Right). That makes six combinations, and a small diagram shows the current one.

- **Sticky bar:** always **High**, a raised two-row card with photo, name, key facts, owner and completeness chips and the CRM button, with the tabs below. The Minimum and Mid options were removed, so there's no Sticky bar row in Review; older links with `&bar=min` or `&bar=mid` open with High.
- **Pin the search bar** (on by default): keeps "Who's on the line?" at the top of Look up a person while you scroll, with the pinned person and tabs sitting just below it. A new search opens the person at the top.
- **Locked sections:** shows the demo team password.
- **Sidebar menu:** an on/off switch for each sidebar item: Overview, People, Look up a person, Identity & audits, Data dictionary and Later phases.
  - Hidden items leave the sidebar, and links to them open the next visible page.
  - At least one page always stays on.

Your choices are remembered on that browser.

## Design versions

Five versions are in the switcher: V1 · Classic, V2 · Learner 360, V3 · Master, V4 · Crisp and V5 · Learner 360 data. Earlier drafts are retired, and links to them open V4.

- **V1 · Classic** (previously V3): a soft grey canvas with white cards, monospace table headers and status chips, and upGrad red as the accent colour. Its Overview is built for live monitoring:
  - **Top numbers:** a row of six key figures. The numbers roll in digit by digit when the page opens, and the live counters keep ticking.
  - **Trends:** a chart with a crosshair that follows the cursor (or the arrow keys). It shows a tooltip with every series for that day and a red date pill on the axis. Each series can be switched on or off from the legend.
  - **Paid leads, checked against the profile:** a table of recent paid leads, filtered by business tabs with a sliding indicator. Clicking a row lifts it into a card with a red top edge, AI fields (next-best programme, intent) and actions.
  - **Business cards:** one per business, with a live profile count and an animated consent ring, plus a bar chart of lookups this week.
  - **Motion everywhere in V1:** tabs and segments use the same sliding indicator. Cards rise in with a stagger. People directory rows open into the same detail card.
  - **Reduced motion:** all of this switches off when the system asks for reduced motion.
- **V2 · Learner 360** (previously V4): V1's design language and motion with a framed sidebar from an earlier draft, and **Look up a person** rebuilt around the Learner 360 content (the Figma frames shared on 6 Nov). It opens on Ananya R., the Learner 360 sample. Everyone else gets the same view, built from their profile data.
  - **Header:** the person, their profile-completeness ring, ID and key facts, and four headline figures: lifetime revenue, businesses, learning health and profile filled. Revenue is shown to the owning business only.
  - **Life with upGrad:** one lane per business (Study Abroad, Internshala, upGrad platform, Working Professionals, KnowledgeHut, International), with lead, counselled, paid and lost periods, milestones and a Today line, under a life-stage band.
  - **Left rail:** Reach her (each channel with its consent state, and **Show contact details**), linked records with the merge note, owners right now, and where her data comes from.
  - **Things to act on:** the moments, each with one action that confirms when it's done.
  - **Four tabs, kept in view with the person while you scroll:**
    - **Learner profile:** one section at a time, so the page never becomes a long scroll. A row of chips (Identity, Personal, Education, Career, Aspiration, Financial, Consent) shows how much of each is filled and stays pinned under the person bar as you scroll, so you can switch sections from anywhere; and the arrow keys or the previous/next links move between them. Each section shows its summary, then every value with its sources, when it was captured, which source won a conflict, and what isn't captured yet. Financial stays locked behind the team password.
    - **Academic and skills:** the current programme (progress, modules, assignment scores, live sessions and instalments), skills graded by upGrad or self-declared, and credentials.
    - **Activity:** a timeline grouped by month, filtered by business and event type, with details per event and the latest 6 first. It can also be read by business, or as a weekly learning rhythm.
    - **Insights:** 13 answers in five groups (value, reach and engagement, health and risk, signals across businesses, counselling model scores), each with how it's worked out.
  - **Layouts (Review panel), as in V1:** the person and headline figures across the top or in the left panel, and the four tabs on top, on the left or on the right. The left panel stays in view and scrolls on its own, so it never makes the page longer. Below 1100px wide, V2 always uses person on top and tabs on top. The sticky bar strength and the pinned search apply to every layout.
- **Look up layouts** (from a retired draft; they live on in V3 and V4 under Review → Look up layout): V2's content and look with less on screen, in three layouts. Every layout opens with V1's white person card, end to end: a large photo, the name, headline, how long upGrad has known them and how they were matched (with the ID to copy and when the data last synced), the CRM action, and a facts row (life stage, age band, city, owner with the owners' names, profile filled). Ananya R. uses the Ananya photo from V1.
  - **Minimal (default):** the card, one pinned bar with the tabs and **Find**, then the details. Contact and the things to act on sit in a dark dock at the bottom of the screen. Linked records, owners and sources are in Identity; Life with upGrad is in Activity, as **Journey**.
  - **Overview first:** the card (with who may be contacted), the pinned bar, and an Overview tab with the headline figures, Life with upGrad, the things to act on, and owners, records and sources.
  - **Folding header:** the card folds into the pinned bar as you scroll. Who may be contacted and the things to act on sit on the card, the selected tab's details follow straight after it, and Life with upGrad is in Activity, as Journey.
  - **The sticky bar (always High) pins** the photo, facts and tabs, and also the owners, who may be contacted (with Show contact) and the things to act on, so they move off the card and out of the dock. Contact and actions always show once on screen.
  - **Calm switching:** changing tab or section updates only the content under the pinned bar, with a short fade. The card and bar don't move or animate again, and if you were scrolled down, the new content starts right under the bar. Filters and details inside a tab update in place. The details area always leaves room to bring the chosen section to the top, so nothing jumps when a section is short.
  - **High bar:** one aligned row of context: the photo and name with the owner ("Working professional · Hyderabad · Owned by WP"), then Reach with each channel's state, Show contact and the things to act on.
  - **Nothing scrolls inside something else:** no panel has its own scroll bar, the section chips wrap instead of scrolling sideways, and the lanes timeline never needs a sideways scroll (on phones it switches to business cards).
  - **A good place to get data:** press **/** (or Find) to search every field you're allowed to see, and jump straight to it (it's highlighted). Hidden contact details and locked financial values are never shown in results. The ID and, once shown, emails, mobile and linked record IDs each have a copy button. Every profile says when it last synced and which sources its values came from.
  - **Life with upGrad, four ways** (Review → Life with upGrad): **Lanes** (one row per business over time), **Journey** (one path of milestones in order, with today's state underneath), **Businesses** (a card per business with its stage steps) and **Strip** (one line of chips).
- **V3 · Master** (previously V6): everything from the Look up layouts above (all three layouts, the sticky bar, Find, copy buttons, Life with upGrad) plus a rebuilt Overview and a motion layer. References came from Mobbin: GitBook, Substack and Posh for area charts with a crosshair tooltip, Mixpanel and Monarch for stacked bars, Uxcel and Semrush for this-period versus last-period, Squarespace, Amplitude and Hotjar for funnels, and Mixpanel flows for the business-to-business chart.
  - **Hero:** a dark card with a slow red glow, a live count of unified profiles, the Phase 1 track (identity graph, unified database, 360 view, merge audits, consent by purpose) and three activity rings (leads resolved against the 80% target, teams on the 360 view, audits done).
  - **Measure cards:** leads resolved, known to 2+ businesses, wrong merges (with the 0.10% cap line) and paid leads already known. Each has a rolling number and a sparkline that draws in, and you can hover the sparkline to read any day.
  - **Trends, three styles** (switch at the top right of the card): **Flow** shows smooth area curves for the three measures, with the three moments that moved them marked on the chart. **Stack** shows weekly paid leads split into already known, shared phone and new to upGrad, with the share already known drawn as a line. **Focus** shows one measure at a time, with last period as a ghost line, the target or cap, and a 30-day forecast with a range. Switching measures morphs the line. Every style has a crosshair tooltip and works with the arrow keys.
  - **From lead to learner:** the funnel from paid leads to enrolment, as **Columns** (with step conversion chips) or **Taper**.
  - **Where learners move:** the flow of the 727K people known to more than one business, from where they first met upGrad to where they joined next. Hover a ribbon or a business to isolate it.
  - **Search (⌘K or Ctrl K, or Search in the sidebar):** jump to a screen, open a person, change the trend style, copy the link to this view, share, or switch design version.
  - **Look up a person · Academic (V3):** a dark course card with an animated progress ring, the module you're on and the key figures; a programme path that fills up to the current module; assignment scores against the cohort average; live-session attendance as a ring and a grid; instalments as a segmented bar; a skills radar (graded by upGrad versus self-declared) next to the skill list; and credentials as badges.
  - **Look up a person · Activity (V3):** **Journey** is a roadmap with one row per business over time (lead, counselled, paid, completed and lost bars, milestones, the life stage on top and a Today line), then chapters by year. **Timeline** opens with a stacked chart of events per month, then filters by business and event type and a feed grouped by month. **By business** gives a card per business with its event mix, when things happened and every event. **Learning rhythm** has the headline figures, weekly bars with the average, a day-by-day heatmap and busy times. The same roadmap is used for Life with upGrad on the Profile tab. References: Productboard, Plane and Miro (roadmaps), Calendly, Shopify and Mixpanel (activity feeds), Base44, Peerlist and Cursor (heatmaps), Quo (busy times), and Headspace, Codecademy and Babbel (course progress).
  - **Look up a person · Insights (V3):** opens with **Before you call**, a short summary built from the signals (learning, reach, how often they've been contacted this week, any re-acquisition and the best next step). Then come scorecards for lifetime value (paid against still due, owner only), learning health, refund risk and how many businesses know them; re-acquisition and next-best programme cards; reach as open and closed channels with contact fatigue for 7 and 30 days; model scores as meters; and any other signals. Every figure keeps its **How** note. References: HubSpot's record summary, Xero and Searchable scorecards, Whop's risk gauge and Vanta's status cards.
  - **Motion:** screens fade in as you open them, cards rise into view as you scroll, a soft spotlight follows the cursor on cards, and segmented controls slide with a spring. If reduced motion is turned on, all of this is switched off.
- **V5 · Learner 360 data** (the latest; `?ver=5`): V4 Crisp, unchanged, filled with the five sample people from the PM's `data/learner360_sample_people.json` (as of 13 Nov 2026; the page embeds a copy): Riya Deshmukh, Karan Malhotra, Sneha Iyer, an under-18 profile in Kochi, and Vikram Rao. All names, IDs and numbers in that file are invented. Every V4 option applies, except Theme: V5 is always Crisp.
  - **No overlap block on People:** People goes straight from the KPI tiles to the directory. A cross-business overlap section (matrix, re-acquisition spend) was tried there and taken out, because totals belong in Overview, whose Crossover section already covers who moved between businesses.
  - **Photos:** V5 uses V4's sample profile photos. Riya and Sneha share the one photo of a woman (as V4's two Ananyas do); Karan has Arjun's photo, Vikram Rohan's and the density test profile Harsh's. The under-18 profile stays hidden with no photo.
  - **People:** the directory shows 30 rows so it reads like the real product. Each row has life stage and city, businesses, overall relationship state, lifetime revenue, reachable channels and last active.
    - The PM's five people and the density test profile come first, and they open.
    - The other 24 are directory rows only, marked "Sample", as in V4. They use only V5's businesses (Internshala, Working Professionals, KnowledgeHut, Study Abroad, International; no Unacademy) and the PM file's words for states and life stages. They cover leads, learners, alumni, a refund and a second under-18 profile, whose name is never stored in the row, so search can't reveal it.
    - Segments, the business filter, search and sorting all work across the 30 rows. The business filter and the Key list only V5's five businesses.
    - **Pages, not one long list:** the directory shows 10 rows at a time. Below the table, choose 10, 25 or 50 rows per page, see the range ("11–20 of 30"), and move with previous, next and page numbers. Long page lists fold into first, last and the pages either side of the current one. A new segment, search, business or sort goes back to page 1; opening a row's details keeps the page. Changing page scrolls back to the top of the directory and keeps keyboard focus on the pager. On phones the page numbers hide and the previous and next buttons grow to 40px. The footer says 19,42,118 people in all and that the preview has 30 sample rows.
    - A row's expanded panel shows Relationship instead of Owned by, because V5 never shows the owning business.
  - **Person card:** name, headline, how long upGrad has known them, the person ID and sync. The facts row shows life stage, age band, city, known since with last active, and then each business with its state and since when. Businesses comes last because it is the one fact whose size depends on the person (one to five businesses).
    - **Space follows the content, the same on every profile.** Default person layout, 821px and wider: on a wide card the facts sit in one row with hairline dividers, each as wide as its content plus an equal share of what's left, so "18–24" no longer gets a wide column and "Final-year undergraduate" doesn't wrap. On a narrower card (laptops around 1280px and below) they form a 3×2 grid: life stage, age band and city on top; known since and Businesses (two cells wide, its businesses side by side) below.
    - **Centre person layout (Review panel):** the tiles stay as they were: white Life stage, Age band and City tiles, a lavender Known since tile (the tint V4 uses for Fields filled, with Last active under the date) and a pink Businesses tile. Each tile is sized by its content, so Businesses is no longer squeezed into the narrowest slot. Between 821px and about 1200px they form the same 3×2 grid, with Businesses two tiles wide.
    - **820px and narrower:** the earlier soft grey tiles, now in a grid that wraps (three columns, then two on phones, with Businesses full width) instead of a strip that scrolls sideways, so no fact is hidden. Under 420px each icon sits above its label so the text has the whole tile. Nothing is clipped or broken mid-word at any width.
  - **Profile:** the file's sections with its attribute names: Identity & contact, Personal details, Life stage, Education (the file calls it "Education (prior, outside upGrad)"), Career / profession, Aspiration, Financial profile (locked as in V4), and Consent & preferences.
    - Life stage is its own section, kept apart from personal information. Personal details holds age band, city, country, timezone, language, gender and account status, and its summary no longer mentions life stage.
    - Each value shows its source and whether it was declared, observed or derived. It also shows the date it was added, in the row's top-right corner where V4 puts its verified date, as plain quiet text with no icon. On phones the label wraps before it reaches the date. There's no verified date. Education and career entries keep the added date under the entry, as in V4.
    - Sales Insights values show "Counselling call on {date}".
    - Emails and phones stay masked until Show contact, and say whether they're verified.
    - Linked system IDs become Linked records.
    - Conflicts show how they were resolved.
    - "Consent to share across upGrad" says it has no source yet.
    - Values worked out by the system say "Worked out by the identity layer".
    - Fields with several values show one per line, for example emails, phones, programmes of interest, roles applied for, languages, interest areas and study-abroad preferences.
    - **Career comes from LinkedIn:** professional history is sourced through the LinkedIn API, not CV fields. A banner says so, with the sync date. Every Career value and role carries a LinkedIn source chip, and a "Professional profile link" row says the LinkedIn profile is connected.
    - **Budget by programme:** budgets differ a lot between programmes, so the Financial section lists each programme the person is pursuing with its business's own options. The bands are Working Professionals (under ₹1 lakh to ₹6 lakh plus), KnowledgeHut (under ₹25K to ₹1 lakh plus), Study Abroad (under ₹10 lakh to ₹40 lakh plus), International (under ₹5 lakh to ₹15 lakh plus) and Internshala (free to ₹10K plus). The stated band is highlighted, along with where it was stated. Programmes without a stated budget say "Not captured yet".
    - Education and Career show profile-style entries, as in V4. They're built from the file's "Education history" and "Work history". Each school gets a crest: a school crest for Class 12 and boards, a university crest for degrees, including a B-school. Each employer gets an initials logo. Entries show years, grade, type (full-time or internship) and total experience. Fields they don't cover are listed under "Also on file". The under-18 profile has no history, so it keeps plain rows.
  - **UG learning journey:** upGrad courses with status, progress and results.
    - Each programme is its own card, stacked vertically and labelled "Programme 1 of 3" and so on, with its own module path. There's no switcher between programmes, and credentials list only certificates, projects and trainings.
    - Programmes with module data (Prism's "module x of y") get the programme path.
    - Internshala Trainings say they have no module data.
    - Skills keep graded ones (proven) apart from self-declared ones.
    - Projects and trainings on the resume are listed under credentials.
  - **Activity:** every event under the model's sub-sections: Attribution, Marketing engagement, Enquiries & business relationships, Interactions, Payments & commerce, Learning activity, Career activity (new) and Support, feedback & referrals. Consent changes aren't shown, as the model decides.
    - Flags show on the event ("Re-acquired", "Under 18").
    - Details show the event type and the source record.
    - Counselling calls show "Counselling call on {date}".
  - **Insights:** the file's summary, lifetime value, programmes and relationship state, then each business, every insight with what it's built from, activity over the last six months, and interest by area.
  - **Under 18:** the profile shows "Name hidden" and its restriction note. It shows only the basics the file gives: contact hidden, every channel blocked, and no intent or next-best programme.
  - **Things to act on:** the person's moment, plus a re-acquisition when there is one.
  - **By business:** no business is labelled as owning the relationship, and the owner isn't listed first, because the owning business is stored but not shown.
  - **Today:** dates are worked out from 13 Nov 2026, the file's as-of date.
  - **Worst-case density test:** a sixth profile, Venkata Lakshmi Narasimha Subrahmanyam, tagged "Density test" in the directory. It is added for design review and is not part of the PM's file. It has a long name and five businesses. It also has five emails, three phones, ten linked records, six languages, four schools, six roles, five programmes of interest, eight roles applied for, fourteen skills, three courses, twenty-four events and nineteen insights. On the card, Businesses lists each business on one line: a coloured code chip, its state and a short date ("WP Learning Aug ’25"), with the full wording on hover. That fact gets a wider column at desktop widths. With three or more businesses it shows the code chips and a count of states, so the facts row stays low.
- **V4 · Crisp** (previously V7; the default): V3 with a new visual layer and two themes (Review → Theme). Bold and Vivid were removed.
  - **Crisp (default): soft lavender.** Built from a reference dashboard's visual language, not its content or layout:
    - **Shell:** one light app surface that runs edge to edge, with no canvas margin or rounded outer corners. On desktop the sidebar has its own deeper lavender surface (#E5E3F0) and a firmer divider down the full height, so it stands apart from the lighter page; the search field and the current page sit on it as white pills.
    - **Surfaces:** white cards with no borders and 16px corners. Type is Figtree, with medium-weight headings and figures.
    - **Sidebar:** grey line icons with no colour tiles. The current page is a white pill. The signed-in person sits at the foot of the sidebar, with no card around them.
    - **Summary rows:** one band of pastel cards running from pink to periwinkle, each figure with a white icon disc. This covers the Overview measures, the People tiles and the Data dictionary tiles.
    - **Controls:** a black pill for the main action (Sign in, Open in CRM, and Look up once something is typed), white outlined pills for everything else, and soft tracks with a white pill for tabs and segmented controls. Chosen filter chips and section pills turn periwinkle.
    - **Colour meaning:** periwinkle for good movement and done states, like the reference's "Taken". Rose for warnings, limits and restrictions, like its "Missed". A lime dot for live and synced.
    - **Tables:** the People directory sits on the shell with hairline rows, as in the reference's tracker. Status is a white pill with an icon: a check for completed, a slash for restricted or refunded, a dot for in-progress states.
    - **Charts:** periwinkle, ink and rose series. The Overview hero is a white card with periwinkle, rose and ink rings. Funnel tracks are hatched, with white value pills. In Focus, the target or cap is a rose dashed line. Businesses in "Where learners move" and the Activity tab use the same palette.
    - **Text contrast:** body and label text is at least 4.5:1, including the white text on chart pills.
    - **Icons:** the upGrad Design System 2026 icon set, which is drawn in the Fluent UI System Icons style (Microsoft, MIT licence). Icons are Regular (outline) by default, and Filled for the current page, as the system specifies. Every icon in Crisp comes from this set: the sidebar, buttons, chips, the reach dock, profile sections, activity events, the command palette and the menus.
      - **Sizes:** the sidebar uses the 20px design. Table, chip and inline icons use the 16px design up to 16px and the 20px design above that.
      - **Figure cards:** a Filled glyph on a white 40px disc, the same on Overview and People. Overview shows a person with a check for leads resolved, people for known to 2+, people with an alert for wrong merges, and a card for paid leads known.
      - **Profile sections and activity events:** tinted discs, one colour per kind.
      - **Profile section tabs:** each tab starts with its section's icon: person (Identity), home (Personal), graduation cap (Education), briefcase (Career), star (Aspiration), wallet (Financial) and a shield with a keyhole (Consent). The selected tab uses the Filled icon. In Colour, each icon takes its section's colour.
      - **People directory:** Reach shows five channel icons (call, email, SMS, WhatsApp, ads), periwinkle when open and grey when closed. Status pills and sort arrows use the same set.
      - **How it's applied:** a small script swaps each icon for its Fluent glyph while Crisp is on and puts the original back when you leave Crisp. Other versions and the Ocean theme keep their own icons. The animated Insights sparkle stays as it is.
  - **Ocean** keeps its own teal look.
  - **No Owner row in Identity (V4, both themes):** Profile › Identity lists emails, mobile, name and linked records. The owning business already shows on the person card as "Owned by", so the separate Owner row is gone. V3 keeps it.
  - **Reach beside Open in CRM (V4, both themes):** in every Look up layout and sticky-bar strength, who may be contacted (the five channel icons), **Show contact** and the things to act on sit in the person card's top line, next to Open in CRM. There's no separate Reach row on the card, no Reach row in the High bar, and no bottom dock. On narrow screens the group wraps under the name.

### Education and experience (V3, V4)

Look up a person › Profile › Education and Career follow a professional-profile pattern (Figma frame 46:10046):
- **Entries:** each school or employer is an entry with a logo tile (its initials), the title in bold, then the organisation and type, the dates with a worked-out duration, and the location.
- **Detail lines:** a grade line, a skills line ("SQL, Power BI and +2 skills") and a description clipped to two lines with "… more".
- **Badges:** the current job is marked **Present**. A job that hasn't started yet shows when it starts.
- **Connected roles:** several roles at one employer sit on a connected timeline under it.
- **Total experience:** shown at the top of Career, with a "No work experience yet" state for students.
- **Also on file:** fields the entries don't cover, such as language tests, industry and LinkedIn, stay below as rows.

The sample entries match each person's existing Education and Career fields.

## People directory

**People** (`#/people`, central data team only) lists everyone upGrad knows: one row per person.

- Each row shows life stage, the businesses that know them, lifecycle state, revenue, how many channels can reach them, and when they were last active.
- Above the list: key numbers, segments (leads, learning, alumni, minors) and a filter.
- **Open** takes you to the full 360 profile. The Overview also lists people recently looked up across teams.

## Sample lookups

The **Look up a person** screen searches sample data by exact phone or email (names are never used). The screen has no sample buttons, so type one of these:

| Search | What it shows |
| --- | --- |
| `ananya.r@gmail.com` | Ananya R. (V2's default): the Learner 360 sample, a WP learner who was an SA lead and is now a new KnowledgeHut lead |
| `arjun.kumar88@gmail.com` | Arjun: learning with WP, alumnus of Internshala, re-acquired through a paid ad. Full profile with photo |
| `+91 98234 41127` | Ananya: known to 3 businesses, no consent for cross-business offers, a "worth acting on" moment |
| `rohan.mehta07@gmail.com` | Rohan: a Study Abroad lead with Sales Insights scores and an "intake passed" moment |
| `+91 99001 22334` | A shared family phone: two linked people to choose from, one of them a minor (restricted) |
| Any other valid number or email | New to upGrad |

Phone numbers work with or without `+91`, spaces or a leading `0`. Only verified phones and emails are used to match.

## Profile and data model

The profile and data model follow the Learner 360 Data Model v4 and its four sheets (Learner Profile, Academic & Skill Profile, Activity Data, Insights).

The 12 Activity event types marked in yellow in v4 are left out of this phase: stage change, owner change, follow-up scheduled, next step agreed / completed, order placed, subscription, coupon used, progress milestone, live session attended, recorded content watched, platform login and support ticket. Nothing in the prototype shows or depends on them. For example, course progress is the latest value only, lifecycle state comes from the lead's current stage plus payments and enrolments, and learning health uses progress, submissions and assessments instead of attendance.

- **Header card:** photo, life stage, age band (the date of birth isn't stored), city, owning business, profile completeness and the global person ID. Which channels are allowed is in **Personal › Consent & preferences**.
- **Worth acting on:** moments such as an intake that has passed, a new enquiry in another business or a certificate issued.
- **Five sections, one row of tabs:**
  - **Personal:** contact, personal details, consent.
  - **Education:** education before upGrad, courses with upGrad, skills.
  - **Professional:** career, aspiration, outlook (intent, next-best programme, call-analysis scores).
  - **Financial:** financial profile, plus revenue and programmes bought with upGrad.
  - **Activity:** where they are with each business (Prospect → … → Alumni), an engagement summary, then the timeline. One filter narrows the timeline by type or business.

  One section shows at a time, and the arrow keys move between them. Switching sections while scrolled down brings the new section to its top, just below the pinned bars, and its content fades in.
- **Always in view:** the person and the section tabs stay on screen while you scroll, in every layout.
  - In the left-panel layouts, the person card stays pinned.
  - In the top-header layouts, a slim bar with the photo, name and key facts takes over once the card scrolls away.
  - The tabs stay pinned at the top, or beside the details when they're listed on the left or right.
- **Locked financial details:** the Financial section starts locked, and its tab shows a small lock. You can see which fields exist, but every value is masked.
  - Selecting the **eye** at the top of the section asks for the team password (demo: `upgrad2026`). The right password shows the values for that profile.
  - Selecting the eye again hides them, and so does opening another person.
  - After three wrong tries, unlocking pauses for 30 seconds.
  - Counsellors from another business never see financial details, password or not.
  - In this prototype the password is checked in the browser. The real product should check it on the server, against the viewer's role, and log each unlock.
- **Less up front:** above the tabs there's only the person card and any "Worth acting on" moments.
- **Card layout:** the detail cards stack in one column on every screen size. On wider cards each row reads label | value | source. In V1 (and the retired draft before it) the left profile column uses lighter type and lists its facts as label and value pairs.
- Every value shows its source system (Prism, LSQ, HubSpot, OMS, SA/WP Sales Insights, CMS or a rule). Where sources conflicted, the merge rule that picked the value is shown.
- **Sensitivity:** T1 contact details are hidden until the viewer gives a reason. T2 values are bands only: the financial profile needs a reason before it's shown. Other businesses never see T2 values, payments or revenue. Every reveal is logged.
- **Data dictionary** (central data team only, `#/data`) lists all 105 items in scope from the four sheets (the 12 yellow-marked events are left out):
  - **For each item:** sample coverage (share of profiles that have it), main source and its share of values, last sync, and whether its mapping is verified (from each sheet's "Check" column), plus its source fields, merge rule, storage, sensitivity tier and P0/P1/P2 priority.
  - **Across the page:** headline numbers (P0 coverage, weak P0 items, sources syncing, mappings verified), source health, who can see what and how a value is stored.
  - **Tables:** the tables behind the profile sit in a collapsed "For engineers" section.

Sample photo: `assets/profile-arjun.jpg`.


| File | Screen | What it answers |
| --- | --- | --- |
| `design/Main.dc.html` | Overview | How far Phase 1 has got, organised by the proposal's three objectives: know our customers, stop buying back our own learners (CAC), right moment and right need. Plus a foundation block for event-schema and consent health. |
| `design/Profile360.dc.html` | Look up a person | A counselor on a call looks someone up by phone or email and sees straight away whether upGrad already knows them, their journey across businesses, purpose-bound consent, masked contact details and a read-only activity timeline. |
| `design/Identity.dc.html` | Identity & audits | The matching rules (merge only on verified phone or email, link but never merge on a shared phone, ignore similar names or devices), an audit of sampled automatic merges that sets the false-merge rate, and the reversible merge log. |

`design/canvas.json` holds the layout of the three artboards on the canvas.

## Design principles

- **Apple-like restraint.** Black, greys and white, with upGrad red only for the single thing that needs attention on a screen. Large titles, grouped lists with hairline dividers, one number or one chart per section.
- **Built from the proposal's logic.** One profile per person; businesses keep their own CRMs, so the 360 view is read-only; wrongly merging two people is worse than missing a match; consent is recorded per purpose and checked before outreach; personal data is masked and access is logged.
- **Phase 1 only.** Decisioning and cross-sell are shown as later phases. Targets in the proposal that are still `[X]%` stay as placeholders.

## About the file format

The `.dc.html` files are Design Component pages for the Claude design canvas. Each one is plain HTML with inline styles plus a small logic block, but it relies on the canvas runtime (`support.js`) for templating and interactivity, so opening a file straight from disk will not render it correctly. Use the live canvas link above to view and click through the screens.
