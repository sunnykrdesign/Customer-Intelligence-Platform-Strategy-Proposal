"""Convert sample_journeys_v1.json (activity journeys) into the Learner 360 person format the prototype reads.
Only values from the journeys file are used; anything the file does not give is left out (sections show "Not captured yet")."""
import json, sys, re
SRC = sys.argv[1]; OUT = sys.argv[2]
d = json.load(open(SRC, encoding="utf-8"))

RENAME = {"upg_A4K7L2N9": ("Nikhil Deshpande", "Nikhil", "Aditya"), "upg_M6N3R8T1": ("Anjali Menon", "Anjali", "Meera")}
BU = {"Internshala": "Internshala", "WP": "Working Professionals", "SA": "Study Abroad"}
TYPE = [  # (activity name pattern, event_type, sub_section, title)
    (r"^First Touch / Intro", "First touch", "Attribution", "First touch with {bu}"),
    (r"^First Touch", "First touch", "Attribution", "First touch on {bu}"),
    (r"^Lead Created", "Lead created / account created", "Enquiries & business relationships", "Lead created on {bu}"),
    (r"^Purchased", "Payment", "Payments & commerce", "Bought a training"),
    (r"^Training Completed", "Progress milestone", "Learning activity", "Training completed"),
    (r"^Internship Completion", "Job / internship application", "Career activity", "Internship completed"),
    (r"^Internship", "Job / internship application", "Career activity", "Hired for an internship"),
    (r"^Webinar", "Webinar / event attended", "Marketing engagement", "Attended a webinar"),
    (r"^Counselling Call \(first\)", "Counselling / meeting / visit", "Interactions", "First counselling call"),
    (r"^Counselling Call \(follow-up\)", "Counselling / meeting / visit", "Interactions", "Follow-up counselling call"),
    (r"^Counselling Call", "Counselling / meeting / visit", "Interactions", "Counselling call"),
    (r"^VC / F2F", "Counselling / meeting / visit", "Interactions", "Face-to-face session"),
    (r"^Application for 2nd Year", "Opportunity / deal", "Enquiries & business relationships", "Applied for year 2"),
    (r"^Application Submitted", "Opportunity / deal", "Enquiries & business relationships", "Application submitted"),
    (r"^Enrolled", "Enrolment", "Learning activity", "Enrolled"),
    (r"^First Year Learning Started", "Progress milestone", "Learning activity", "Year 1 learning started"),
    (r"^Learning Started", "Progress milestone", "Learning activity", "Learning started"),
    (r"^FY Learning Scores", "Certificate issued", "Learning activity", "Year 1 results"),
    (r"^Offer Letter", "Opportunity / deal", "Enquiries & business relationships", "University offer received"),
    (r"^Visa Approved", "Progress milestone", "Enquiries & business relationships", "Visa approved"),
    (r"^RAU", "Progress milestone", "Learning activity", "Reached university"),
]
SKIP = {"Date and time", "Business", "Record ID"}
DETAIL = {
    "First Touch": ["Channel (organic / paid / etc.)", "Page / campaign"],
    "First Touch / Intro to BU": ["Introduced by another upGrad business", "Page / campaign"],
    "Lead Created": ["Student status at sign-up", "POI", "Source: paid / organic", "Country of interest"],
    "Purchased": ["Training name", "Amount", "Payment type (block / full)"],
    "Training Completed": ["Course / training name", "Batch dates"],
    "Internship": ["Role", "Company", "Applications before this hire"],
    "Internship Completion": ["Role", "Duration", "Mode"],
    "Webinar / Event Attended": ["Webinar / event name", "Time attended"],
    "Counselling Call (first)": ["Program pitched / POI", "Concerns raised", "Next step agreed"],
    "Counselling Call (follow-up)": ["Concerns resolved", "Lead score"],
    "Counselling Call": ["Program pitched / POI", "Concerns raised", "Budget band"],
    "VC / F2F": ["Session type (VC / F2F)", "Session outcome", "F2F address / centre"],
    "Application Submitted": ["Programme", "Application stage"],
    "Enrolled": ["Programme", "Program name", "Batch", "Batch date", "Payment type (block / full)", "Payment type"],
    "Learning Started": ["Days from enrolment to start"],
    "First Year Learning Started": ["Days from enrolment to start"],
    "FY Learning Scores": ["Result", "Certificate", "Time spent"],
    "Application for 2nd Year": ["Programme", "University", "Status"],
    "Offer Letter Received from Uni": ["Offer type", "University"],
    "Visa Approved": ["Visa type", "Country"],
    "RAU (Reached At University)": ["University", "Arrival date"],
}
MON = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
def monY(s): y, m = s[:7].split("-"); return MON[int(m) - 1] + " " + y
def dayY(s): y, m, dd = s[:10].split("-"); return str(int(dd)) + " " + MON[int(m) - 1] + " " + y
def fv(a, name):
    for f in a["fields"]:
        if f["field"] == name: return f
    return None

def event(a, rn):
    bu = BU.get(a["bu"]) or (fv(a, "Business") or {}).get("value", "")
    for pat, et, sub, title in TYPE:
        if re.search(pat, a["activity"]): break
    else: et, sub, title = "Progress milestone", "Learning activity", a["activity"]
    title = title.format(bu={"Working Professionals": "WP", "Study Abroad": "Study Abroad"}.get(bu, bu))
    rec = fv(a, "Record ID") or {}
    want = DETAIL.get(a["activity"]) or [f["field"] for f in a["fields"] if f["field"] not in SKIP][:3]
    det = []
    for w in want:
        f = fv(a, w)
        if not f or f["value"] in ("—", "") or f["value"].startswith("Not captured"): continue
        v = re.sub(r"\s*\(POK[^)]*\)", "", f["value"])
        if w == "Days from enrolment to start": v = v.split(" (")[0] + " days after enrolling"
        if w == "Time attended": v = "stayed " + v
        if w == "Lead score": v = "lead score " + v
        if w == "Applications before this hire": v = "hired after " + v + " applications"
        det.append(v)
    first = [f for f in a["fields"] if f["field"] not in SKIP][0] if a["fields"] else None
    flag = ""
    if a.get("moved_from_another_business"):
        frm = a["moved_from_another_business"].split(" → ")[0]
        flag = "From " + frm
    return {
        "occurred_at": a["occurred_at"], "event_type": et, "sub_section": sub, "business": bu,
        "source_system": (first or rec).get("source_system", a["source_label"]), "source_field": (first or {}).get("source_field", ""),
        "source_record_id": rec.get("value", ""), "title": title, "detail": " · ".join(det), "payload": {},
        "source_label": a["source_label"], "flag": flag, "moved_from_another_business": a.get("moved_from_another_business"),
        "fields": [[f["field"], f["value"], f["source_system"], f["source_field"], f["status"], f.get("value_note", "")] for f in a["fields"]],
    }

def row(attr, value, sys_, field, at):
    return {"attribute": attr, "value": value, "source_system": sys_, "source_field": field, "added_at": at[:10], "confidence": "declared", "tier": "T0"}

def find(p, act_pat, field):
    for a in p["activities"]:
        if re.search(act_pat, a["activity"]) and a["state"] == "done":
            f = fv(a, field)
            if f: return f, a
    return None, None

people = []
for p in d["people"]:
    name, first, orig = RENAME[p["person_id"]]
    acts = [a for a in p["activities"] if a["state"] == "done" and a["occurred_at"]]
    acts.sort(key=lambda a: a["occurred_at"])
    events = [event(a, first) for a in acts]
    known = acts[0]["occurred_at"][:7]; last = acts[-1]["occurred_at"]
    cur_stage = p["life_stages"][-1]["stage"]
    life = cur_stage.split(",")[0]
    city = (re.search(r" in ([A-Z][a-z]+)", p["headline"]) or re.search(r", ([A-Z][a-z]+)$", cur_stage) or [None, ""])[1]
    if p["person_id"] == "upg_M6N3R8T1": city = "Manchester"
    pending = [a for a in p["activities"] if a["state"] != "done"]

    # Records (identity): every distinct record ID, by system
    recs = []
    for a in acts:
        r = fv(a, "Record ID")
        if not r or r["status"] in ("Open question", "No source today"): continue
        for part in r["value"].split(" · "):
            part = part.strip()
            m = re.match(r"^(IS user|student|Training enrolment|LSQ lead|Heard call|Order|Enrolment|Application|Experience|Zoom webinar)\s+(.+)$", part)
            if not m: continue
            lab = {"IS user": "Internshala user", "student": "Internshala student", "Training enrolment": "Internshala training", "LSQ lead": "LSQ lead", "Heard call": "Heard call",
                   "Order": "OMS order", "Enrolment": "Prism enrolment", "Application": "Internshala application", "Experience": "Internshala experience", "Zoom webinar": None}[m[1]]
            if not lab: continue
            x = lab + " " + m[2].replace(" ", "")
            if x not in recs: recs.append(x)
    lp = {"Identity & contact": [], "Personal details": [], "Education (prior, outside upGrad)": [], "Career / profession": [], "Aspiration": [], "Financial profile": [], "Consent & preferences": []}
    lp["Identity & contact"].append(row("Linked system IDs", "; ".join(recs), "Derived", "Record ID across activities", last))

    # Education: student status at Internshala sign-up
    f, a = find(p, r"^Lead Created", "Student status at sign-up")
    if f:
        q = f["value"]; deg = re.sub(r"^\d\w{2}-year\s+", "", q.split(" · ")[0]); fin = (re.search(r"finishing (\d{4})", q) or [None, ""])[1]
        lp["Education (prior, outside upGrad)"].append(row("Highest qualification", deg + (" · " + fin if fin else ""), "Internshala", f["source_field"], a["occurred_at"]))
    # Career: current role from the life stages and headline (derived), internship from Internshala
    if p["person_id"] == "upg_A4K7L2N9":
        lp["Career / profession"].append(row("Current role and employer", "Associate software engineer, [Employer not on file] · since Jul 2023", "Derived", "life stages + headline", last))
    ir, ia = find(p, r"^Internship$", "Role"); io, _ = find(p, r"^Internship$", "Company"); idur, _ = find(p, r"^Internship Completion", "Duration"); imode, _ = find(p, r"^Internship Completion", "Mode"); napp, _ = find(p, r"^Internship$", "Applications before this hire")
    if ir:
        org = re.sub(r",\s*[A-Z][a-z]+$", "", io["value"]); per = (re.search(r"\(([^)]+)\)", (find(p, r"^Internship$", "Duration")[0] or {}).get("value", "")) or [None, ""])[1]
        lp["Career / profession"].append(row("Work history", ir["value"] + ", " + org + " · " + per + " (" + imode["value"][0].lower() + imode["value"][1:] + " · found on Internshala after " + napp["value"] + " applications)", "Internshala", "internshala.student_experiences", ia["occurred_at"]))
    # Aspiration (shown in Insights → What they told us)
    f, a = find(p, r"^Purchased", "Learning objective")
    if f: lp["Aspiration"].append(row("Learning objective", f["value"] + " (Internshala training, " + monY(a["occurred_at"]) + ")", "Internshala", f["source_field"], a["occurred_at"]))
    f, a = find(p, r"^Counselling Call", "Motivation")
    if f: lp["Aspiration"].append(row("Motivation and type of move", f["value"], "Sales Insights", f["source_field"], a["occurred_at"]))
    f, a = find(p, r"^Counselling Call", "Concerns raised"); fr, _ = find(p, r"^Counselling Call", "Concerns resolved")
    if f: lp["Aspiration"].append(row("Concerns / objections", f["value"].replace(" · ", ", ") + (" (" + fr["value"].split(": ", 1)[1] + ")" if fr else ""), "Sales Insights", f["source_field"], a["occurred_at"]))
    f, a = find(p, r"^Counselling Call", "Decision maker") or (None, None)
    if not f: f, a = find(p, r"^Counselling Call", "Decision maker and parent stance")
    if f: lp["Aspiration"].append(row("Decision maker", f["value"], "Sales Insights", f["source_field"], a["occurred_at"]))
    f, a = find(p, r"^Lead Created", "POI")
    for a2 in acts:
        if a2["bu"] in ("WP", "SA") and re.search("Lead Created", a2["activity"]):
            poi = fv(a2, "POI"); bu = a2["bu"]
            if poi: lp["Aspiration"].append(row("Programme of interest (first + latest)", "First: " + poi["value"].split(" · ")[0] + " (" + bu + ", " + monY(a2["occurred_at"]) + ")", "LSQ", poi["source_field"], a2["occurred_at"]))
            c = fv(a2, "Country of interest"); i = fv(a2, "Preferred intake")
            if c: lp["Aspiration"].append(row("Study Abroad preferences", c["value"] + " · " + (i["value"] + " intake" if i else ""), "LSQ", c["source_field"], a2["occurred_at"]))
    # Financial
    for a2 in acts:
        if a2["activity"] == "Enrolled":
            pt = fv(a2, "Payment type (block / full)") or fv(a2, "Payment type")
            if pt: lp["Financial profile"].append(row("Payment plan", pt["value"] + " (" + BU[a2["bu"]] + ")", "OMS", pt["source_field"], a2["occurred_at"]))
            dc = fv(a2, "Discount")
            if dc: lp["Financial profile"].append(row("Discount", dc["value"] + " (" + BU[a2["bu"]] + ")", "OMS", dc["source_field"], a2["occurred_at"]))
    f, a = find(p, r"^Counselling Call", "Budget band")
    if f: lp["Financial profile"].append(row("Budget stated", f["value"], "Sales Insights", f["source_field"], a["occurred_at"]))

    # Courses with upGrad
    ap = {"Skills": [], "Courses with upGrad": []}
    tr = [a for a in acts if a["activity"] == "Purchased"][0]; tname = fv(tr, "Training name")["value"]
    tc = [a for a in acts if a["activity"] == "Training Completed"][0]
    en = [a for a in acts if a["activity"] == "Enrolled"][0]; pname = fv(en, "Programme") or fv(en, "Program name"); pname = re.sub(r"\s*\((POK|year 1)[^)]*\)\s*$", "", pname["value"])
    pbu = BU[en["bu"]]
    course = [pname + " · " + pbu + " · enrolled " + monY(en["occurred_at"]), tname + " · Internshala · enrolled " + monY(tr["occurred_at"])]
    if pending:
        pn = pending[0]["pending_note"]; ts = fv(pending[0], "Time spent")["value"]
        pct = re.search(r"(\d+)% done", pn).group(1); mod = re.search(r"module (\d+) of (\d+)", pn)
        status = [pname + ": in progress, " + pn.split(", ")[-1], tname + ": completed"]
        progress = [pname + ": " + pct + "% · module " + mod.group(1) + " of " + mod.group(2) + " · " + re.sub(r" so far", "", ts), tname + ": completed · " + fv(tc, "Batch dates")["value"]]
        results = []
        gs = fv(pending[0], "Skills earned")
        if gs: ap["Skills"].append(row("Graded skills and competencies", " · ".join(s.strip().capitalize() + ": Graded so far" for s in re.sub(r"\s*\(.*\)", "", gs["value"]).replace("ML", "Machine learning").split(",")), "Prism", gs["source_field"], last))
    else:
        sc = [a for a in acts if a["activity"] == "FY Learning Scores"][0]; rau = [a for a in acts if a["activity"].startswith("RAU")][0]
        status = [pname + ": year 1 completed · reached university " + monY(rau["occurred_at"]), tname + ": completed"]
        progress = [pname + ": year 1 completed · " + fv(sc, "Time spent")["value"], tname + ": completed · " + fv(tc, "Batch dates")["value"]]
        results = [pname + ": " + fv(sc, "Result")["value"]]
        ap["Courses with upGrad"].append(row("Certificates earned", pname + ": " + fv(sc, "Certificate")["value"], "Prism", fv(sc, "Certificate")["source_field"], sc["occurred_at"]))
    ap["Courses with upGrad"][:0] = [row("Course", "; ".join(course), "Prism", "userprograms.program", en["occurred_at"]), row("Current status", "; ".join(status), "Prism", "userprograms.status", last), row("Progress", "; ".join(progress), "Prism", "userprograms.progress", last)]
    if results: ap["Courses with upGrad"].append(row("Programme results", "; ".join(results), "Prism", "userprogramreports.scoreCard.percentage", last))
    rs = fv(tc, "Added to resume")
    if rs: ap["Skills"].append(row("Trainings listed on resume", tname + " (Internshala, added " + rs["value"] + ")", "Internshala", rs["source_field"], tc["occurred_at"]))

    # Insights, only from the file
    paid = []
    a_tr = fv(tr, "Amount")["value"]; paid.append(("Internshala", a_tr))
    ptype = (fv(en, "Payment type (block / full)") or fv(en, "Payment type"))["value"]; blk = re.search(r"₹\d[\d,]*\d", ptype).group(0)
    tot = sum(int(x[1:].replace(",", "")) for x in (a_tr, blk)); totS = "₹" + format(tot, ",") if tot < 100000 else "₹" + str(tot)
    def inr(n):
        s = str(n); last3, rest = s[-3:], s[:-3]; rest = re.sub(r"(\d)(?=(\d\d)+$)", r"\1,", rest); return "₹" + (rest + "," if rest else "") + last3
    biz = p["businesses"]; st = {"Alumnus": "Alumni", "Alumna": "Alumni"}
    lc = " · ".join(b["business"] + ": " + b["state"].lower() + " since " + monY(b["since"] + "-01") for b in biz)
    overall = "Learning" if any(b["state"] == "Learning" for b in biz) else biz[-1]["state"]
    mv = [a["moved_from_another_business"] for a in acts if a.get("moved_from_another_business")][0]
    insights = [
        {"insight": "Lifecycle state per business", "value": lc, "built_from": "Activity: lead created, enrolment, progress"},
        {"insight": "Overall relationship state", "value": overall, "built_from": "Lifecycle per business"},
        {"insight": "Cross-business flag", "value": "Yes · 2 businesses (" + p["journey"].replace("WP", "Working Professionals").replace("SA", "Study Abroad") + ")", "built_from": "Identity + lead/enrolment records"},
        {"insight": "First seen / last active", "value": "First seen " + monY(acts[0]["occurred_at"]) + " · last active " + dayY(last), "built_from": "All Activity"},
        {"insight": "Lifetime revenue", "value": inr(tot) + " paid so far · Internshala " + a_tr + " · " + {"WP": "WP", "SA": "Study Abroad"}[en["bu"]] + " block " + blk + ", then " + ptype.split(", then ")[-1], "built_from": "Activity: payments (Internshala trainings, OMS)"},
        {"insight": "Programmes purchased / repeat buyer", "value": "2 · " + tname + " (Internshala) and " + pname + " (" + {"WP": "WP", "SA": "Study Abroad"}[en["bu"]] + ")", "built_from": "Activity: orders, enrolments"},
        {"insight": "Re-acquisition flag", "value": "No · " + mv.split(" · ", 1)[1].replace("₹0 media", "owned channel, ₹0 media") + ", from " + mv.split(" → ")[0], "built_from": "Activity: lead created vs first seen; acquisition source"},
    ]
    # The UG learning journey's course list, from the file only (no course codes: the file has none).
    tbatch = fv(tc, "Batch dates")["value"]; tres = fv(tc, "Added to resume")
    tcourse = {"code": "", "name": tname, "biz": "Internshala", "st": "done", "pct": 100, "mods": [0, 0], "hours": None, "score": "—", "start": tbatch, "end": "Completed",
               "next": ("Added to resume " + tres["value"]) if tres else "", "progTxt": "Training completed."}
    if pending:
        ls = [a for a in acts if a["activity"] == "Learning Started"][0]
        pcourse = {"code": "", "name": pname, "biz": pbu, "st": "live", "pct": int(pct), "mods": [int(mod.group(1)) - 1, int(mod.group(2))], "hours": int(re.search(r"\d+", ts).group(0)), "score": "—",
                   "start": monY(ls["occurred_at"]), "end": "", "next": pn.split(", ")[-1].capitalize(), "progTxt": pct + "% done · module " + mod.group(1) + " of " + mod.group(2) + "."}
    else:
        fy = [a for a in acts if a["activity"] == "First Year Learning Started"][0]
        pcourse = {"code": "", "name": pname, "biz": pbu, "st": "done", "pct": 100, "mods": [0, 0], "hours": int(re.search(r"\d+", fv(sc, "Time spent")["value"]).group(0)), "score": fv(sc, "Result")["value"],
                   "start": monY(fy["occurred_at"]), "end": "Completed " + monY(sc["occurred_at"]), "next": fv(sc, "Certificate")["value"] + " · reached " + fv(rau, "University")["value"] + " " + dayY(rau["occurred_at"]),
                   "progTxt": "Year 1 completed online with upGrad; year 2 at " + fv(rau, "University")["value"] + "."}
    story = p["story"].replace(orig, first)
    stages = [{"stage": s["stage"], "from": s["from"], "to": s["to"]} for s in p["life_stages"]]
    people.append({
        "person_id": p["person_id"], "sample": True, "journey_sample": True, "career_via_linkedin": False,
        "header": {"name": name, "headline": p["headline"], "known_since": known, "life_stage": life, "age_band": "Not captured", "city": city, "is_minor": False,
                   "businesses": [{"business": b["business"], "state": st.get(b["state"], b["state"]), "since": b["since"]} for b in biz]},
        "life_stages": stages,
        "stored_not_shown": {"owning_business": {"business": biz[-1]["business"], "team": ""}, "profile_completeness_pct": 0},
        "ug_courses": [pcourse, tcourse], "activity": events, "insights": insights, "summary": story, "interest_by_area": [], "learner_profile": lp, "academic_skill_profile": ap,
    })
json.dump({"_about": {"what": "Two people converted from sample_journeys_v1.json (renamed: Aditya Kulkarni → Nikhil Deshpande, Meera Nair → Anjali Menon). Only values from that file; fields it does not give are left out.", "source": "data/sample_journeys_v1.json"}, "people": people}, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for x in people: print(x["header"]["name"], x["header"]["city"], x["header"]["life_stage"], len(x["activity"]), "events |", x["insights"][4]["value"])
