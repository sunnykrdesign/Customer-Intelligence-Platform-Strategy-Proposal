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

- **Share this view:** **Copy link** gives a link that opens exactly what you're looking at: the design version, the profile layout, the sticky bar, the pinned search bar, the sidebar menu items you've left on, the screen you're on and, on Look up a person, the person who's open. It skips sign-in and hides the Review panel, so the person you send it to sees only that view. For example: `…/?preview=1&ver=1&card=top&tabs=left&bar=high&pin=1&nav=overview,people,lookup&p=ananya&review=0#/lookup`
- **Design version:** four versions, named in order. A note under the switcher says which one is on screen. Links use `?ver=1` to `?ver=4`, and older links with the previous numbers still open the right version. Retired drafts, and old links or saved choices for them, open V4. Switching away from V4 puts every colour it changed back, so its theme never shows in another version. A V3 or V4 link also keeps the trend style, for example `&tr=stack`, and a V4 link keeps the theme, for example `&t=ocean`.
  - **V1 · Classic** (previously V3)
  - **V2 · Learner 360** (previously V4)
  - **V3 · Master** (previously V6)
  - **V4 · Crisp** (previously V7): the latest, and the default for new visitors.
- **Theme (V4 options):** **Crisp** (default) or **Ocean**. Shown only in V4. A saved or linked Bold or Vivid theme opens as Crisp.
- **Icons:** **Mono** (default) or **Colour**. Shown only in V4 with the Crisp theme. Colour fills the same icons with the theme's gradients: the figure cards run pink to periwinkle along each row, the sidebar runs rose to periwinkle, and activity events and profile sections get gradient discs with white icons. A link keeps the choice with `&ic=color`.
- **Tab icons:** **On** (default) or **Off**. Shown only in V4 with the Crisp theme. It shows or hides the icons on the profile section tabs (Identity, Personal, Education, Career, Aspiration, Financial, Consent) so you can compare both. A link keeps Off with `&ti=off`.
- **Sidebar:** **Current** (default), **Darker** or **Darkest**, all in the same lavender family. Shown only in V4 with the Crisp theme, on desktop. Current is the soft lavender #E5E3F0. Darker is #D6D2E8 with darker text. Darkest is a deep lavender-indigo #2C2850 with light text, a lighter upGrad red in the logo, and the current page still a white pill. Every shade keeps sidebar text at 4.5:1 or better. On Darker and Darkest the menu icons follow the text colour, even with Colour icons, because the gradient glyphs lose contrast on the deeper shades. A link keeps the choice with `&sb=darker` or `&sb=darkest`.
- **Person card:** **Current** (default, white), **Darker** or **Darkest**, the same lavender family as the sidebar shades. Shown only in V4 with the Crisp theme, in every Look up layout. Darker is #DCD8EC with darker text. Darkest is a deep lavender-indigo #2C2850 with light text, translucent chips, Show contact and tabs, white fact glyphs (with Mono icons), and a white Open in CRM so it stays the main action. A link keeps the choice with `&pc=darker` or `&pc=darkest`.
- **Header fold:** **Snap** (default) or **Smooth**. Shown only in V4 with the Crisp theme; it affects the Folding header layout.
  - **Snap:** a two-state header. It scrolls with the page while it's fully in view. The moment it reaches the top, it pins and folds into the slim bar in one eased step (about 0.3s), with the content below sliding up with it. Scroll back to where it started and it opens again the same way.
  - **Never cut off:** the card is never half folded or partly off the screen, whether or not the search bar is pinned.
  - **Steady behaviour:** the page never scrolls on its own, and the tab slider moves with the tabs. Scroll anchoring is off in this mode, so the fold can't nudge the page back.
  - **Smooth:** the old behaviour, where the card shrinks and fades step by step as you scroll.
  - A link keeps Smooth with `&fold=smooth`.
- **Spacing:** **Compact** (default) or **Current**. Shown only in V4 with the Crisp theme. Compact tightens vertical spacing across V4:
  - **Person card:** less room above it (the space above the photo drops from 61px to 29px in the Folding header layout), with the person header about 60px shorter.
  - **Pages:** less room at the top of every page and between sections, and slimmer padding in cards, figure tiles and profile rows.
  - A link keeps Current with `&sp=current`.
- **Fact icons:** **On** (default) or **Off**. Shown only in V4 with the Crisp theme. Each fact on the person card (life stage, age band, city, owner, fields filled) gets an icon tile from the design-system set: a briefcase, or a graduation cap for students, then a calendar with a person, a location pin, a team and a pie. With Icons on Mono the tiles are ink on soft lavender; on Colour each fact gets its own pastel tile and tinted glyph. A link keeps Off with `&fi=off`.
- **Look up a person · layout** (all versions): pick where the **person card** sits (Left panel or Top header) and where the **section tabs** sit (Top, Left or Right). That makes six combinations, and a small diagram shows the current one.

- **Sticky bar:** how strongly the pinned person and tabs stand out once you scroll (default **Mid**):
  - **Minimum:** a light bar with a hairline.
  - **Mid:** a white card bar with a soft shadow and a larger name.
  - **High:** a raised two-row card with photo, name, key facts, owner and completeness chips and the CRM button, with the tabs below.
- **Pin the search bar** (on by default): keeps "Who's on the line?" at the top of Look up a person while you scroll, with the pinned person and tabs sitting just below it. A new search opens the person at the top.
- **Locked sections:** shows the demo team password.
- **Sidebar menu:** an on/off switch for each sidebar item: Overview, People, Look up a person, Identity & audits, Data dictionary and Later phases.
  - Hidden items leave the sidebar, and links to them open the next visible page.
  - At least one page always stays on.

Your choices are remembered on that browser.

## Design versions

Four versions are in the switcher: V1 · Classic, V2 · Learner 360, V3 · Master and V4 · Crisp. Earlier drafts are retired, and links to them open V4.

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
  - **Sticky bar strength (Review → Sticky bar) decides what stays pinned:** **Minimum** keeps only the tabs and Find, with the name once the card has gone. **Mid** adds the photo and facts. **High** also pins the owners, who may be contacted (with Show contact) and the things to act on, so they move off the card and out of the dock. Contact and actions always show once on screen.
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
- **V4 · Crisp** (previously V7; the latest and the default): V3 with a new visual layer and two themes (Review → Theme). Bold and Vivid were removed.
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
