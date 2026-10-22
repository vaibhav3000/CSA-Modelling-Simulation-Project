# E0 240: Modeling and Simulation — COURSE KNOWLEDGE BASE (MCQ-Optimized)

**Purpose:** AI-readable exam knowledge base built from ALL lecture slides. Designed for fast, accurate retrieval to answer MCQs ("Which option is correct / false / NOT true?", "X vs Y?", "Which formula?", "Which step comes first?", "Which value is correct?").

**Instructor:** Sumit K. Mandal (skmandal@iisc.ac.in), CSA A359, IISc. Office hours: Friday 12:30–1:00 PM, CSA A359. *(L1 S2)*
**Teaching Assistants:** Mohammed Sufyan Azam, Vivek Kumar, Samip Poudel. *(L1 S2)*

**Source files processed (complete, in order):**
1. `1_Lecture_11_08_26.pdf` — Lecture #1, 11 Aug 2026, 32 slides
2. `2_Lecture_13_08_26.pdf` — Lecture #2, 13 Aug 2026, 47 slides
3. `3_lecture_18_08_26.pdf` — Lecture #3, 18 Aug 2026, 13 slides
4. `4_lecture_20_08_26.pdf` — Lecture #4, 20 Aug 2026, 24 slides

All 116 slides were processed, including image-only, handwritten, and figure-based slides (transcribed below). Slide titles in the decks: "Journey from Mobile Platforms to Self-Powered Wearable Systems" (deck template title; actual content is the Modeling & Simulation course).

**How to use:** Search by keyword; every fact carries a source tag *(L# S#)* = Lecture # / Slide #. Sections "MCQ-Relevant Facts", "Common Confusions", "MCQ Traps" hold the answer-discriminating details. Consolidated cross-lecture material is in the GLOBAL EXAM KNOWLEDGE INDEX at the end.

---

# Lecture 1: Course Introduction + Examples from Computer Systems and Road Traffic

**Date:** 11 August 2026
**Source File:** `1_Lecture_11_08_26.pdf` (32 slides)

## Topics Covered
- Course logistics, evaluation criteria, timeline *(L1 S3–S13)*
- Course scope: Modeling & Simulation awareness — why, what, how *(L1 S13)*
- Example from Computer Systems: simulating core & memory of SoC; modelling power & performance of SoCs *(L1 S14, S22, S26)*
- Example outside Computer Systems: road traffic *(L1 S14, S26)*
- Typical structure of a core (Knights Landing / Xeon Phi) *(L1 S15)*
- Components of heterogeneous SoCs; designer considerations *(L1 S16–S17)*
- Models vs. simulation; gem5 simulator *(L1 S18–S19)*
- Queue simulation overview (switch micro-architecture example) *(L1 S20–S21)*
- Why power-performance modelling matters; one technique (linear regression); use-case (dynamic power management) *(L1 S23–S25)*
- Road as a queuing network; metrics for different cities *(L1 S27–S28)*
- How to model: stochastic process, Markov chain, queuing theory *(L1 S29)*
- Key takeaways *(L1 S32)*

## Key Definitions
- **Logistics:** Class Tue/Thu 11:35 AM–1:05 PM (5-min cool-down after previous class), room CSA 112 (Ground Floor). Almost **50% of lectures via board-work** (take notes). Course material on Teams. **Absolutely no extension of deadlines** — "Unfairness is a part of life unfortunately." *(L1 S4)*
- **Attendance:** NO attendance is taken, BUT students are **evaluated on a daily basis**. *(L1 S5)*
- **Class participation (20%):** Instructor's goal = know all names; students should ask AND answer (meaningful) questions. "*If you are silent, you are not learning*" — but do not talk just to talk. Problems → office hours. *(L1 S9)*
- **Purpose of course material:** AI can teach scientific material (e.g., "lecture material on Markov chain" in GPT); what AI cannot develop is **'practical awareness'**. Course = developing awareness of Modeling and Simulation (why, what, how). New teaching ways tried (e.g., top-down vs bottom-up). *(L1 S13)*

## Core Concepts

### Evaluation Criteria (total = 100%) *(L1 S5)*
| Component | Weight |
|---|---|
| Assignments | 30% |
| Quiz | 10% |
| Class participation | 20% |
| Project **or** Exam | 40% |

### Assignments (30%) *(L1 S6–S7)*
- 5 assignments. Marks are **sorted**; X is the sorted array.
- **Grade formula:** $0.4 \cdot X(3) + 0.2 \cdot (X(2) + X(4)) + 0.1 \cdot (X(1) + X(5))$
  - **Higher weight to the median** (X(3)), lower weight to the outliers.
- Late submission: up to **3 days** after deadline; $Y = X(1 - d \cdot 0.1)$ where Y = final grade, X = original grade, d = number of days delayed. Slide also states "**One late day is allowed**."
- Mix of coding and descriptive work; **submit in PDF format** (not handwritten/scanned).
- Coding languages: MATLAB, Python, C/C++, …
- Evaluation criteria: **Correctness, Clarity, Conciseness.**
- **AI tools allowed** — "You can even *blatantly copy-paste* from AI tool with your own risk"; 'Risk' explained via project rigor rule (below).
- **Heavy penalty based on similarity score between class** (i.e., between classmates' submissions).

### Quiz (10%) *(L1 S8)*
- **5 quizzes**, **15 minutes each**, at the **end of the class**, **equal weightage**; **you must be present in class**.
- Quizzes are **surprise** quizzes.
- **Make-up quiz** possible for absence **with prior notice**.
- A quiz can be **traded in with a report submission upon attending a related seminar, with a 30% penalty** (to compensate absence).

### Project (40%) *(L1 S10–S11)*
- **Semi-open ended**: must be relevant to course material; must **apply at least 20% of the material taught in the course**.
- **Group project** (group size depends on class size). **The 'group' is evaluated, NOT the individuals.**
- Three phases:
  1. **Phase-1:** 2-page problem statement — answers **'why'** are you doing this? (5%)
  2. **Phase-2:** 3-page progress report — answers **'how'** are you doing this? (15%)
  3. **Phase-3:** 4-page report + presentation — **'what'** have you done? (20%)
- Evaluation criteria: correctness, clarity, conciseness, ***research rigor***.
- **Points range: [−x, x]** — **negative points** are awarded if very high marks in assignments but absolutely no rigor in project submissions (this is the 'risk' of copy-pasting AI output).

### Exams (alternative to project, 40%) *(L1 S12)*
- Opt for examination **instead of** project; **firm decision by 1st September**.
- Midterm-1: 5%, Midterm-2: 15%, End term: 20%.
- Dates decided later (~project submission dates).
- **Points range [0, x]** (no negative points — "since exam is time-bound in constrained environment, penalty is less severe").
- **Open-world exam** (but you cannot leave the exam hall).

### Examples where Modelling/Simulation is used *(L1 S14, S22–S23)*
- **Computer Systems:** simulating the Core and Memory of SoC; modelling power and performance of SoCs.
- **Outside Computer Systems:** road traffic.
- **Why power-performance modelling is important:** (a) explore different micro-architectural choices at **design-time** (out-of-order processing, size of I-$/D$ etc.); (b) **dynamic resource management** — a policy that dynamically chooses the required configuration of processing cores.

### Models vs. Simulation (class input) *(L1 S18)*
- Measure SoC performance via: models of core/cache/interconnect; real-time simulation; workload modelling.
- **Use MODELS when:** need **fast** performance analysis.
- **Use SIMULATION when:** need **detailed** performance analysis.

### Queue simulation overview *(L1 S20–S21)*
- **Objective:** to know **average occupancy**.
- **Need to know:** input distribution; service time distribution; **number of servers**.
- Summary: need a good hold of **stochastic process**.

### How to Model? *(L1 S29)*
- Stochastic process; Markov chain; Queuing theory; …

### Key Takeaway from the Course *(L1 S32)*
- **Tools:** LaTeX, Weka, Origin.
- **Communication skills** (key in engagement after degree): taking notes, preparing project reports, project presentation.
- **Strong analytical skill** (useful for daily life).
- **Networking** (group project).
- **Timeliness.**

## Diagrams / Figures / Tables

### Diagram: Typical Structure of a Core — Knights Landing (Xeon Phi) Overview
**Slide/Page:** L1 S15 (repeated as L4 S5)
**Purpose:** Show the micro-architecture/fabric of a real HPC core (Xeon Phi KNL) as an example of "typical structure of a core."
**Components / labels extracted:**
- **TILE** = [2 VPU | CHA | 2 VPU] over [Core | **1 MB L2** | Core] — i.e., a tile has 2 cores, each with a VPU, sharing 1 MB L2 (CHA = cache home agent).
- **Chip: 36 Tiles interconnected by 2D Mesh.**
- **Tile: 2 Cores + 2 VPU/core + 1 MB L2.**
- **Memory:** MCDRAM: **16 GB on-package**, high BW; DDR4: **6 channels @ 2400, up to 384 GB**.
- **IO: 36 lanes PCIe Gen3; 4 lanes of DMI** for chipset.
- **Node: 1-Socket only.**
- **Fabric: Omni-Path on-package (not shown).**
- **Vector Peak Perf: 3+ TF DP and 6+ TF SP Flops.**
- **Scalar Perf: ~3x over Knights Corner.**
- **Streams Triad (GB/s): MCDRAM: 400+; DDR: 90+.**
- Package edge: MCDRAM stacks around the package, EDC units, DDR MC, DDR4 channels, PCIe Gen 3 block, DMI, "misc". "Omni-path not shown."
**MCQ-relevant information:**
- Tile count = **36**; interconnect = **2D mesh**; L2 per tile = **1 MB**; MCDRAM = **16 GB on-package**; DDR4 = **6 channels @ 2400 (up to 384 GB)**; VPU = Vector Processing Unit.

### Diagram: Usual Components in Heterogeneous SoCs (SoC floorplan)
**Slide/Page:** L1 S16 (identical figure reused at L1 S17, L4 S8)
**Purpose:** Show which functional blocks a modern heterogeneous SoC contains and how they are arranged.
**Components:**
- Executing cores; Last level cache (LLC); Memory controllers (MC) & controllers; I/O controllers; QPI controllers; Power control unit (PCU); ….
- **"Constitutes a large-scale distributed system."**
- Floorplan labels: **PCU** (top-left corner), **Memory Controller** strips along top and bottom edges (**MC** at bottom), grid of **Core/C** tiles, rows of **LLC + R (router)** pairs, **QPI** block and **PCIe** block on the right periphery; red lines = on-chip interconnect mesh.
**What the diagram means:** SoC = distributed system of cores with LLC+router per tile, memory/controllers at periphery, PCU for power control.
**MCQ-relevant information:**
- The SoC "constitutes a **large-scale distributed system**."
- Designer considerations (L1 S17): **Size of the cache; Position of the MC; Interconnect; …**

### Diagram: One Example with Queues (Switch μ-arch.)
**Slide/Page:** L1 S20
**Purpose:** Show where **queues (buffers)** arise inside a network switch micro-architecture — motivates queue simulation.
**Components / flow:**
- Physical channel → **Link Control** → **DEMUX** → **Input buffers (IB)** → **MUX** → **CrossBar** → **DEMUX** → **Output buffers** → **MUX** → **Link Control** → Physical channel (per port; two input and two output ports drawn).
- **Routing Control and Arbitration Unit** connects to input buffers, output buffers and crossbar.
- Bracketed phases: **Link Traversal (LT)** (outside, on the link), **Switch Traversal (ST)** (IB through output buffers), **Route Computation (RC)** (at the routing control & arbitration unit).
- Red ellipses highlight **buffers** (input buffers and output buffers) — the queues.
- Legend (block color coding): Buffers; Switch; Routing and Arbitration; Link Controllers; Processor Interface.
- Parameters listed bottom-right: **D hops, L bit message, W bit wide channels.**
- Credit line: © T.M. Pinkston, J. Duato, with major contributions by J. Flich.
**MCQ-relevant information:**
- Buffers/queues exist at **input buffers AND output buffers**.
- Phase names: **LT = Link Traversal, ST = Switch Traversal, RC = Route Computation, IB = Input Buffer(s)**.
- Parameters: **D** = hops, **L** = message size in bits, **W** = channel width in bits. (Same figure reused at L4 S19 "Basic Switch Microarchitecture".)

### Diagram: One Technique to Model Power-Performance (display power graphs)
**Slide/Page:** L1 S24
**Purpose:** Empirical observation that display power depends (linearly) on brightness and colour → motivates **linear regression** modelling.
**Extracted content:**
- Power consumption of the display for different **brightness and colour** [ref [2]: Bhat, Mandal, Manchukonda, Vadlamudi, Agarwal, Wang, Ogras (2021). Per-Core Power Modeling for Heterogenous SoCs. *Electronics*, 10(19), 2428.]
- **Observation: Linear dependency → Linear regression.**
- Graph: x-axis **Normalized Brightness Level** (0→1); y-axis **P_disp (W)** (0→~1.1). Curves per colour: **White** (highest, ≈1.0–1.1 W at brightness 1), **Blue** (≈0.8), **Red** (≈0.6), **Green** (≈0.45), **Black** (lowest, nearly flat ≈0.05). All approximately straight lines through origin.
- Photo of a phone main board with "Connection to power supply" callout (measurement setup).
**MCQ-relevant information:**
- Technique = **linear regression** because dependency is **linear**.
- White consumes the most; Black the least (among the colours shown).

### Diagram: Use-case of the Power-Performance Models (dynamic power management flowchart)
**Slide/Page:** L1 S25
**Purpose:** Show how power-performance models are used **online** for dynamic power management.
**Flow / Process (from the figure):**
1. **(Once)** Construct Offline Policy → $\pi_{offline}$
2. **(For every epoch)** Execute the Current Policy
3. Online Power-Performance Modeling
4. **Predict Best Decision via Analytical Models**
5. **Decisions Match?** — Yes → Next Snippet (→ back to Execute the Current Policy); No → **Collect the Training Data in a Buffer**
6. **(Buffer is full)** Aggregate Training Data → **Regression Learner** → **New policy $\pi_{new}$** → back to Execute the Current Policy.
- Bullets: Dynamic power management [ref [3]: Mandal, Bhat, Doppa, Pande, Ogras (2020). An energy-aware online learning framework for resource management in heterogeneous platforms. *ACM TODAES*, 25(3), 1-26.]: **Estimate power at runtime; Take decision (core configuration) based on the decision.**
**MCQ-relevant information:**
- Decision taken = **core configuration**; power estimated **at runtime**; offline policy constructed **once**; per-epoch loop; regression learner updates the policy when the buffer fills and decisions did not match.

### Diagram: Road as a Queuing Network
**Slide/Page:** L1 S27
**Purpose:** Model road traffic as a network of queues with arrival processes and servers characterized by rate + coefficient of variation.
**Components / sub-figures:**
- **(a)** A line of cars on a single road → abstracted to a single queue with arrival process $(\lambda, C_a)$ and server $(\mu, C_s)$.
- **(b)** Two-way road (two streams of cars) → one queue fed by two arrival processes $(\lambda_1, C_{a1})$ and $(\lambda_2, C_{a2})$ → two servers $(\mu_1, C_{s1})$ and $(\mu_2, C_{s2})$.
- **(c)** Intersection of roads **R1, R2, R3, R4** → queuing network: arrivals $(\lambda_1,C_{a1}), (\lambda_2,C_{a2})$ feed queue **Q1** served at $(\mu_1,C_{s1})$; outputs route via $(\lambda_3,C_{a3})$ → **Q2** $(\mu_3,C_{s3})$, $(\lambda_4,C_{a4})$ → **Q4** $(\mu_4,C_{s4})$, and $(\lambda_5,C_{a5})$/$(\lambda_6,C_{a6})$ → **Q3** $(\mu_6,C_{s6})$ (circles = routing/turn points).
**Notation meaning:** $\lambda$ = arrival rate, $C_a$ = coefficient of variation of arrivals; $\mu$ = service rate, $C_s$ = coefficient of variation of service. *(Parameters labeled in the figure; semantic meaning of C_a/C_s not spelled out in the lecture — [NOT PROVIDED IN LECTURE MATERIAL beyond the symbols].)*
**MCQ-relevant information:**
- Road traffic is modelled as a **queuing network**; each road/intersection contributes queues with $(\lambda, C_a)$ arrival and $(\mu, C_s)$ service descriptors.

### Diagram: Change in Metrics for Different Cities
**Slide/Page:** L1 S28
**Purpose:** Simulation study comparing traffic congestion metrics across three cities.
**Extracted content:**
- Three map snippets: **(a) Portland, USA** (grid streets: SE Taylor St, SE Salmon St, SE Main St, SE Madison St., Aves), **(b) Delhi, India** (Street No. 5/6, Gall Number 8, हाउस नंबर 6; irregular streets circled in red), **(c) Milan, Italy** (Via Gluck, Via B., Wagner, Majornoli; irregular pattern boxed).
- Three plots: x-axis **Arrival Rate of Vehicles (count/time unit/road)** (0→~0.26); y-axis **Average Occupancy per Road** (0→50). Curves for **pb = 0, pb = 0.4, pb = 0.8**.
- Behaviour in all cities: occupancy ≈ 0 at low arrival rate, then **shoots up sharply to 50 (saturation)**. Larger **pb** saturates **earlier** (at lower arrival rate). City comparison: **Delhi saturates earliest (~0.20)**, **Milan close (~0.17–0.18)**, **Portland latest (~0.24–0.25)**. [precise crossing values read from plot; OCR/plot-reading approximate]
**MCQ-relevant information:**
- Y-axis = **Average Occupancy per Road**; X-axis = **Arrival Rate of Vehicles (count/time unit/road)**; parameter **pb ∈ {0, 0.4, 0.8}** (definition of pb not given in the slides — [NOT PROVIDED IN LECTURE MATERIAL]).
- All cities eventually saturate at the same occupancy (~50); higher pb → earlier saturation.

## Algorithms / Procedures
- (From flowchart L1 S25) Online learning power-management loop: see Diagram section above — order: Construct offline policy (once) → per epoch: execute policy → online modelling → predict best decision → match? (yes: next snippet; no: buffer training data) → on buffer full: aggregate → regression learner → new policy.

## Formulas
### Formula: Assignment grade aggregation
$$0.4 \cdot X(3) + 0.2 \cdot (X(2) + X(4)) + 0.1 \cdot (X(1) + X(5))$$
**Variables:** $X$ = array of the 5 assignment marks **sorted** ascending (X(1) lowest … X(5) highest).
**Used for:** computing the assignments (30%) component.
**Important MCQ details:** median X(3) gets the **highest weight 0.4**; extremes get 0.1 each.
**Common mistake:** applying weights without sorting the marks first.

### Formula: Late-submission penalty
$$Y = X(1 - d \cdot 0.1)$$
**Variables:** $Y$ = final grade, $X$ = original grade, $d$ = number of days delayed (submit up to 3 days late; slide also says "One late day is allowed").
**Important MCQ details:** each delayed day costs 10% of the original grade.

## Examples
### Example: Choosing model vs simulation
**Given:** Need to evaluate an SoC design.
**Method:** fast rough analysis → **model**; detailed analysis → **simulation**.
**MCQ-relevant takeaway:** model = fast; simulation = detailed. *(L1 S18)*

## Comparisons

| Feature | Project | Exam (alternative) |
|---|---|---|
| Weight | 40% (5%+15%+20%) | 40% (5%+15%+20%) |
| Points range | [−x, x] (negative possible) | [0, x] |
| Decision deadline | — | Firm by 1st September |
| Format | Group; 3 phase reports + presentation | Time-bound, open-world, in hall |
| Penalty rationale | "risk" of no rigor | "penalty is less severe" (constrained environment) |

| Feature | Model | Simulation |
|---|---|---|
| Use when | Fast performance analysis | Detailed performance analysis |

| Feature | Bus-based SoC interconnect (implied) | Point-to-point |
|---|---|---|
| Shown in | L1 S27-style road analogy n/a | — |

*(Bus vs point-to-point comparison belongs to Lecture 4 S12; see Lecture 4.)*

## Important Numerical Values
- Evaluation: Assignments 30%, Quiz 10%, Participation 20%, Project/Exam 40%. *(L1 S5)*
- Assignment weighting: 0.4 median, 0.2 the 2nd/4th, 0.1 the 1st/5th. *(L1 S6)*
- Late days allowed: 3 (−10% per day). *(L1 S6)*
- Quizzes: 5 × 15 min, end of class, equal weight; seminar-report trade: −30%. *(L1 S8)*
- Project: ≥20% course material must be applied; phases 5%/15%/20%. *(L1 S10–S11)*
- Exams: MT1 5%, MT2 15%, End 20%; project-vs-exam decision by 1 Sep. *(L1 S12)*
- ~50% of lectures are board-work. *(L1 S4)*
- KNL: 36 tiles; 2D mesh; 1 MB L2/tile; MCDRAM 16 GB; DDR4 6×2400 up to 384 GB; 36 PCIe Gen3 lanes; 4 DMI lanes; 3+ TF DP / 6+ TF SP; MCDRAM ≥400 GB/s; DDR ≥90 GB/s; ~3× scalar over Knights Corner. *(L1 S15)*
- Display power: linear in normalized brightness (0→1) for White/Red/Green/Blue/Black; White highest, Black ≈ 0. *(L1 S24)*
- City study: pb ∈ {0, 0.4, 0.8}; saturation occupancy 50; Delhi earliest ~0.20, Milan ~0.17–0.18, Portland ~0.24–0.25 arrival rate. *(L1 S28)*

## Important Conditions / Assumptions
- No deadline extensions at all. *(L1 S4)*
- Quiz absence: make-up only with **prior notice**; or trade for seminar report with 30% penalty. *(L1 S8)*
- Project must apply **≥20%** of course material. *(L1 S10)*
- Negative project points possible despite high assignment marks (rigor risk). *(L1 S11)*
- Queue simulation requires: input distribution + service time distribution + number of servers. *(L1 S21)*

## Exceptions / Special Cases
- Exam path has **no negative points** (range [0, x]) unlike project ([−x, x]). *(L1 S11–S12)*
- MCDRAM is on-package (not off-chip); Omni-Path fabric on-package but "not shown" in the figure. *(L1 S15)*

## MCQ-Relevant Facts
- Quiz weight = 10%; 5 surprise quizzes, 15 min each, at the END of class, equal weightage. *(L1 S5, S8)*
- Assignments 30%; participation 20%; project OR exam 40%. *(L1 S5)*
- The project is evaluated at GROUP level, not individual. *(L1 S11)*
- Phase-1 = **why** (2 pages, 5%); Phase-2 = **how** (3 pages, 15%); Phase-3 = **what** (4 pages + presentation, 20%). *(L1 S11)*
- Models → fast analysis; Simulation → detailed analysis. *(L1 S18)*
- For queue simulation you need: input distribution, service-time distribution, number of servers; objective = average occupancy. *(L1 S21)*
- Display power modelling technique = linear regression (linear dependency observed). *(L1 S24)*
- Dynamic power management: estimate power at runtime → decide core configuration. *(L1 S25)*
- Modelling tools named for the course: **LaTeX, Weka, Origin**. *(L1 S32)*
- Course examples: SoC core/memory simulation, power-performance modelling (CS); road traffic (non-CS). *(L1 S14)*
- "How to model?" answers: stochastic process, Markov chain, queuing theory. *(L1 S29)*
- gem5 is a **simulator** (reference: Lowe-Power et al. 2020, "The gem5 simulator: Version 20.0+", arXiv:2007.03152). *(L1 S19)*

## Common Confusions
- **Attendance vs evaluation:** No attendance is taken, BUT daily evaluation happens — "no attendance" ≠ "no participation requirement." *(L1 S5)*
- **Project vs Exam ranges:** Project [−x, x] vs Exam [0, x] — only the project can produce negative points. *(L1 S11–S12)*
- **Model vs Simulation:** both estimate the real system; they differ in speed vs detail, not in validity. *(L1 S18)*
- **MCDRAM vs DDR4 (KNL):** MCDRAM = 16 GB **on-package**, high BW (400+ GB/s); DDR4 = 6 channels @ 2400, up to 384 GB, 90+ GB/s. *(L1 S15)*

## MCQ Traps
- "Attendance is taken daily" — FALSE; attendance is NOT taken, but daily evaluation occurs. *(L1 S5)*
- "Late submission is never allowed" — FALSE; up to 3 days with 10%/day penalty. *(L1 S6)*
- "The median assignment gets the lowest weight" — FALSE; median X(3) gets 0.4 (highest). *(L1 S6)*
- "Quizzes are announced in advance" — FALSE; they are surprise quizzes. *(L1 S8)*
- "Individuals are evaluated in the group project" — FALSE; the group is evaluated. *(L1 S11)*
- "KNL tiles are connected by a ring" — FALSE; 2D mesh, 36 tiles. *(L1 S15)*

## Quick Retrieval Facts
- Instructor = Sumit K. Mandal; TAs = Sufyan Azam, Vivek Kumar, Samip Poudel.
- Weights: 30 (assign) / 10 (quiz) / 20 (participation) / 40 (project-or-exam).
- Assignment formula: 0.4·X(3) + 0.2·(X(2)+X(4)) + 0.1·(X(1)+X(5)); sorted marks.
- Late: Y = X(1 − 0.1·d), d ≤ 3.
- Quiz: 5 × 15 min, surprise, end of class; seminar trade = 30% penalty.
- Project phases: why(5)/how(15)/what(20); group-level; range [−x, x].
- Exam: MT1 5 / MT2 15 / End 20; decide by Sep 1; range [0, x]; open-world.
- Model = fast; Simulation = detailed.
- KNL = 36 tiles, 2D mesh, tile = 2 cores + 2 VPU + 1 MB L2; MCDRAM 16 GB.
- Switch μ-arch phases: LT (link), ST (switch), RC (route), IB (input buffer); queues at input AND output buffers.
- Display power → linear regression; DPM loop: offline policy → per-epoch execute/model/predict → buffer → regression learner → new policy.
- Road traffic → queuing network with (λ,Ca) arrivals and (μ,Cs) services; cities: Portland/Delhi/Milan; pb 0/0.4/0.8.
- gem5 = simulator (Lowe-Power et al. 2020).

## Source Map
- S1: Title (E0 240 Lecture #1, 11 Aug 2026; wearable-system artwork: Battery, Sensor, μP, Mem)
- S2: Instructor & TAs
- S3: Agenda (Logistics, Evaluation, Timeline, Overview, Questions)
- S4: Logistics (time, room, board-work, Teams, no extensions)
- S5: Evaluation criteria (30/10/20/40)
- S6: Assignments — weights, late policy, formats
- S7: Assignments — criteria, AI policy, similarity penalty
- S8: Quiz rules
- S9: Class participation
- S10: Project — semi-open, 20% rule, phases
- S11: Project — group evaluation, phase deliverables, rigor, [−x, x]
- S12: Exams — opt-out by 1 Sep, 5/15/20, [0, x], open-world
- S13: Class material philosophy (awareness; AI limits)
- S14: Agenda — examples (SoC core/memory, power-performance; road traffic)
- S15: Typical Structure of a Core (Knights Landing overview figure)
- S16: Usual Components in Heterogeneous SoCs (+ floorplan figure)
- S17: What should the Designers Consider? (+ floorplan figure)
- S18: Class Input (models vs simulation)
- S19: Gem5 [1] (figure + citation)
- S20: One example with Queues (Switch μ-arch figure)
- S21: Overview of Queue Simulation (objective, needs)
- S22: Agenda repeat
- S23: Why Power-Performance Modelling is Important?
- S24: One Technique to Model Power-Performance (display graphs) [2]
- S25: Use-case of the Power-Performance Models (DPM flowchart) [3]
- S26: Agenda repeat
- S27: Road as a Queuing Network (a/b/c figure)
- S28: Change in Metrics for Different Cities (maps + plots)
- S29: How to Model? (stochastic process, Markov chain, queuing theory)
- S30: Questions?
- S31: "This slide deck is available at" (link graphic)
- S32: Key Takeaway from the Course

---

# Lecture 2: Basics of Simulation (1) — Simulation Concepts & Single-Queue Simulation

**Date:** 13 August 2026
**Source File:** `2_Lecture_13_08_26.pdf` (47 slides)

## Topics Covered
- Timeline of the course *(L2 S3–S5)*
- Overview of topics: Basics of Simulation (today), Queue Simulation, Random Numbers, Queuing Network Simulation, Relation between Modelling and Simulation *(L2 S6)*
- Definition of simulation; system model vs physical system; time scaling *(L2 S7–S8)*
- Typical flow in simulation (flowchart) *(L2 S9)*
- Components of Discrete-Event Simulation (DES) *(L2 S10)*
- Updating simulation time: next-event vs fixed-increment *(L2 S11)*
- Developing a simulation program (skeleton) *(L2 S12)*
- Simulation of a queue with a single server: notation t_i, A_i, S_i, D_i *(L2 S13–S17)*
- Performance metrics: average delay, average queue length, server utilization *(L2 S18–S25)*
- Single queue simulation worked example (graph + step-by-step event trace) *(L2 S26–S40)*
- Output of the simulation (final metrics) *(L2 S41–S45)*
- Arrival routine flowchart *(L2 S46)*

## Key Definitions
- **Simulation (from Wikipedia, quoted on slide):** "A simulation is an imitation of some real thing, state of affairs, or process. The act of simulating something generally entails representing certain key characteristics or behaviors of a selected physical or abstract system." Used for modelling natural or human systems to gain insight into functioning; also performance optimization, safety engineering, testing, training and education. *(L2 S7)*
- **System model:** **Abstraction of real system.** A simulation model considers a **system model instead of the actual physical system**. Simplifying assumptions capture only important behaviors, may even make analysis tractable. Outputs of the model represent an **estimate** of the real outputs of the physical system. *(L2 S8)*
- **Time scale may be altered:** **compress time** to capture **rare events**; **expand time** to capture **rapidly occurring events**. *(L2 S8)*
- **System State:** collection of state variables. *(L2 S10)*
- **Simulation Clock:** current value of simulated time. *(L2 S10)*
- **Stat. counters:** variables used for system performance. *(L2 S10)*
- **Initialization Routines:** initialize relevant counters. *(L2 S10)*
- **Timing Routine:** for determining **next event**. *(L2 S10)*
- **Event Routine:** collection of state variables (updates). *(L2 S10)*
- **Library Routine:** collection of routines for probability distributions. *(L2 S10)*
- **Event Queue:** holds events in **chronological (increasing time) order**. *(L2 S11)*
- **Notation (single-server queue):** $t_i$ = arrival time of i-th customer; $A_i$ = inter-arrival time of i-th customer $= (t_i - t_{i-1})$; $S_i$ = service (time) for i-th customer; $D_i$ = delay in queue of i-th customer. *(L2 S14–S17)*

## Core Concepts

### Components of Discrete-Event Simulation *(L2 S10)*
1. System state 2. Simulation clock 3. Stat. counters 4. Initialization routines 5. Timing routine 6. Event routine 7. Library routine.

### Updating Simulation Time *(L2 S11)*
- **Next-event time advance:** simulation time updated **to next-event time**.
- **Fixed-increment time advance:** simulation time incremented by a **fixed amount**; drawback: **many increments before an actual event!**

### Simulation program skeleton *(L2 S12)*
```
Initialize ( );
While (1) {
  Invoke timing routine;
  Invoke Event routine;
}
Output Result;
```
- `Timing Routine( ) { Determine next event; Advance Sim. Time; }`
- `Event Routine( ) { Update sys. state; Update stat. counters; Generate and add new event to event queue; }`
- `Initialize( ) { … }` initializes the model.

## Detailed Notes

### Course timeline (from L2 S3–S5) — events/deadlines
| Date | Topic | Event/Deadline |
|---|---|---|
| 11/08 | Introduction | — |
| 13/08 | Basics of Simulation (1) | — |
| 18/08 | Basics of Simulation (2) | **List of project releases** |
| 20/08 | Single queue simulation; Introduction to LaTeX | **Assignment-1 released** |
| 25/08, 27/08 | No class (tentative) | **Assignment-1 submission deadline (27/08)** |
| 01/09 | Queuing Network Simulation | — |
| 03/09 | Introduction to Network-on-Chip, Demo on BookSim (1) | Assignment-2 released |
| 08/09 | Demo on BookSim (2), Introduction to Chiplet-based system | — |
| 10/09 | Demo on SIAM | Assignment-2 submission deadline |
| 15/09, 17/09 | Random Number Generation (1),(2) | — |
| 22/09 | Queuing Theory (1) | Assignment-3 released; **Phase-1 due** |
| 24/09, 29/09 | Queuing Theory (2),(3) | Assignment-3 submission deadline (29/09) |
| 01/10 | Queuing Network | Assignment-4 released |
| 06/10, 08/10 | No class (tentative) | — |
| 13/10 | Markov Chain (1) | Assignment-4 submission deadline |
| 15/10 | Markov Chain (2) | — |
| 20/10 | Holiday (NO CLASS) | — |
| 22/10 | No class (tentative) | — |
| 27/10 | Markov Chain (3) | **Phase-2 due** |
| 29/10 | Stochastic Process | Assignment-5 released |
| 03/11 | Simulation and Modelling | — |
| 05/11 | ML-based modelling (1); Demonstration of Weka | — |
| 10/11 | ML-based modelling (2) | Assignment-5 submission deadline |
| 16/11, 17/11, 19/11 | Final Presentation 1–3 | — |
| 24/11 | Holiday (NO CLASS) | — |
| 26/11 | Final report submission / end-term | — |

## Algorithms / Procedures

### Procedure: Typical Flow in Simulation *(L2 S9, flowchart)*
**Flow:** 
1. **Problem Formulation** → 2. **Setting of Objectives** → 3. (parallel) **Develop Model** + **Data Collection** → 4. **Model Translate** → 5. **Verify** → 6. **Validate** → 7. **Exptl. Design** → 8. **Production Run & Anal.** → 9. **Output & Document**.
**Feedback loops:** Validate → back to **Develop Model**; Verify ↔ **Model Translate** (verify feeds back to model translation).
**MCQ-relevant information:**
- Order: Verify comes **before** Validate; both come **after** Model Translate; Experimental Design comes **after** Validate; Production Run after Exptl. Design; Output & Document is last.
- [The slides show only the order; definitions of "verify" vs "validate" are NOT PROVIDED IN LECTURE MATERIAL.]

### Procedure: Arrival Routine (single-server queue) *(L2 S46, flowchart)*
**Flow:**
1. **Arrival Event** occurs.
2. **Schedule Next Arrival** (always).
3. **Server Busy?**
   - **Yes** → **Add 1 to Queue** → **Store Arr. Time** → **Return**.
   - **No** → **Set Delay = 0** → **Add 1 to Delayed Customers** → **Make Server Busy** → **Schedule Departure Event** → **Return**.
**MCQ-relevant information:**
- "Schedule next arrival" happens **FIRST**, before the busy check.
- Server NOT busy → delay set to 0, delayed-customers counter incremented, server made busy, departure event scheduled.
- Server busy → queue length +1 and the arrival time is stored (needed to compute delay later).
- *(A departure-routine flowchart is not in the deck — likely done on the board [NOT PROVIDED IN LECTURE MATERIAL].)*

## Formulas

### Formula: Average Delay
$$\text{Average Delay} = \frac{\sum_i D_i}{n}$$
**Variables:** $D_i$ = delay in queue of i-th customer; $n$ = number of (delayed) customers.
**Used for:** customer-average waiting time.
**Important MCQ details:** it is a **customer average** (divide by number of customers), NOT a time average.
**Common mistake:** dividing by total time T instead of n.

### Formula: Average Queue Length
$$\text{Average queue length} = \frac{\sum_i I \cdot T_i}{T}$$
**Variables:** $I$ = queue length during the i-th interval; $T_i$ = duration of i-th interval; $T$ = total time.
**Used for:** time-integral of queue length over total time.
**Important MCQ details:** slide emphasizes: **"Avg. Queue length is a TIME-AVERAGE!"** *(L2 S21)*. Worked arithmetic: $(5{\cdot}1 + 2{\cdot}2 + 2{\cdot}3 + 7{\cdot}2 + 2{\cdot}1)/25 = 31/25 = 1.24$ *(L2 S22, S44)*.
**Common mistake:** dividing by n (number of customers) instead of T.

### Formula: Server Utilization
$$\text{Utilization} = \frac{\text{time for which server is busy}}{\text{total time}}$$
**Used for:** fraction of time the server is busy — a **time average** *(L2 S23)*.
**Worked value:** $23/25 = 0.92$ *(L2 S23–S25, S45)*.

## Examples

### Example: Single-Queue Single-Server Simulation (the class worked example)
**Given (L2 S27–S28):**
- Arrival times $t_i$: **1, 4, 9, 11, 24** (5 customers)
- Service times $S_i$: **13, 7, 2, 1, 1**
- Definitions: $D(t)$ – Delay (waiting time in the queue); $Q(t)$ – Queue Length; $B(t)$ – Utilization (busy-time accumulator). *(L2 S29–S30)*

**Queue-length graph reading (L2 S18–S28):** green ↑ arrows = arrivals (at 1, 4, 9, 11, 24); red ↓ arrows = departures (at 13, 20, 22, 23, 25). Shaded Q(t) levels over segments (total time T = 25): 
| Interval | 0–4 | 4–9 | 9–11 | 11–13 | 13–20 | 20–22 | 22–24 | 24–25 |
|---|---|---|---|---|---|---|---|---|
| Q(t) | 0 | 1 | 2 | 3 | 2 | 1 | 0 | 0 |
- **Q(t) counts customers waiting in the queue; the customer IN SERVICE is not counted** (Q=0 during 1–4 while customer 1 is being served, and Q=0 during 24–25 while customer 5 is served).

**Method — event trace ("How Simulation Proceeds", L2 S30–S40).** Table state = (Server Status, Q. Len, stored Arrival Times, Event List, Clock) + counters (Num Arrival, D(t), Q(t), B(t)):

| Step | Clock | Server | Q.Len | Stored arr. times | Event list | NumArr | D(t) | Q(t) | B(t) | Event processed |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 (S30) | 0 | I | 0 | — | A-1 | 0 | 0 | 0 | 0 | initialize |
| 2 (S31) | 1 | B | 0 | — | A-4, D-13 | 1 | 0 | 0 | 0 | cust1 arrives: delay=0, server→Busy, schedule D-13 |
| 3 (S32) | 4 | B | 0 | 4 | A-9, D-13 | 2 | 0 | 0 | 3 | cust2 arrives → queued, arrival time stored |
| 4 (S33) | 9 | B | 2 | 4, 9 | A-11, D-13 | 3 | 0 | 5 | 8 | cust3 arrives → queued |
| 5 (S34) | 11 | B | 3 | 4, 9, 11 | A-24, D-13 | 4 | 0 | 9 | 10 | cust4 arrives → queued |
| 6 (S35) | 13 | B | 2 | 9, 11 | A-24, D-20 | 4 | 9 | 15 | 12 | cust1 departs; cust2 starts service, delay = 13−4 = 9 |
| 7 (S36) | 20 | B | 1 | 11 | A-24, D-22 | 4 | 20 | 29 | 18 | cust2 departs; cust3 starts, delay = 20−9 = 11 |
| 8 (S37) | 22 | B | 0 | — | A-24, D-23 | 4 | 31 | 31 | 21 | cust3 departs; cust4 starts, delay = 22−11 = 11 |
| 9 (S38) | 23 | I | 0 | — | A-24 | 4 | 41 | 31 | 22 | cust4 departs; server → Idle |
| 10 (S39) | 24 | B | 0 | — | D-25 | 5 | 41 | 31 | 22 | cust5 arrives: server idle → delay=0, busy, schedule D-25 |
| 11 (S40) | 25 | B | 0 | — | (empty) | 5 | 41 | 31 | 23 | cust5 departs; end |

- Event-list notation: **A-x = arrival at time x; D-x = departure at time x.** Events processed in chronological order (event list kept sorted).
- Departures occur at **13, 20, 22, 23, 25**; per-customer queueing delays added to D(t): **9 (cust2), 11 (cust3), 11 (cust4)**; customers 1 and 5 have delay 0 (server idle on arrival).

**Result (Output of the Simulation, L2 S41–S45):**
- **Num Delayed = 5; D(t) = 41; Q(t) = 31; B(t) = 23.**
- **Average Delay = 41/5 = 8.2** *(L2 S43)*
- **Average queue length = 31/25 = 1.24** *(L2 S44)*
- **Server utilization = 23/25 = 0.92** *(L2 S45)*

**MCQ-relevant takeaway:**
- Memorize the quadruple **(Num Delayed, D(t), Q(t), B(t)) = (5, 41, 31, 23)** and the three finals **8.2, 1.24, 0.92** — these are the slide's official answers.
- Delay is recorded when a waiting customer **starts service** (delay = service-start time − arrival time).
- Busy time = [1,23) ∪ [24,25) = 22 + 1 = 23.

**Potential inconsistency in source (report, do not silently fix):**
1. Customer 1 arrives at t=1 with S₁=13, but its departure is scheduled at **D-13** (not 14 = 1+13). The trace chains departures as depᵢ = depᵢ₋₁ + Sᵢ (13→20→22→23), and cust5 departs at arrival+service = 25. Follow the slide values.
2. **D(t) jumps 31 → 41 at slide 38 (clock 23)** although no customer starts service at t=23 (cust4 merely departs). Sum of per-customer delays by the trace's own arithmetic = 0+9+11+11+0 = **31**, yet all final slides report **D(t) = 41 and average delay 8.2**. The deck's official final answers are 41/8.2.
3. Intermediate B(t): at clock 20 the slide shows 18 (interval arithmetic gives 12+7 = 19), at clock 22 it shows 21 (18+2 = 20); the **final B = 23** is consistent with busy-interval arithmetic.
4. At clock 4 (slide 32) Q.Len is displayed as 0 although customer 2 is queued (slide 33 then shows Q.Len = 2 for customers 2 and 3).
If an MCQ uses this example, match the **slide's official numbers** (8.2, 1.24, 0.92, 41, 31, 23, 5).

## Diagrams / Figures / Tables

### Diagram: Typical Flow in Simulation
**Slide/Page:** L2 S9 — see *Algorithms/Procedures* above for the full box-and-arrow sequence and feedback loops.

### Diagram: Simulation of Queue with a Single Server
**Slide/Page:** L2 S13–S17
**Purpose:** Define the physical queueing picture and its notation.
**Components:** arrival (blue dot) → **queue** (drawn as vertical slots) → **Server** (ellipse) → departure (blue dot).
**Labels:** $t_i$ (arrival time), $A_i = t_i - t_{i-1}$ (inter-arrival time), $S_i$ (service), $D_i$ (delay in queue).
**What it means:** customers arrive at t_i, wait D_i in the queue, receive S_i service at the server, and leave.
**MCQ-relevant information:** $A_i$ is defined as $(t_i - t_{i-1})$ — the gap between consecutive arrivals.

### Diagram: Q-Length vs Time (performance metrics graph)
**Slide/Page:** L2 S18–S28 (built progressively), S41–S45 (with output boxes)
**Purpose:** Derive time-averaged metrics from the queue-length trajectory.
**Content:** x-axis Time (segments 4, 5, 2, 2, 7, 2, 2, 1 → total 25); y-axis Q Length; green up-arrows = arrivals (1, 4, 9, 11, 24); red down-arrows = departures (13, 20, 22, 23, 25); shaded step levels: Q=1 (5 units), Q=2 (2), Q=3 (2), Q=2 (7), Q=1 (2), Q=0 (4+2+1 units).
**Key computation shown on slide:** $(5{\cdot}1 + 2{\cdot}2 + 2{\cdot}3 + 7{\cdot}2 + 2{\cdot}1)/25 = 31/25 = 1.24$.
**Output boxes (S42):** Num Delayed = 5, D(t) = 41, Q(t) = 31, B(t) = 23.

### Diagram: Developing a Simulation Program
**Slide/Page:** L2 S12
**Purpose:** Show the calling structure of a DES program.
**Content:** Main = Initialize( ); While(1){ invoke timing routine; invoke event routine; } Output Result. Timing Routine = {determine next event; advance sim. time}. Event Routine = {update sys. state; update stat. counters; generate and add new event to event queue}.

### Diagram: How Simulation Proceeds (state snapshots)
**Slide/Page:** L2 S30–S40
**Purpose:** Step-by-step DES execution shown as snapshots of (Server Status, Q. Len, Arrival Time store, Clock, Event List) plus counters (Num Arrival, D(t), Q(t), B(t)). Full table reproduced in the Example above.

## Comparisons

| Feature | Next-event time advance | Fixed-increment time advance |
|---|---|---|
| Clock update | To the time of the next event | By a fixed amount Δ |
| Efficiency | Jumps directly between events | Many increments may pass before an actual event |
| Slide note | "Simulation time updated to next-event time" | "Many increments before an actual event!" |

*(L2 S11)*

| Metric | Type of average | Divided by |
|---|---|---|
| Average delay $\sum D_i / n$ | Customer average | n (customers) |
| Average queue length $\sum I \cdot T_i / T$ | **Time average** | T (total time) |
| Server utilization (busy/total) | **Time average** | T (total time) |

*(L2 S19–S25)*

## Important Numerical Values
- Worked example inputs: arrivals **1, 4, 9, 11, 24**; services **13, 7, 2, 1, 1**; T = **25**. *(L2 S27–S28)*
- Departure times: **13, 20, 22, 23, 25**. *(L2 S31–S39, graph)*
- Per-customer delays: cust1 = 0, cust2 = 9, cust3 = 11, cust4 = 11, cust5 = 0. *(trace)*
- Final counters: **D(t)=41, Q(t)=31, B(t)=23, Num Delayed=5.** *(L2 S42)*
- Final metrics: **avg delay 8.2; avg Q length 1.24; utilization 0.92.** *(L2 S43–S45)*

## Important Conditions / Assumptions
- Event list is maintained in **chronological (increasing time) order**. *(L2 S11)*
- Arrival routine always schedules the next arrival before handling the current customer. *(L2 S46)*
- Delay is set to 0 only when the server is idle at arrival. *(L2 S46)*
- Q(t) as plotted counts only waiting customers (excludes the one in service). *(L2 graph)*

## Exceptions / Special Cases
- Fixed-increment advance wastes steps when events are sparse ("many increments before an actual event!"). *(L2 S11)*
- A customer arriving to an idle server never enters the queue (Q unchanged, delay 0). *(L2 S46, trace steps 2 & 10)*

## MCQ-Relevant Facts
- A simulation model uses a **system model (abstraction)**, not the physical system; outputs are **estimates**. *(L2 S8)*
- Compress time → rare events; expand time → rapidly occurring events. *(L2 S8)*
- DES has 7 components: system state, simulation clock, stat. counters, initialization routines, timing routine, event routine, library routine. *(L2 S10)*
- Event queue = chronological order. Timing routine determines the next event. *(L2 S10–S11)*
- Main loop order: Initialize → (timing routine → event routine)* → output. *(L2 S12)*
- Verify precedes Validate in the simulation flow; Exptl. Design follows Validate; Output & Document is last. *(L2 S9)*
- $A_i = t_i - t_{i-1}$. *(L2 S15)*
- Average queue length is a TIME-average; average delay is a per-customer average. *(L2 S21)*
- Official worked-example answers: 41/5 = 8.2; 31/25 = 1.24; 23/25 = 0.92. *(L2 S43–S45)*
- Arrival routine: schedule next arrival → server busy? (yes: queue+1, store arrival time; no: delay=0, delayed+1, make busy, schedule departure). *(L2 S46)*
- In the trace, delay of a queued customer = (time it starts service) − (its arrival time). *(trace)*

## Common Confusions
- **Average delay vs average queue length:** delay divides by **n** (customers); queue length divides by **T** (time) — slide explicitly warns "Avg. Queue length is a time-average!" *(L2 S21–S22)*
- **Q(t) vs number in system:** Q(t) in this example excludes the customer in service (Q=0 during 1–4 and 24–25). *(graph)*
- **Next-event vs fixed-increment:** next-event jumps to event times; fixed-increment steps by Δ and can waste many steps. *(L2 S11)*
- **Timing vs event routine:** timing routine chooses the next event and advances the clock; event routine updates state/counters and schedules NEW events. *(L2 S12)*
- **Verify vs Validate:** the slides give the ORDER only (verify before validate, both after model translation); their definitions are [NOT PROVIDED IN LECTURE MATERIAL].
- **D(t) 41 vs 31:** see "Potential inconsistency in source" in the worked example — official slide answer is 41 (avg 8.2).

## MCQ Traps
- "Average delay = ΣD_i / T" — FALSE; it is ΣD_i / **n**. *(L2 S19)*
- "Average queue length is a customer-average" — FALSE; it is a **time-average**. *(L2 S21)*
- "Utilization = busy time / busy+idle time only while queued" — the slide's utilization = busy time / **total time** = 23/25. *(L2 S23)*
- "The customer in service is counted in Q(t)" — FALSE in this example's graph (Q=0 while cust 1 is in service during 1–4). *(L2 graph)*
- "Arrival routine first checks whether the server is busy" — FALSE; it FIRST schedules the next arrival. *(L2 S46)*
- "Events in the event list are kept in random/FILO order" — FALSE; chronological (increasing time) order. *(L2 S11)*
- "Departure of customer 1 is at 14 (=1+13)" — the slide's trace uses **13**; use slide values for this example. *(L2 S31)*

## Quick Retrieval Facts
- Simulation = imitation of a real thing/state/process, representing key characteristics/behaviors. *(L2 S7)*
- System model = abstraction; model outputs ≈ estimates of real outputs. *(L2 S8)*
- 7 DES components; event queue chronological; two time-advance mechanisms. *(L2 S10–S11)*
- Flow: Problem Formulation → Objectives → Develop Model + Data Collection → Model Translate → Verify → Validate → Exptl. Design → Production Run & Anal. → Output & Document. *(L2 S9)*
- Notation: t_i arrival, A_i = t_i − t_{i−1} inter-arrival, S_i service, D_i queue delay. *(L2 S14–S17)*
- Metrics: avg delay ΣDᵢ/n; avg Q length ΣI·Tᵢ/T; utilization busy/T. *(L2 S19–S25)*
- Example: t = (1,4,9,11,24), S = (13,7,2,1,1) → (5, 41, 31, 23) → 8.2 / 1.24 / 0.92. *(L2 S42–S45)*
- Delayed customers: 5; their delays: 0, 9, 11, 11, 0. *(trace)*
- Arrival routine order: schedule next arrival → busy? yes: queue+store time; no: delay=0 + delayed+1 + busy + schedule departure. *(L2 S46)*
- A-4 / D-13 notation = arrival/departure event at that time. *(trace)*

## Source Map
- S1: Title (Lecture #2, 13 Aug 2026)
- S2: "This slide deck is available at" (link graphic)
- S3–S5: Timeline of the course (tables)
- S6: Overview of topics
- S7: Simulation (Wikipedia definition)
- S8: Simulation (system model, time scaling)
- S9: Typical Flow in Simulation (flowchart)
- S10: Components of DES
- S11: Updating Simulation Time (next-event vs fixed-increment; event queue)
- S12: Developing a Simulation Program (skeleton)
- S13–S17: Simulation of Queue with a Single Server (diagram; t_i, A_i, S_i, D_i introduced one per slide)
- S18–S25: Performance Metrics (graph + avg delay + avg queue length + time-average emphasis + utilization 23/25)
- S26–S29: Single Queue Simulation (graph; t_i arrivals; S_i services; D(t), Q(t), B(t) defined)
- S30–S40: How Simulation Proceeds (1)–(11) (trace snapshots)
- S41–S45: Output of the Simulation (boxes 5/41/31/23; 8.2; 1.24; 0.92)
- S46: Arrival Routine (flowchart)
- S47: Questions?

---

# Lecture 3: Basics of Simulation (2) — Random Number Generation

**Date:** 18 August 2026
**Source File:** `3_lecture_18_08_26.pdf` (13 slides)
**Note:** Slide 3 states: *"Slide Courtesy: Prof. R Govindarajan (Modeling and Simulation, Jan. 2007)"*. Important event on this date: **List of project releases** *(L2 timeline)*.

## Topics Covered
- Random number generation *(L3 S3–S4)*
- Demonstration of single queue simulation with synthetic traffic *(L3 S3)*
- Quick recap (handwritten slides): Random Variable; Continuous Random Variable; Uniform Random Variable *(L3 S6–S8)*
- Inverse Transformation Technique (ITT): continuous, exponential, discrete *(L3 S9–S11)*
- Generating packets with Geometric distribution *(L3 S12)*

## Key Definitions
- **Random number generation goal:** generate random numbers that follow certain distributions (**continuous or discrete**). *(L3 S4)*
- **Standing assumption:** a source of **uniform random variable** is available. *(L3 S4)*
- **Random number generation techniques (4):** *(L3 S4–S5)*
  1. **Inverse transformation technique (ITT)**
  2. **Composition method**
  3. **Convolution method**
  4. **Acceptance-rejection method**
- **Random Variable (handwritten, L3 S6):** "The real-valued functions defined on the sample space are known as random variable."
- **Two kinds of random variables:** **Discrete** and **Continuous**. *(L3 S6, handwritten)*
- **Continuous Random Variable (CRV) (handwritten, L3 S7):** a random variable X whose **set of possible values are continuous**; there should be a **non-negative function f(x)** defined for all real $x \in (-\infty, \infty)$.
- **Uniform Random Variable (URV) (handwritten, L3 S8):** X is **uniformly distributed over the interval (0,1)** if its PDF is $f_X(x) = 1$ for $0 < x < 1$ and 0 otherwise. General: X ~ U(α, β) has PDF $1/(\beta-\alpha)$ on (α, β), 0 otherwise.

## Formulas

### Formula: Probability of an event for a CRV
$$P_X\{x \in B\} = \int_B f(x)\,dx$$
**Variables:** $f(x)$ = PDF (non-negative, defined for all real x); B = set of interest. *(L3 S7, handwritten)*

### Formula: Properties of the PDF (handwritten, L3 S7)
1. $\int_{-\infty}^{\alpha} f(x)\,dx = 1$ — i.e., the **total integral over all x equals 1** (the slide writes the upper limit as α; semantically the normalization condition $\int_{-\infty}^{\infty} f(x)\,dx = 1$).
2. $P\{a \le x \le b\} = \int_a^b f_X(x)\,dx$
3. $P\{x = a\} = \int_a^a f_X(x)\,dx = 0$ — **probability at a single point is zero** for a CRV.
4. **CDF:** $F_X(a) = \int_{-\infty}^{a} f_X(x)\,dx$

### Formula: Uniform RV on (0,1)
$$f_X(x) = \begin{cases} 1, & 0 < x < 1 \\ 0, & \text{o/w} \end{cases}$$
$$P(a \le x \le b) = \int_a^b f_X(x)\,dx = b - a, \quad 0 < a, b < 1$$
*(L3 S8, handwritten; figure: rectangle of height 1 over [0,1])*

### Formula: Uniform RV on general interval (α, β)
$$f_X(x) = \begin{cases} \dfrac{1}{\beta-\alpha}, & \alpha < x < \beta \\ 0, & \text{o/w} \end{cases}$$
**Derivation (handwritten):** $\int_{-\infty}^{\infty} f_X(x) = 1 \Rightarrow \int_{\alpha}^{\beta} k\,dx = 1 \Rightarrow k(\beta - \alpha) = 1 \Rightarrow k = \dfrac{1}{\beta-\alpha}$
*(L3 S8)*

### Formula: ITT (general)
**Procedure:** Given PDF $f(x)$ and CDF $F(x)$: since $F(x)$ lies in the range [0,1], assign $F(x) = U(0,1)$ ($U(.)$ = uniform random variable); **return $X = F^{-1}(U)$**. *(L3 S9)*
**Figure:** CDF curve F(x) rising from 0 to 1; draw U1 on y-axis → across to the curve → down to **X1** on x-axis (X1 = F⁻¹(U1)).
**Conditions/assumptions:** requires the inverse of the CDF; F must map into [0,1].
**Common mistake:** using the PDF inverse instead of the CDF inverse.

### Formula: ITT for the Exponential distribution
$$f_X = \lambda e^{-\lambda x}, \qquad F_X = 1 - e^{-\lambda x}$$
**Derivation (as on slide L3 S10):**
Let $U \sim U(0,1)$:
$$U = 1 - e^{-\lambda X} \Rightarrow e^{-\lambda X} = 1 - U \Rightarrow -\lambda X = \ln(1-U) \Rightarrow X = -\frac{1}{\lambda}\ln(1-U)$$
**Used for:** generating exponential inter-arrival times from uniform numbers.
**Important MCQ details:** the slide's result uses $\ln(1-U)$ with a **minus sign and 1/λ factor**.
**Common mistake:** writing $\ln(U)$ or dropping the sign.

### Formula: ITT for discrete random variables
**Procedure (L3 S11):** given p.m.f. $p(x)$ and CDF $F(x)$: generate $U \sim U(0,1)$; determine the **smallest positive integer I such that $U \le F(I)$**; return $X = I$.

## Examples

### Example: ITT for a discrete variable
**Given:** values 1, 2, 3 with p.m.f. $p(1) = 0.5;\ p(2) = 0.15;\ p(3) = 0.35$.
**Method:** CDF: $F(1) = 0.5;\ F(2) = 0.65;\ F(3) = 1.0$. Generate U.
**Decision rule (slide):** if $0 \le U \le 0.5$ return **1**; else if $U \le 0.65$ return **2**; else return **3**.
**MCQ-relevant takeaway:** boundaries use ≤; compare U against cumulative probabilities in order.

### Example: Generate Packets with Geometric Distribution
**Given (L3 S12):** packet generation rate $\lambda$ with $0 \le \lambda \le 1$; generate a packet with **probability of success λ**.
**Method:**
1. Draw a random number in $U(0,1)$.
2. **Generate packet if $U(0,1) < \lambda$** (strictly less than).
**Result:** with λ = 0.2: $F_X(0.2) = 0.2$ — i.e., 20% of draws produce a packet.
**Figure:** uniform PDF $f_X(x)$ = rectangle of height 1 on [0,1]; dotted vertical line at x = 0.2; region left of 0.2 labeled **"Generate packet"**, right region labeled **"Don't generate packet"**.
**MCQ-relevant takeaway:** the acceptance test is $U < \lambda$ (not ≤ on the slide's figure; the probability content is identical).

## Diagrams / Figures / Tables

### Handwritten Derivation: Random Variable recap
**Source page:** L3 S6 (handwritten slide)
1. Definition: real-valued functions defined on the sample space are random variables.
2. Example: X = sum of outcomes of **two fair dice**: $P\{X=2\} = P\{(1,1)\} = \frac{1}{36}$; $P\{X=11\} = P\{(5,6),(6,5)\} = \frac{1}{36} + \frac{1}{36} = \frac{1}{18}$.
3. Two kinds of r.v.: **Discrete, Continuous**.

### Handwritten Derivation: Continuous Random Variable & PDF properties
**Source page:** L3 S7
1. CRV definition with non-negative f(x) on $(-\infty, \infty)$.
2. $P_X\{x \in B\} = \int_B f(x)\,dx$.
3. PDF properties: normalization (=1); interval probability $P\{a \le x \le b\} = \int_a^b f_X(x)\,dx$; $P\{x=a\} = 0$; CDF $F_X(a) = \int_{-\infty}^{a} f_X(x)\,dx$.
4. Small sketch: a PDF curve with the shaded area between a and b representing $P\{a \le x \le b\}$.
(One crossed-out intermediate expression appears on the slide — the professor's correction; final content as listed.)

### Handwritten Derivation: Uniform Random Variable
**Source page:** L3 S8
1. U(0,1): f_X(x) = 1 on (0,1), 0 otherwise; sketch of unit-height rectangle over [0,1].
2. $P(a \le x \le b) = b - a$ for 0 < a, b < 1.
3. General (α, β): $f_X(x) = 1/(\beta-\alpha)$; normalization derivation: $\int_{-\infty}^{\infty} f_X = 1 \Rightarrow \int_{\alpha}^{\beta} k\,dx = 1 \Rightarrow k(\beta-\alpha) = 1 \Rightarrow k = \frac{1}{\beta-\alpha}$.

### Diagram: ITT mapping figure
**Slide/Page:** L3 S9
**Purpose:** Geometric illustration of the inverse transform.
**Content:** axes F(x) vs x; CDF curve from origin asymptotic to 1; U1 marked on the F-axis, horizontal line to the curve, vertical line down to X1 on the x-axis.
**Meaning:** pick U, read X = F⁻¹(U) off the CDF.

### Diagram: Geometric packet generation figure
**Slide/Page:** L3 S12
**Purpose:** Visualize the U < λ acceptance test.
**Content:** uniform PDF rectangle (height 1) on [0,1]; vertical dotted line at 0.2; "Generate packet" arrow pointing to the region x < 0.2; "Don't generate packet" arrow for x > 0.2.

## Comparisons

| Feature | ITT (continuous) | ITT (discrete) |
|---|---|---|
| Input | PDF f(x), CDF F(x) | p.m.f. p(x), CDF F(x) |
| Step | Set F(X) = U; invert | Find smallest I with U ≤ F(I) |
| Output | $X = F^{-1}(U)$ | X = I |
| Example | Exponential: $X = -\frac{1}{\lambda}\ln(1-U)$ | dice-like p.m.f. 0.5/0.15/0.35 |

*(L3 S9–S11)*

| Feature | The 4 RNG techniques (all listed) |
|---|---|
| 1 | Inverse transformation technique |
| 2 | Composition method |
| 3 | Convolution method |
| 4 | Acceptance-rejection method |

*(L3 S4; only ITT is detailed in these slides — the other three are [NOT PROVIDED IN LECTURE MATERIAL].)*

## Important Numerical Values
- p.m.f. example: p(1)=0.5, p(2)=0.15, p(3)=0.35; F(1)=0.5, F(2)=0.65, F(3)=1.0. *(L3 S11)*
- Geometric example: λ = 0.2; $F_X(0.2) = 0.2$. *(L3 S12)*
- Two-dice example: P{X=2} = 1/36; P{X=11} = 1/18. *(L3 S6)*

## Important Conditions / Assumptions
- A uniform random variable source is assumed available for all techniques. *(L3 S4)*
- ITT requires F(x) ∈ [0,1] and an invertible CDF. *(L3 S9)*
- Discrete ITT: choose the **smallest positive integer I** with $U \le F(I)$. *(L3 S11)*
- Geometric generation condition: $0 \le \lambda \le 1$; generate iff $U < \lambda$. *(L3 S12)*

## Exceptions / Special Cases
- For a CRV, P{X = a} = 0 — single points carry no probability mass. *(L3 S7)*
- U(0,1) interval probability reduces to b − a. *(L3 S8)*

## MCQ-Relevant Facts
- The four RNG techniques: inverse transformation, composition, convolution, acceptance-rejection. *(L3 S4)*
- ITT: assign F(x) = U(0,1), return X = F⁻¹(U). *(L3 S9)*
- Exponential ITT result: $X = -\frac{1}{\lambda}\ln(1-U)$. *(L3 S10)*
- Exponential PDF/CDF: $f = \lambda e^{-\lambda x}$; $F = 1 - e^{-\lambda x}$. *(L3 S10)*
- Discrete ITT rule: smallest I with U ≤ F(I); example thresholds 0.5 / 0.65 / 1.0. *(L3 S11)*
- Geometric packet generation: generate iff U(0,1) < λ. *(L3 S12)*
- Random variable = real-valued function on the sample space (handwritten definition). *(L3 S6)*
- CDF definition: $F_X(a) = \int_{-\infty}^{a} f_X(x)\,dx$. *(L3 S7)*
- URV on (α,β): PDF = 1/(β−α) inside, 0 outside. *(L3 S8)*
- Lecture 3 slides courtesy: Prof. R Govindarajan (Modeling and Simulation, Jan. 2007). *(L3 S3)*

## Common Confusions
- **PDF vs CDF:** PDF f(x) gives interval probabilities via integration; CDF F(x) = cumulative integral and lives in [0,1] — ITT inverts the **CDF**, not the PDF. *(L3 S7, S9)*
- **ln(1−U) vs ln(U):** the slide's exponential result uses $\ln(1-U)$ (with a leading minus). Both are valid in theory since 1−U ~ U(0,1), but match the slide form in answers. *(L3 S10)*
- **Discrete boundary rule:** use $U \le F(I)$ (≤), and start from the smallest I. *(L3 S11)*
- **P{X=a} for continuous vs discrete:** zero for CRV; for discrete variables the p.m.f. p(a) is the mass. *(L3 S7 vs S11)*

## MCQ Traps
- "ITT inverts the PDF" — FALSE; it inverts the CDF. *(L3 S9)*
- "F(x) can exceed 1" — FALSE; F lies in [0,1], which is why it can be assigned U(0,1). *(L3 S9)*
- "For the discrete example, U=0.5 returns 2" — FALSE; rule says $U \le 0.5$ returns 1. *(L3 S11)*
- "Uniform PDF on (α,β) has height 1" — FALSE in general; height is $1/(\beta-\alpha)$ (equals 1 only for the unit interval). *(L3 S8)*
- "Packet is generated when U > λ" — FALSE; generate when U < λ. *(L3 S12)*
- "Convolution method = inverse transformation" — FALSE; they are two different listed techniques. *(L3 S4)*

## Quick Retrieval Facts
- 4 RNG techniques: ITT, composition, convolution, acceptance-rejection. *(L3 S4)*
- ITT: X = F⁻¹(U), U ~ U(0,1). *(L3 S9)*
- Exponential: X = −(1/λ)·ln(1−U). *(L3 S10)*
- Discrete ITT: smallest I with U ≤ F(I). *(L3 S11)*
- Example CDFs: F(1)=0.5, F(2)=0.65, F(3)=1.0. *(L3 S11)*
- Geometric: generate iff U < λ; λ=0.2 → F(0.2)=0.2. *(L3 S12)*
- PDF normalization: ∫f = 1; P{a≤x≤b} = ∫ₐᵇ f; P{X=a}=0 (CRV); F_X(a)=∫_{−∞}^{a} f. *(L3 S7)*
- U(0,1): f=1 on (0,1); P(a≤x≤b) = b−a; general (α,β): f = 1/(β−α). *(L3 S8)*
- RV = real-valued function on sample space; kinds: discrete, continuous. *(L3 S6)*

## Source Map
- S1: Title (Lecture #3, 18 Aug 2026)
- S2: "This slide deck is available at"
- S3: Agenda + slide courtesy (Prof. R Govindarajan, Jan. 2007)
- S4: Random Number Generation (goal, assumption, 4 techniques)
- S5: Repeat of S4 (animation step)
- S6: Random Variable (quick recap) — HANDWRITTEN
- S7: Continuous Random Variable (quick recap) — HANDWRITTEN (PDF properties)
- S8: Uniform Random Variable (quick recap) — HANDWRITTEN
- S9: Inverse Transformation Technique (ITT) + CDF figure
- S10: ITT contd. — exponential derivation
- S11: Example of ITT to Generate Discrete Random Number
- S12: Generate Packets with Geometric Distribution (+ figure)
- S13: THANK YOU

---

# Lecture 4: Single Queue Simulation, Introduction to LaTeX → Network-on-Chip (NoC)

**Date:** 20 August 2026
**Source File:** `4_lecture_20_08_26.pdf` (24 slides)
**Context:** Per the course timeline, this class covers "Single queue simulation, Introduction to LaTeX" and **Assignment-1 is released today**. The deck's technical content is the **Introduction to Network-on-Chip (NoC)** + BookSim demo intro. *(L4 S2–S3; L2 S3)*

## Topics Covered
- Announcements *(L4 S2)*
- Agenda: Revisiting Multicore Processors; On-chip Communication; Types of Interconnects; Network-on-Chip (NoC); Demo on BookSim *(L4 S3)*
- Multicore processors; example fabric Xeon Phi (KNL) *(L4 S4–S5)*
- A System-on-Chip example; usual components in heterogeneous SoCs *(L4 S6, S8)*
- On-chip communication: message passing; cache-coherent communication flow *(L4 S9–S10)*
- The nightmare of SoC communication; bus-based vs point-to-point *(L4 S12)*
- "The Chip IS the Network": design constraints vs on-chip network benefits *(L4 S14)*
- On-chip networks: why different, different functions *(L4 S15)*
- Topologies *(L4 S16)*
- The network model; router pipeline *(L4 S17–S18)*
- Basic switch microarchitecture *(L4 S19)*
- NoC is a network of queues *(L4 S20)*
- BookSim simulator; example of a trace file *(L4 S22–S23)*

## Key Definitions
- **Multicore processor architecture:** contains **two or more execution cores, or computational engines, within a single processor package**. *(L4 S4)*
- **Examples of execution cores:** CPU and GPU cores; Digital signal processing (DSP); Video encoder/decoders; Vector processing unit; Security engines; and many more. *(L4 S4)*
- **BookSim:** a **cycle accurate NoC simulator**. Input: a **config file consisting of all design parameters**. Output: **performance numbers**. *(L4 S22)*
- **Trace file (BookSim):** **three columns** — Source router, Destination router, Time stamp. **Routers cannot send more than one packet per cycle** ("at once cycle" [sic]); **the number of lines in the trace file = number of packets**. *(L4 S23)*
- **VPU:** Vector Processing Unit. *(L4 S5)*

## Core Concepts

### A System-on-Chip Example *(L4 S6)*
- State-of-the-art SoC blocks (figure): IO ring; **Security Engine, Power Manager, Low Power Audio, Storage, CPU, CPU, 2D/3D Graphics, Image Signal Processor, Video Encode/Decode (1080p), Display Controller**; plus its die floorplan photo.
- **Tens of unique IPs, multiple vendors, multiple protocols.**
- **CPU cores are only a small(er) portion of the whole SoC.**

### Usual Components in Heterogeneous SoCs *(L4 S8; same as L1 S16)*
- Executing cores; Last level cache (LLC); Memory controllers (MC) & controllers; I/O controllers; QPI controllers; Power control unit (PCU); ….
- **Constitutes a large-scale distributed system.**

### On-chip communication *(L4 S9–S10)*
- **Typical example (Message Passing):** an executing core (e.g., CPU) **requests data from a specific address in cache**; the **cache returns the data** stored in that address.
- Figure: CPU Core 1 … CPU Core n, GPU, Video Codec, Display ↔ **Interconnection Network** ↔ **Memory Controller** (annotation: **"Placed at the periphery due to pin locations"**) ↔ **Memory**.
- **Communication Flow (Cache-coherent)** — sequence diagram with lifelines **Core 1, Core 2, LLC m, LLC n, Memor Cont. [sic = Memory Controller], Memory**:
  1. **Core 1 → Read → LLC m: Hit** (blue) → data returned to Core 1.
  2. **Core 2 → Read → LLC m: Miss** (red) → request forwarded → **Memory Controller → Memory** → data returns along **Memory → Memory Controller → LLC m → Core 2**.

### The Nightmare of SoC Communication *(L4 S12)*
- **Increasing bandwidth requirement**
- **Increasing interconnect delay and power consumption**
- **Increasing difficulty in optimization**
- Figure contrast: **Bus based** (DMA, CPU, DSP on a System Bus; Mem Ctrl., Bridge, Peripheral Bus, MPEG, C/I/O blocks, custom interfaces, control wires) vs **Point-to-Point** (dedicated links: DMA—Mem Ctrl.—DSP; CPU—MPEG).

### The Chip IS the Network *(L4 S14)*
- Figure evolution: **Buses** (shared lines) → **P2P irregular architectures** → **Regular NoC architectures** (3×3 grid of switches).
- **Design constraints:** High performance; Low power and reliable operation; **Time-to-market** (ease of design, modularity, CAD tools); Cost.
- **On-chip networks (advantages):** Better scalability; Better predictability; **Higher bandwidth; Concurrent communication; Energy efficiency.**

### On-Chip Networks — why different from other networks? *(L4 S15)*
- **Why are they different?** — **Abundant bandwidth; Power; Wire length distribution.**
- **Different functions:** Operand networks; Cache memory; Message passing.
- Figure: 3×3 mesh of **routing nodes**, each attached to a **Processor (master)**; right column: **Global memory slave, Global I/O slave, Global I/O slave**.

### NoC is a Network of Queues *(L4 S20)*
- **A representative NoC connecting 4 cores (tiles).**
- **Buffers in input, output and link.**
- Figure: four dashed tiles **Tile-1 … Tile-4**; per tile an **Egress** buffer and a **Transgress** buffer; sink points $p_{sink}^1 \ldots p_{sink}^4$; legend: **Backpressure** (red dashed arrows, opposite to traffic), **Traffic flow** (solid), **WRR Arbiter** (weighted round robin), **Split**.
- **MCQ-relevant:** buffer locations = **input, output, and link**; arbiter named = **WRR (weighted round robin)**; backpressure flows opposite to traffic.

## Algorithms / Procedures

### Procedure: Router Pipeline *(L4 S18)*
**Flow:** **Input Buffering → Route Calculation → Switch Allocation → Switch Traversal**
1. **Input Buffering:** the incoming packets are buffered in the input queues.
2. **Route Calculation:** routing information calculated for the **head of each input buffer**.
3. **Switch Allocation (SA):** each input queue sends a request to the SA; **SA does conflict resolution**.
4. **Switch Traversal:** the input channel that **wins arbitration** sends entry **through the crossbar** to the output buffers.
- Related figure (L4 S17): **Router Operational Pipeline: IB | RC & SA | ST | LT** (LT = link traversal to the next router).
**MCQ-relevant information:**
- Stage order: IB → RC → SA → ST (then LT to travel the link).
- Routing decision is computed for the **head** flit/packet of each input buffer.
- SA resolves **conflicts** (arbitration); the crossbar is traversed by the **winning** input channel.

## Formulas
*(No numerical formulas in this lecture; the quantitative content is architectural, below.)*

## Examples

### Example: Xeon Phi (KNL) fabric *(L4 S5; full detail at L1 S15)*
**Given:** Knights Landing tile/chip organization.
**Result:** Chip = **36 tiles on a 2D mesh**; tile = **2 cores + 2 VPU/core + 1 MB L2** (+CHA); MCDRAM 16 GB on-package; DDR4 6×2400 up to 384 GB; 36 PCIe Gen3 lanes; 4 DMI lanes; Omni-Path on-package; 3+ TF DP / 6+ TF SP; ~3× scalar over Knights Corner; Streams Triad: MCDRAM 400+ / DDR 90+ GB/s.
**MCQ-relevant takeaway:** slide adds: **"Also used in client and Xeon server (e.g., Skylake, Icelake)"**; VPU = Vector Processing Unit.

### Example: Example of a Trace File *(L4 S23)*
**Given:** screenshot of a trace file with rows:
```
0 1 1
2 1 1
4 1 1
0 1 2
2 1 2
4 1 2
0 1 3
2 1 3
4 1 3
```
**Method/interpretation:** columns = (source router, destination router, time stamp) per the slide's bullet order. Sources 0, 2, 4 each send one packet to router 1 at time stamps 1, 2, 3 (each source appears once per time stamp — consistent with "routers cannot send more than one packet per cycle").
**Result:** 9 lines = 9 packets.
**MCQ-relevant takeaway:** 3 columns; 1 packet/cycle/source-router max; line count = packet count.

## Diagrams / Figures / Tables

### Diagram: Big/LITTLE-style multicore *(L4 S4)*
**Content:** package containing **BIG CPU CLUSTER** (Core 0–3), **LITTLE CPU CLUSTER** (Core 0–3), **GPU**, **MEMORY**, **ACCELERATORS**.
**Meaning:** a multicore package can mix heterogeneous execution cores.

### Diagram: Communication Flow (Cache-coherent) *(L4 S10)*
**Lifelines:** Core 1, Core 2, LLC m, LLC n, Memor Cont. [sic], Memory.
**Flow:** Core1 Read → LLC m **Hit** → return to Core 1. Core2 Read → LLC m **Miss** → Memory Cont. → Memory → back to Memory Cont. → LLC m → Core 2.
**MCQ-relevant:** On a **hit**, the LLC answers directly; on a **miss**, the request goes through the **memory controller to memory** and the data retraces the path back.

### Diagram: The Network Model *(L4 S17)*
**Content:** Router with **Input 0 … Input (p−1)** → per-input **Input Buffers** with **Route Computation** blocks; **Switch Allocator**; **Crossbar**; **Output 0 … Output (p−1)**. **Router Operational Pipeline: IB | RC & SA | ST | LT.** Text: **"Metrics (for now): latency and bandwidth"**; mesh figure with a dashed **message path**; label: "**Routing, switching, flow control, error control**".
**MCQ-relevant:** current performance metrics = **latency and bandwidth**; the four network functions = routing, switching, flow control, error control; router has p inputs/p outputs with per-input buffers + crossbar.

### Diagram: Basic Switch Microarchitecture *(L4 S19; same figure as L1 S20)*
**Flow:** Physical channel → **Link Control** → **DEMUX** → **Input buffers (IB)** → **MUX** → **CrossBar** → **DEMUX** → **Output buffers** → **MUX** → **Link Control** → Physical channel. **Routing Control and Arbitration Unit** ↔ input buffers / output buffers / crossbar. Phase brackets: **LT** (link), **ST** (IB→output buffers), **RC** (routing control unit). Legend: Buffers; Switch; Routing and Arbitration; Link Controllers; Processor Interface. Parameters: **D hops, L bit message, W bit wide channels**. © T.M. Pinkston, J. Duato, with major contributions by J. Flich.

### Diagram: NoC is a Network of Queues *(L4 S20)*
See *Core Concepts* above. Tiles 1–4, each with **Egress** and **Transgress** buffers, sinks $p_{sink}^{1..4}$, **WRR arbiter**, **split** points, **backpressure** opposite to traffic flow.

### Diagram: Topologies *(L4 S16)*
**Content (6 named topologies with figures):**
- **Mesh** (4×4 grid of crossbar-switch nodes),
- **k-ary n-cube** — "(**Torus is a special case**)",
- **Mixed Topology** (four rings cross-connected),
- **Binary Tree**,
- **Fat Tree** (tree with progressively wider links toward the root),
- **Multistage Interconnection** network (stages of 2×2 switches; inputs labeled 0000, 0001 … outputs 1110, 1111).

## Comparisons

| Feature | Bus based | Point-to-Point | Regular NoC |
|---|---|---|---|
| Structure | Shared system bus (+ bridge to peripheral bus) | Dedicated links between pairs | Grid of routers/switches |
| Shown as | "Nightmare" starting point | Intermediate step | Final evolution ("The Chip IS the Network") |

*(L4 S12, S14)*

| Feature | Design constraints | On-chip network advantages |
|---|---|---|
| Items | High performance; low power & reliable operation; time-to-market (ease of design, modularity, CAD tools); cost | Better scalability; better predictability; higher bandwidth; concurrent communication; energy efficiency |

*(L4 S14)*

| Feature | Hit path (cache-coherent read) | Miss path |
|---|---|---|
| Who answers | LLC m directly | Memory Controller ← Memory, then back through LLC |
| Latency | Shorter | Longer (traverses MC + memory) |

*(L4 S10)*

## Important Numerical Values
- KNL: 36 tiles; 2D mesh; 1 MB L2/tile; MCDRAM 16 GB; DDR4 6 channels @ 2400 up to 384 GB; 36 PCIe Gen3 lanes; 4 DMI lanes; 3+ TF DP / 6+ TF SP flops; MCDRAM 400+ GB/s, DDR 90+ GB/s. *(L4 S5)*
- Representative NoC example connects **4 cores (tiles)**. *(L4 S20)*
- Router operational pipeline: 4 boxes — IB, RC & SA, ST, LT. *(L4 S17)*
- Trace file: 3 columns; ≤1 packet per router per cycle; lines = packets. *(L4 S23)*
- SoC video block: **Video Encode/Decode (1080p)**. *(L4 S6)*
- Deadline: choose project vs exam by **1 September**; Assignment-1 released 20/08. *(L4 S2)*

## Important Conditions / Assumptions
- Routers cannot send more than **one packet per cycle**. *(L4 S23)*
- BookSim input = config file with ALL design parameters; output = performance numbers; it is **cycle-accurate**. *(L4 S22)*
- Memory controllers are placed at the **periphery due to pin locations**. *(L4 S9)*
- Torus is a **special case** of the k-ary n-cube. *(L4 S16)*
- For absence: take appropriate leave on **SAP**, share the screenshot with the instructor **along with a prior email**. *(L4 S2)*

## Exceptions / Special Cases
- On a cache **hit**, memory and the memory controller are never involved. *(L4 S10)*
- CPU cores are only a **small(er)** portion of the whole SoC — the SoC contains tens of IPs from multiple vendors/protocols. *(L4 S6)*

## MCQ-Relevant Facts
- Multicore = ≥2 execution cores within a single processor package. *(L4 S4)*
- Example execution cores: CPU, GPU, DSP, video encoder/decoder, vector processing unit, security engines. *(L4 S4)*
- Xeon Phi (KNL) tile: 2 cores + 2 VPU + 1 MB L2; chip: 36 tiles on 2D mesh. *(L4 S5)*
- SoC communication nightmare triad: ↑bandwidth requirement, ↑interconnect delay & power, ↑optimization difficulty. *(L4 S12)*
- On-chip network advantages: scalability, predictability, higher bandwidth, concurrent communication, energy efficiency. *(L4 S14)*
- On-chip networks differ because of: abundant bandwidth, power, wire length distribution. *(L4 S15)*
- On-chip network functions: operand networks, cache memory, message passing. *(L4 S15)*
- Topologies shown: mesh, k-ary n-cube (torus = special case), mixed, binary tree, fat tree, multistage interconnection. *(L4 S16)*
- Router pipeline stages in order: Input Buffering → Route Calculation → Switch Allocation → Switch Traversal. *(L4 S18)*
- Route calculation uses the **head** of each input buffer; SA resolves conflicts; the arbitration winner crosses the crossbar. *(L4 S18)*
- Router operational pipeline compact form: IB | RC & SA | ST | LT. *(L4 S17)*
- Metrics (for now): **latency and bandwidth**. *(L4 S17)*
- Network responsibilities: routing, switching, flow control, error control. *(L4 S17)*
- Switch μ-arch parameters: D = hops, L = message bits, W = channel width bits. *(L4 S19)*
- Buffers exist at input, output, and link; WRR = weighted round robin arbiter; backpressure opposes traffic flow. *(L4 S20)*
- BookSim = cycle-accurate NoC simulator; files to note: **main.cpp, examples, booksim_config.cpp, traffic.cpp, trafficmanager.cpp**. *(L4 S22)*
- Trace file columns: source router, destination router, time stamp. *(L4 S23)*

## Common Confusions
- **Switch Traversal vs Link Traversal:** ST = through the switch (input buffers → crossbar → output buffers); LT = on the physical link between routers. *(L4 S17, S19)*
- **Route Computation vs Switch Allocation:** RC computes the route from the head of the input buffer; SA arbitrates/conflict-resolves requests for the crossbar. *(L4 S18)*
- **Torus vs k-ary n-cube:** torus is a SPECIAL CASE of k-ary n-cube (not a separate family). *(L4 S16)*
- **Hit vs Miss path:** hit answered by LLC; miss must reach memory via the memory controller. *(L4 S10)*
- **Bus vs NoC:** NoC = regular network of routers (scalable, concurrent); bus = shared medium (the "nightmare" starting point). *(L4 S12, S14)*
- **Egress vs Transgress buffers (L4 S20 figure):** egress = leaving toward the local tile/sink; transgress = passing through to the next tile. [Exact semantic definitions are NOT PROVIDED IN LECTURE MATERIAL; only the figure labels exist.]

## MCQ Traps
- "Torus and k-ary n-cube are unrelated topologies" — FALSE; torus is a special case of k-ary n-cube. *(L4 S16)*
- "The router pipeline is RC → IB → SA → ST" — FALSE; buffering comes FIRST (IB → RC → SA → ST). *(L4 S18)*
- "Route calculation is done for every flit" — slide says for the **head** of each input buffer. *(L4 S18)*
- "Routers can send multiple packets per cycle" — FALSE; at most one. *(L4 S23)*
- "Trace file lines = number of flits" — FALSE; lines = **packets**. *(L4 S23)*
- "BookSim is an analytical (formula-based) simulator" — FALSE; it is **cycle-accurate**. *(L4 S22)*
- "Memory controllers sit at the center of the SoC" — FALSE; placed at the **periphery due to pin locations**. *(L4 S9)*
- "Backpressure arrows point along the traffic flow" — FALSE; they point opposite. *(L4 S20)*
- "Only input buffers exist in a NoC" — FALSE; buffers in **input, output AND link**. *(L4 S20)*

## Quick Retrieval Facts
- NoC agenda: multicore → on-chip communication → interconnect types → NoC → BookSim. *(L4 S3)*
- On a miss: Core → LLC → Memory Controller → Memory → back. *(L4 S10)*
- Nightmare: bandwidth ↑, interconnect delay/power ↑, optimization difficulty ↑. *(L4 S12)*
- NoC benefits: scalability, predictability, bandwidth, concurrency, energy efficiency. *(L4 S14)*
- Why different: abundant bandwidth, power, wire-length distribution. *(L4 S15)*
- Topologies: mesh; k-ary n-cube (torus special case); mixed; binary tree; fat tree; multistage. *(L4 S16)*
- Pipeline: IB → RC → SA → ST → LT; metrics = latency & bandwidth. *(L4 S17–S18)*
- Switch params: D hops, L-bit message, W-bit channels. *(L4 S19)*
- NoC = network of queues; buffers at input/output/link; WRR arbiter. *(L4 S20)*
- BookSim files: main.cpp, examples/, booksim_config.cpp, traffic.cpp, trafficmanager.cpp. *(L4 S22)*
- Trace file: (source, destination, timestamp); 1 packet/cycle; lines = packets. *(L4 S23)*

## Source Map
- S1: Title (Lecture #4, 20 Aug 2026)
- S2: Announcements (Teams, sample projects, A1 today, project/exam by 1 Sep, SAP leave)
- S3: Agenda
- S4: Revisiting Multicore Processors (+ big/little cluster figure)
- S5: Example Fabric: Xeon Phi (KNL) (+ tile figure)
- S6: A System-on-Chip Example (+ SoC blocks & floorplan)
- S7: Agenda repeat
- S8: Usual Components in Heterogeneous SoCs (+ floorplan)
- S9: Message Passing (+ interconnect/MC/memory figure)
- S10: Communication Flow (Cache-coherent) (sequence diagram)
- S11: Agenda repeat
- S12: The Nightmare of SoC Communication (+ bus vs P2P figures)
- S13: Agenda repeat
- S14: The Chip IS the Network (buses → P2P → regular NoC; constraints vs advantages)
- S15: On-Chip Networks (3×3 mesh figure; why different; functions)
- S16: Topologies (6 topology figures)
- S17: The Network Model (router internals + pipeline IB|RC&SA|ST|LT; metrics)
- S18: Router Pipeline (4 stages with descriptions; 2 figure crops)
- S19: Basic Switch Microarchitecture (Pinkston/Duato figure)
- S20: NoC is a Network of Queues (4-tile figure)
- S21: Agenda repeat
- S22: BookSim (simulator description, files)
- S23: Example of a Trace File (+ screenshot)
- S24: THANK YOU

---

# GLOBAL EXAM KNOWLEDGE INDEX

Consolidated across Lectures 1–4. Every entry names its lecture/slide source.

## Important Definitions
- **Simulation:** imitation of some real thing, state of affairs, or process; representing key characteristics/behaviors of a selected physical or abstract system (Wikipedia, quoted). *(L2 S7)*
- **System model:** abstraction of the real system; simplifying assumptions capture only important behaviors; outputs are estimates of real outputs. *(L2 S8)*
- **System State:** collection of state variables. **Simulation Clock:** current value of simulated time. **Timing routine:** determines next event. **Event routine:** updates state/counters, schedules new events. **Event queue:** holds events in chronological order. *(L2 S10–S11)*
- **Random Variable:** real-valued function defined on the sample space; kinds = discrete, continuous. *(L3 S6, handwritten)*
- **CRV:** RV with a continuous set of possible values, with a non-negative f(x) on (−∞, ∞). *(L3 S7)*
- **PDF properties:** ∫f = 1; P{a≤x≤b} = ∫ₐᵇ f; P{X=a} = 0; CDF F_X(a) = ∫_{−∞}^a f. *(L3 S7)*
- **Uniform RV:** U(0,1): f = 1 on (0,1); general (α,β): f = 1/(β−α). *(L3 S8)*
- **Multicore processor:** ≥2 execution cores within a single processor package. *(L4 S4)*
- **VPU:** Vector Processing Unit. *(L4 S5)*
- **BookSim:** cycle-accurate NoC simulator; config file in, performance numbers out. *(L4 S22)*
- **Trace file:** 3 columns (source router, destination router, time stamp); ≤1 packet/router/cycle; #lines = #packets. *(L4 S23)*
- **LLC:** Last Level Cache. **MC:** Memory Controller. **PCU:** Power Control Unit. **QPI:** on-chip interconnect controller block. *(L1 S16 / L4 S8)*
- **Course roles:** Instructor Sumit K. Mandal; TAs Mohammed Sufyan Azam, Vivek Kumar, Samip Poudel. *(L1 S2)*

## Important Formulas
| Formula | Expression | Source |
|---|---|---|
| Assignment grade | $0.4X(3) + 0.2(X(2)+X(4)) + 0.1(X(1)+X(5))$ (X sorted) | L1 S6 |
| Late penalty | $Y = X(1 - 0.1d)$, d ≤ 3 days | L1 S6 |
| Average delay | $\sum_i D_i / n$ (customer average) | L2 S19 |
| Average queue length | $\sum_i I \cdot T_i / T$ (time average) | L2 S20–S22 |
| Server utilization | busy time / total time = 23/25 = 0.92 (example) | L2 S23 |
| Queue-length example | (5·1+2·2+2·3+7·2+2·1)/25 = 31/25 = 1.24 | L2 S22, S44 |
| CRV event probability | $P_X\{x \in B\} = \int_B f(x)dx$ | L3 S7 |
| CDF | $F_X(a) = \int_{-\infty}^{a} f_X(x)dx$ | L3 S7 |
| U(0,1) interval | $P(a \le x \le b) = b - a$ | L3 S8 |
| URV on (α,β) | $f_X(x) = 1/(\beta-\alpha)$ inside, 0 otherwise | L3 S8 |
| ITT | $X = F^{-1}(U)$, U ~ U(0,1) | L3 S9 |
| Exponential PDF/CDF | $f = \lambda e^{-\lambda x}$; $F = 1 - e^{-\lambda x}$ | L3 S10 |
| ITT exponential | $X = -\frac{1}{\lambda}\ln(1-U)$ | L3 S10 |
| Discrete ITT | smallest positive integer I with $U \le F(I)$ | L3 S11 |
| Geometric test | generate packet iff $U(0,1) < \lambda$ | L3 S12 |

## Algorithms / Procedures
1. **Typical flow in simulation (order):** Problem Formulation → Setting of Objectives → Develop Model + Data Collection → Model Translate → Verify → Validate → Exptl. Design → Production Run & Anal. → Output & Document (feedback: Validate→Develop Model; Verify→Model Translate). *(L2 S9)*
2. **DES main loop:** Initialize( ); while(1){ timing routine (determine next event, advance sim time); event routine (update state, update counters, generate+add new event); } Output Result. *(L2 S12)*
3. **Arrival routine:** Arrival event → Schedule next arrival → Server busy? YES: add 1 to queue, store arrival time, return. NO: set delay = 0, add 1 to delayed customers, make server busy, schedule departure event, return. *(L2 S46)*
4. **Single-server trace (worked example):** arrivals 1,4,9,11,24; services 13,7,2,1,1 → departures 13,20,22,23,25; delays 0,9,11,11,0 → final (NumDelayed, D, Q, B) = (5, 41, 31, 23) → avg delay 8.2, avg QL 1.24, util 0.92. *(L2 S30–S45)*
5. **ITT continuous:** F(X) = U → X = F⁻¹(U); exponential case: X = −(1/λ)ln(1−U). *(L3 S9–S10)*
6. **ITT discrete:** generate U; return smallest I with U ≤ F(I); example thresholds 0.5/0.65/1.0 → outputs 1/2/3. *(L3 S11)*
7. **Geometric packet generation:** draw U; packet generated iff U < λ (example λ = 0.2). *(L3 S12)*
8. **Router pipeline:** Input Buffering → Route Calculation (head of input buffer) → Switch Allocation (requests + conflict resolution) → Switch Traversal (arbitration winner crosses crossbar) → (Link Traversal to next router). *(L4 S17–S18)*
9. **Dynamic power management loop:** construct offline policy (once) → per epoch: execute current policy → online power-performance modelling → predict best decision → match? yes → next snippet; no → buffer training data → (buffer full) aggregate → regression learner → new policy. *(L1 S25)*

## Important Comparisons
- **Model vs Simulation:** model = fast analysis; simulation = detailed analysis. *(L1 S18)*
- **Next-event vs fixed-increment time advance:** jump to next event vs fixed Δ (wastes increments between events). *(L2 S11)*
- **Customer-average vs time-average:** avg delay ÷ n; avg queue length & utilization ÷ T. *(L2 S19–S25)*
- **Verify vs Validate:** verify comes first; both after Model Translate (definitions not given in slides). *(L2 S9)*
- **Continuous vs discrete ITT:** invert CDF vs find smallest I with U ≤ F(I). *(L3 S9, S11)*
- **Bus vs Point-to-Point vs Regular NoC:** shared bus → dedicated links → grid of routers ("The Chip IS the Network"). *(L4 S12, S14)*
- **Design constraints vs NoC advantages:** performance/low power/time-to-market/cost ↔ scalability/predictability/bandwidth/concurrency/energy efficiency. *(L4 S14)*
- **Hit vs Miss (cache-coherent read):** LLC answers directly vs goes to Memory via Memory Controller. *(L4 S10)*
- **Switch Traversal vs Link Traversal:** inside the switch vs on the link. *(L4 S17, S19)*
- **Project vs Exam:** [−x, x] & group & 3 phases vs [0, x] & time-bound & MT1/MT2/End. *(L1 S10–S12)*
- **MCDRAM vs DDR4 (KNL):** 16 GB on-package, 400+ GB/s vs 6 DDR4 channels @2400, up to 384 GB, 90+ GB/s. *(L1 S15 / L4 S5)*

## Numerical Values / Parameters
- **Evaluation:** Assignments 30 / Quiz 10 / Participation 20 / Project-or-Exam 40. *(L1 S5)*
- **Assignment weights:** median 0.4; 2nd & 4th 0.2 each; 1st & 5th 0.1 each. Late: 3 days max, −10%/day. *(L1 S6)*
- **Quizzes:** 5 × 15 min, end of class, equal weight, surprise; seminar-trade penalty 30%. *(L1 S8)*
- **Project phases:** 5% (why, 2p) + 15% (how, 3p) + 20% (what, 4p+talk); ≥20% course material; range [−x, x]. *(L1 S10–S11)*
- **Exams:** MT1 5 / MT2 15 / End 20; decide by 1 Sep; range [0, x]; open-world. *(L1 S12)*
- **Worked queue example:** arrivals (1,4,9,11,24); services (13,7,2,1,1); T = 25; departures (13,20,22,23,25); delays (0,9,11,11,0); outputs D=41, Q=31, B=23, delayed=5; averages 8.2, 1.24, 0.92. *(L2 S27–S45)* — see inconsistency note in Lecture 2 (D jump 31→41; cust-1 departure at 13).
- **Discrete p.m.f. example:** 0.5 / 0.15 / 0.35; CDF 0.5 / 0.65 / 1.0. *(L3 S11)*
- **Geometric example:** λ = 0.2; F(0.2) = 0.2. *(L3 S12)*
- **Dice example:** P{X=2} = 1/36; P{X=11} = 1/18. *(L3 S6)*
- **KNL:** 36 tiles, 2D mesh, 2 cores + 2 VPU + 1 MB L2 per tile, MCDRAM 16 GB, DDR4 6×2400 → 384 GB, 36 PCIe Gen3 lanes, 4 DMI, 3+ TF DP / 6+ TF SP, MCDRAM 400+ / DDR 90+ GB/s. *(L1 S15 / L4 S5)*
- **Switch μ-arch params:** D hops, L-bit message, W-bit channels. *(L1 S20 / L4 S19)*
- **NoC example:** 4 tiles; buffers in input/output/link; WRR arbiter. *(L4 S20)*
- **City traffic study:** pb ∈ {0, 0.4, 0.8}; saturation occupancy 50; Delhi earliest ~0.20, Milan ~0.17–0.18, Portland ~0.24–0.25. *(L1 S28)*

## Important Conditions
- If the server is **idle** at arrival → delay = 0, server made busy, departure scheduled; if **busy** → queue+1, store arrival time. *(L2 S46)*
- Delay of a queued customer = service-start time − arrival time. *(L2 trace)*
- Event list must remain in chronological order. *(L2 S11)*
- ITT valid because F(x) ∈ [0,1]; X = F⁻¹(U). *(L3 S9)*
- Discrete ITT: use ≤ against cumulative F; pick smallest I. *(L3 S11)*
- Geometric: generate iff U < λ, with 0 ≤ λ ≤ 1. *(L3 S12)*
- Q(t) in the worked example counts waiting customers only (customer in service excluded). *(L2 graph)*
- NoC routers: ≤1 packet sent per router per cycle. *(L4 S23)*
- Torus = special case of k-ary n-cube. *(L4 S16)*
- Route calculation uses the HEAD of each input buffer; SA resolves conflicts; winner crosses the crossbar. *(L4 S18)*
- Project requires ≥20% course-material application; group-level evaluation. *(L1 S10–S11)*
- Quiz absence: prior notice → make-up; or seminar report with 30% penalty. *(L1 S8)*

## Commonly Confused Concepts (A vs B quick reference)
- **Average delay (ΣD/n) vs Average queue length (ΣI·T/T):** divide by customers vs divide by time; queue length is explicitly a time-average. *(L2 S19–S22)*
- **Verify vs Validate:** order only (verify first) — definitions not in slides. *(L2 S9)*
- **Next-event vs fixed-increment:** jump to event vs fixed step. *(L2 S11)*
- **PDF vs CDF:** density (integrate to get probability) vs cumulative (in [0,1]); ITT inverts the CDF. *(L3 S7, S9)*
- **ln(1−U) vs ln(U):** slide form is X = −(1/λ)ln(1−U). *(L3 S10)*
- **Torus vs k-ary n-cube:** special case vs general family. *(L4 S16)*
- **ST vs LT vs RC vs IB:** switch traversal / link traversal / route computation / input buffering. *(L4 S17–S19)*
- **Hit vs Miss paths:** LLC-local vs via memory controller to memory. *(L4 S10)*
- **Model vs Simulation:** fast vs detailed. *(L1 S18)*
- **Q(t) vs # in system:** worked example's Q(t) excludes the customer in service. *(L2 graph)*
- **Project [−x, x] vs Exam [0, x]:** negative points only possible in project. *(L1 S11–S12)*
- **Egress vs Transgress buffers:** figure labels only (definitions not in slides). *(L4 S20)*

## Diagram Knowledge
- **Knights Landing tile/chip (L1 S15, L4 S5):** tile = 2 cores + 2 VPU + 1 MB L2 (+CHA); 36 tiles on 2D mesh; MCDRAM on-package; PCIe Gen3 + DMI at edge; Omni-Path not shown.
- **Heterogeneous SoC floorplan (L1 S16–S17, L4 S8):** PCU corner; memory controllers on edges; core/LLC+router grid; QPI & PCIe periphery; = large-scale distributed system; designers tune cache size, MC position, interconnect.
- **Switch microarchitecture (L1 S20, L4 S19):** physical channel → link control → DEMUX → input buffers → MUX → crossbar → DEMUX → output buffers → MUX → link control; routing control & arbitration unit; phases LT/ST/RC; queues at input AND output buffers; D hops / L-bit message / W-bit channels.
- **Simulation flow (L2 S9):** 9 boxes with verify/validate feedback loops (see Algorithms).
- **Single-server queue picture (L2 S13–S17):** arrival → queue → server → departure; t_i, A_i, S_i, D_i.
- **Q-length trajectory (L2 S18–S28, S41–S45):** arrivals ↑ at 1,4,9,11,24; departures ↓ at 13,20,22,23,25; levels 0,1,2,3,2,1,0,0 over segments 4,5,2,2,7,2,2,1.
- **DES trace snapshots (L2 S30–S40):** state = server status, Q.Len, arrival-time store, event list (A-x/D-x), clock + counters (NumArr, D(t), Q(t), B(t)).
- **Arrival routine flowchart (L2 S46):** schedule next arrival first → busy branch (queue+store) vs idle branch (delay 0, delayed+1, busy, schedule departure) → return.
- **Handwritten recap slides (L3 S6–S8):** RV definition & dice example; CRV & PDF properties; URV PDFs (unit rectangle; 1/(β−α)).
- **ITT figure (L3 S9):** U1 on CDF axis → curve → X1 = F⁻¹(U1).
- **Geometric figure (L3 S12):** uniform rectangle; U < 0.2 → generate, else don't.
- **Display power graphs (L1 S24):** P_disp linear in normalized brightness; White > Blue > Red > Green > Black.
- **DPM flowchart (L1 S25):** offline policy once; per-epoch loop; regression learner on buffer full.
- **Road queuing network (L1 S27):** (a) road→(λ,Ca)→queue→(μ,Cs); (b) two streams → 2 servers; (c) intersection R1–R4 → Q1–Q4 network.
- **City metrics (L1 S28):** occupancy vs arrival rate; pb = 0/0.4/0.8; saturation at 50; Delhi < Milan < Portland saturation rate.
- **Cache-coherent sequence (L4 S10):** lifelines Core1, Core2, LLC m, LLC n, Memory Cont. [sic], Memory; hit vs miss paths.
- **Network model (L4 S17):** router = input buffers + route computation + switch allocator + crossbar; pipeline IB | RC&SA | ST | LT; metrics = latency & bandwidth; routing/switching/flow/error control.
- **Router pipeline (L4 S18):** IB → RC → SA → ST with per-stage descriptions.
- **Topologies (L4 S16):** mesh, k-ary n-cube (torus special case), mixed, binary tree, fat tree, multistage interconnection.
- **NoC as network of queues (L4 S20):** 4 tiles; egress + transgress buffers; p_sink nodes; backpressure opposite to flow; WRR arbiter; split.
- **Trace file screenshot (L4 S23):** columns (source, destination, timestamp): 0/2/4 → 1 at t = 1,2,3.
- **gem5 figure (L1 S19):** Core+L1 pair → L2 → Memory; Python config; `./gem5 script.py`; outputs "hello world!", l1.misses 2836, l1.hits 10374, cpu.ipc 1.3.

## High-Yield MCQ Facts
1. Evaluation split: 30/10/20/40 (assignments/quiz/participation/project-or-exam). *(L1 S5)*
2. Assignment grade weights the sorted median highest (0.4). *(L1 S6)*
3. Late policy: Y = X(1−0.1d), up to 3 days. *(L1 S6)*
4. 5 surprise quizzes, 15 min, end of class, equal weight. *(L1 S8)*
5. Project phases why/how/what = 5/15/20; group evaluated; range [−x, x]; ≥20% course material. *(L1 S10–S11)*
6. Exam alternative: 5/15/20, decide by 1 Sep, range [0, x], open-world. *(L1 S12)*
7. Simulation = imitation/representation of key behaviors; model outputs = estimates. *(L2 S7–S8)*
8. Compress time → rare events; expand → fast events. *(L2 S8)*
9. DES = 7 components; event queue chronological; timing routine picks next event. *(L2 S10–S11)*
10. Simulation flow order: … Model Translate → Verify → Validate → Exptl. Design → Production Run → Output. *(L2 S9)*
11. Next-event advance jumps to events; fixed-increment wastes steps. *(L2 S11)*
12. A_i = t_i − t_{i−1}. *(L2 S15)*
13. Avg delay = ΣDᵢ/n (customer avg); avg Q length = ΣI·Tᵢ/T (TIME avg); utilization = busy/T. *(L2 S19–S25)*
14. Worked example: (1,4,9,11,24)/(13,7,2,1,1) → 8.2 / 1.24 / 0.92 with (5, 41, 31, 23). *(L2 S42–S45)*
15. Arrival routine: schedule next arrival FIRST; idle → delay 0 + schedule departure; busy → queue + store arrival time. *(L2 S46)*
16. Four RNG techniques: ITT, composition, convolution, acceptance-rejection; uniform source assumed. *(L3 S4)*
17. ITT: X = F⁻¹(U). *(L3 S9)*
18. Exponential: X = −(1/λ)ln(1−U). *(L3 S10)*
19. Discrete ITT: smallest I with U ≤ F(I); example 0.5/0.65/1.0. *(L3 S11)*
20. Geometric packets: generate iff U < λ. *(L3 S12)*
21. P{X = a} = 0 for a continuous RV. *(L3 S7)*
22. U(α,β): f = 1/(β−α); P(a≤x≤b) = b−a on U(0,1). *(L3 S8)*
23. Multicore = ≥2 cores per package; cores can be CPU/GPU/DSP/VPU/security engines. *(L4 S4)*
24. KNL: 36 tiles, 2D mesh, tile = 2 cores + 2 VPU + 1 MB L2. *(L4 S5)*
25. SoC = tens of IPs, multiple vendors/protocols; CPUs are a small portion; SoC = large-scale distributed system. *(L4 S6, S8)*
26. Nightmare: bandwidth ↑, interconnect delay & power ↑, optimization difficulty ↑. *(L4 S12)*
27. NoC advantages: scalability, predictability, higher bandwidth, concurrent communication, energy efficiency. *(L4 S14)*
28. On-chip networks differ due to abundant bandwidth, power, wire-length distribution; functions: operand/cache-memory/message-passing. *(L4 S15)*
29. Topologies: mesh, k-ary n-cube (torus special case), mixed, binary tree, fat tree, multistage. *(L4 S16)*
30. Router pipeline: IB → RC → SA → ST (+LT); RC uses head of buffer; SA resolves conflicts. *(L4 S17–S18)*
31. Metrics (for now): latency and bandwidth. *(L4 S17)*
32. Switch params: D hops, L-bit message, W-bit channels. *(L4 S19)*
33. NoC = network of queues; buffers in input, output, link; WRR arbiter; backpressure opposes flow. *(L4 S20)*
34. BookSim = cycle-accurate; config in → performance out; files: main.cpp, examples, booksim_config.cpp, traffic.cpp, trafficmanager.cpp. *(L4 S22)*
35. Trace file: (source, destination, timestamp); ≤1 packet/cycle; lines = packets. *(L4 S23)*

---

## Final Accuracy Audit (performed before saving)
1. ✅ Every lecture file processed (4/4: 1_Lecture_11_08_26.pdf, 2_Lecture_13_08_26.pdf, 3_lecture_18_08_26.pdf, 4_lecture_20_08_26.pdf).
2. ✅ Every page/slide processed — 32 + 47 + 13 + 24 = 116 slides, each covered in the Source Maps above.
3. ✅ Image-heavy slides rendered to PNG and visually inspected (L1 S15–S17, S19–S20, S24–S25, S27–S28; L2 S9, S12–S13, S17–S18, S22, S26, S28, S30–S42, S46; L3 S6–S9, S12; L4 S4–S6, S8–S10, S12, S14–S20, S23).
4. ✅ Diagram content extracted (components, arrows, flow, labels, values).
5. ✅ Handwritten slides transcribed (L3 S6–S8) with mathematical meaning preserved.
6. ✅ Formulas preserved exactly (signs, subscripts, limits as on slides; normalization integral upper limit noted as printed).
7. ✅ Numerical values preserved (evaluation weights, worked-example quadruple, KNL specs, p.m.f. values).
8. ✅ Worked examples retained with full trace table.
9. ✅ Distinctions between similar concepts in "Common Confusions" everywhere.
10. ✅ No invented content; gaps marked [NOT PROVIDED IN LECTURE MATERIAL] (verify/validate definitions, pb parameter, egress/transgress semantics, non-ITT RNG methods, departure-routine flowchart).
11. ✅ Uncertain OCR/plot readings flagged as approximate (city saturation points; L3 S7 normalization upper limit).
12. ✅ Source (lecture, slide) references throughout.
13. ✅ Markdown structured for AI retrieval (headings, tables, keyword-dense bullets, quick-retrieval sections).
14. ✅ AI can retrieve precise MCQ facts via the Global Index and per-lecture Quick Retrieval Facts.

**Reported source inconsistencies (not silently corrected):**
- L2 worked example: customer 1 departs at 13 (not 1+13=14); D(t) jumps 31→41 at slide 38 (slide's official final = 41, avg delay 8.2); intermediate B(t) values at clocks 20/22 (18/21) vs interval arithmetic (19/20); Q.Len shown as 0 at clock 4 although a customer queues.
- L3 S7: PDF normalization written with upper limit "α" (semantically ∫ over all x = 1).
- L4 S10: "Memor Cont." [sic] = Memory Controller; L4 S23 "at once cycle" [sic] = per cycle.
