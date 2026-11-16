"""Convert learner360_full_profiles_v1.json (full Learner 360 profiles + journey activity) into the prototype's person format.
Profile sections, skills and insights are the file's own rows; activity milestones become events with every field kept.
Renames: Aditya Kulkarni -> Nikhil Deshpande, Meera Nair -> Anjali Menon (names and emails only)."""
import json, re, sys, copy
SRC, JOURNEY_CONVERTER, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
# Reuse the activity -> event mapping from the journeys converter (everything above its people loop).
src = open(JOURNEY_CONVERTER, encoding="utf-8").read()
ns = {"__name__": "jc"}; sys_argv = sys.argv; sys.argv = ["x", SRC, "/dev/null"]
exec(src[:src.index("people = []")], ns); sys.argv = sys_argv
event = ns["event"]
d = json.load(open(SRC, encoding="utf-8"))
REN = {"upg_A4K7L2N9": [("Aditya Kulkarni", "Nikhil Deshpande"), ("aditya.k@", "nikhil.d@"), ("a•••••@", "n•••••@"), ("Aditya", "Nikhil")],
       "upg_M6N3R8T1": [("Meera Nair", "Anjali Menon"), ("meera.nair@", "anjali.menon@"), ("m•••••@", "a•••••@"), ("Meera", "Anjali")]}
COURSES = {  # The UG learning journey's rows, rewritten into the "Title: value; Title: value" shape the page reads. Values are the file's.
    "upg_A4K7L2N9": {
        "Course": "Executive PG in Data Science and AI [sample] · Working Professionals · enrolled Mar 2025; Web Development · Internshala · enrolled Sep 2021",
        "Current status": "Executive PG in Data Science and AI: in progress, near completion; Web Development: completed",
        "Progress": "Executive PG in Data Science and AI: 91% · module 10 of 11 · 236 hours; Web Development: completed",
        "Programme results": "Executive PG in Data Science and AI: Interim 81%",
        "Certificates earned": None},
    "upg_M6N3R8T1": {
        "Course": "MSc Business Analytics pathway [sample] · Study Abroad · enrolled Feb 2024; Business Analytics · Internshala · enrolled Jun 2022",
        "Current status": "MSc Business Analytics pathway: completed: year 1 with upGrad, year 2 in Manchester; Business Analytics: completed",
        "Progress": "MSc Business Analytics pathway: 100% · module 8 of 8 · 410 hours; Business Analytics: completed",
        "Programme results": "MSc Business Analytics pathway: 82% · CGPA 3.6 of 4",
        "Certificates earned": "MSc Business Analytics pathway: Pathway year 1 completion certificate (Jun 2025)"}}
UG = {
    "upg_A4K7L2N9": [
        {"code": "", "name": "Executive PG in Data Science and AI", "biz": "Working Professionals", "st": "live", "pct": 91, "mods": [9, 11], "hours": 236, "score": "Interim 81%", "start": "Mar 2025", "end": "", "next": "Capstone next · certificate due on completion", "progTxt": "91% done · module 10 of 11."},
        {"code": "", "name": "Web Development", "biz": "Internshala", "st": "done", "pct": 100, "mods": [0, 0], "hours": None, "score": "—", "start": "6 Sep – 31 Oct 2021", "end": "Completed", "next": "Added to resume 4 Nov 2021", "progTxt": "Training completed."}],
    "upg_M6N3R8T1": [
        {"code": "", "name": "MSc Business Analytics pathway", "biz": "Study Abroad", "st": "done", "pct": 100, "mods": [8, 8], "hours": 410, "score": "82% · CGPA 3.6 of 4", "start": "Aug 2024", "end": "Completed Jun 2025", "next": "Pathway year 1 completion certificate (Jun 2025) · year 2 in Manchester", "progTxt": "Year 1 completed with upGrad, module 8 of 8; year 2 in Manchester."},
        {"code": "", "name": "Business Analytics", "biz": "Internshala", "st": "done", "pct": 100, "mods": [0, 0], "hours": None, "score": "—", "start": "20 Jun – 15 Aug 2022", "end": "Completed", "next": "Added to resume 20 Aug 2022", "progTxt": "Training completed."}]}

people = []
for p0 in d["people"]:
    pid = p0["person_id"]
    txt = json.dumps(p0, ensure_ascii=False)
    for a, b in REN[pid]: txt = txt.replace(a, b)
    p = json.loads(txt)
    acts = sorted([a for a in p["activity"] if a["state"] == "done" and a["occurred_at"]], key=lambda a: a["occurred_at"])
    # Profile rows: drop the ones the file marks as stored, not shown.
    lp = {s: [r for r in rows if not str(r.get("shown_on_ui", "Yes")).startswith("No")] for s, rows in p["learner_profile"].items()}
    for r in lp.get("Identity & contact", []):  # a phone value that carries a note: the number is the value, the note is kept beside it
        if r["attribute"] == "Phones (all known)":
            m = re.match(r"^(\+?[\d ]{8,})\s*(?:\(([^)]*)\))?\s*(?:·\s*(.+))?$", r["value"])
            if m and (m.group(2) or m.group(3)):
                r["value"] = m.group(1).strip(); r["conflict"] = "; ".join(x for x in [(m.group(2) + " number") if m.group(2) else "", (m.group(3) or "").strip()] if x) + "."
    ap = copy.deepcopy(p["academic_skill_profile"])
    by = {r["attribute"]: r for r in ap["Courses with upGrad"]}; rows = []
    for k, v in COURSES[pid].items():
        if v is None or k not in by: continue
        r = dict(by[k]); r["value"] = v; rows.append(r)
    ap["Courses with upGrad"] = rows
    h = p["header"]
    people.append({
        "person_id": pid, "sample": True, "journey_sample": True, "career_via_linkedin": False,
        "header": {k: v for k, v in h.items() if k not in ("journey", "life_stages")}, "life_stages": h.get("life_stages"),
        "stored_not_shown": p.get("stored_not_shown", {}), "summary": p.get("summary", ""), "interest_by_area": p.get("interest_by_area") or [],
        "learner_profile": lp, "academic_skill_profile": ap, "insights": p["insights"], "ug_courses": UG[pid],
        "activity": [event(a, "") for a in acts]})
json.dump({"_about": {"what": "Two people converted from learner360_full_profiles_v1.json (renamed: Aditya Kulkarni → Nikhil Deshpande, Meera Nair → Anjali Menon).", "source": "data/learner360_full_profiles_v1.json"}, "people": people},
          open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for x in people: print(x["header"]["name"], "|", x["header"]["city"], "|", len(x["activity"]), "events |", sum(len(v) for v in x["learner_profile"].values()), "profile rows |", len(x["insights"]), "insights")
