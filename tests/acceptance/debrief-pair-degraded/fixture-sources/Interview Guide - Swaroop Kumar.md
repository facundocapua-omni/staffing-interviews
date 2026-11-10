---
candidate: "Swaroop Kumar Reddy"
date: "2026-06-23"
round: "Technical + Behavioral"
interviewer: ""
tags: [interview-guide]
---

# Interview Guide — Swaroop Kumar Reddy

**Round:** Technical + Behavioral
**Estimated duration:** 60 min
**Interviewer(s):**
**Level assessed:** SSr Advanced AEM Developer

---

## Prior Context (read before the interview)

Swaroop has ~7 years in AEM, a valid ACE certification, and projects covering Content Fragments, OSGi, Sling Models, and MSM. He's been at Globant for 6 months (Qiddiya, Nissan projects). **Key watch points:** inflated description at IBM, content-author work listed as dev at Springroutes, and zero evidence of AEM as a Cloud Service across his entire career.

---

## Opening (5 min)

- [ ] Introduce yourself and explain the format
- [ ] "There are no right or wrong answers — we want to understand how you think and work"
- [ ] "We'll cover your AEM experience, some technical scenarios, and how you work with your team. You'll have time for questions at the end."

---

## Section 1 — CV Verification and Context (10 min)

*Goal: surface CV inconsistencies before diving into technical questions.*

**Opening question:**
> Walk me through your career path in AEM. How did you get to where you are today?

**Follow-up if Springroutes isn't clarified:**
> At Springroutes, the Krishshop project description mentions content creation, metadata management, and DAM. Was that role more development or content authoring?

**Follow-up on IBM:**
> At IBM you were an Associate Developer. The description mentions "expert-level guidance on AEM architecture and best practices." Can you tell me more about that team and what your actual day-to-day responsibilities were?

**What to look for:**
- Does he honestly acknowledge the limits of his earlier roles?
- Or does he defend inflated descriptions without concrete examples?
- Green flag: "it was a small team, we wore many hats," "that project was more authoring than development"
- Red flag: defends the descriptions but cannot give specific examples when probed

---

## Section 2 — Core AEM Technical (15 min)

*Goal: verify real depth, not surface-level familiarity.*

### 2A — Sling Models and OSGi

**Question:**
> Explain how a Sling Model works. What annotations do you use regularly, and what does each one do?

**Follow-up:**
> When would you use a Sling Model instead of a Servlet, and vice versa?

**Deep follow-up:**
> Tell me about a time you had to debug an OSGi service that wasn't registering correctly. What was the issue and how did you resolve it?

**Expected answer (Senior level):**
- `@Model`, `@Inject` / `@Via`, `@Self`, `@ScriptVariable`, difference between `adaptables`
- Servlet: complex HTTP logic, REST endpoints. Sling Model: component/view logic.
- Debugging: Felix console (`/system/console/components`), unsatisfied `@Reference` dependencies, bundle lifecycle

**Watch for:**
- Cannot name specific annotations
- Cannot explain when to choose one over the other
- Has never used the Felix console for debugging

---

### 2B — Content Fragments and Headless

**Question:**
> In Qiddiya and Nissan you worked with Content Fragments and AEM Content Services. Walk me through the full flow: from an author creating a CF to the frontend consuming it.

**Follow-up:**
> What's the difference between using Content Services versus AEM's GraphQL API to expose Content Fragments?

**Follow-up if he mentions GraphQL:**
> Have you worked with persisted queries? Why are they recommended in production environments?

**Expected answer (Senior level):**
- CF Model → CF instance → Content Services endpoint (`/api/assets/`) or exported via Sling Model
- Content Services: REST-based, good for simpler integrations. GraphQL: more flexible, avoids over-fetching
- Persisted queries: security (GET vs POST), CDN cacheability

**Watch for:**
- Cannot distinguish Content Fragments from Experience Fragments
- Cannot explain how to configure a Content Services endpoint
- Has never worked with AEM GraphQL

---

### 2C — Svelte + AEM Integration (Qiddiya)

**Question:**
> At Qiddiya you integrated Svelte with AEM. How did that integration work? Was it SPA Editor, a decoupled front-end setup, or something else?

**Follow-up:**
> What were the specific challenges of combining AEM authoring with a frontend framework like Svelte?

**Why this matters:**
This is the most technically distinctive item on the CV. AEM's SPA Editor officially supports React and Angular — not Svelte. How they built this reveals real architectural understanding. A well-reasoned answer here is a strong positive signal.

**Expected answer (Senior level):**
- Should describe whether it was headless/decoupled (AEM delivers JSON, Svelte consumes) or used custom wrappers
- Should acknowledge limitations for content authoring in that setup
- Green flag: understands the trade-off between editorial experience and developer freedom

---

### 2D — AEM as a Cloud Service (gap check)

**Question:**
> In your recent projects, did you work with AEM as a Cloud Service or with on-premise / AMS instances?

**Follow-up (if only on-prem/AMS):**
> Do you know the main differences between AEM 6.5 and AEMaaCS from a development perspective? For example, how it affects OSGi bundle development or the deployment model?

**Expected answer for SSr level:**
- Should at least know the key differences: no mutable `/apps` at runtime, Cloud Manager, pipeline-based deployment, mutable vs immutable content split
- If unaware: this is a real gap. Evaluate willingness and capacity to learn.

---

## Section 3 — Soft Skills: Communication and Collaboration (10 min)

**Main question:**
> Tell me about a time you had to explain a technical AEM constraint to a non-technical person — a content author, a business stakeholder, or a PM. How did you handle it?

**Follow-up:**
> What was the hardest part? How did you know they understood?

**What to look for:**
- Adapts language to the audience
- Gives concrete examples, not generalizations ("I always draw diagrams")
- Treats communication as bidirectional
- Green flag: mentions training content authors (he has evidence of this in OOKA)
- Red flag: "technical and non-technical people just don't understand each other, it's normal"

---

## Section 4 — Growth Mindset and Attitude (10 min)

**Main question:**
> What's the most important technical thing you've learned recently, and how did you learn it?

**Follow-up:**
> Is there anything in AEM or adjacent technologies that you feel you still need to deepen or would like to learn?

**Second question:**
> Tell me about a technical decision you made that, looking back, you would change. What did you learn from it?

**What to look for:**
- Genuine continuous learning, not performative answers
- Honest about gaps — AEMaaCS is a natural opening if he brings it up on his own
- Can articulate why he'd change a decision, not just "I made a mistake"
- Green flag: mentions AEMaaCS or EDS as a growth area
- Red flag: "I already have everything I need for this role covered"

---

## Section 5 — Ownership and Problem Solving (5 min)

**Question:**
> Describe a time something broke in a production or staging AEM environment. What happened, what was your role, and how did you resolve it?

**Follow-up (STAR method):**
> What changed in your process or your team's process after that incident?

**What to look for:**
- Takes ownership of his part (doesn't blame team/client/infrastructure)
- Describes concrete actions ("I checked the logs, I contacted the DevOps team")
- Extracts a real lesson, not a generic one

---

## Closing (5 min)

- [ ] **Situational question:** Why are you exploring a new opportunity outside of Globant? (Only 6 months in — worth asking)
- [ ] "Is there anything about your experience or skills that we didn't cover that you'd like me to know?"
- [ ] Open floor for candidate questions
- [ ] Explain next steps and timeline
- [ ] Thank them for their time

---

## Signals to Watch in Candidate Questions

| Candidate question | What it may indicate |
|---|---|
| About the technical stack / AEMaaCS | Genuine technical curiosity ✅ |
| About the team, dynamics, how work is organized | Interest in culture and fit ✅ |
| About growth opportunities | Positive ambition ✅ |
| Only about salary / working hours | Focused on conditions, not the role ⚠️ |
| No questions at all | Disengagement or excessive nervousness ⚠️ |

---

## Live Interview Notes

*(Take notes here in real time)*

**CV inconsistencies — confirmed / refuted:**
-

**Technical evidence observed:**
-

**Soft skills observed:**
-

**Questions the candidate asked:**
-

---

## Bias Reminder

- [ ] Score with the rubric BEFORE discussing with other interviewers
- [ ] Don't over-weight the ACE certification — it's a credential, not a proxy for deep experience
- [ ] Cultural bias: candidates from India may be more reserved when describing personal achievements
- [ ] Don't penalize the AEMaaCS gap if he demonstrates learning capacity and acknowledges it honestly
