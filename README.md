# baby-blind
Baby (read: beginner) 3BLD solver

**If you are here to learn blindfolded solving, start here: [01 - Introduction](01_intro.md)**

---

## Original Vision

This project started as a program to teach users how to solve a 3x3 Rubik's cube
blindfolded. The end goal was a structured series of scrambles with progressively
increasing difficulty, starting from a very small subset of letters and slowly
expanding to the full set.

The original letter difficulty system for edges:

```
Edge Letters: A_CD EFGH IJKL _NOP QRST UVWX

Level 1: ACD
Level 2: ACD UVWX
Level 3: ACD UVWX LR JT
Level 4: ACD UVWX LR JT FH NP
Level 5: ACD UVWX LR JT FH NP EIQ
Level 6: ACD UVWX LR JT FH NP EIQ KS GO
```

### The Vision

1. The human picks a level
2. The computer generates a random string of letters from the letter set of the
   selected level
3. The computer simplifies that random string until it is something you would
   actually memorize
4. The computer finds the scrambled cube that would result from applying those
   letters backwards
5. The computer converts that scrambled cube into a friendlier format
6. The computer applies Kociemba's algorithm, or some other algorithm, to find
   the scramble sequence that results in that cube
7. The computer gives the human the scramble sequence
8. The human applies the scramble sequence, and then solves the cube and times
   themselves
9. This process repeats dozens or hundreds of times until the human feels
   confident with all of the letters in the level, and then the human manually
   chooses to advance to the next level

---

## What Has Been Built

The original vision has been fully realized and expanded:

- A complete cube simulation and Old Pochmann solver in Python
- A Kociemba-based scramble generator that produces scrambles with controlled
  memo difficulty
- **Phase 1** (Recognition Training): 6 levels of edge-only scrambles and 6 levels
  of corner-only scrambles, using progressively larger letter sets
- **Phase 2** (Memo Retention Training):
  - Phase 2A: Constructed short memos (2-14 letters, no parity)
  - Phase 2B: Natural length memos (16-22 letters, no parity)
  - Phase 2C: Parity guaranteed (2 and 16 letters)
  - Phase 2D: Full unrestricted solves
- A complete set of student-facing guides walking a complete beginner through the
  entire learning path

---

## Repository Structure

```
01_intro.md                   ← Start here
phase_1_recog/                ← Phase 1: Recognition Training
    02_phase1_overview.md
    phase_1a_edges/           ← Edge scrambles and guide
    phase_1b_corners/         ← Corner scrambles and guide
    05_bridge.md
phase_2_memo/                 ← Phase 2: Memo Retention Training
    06_phase2_overview.md
    phase_2a_constructed/
    phase_2b_no_parity/
    phase_2c_parity_guaranteed/
    phase_2d_full/
scripts/                      ← Python scripts for generating scrambles
docs/                         ← Reference documents
notebooks/                    ← Development notebooks
```
```

How does that look?