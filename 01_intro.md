# 01 - Introduction to Blindfolded Solving

## Welcome

This repository is a structured training program for learning to solve a Rubik's cube
blindfolded, starting from absolute zero. If you work through it patiently and
systematically, you will be able to solve a Rubik's cube without looking at it.

This is not a quick process. Take your time. Enjoy it.

---

## Prerequisites

You should know how to solve a Rubik's cube with your eyes open before starting this
program. If you don't yet, here are some great resources:

- [How to Solve a Rubik's Cube - WIRED](https://www.youtube.com/watch?v=R-R0KrXvWbc)
- [How to Solve a Rubik's Cube - JPerm](https://www.youtube.com/watch?v=7Ron6MN45LY)

---

## What is Blindfolded Solving?

In a blindfolded solve, the solver is allowed to inspect the cube with their eyes open
for a period of time (called **inspection** or **memo**), then puts on a blindfold and
solves the cube entirely from memory.

The key insight is that you don't need to be able to *see* the cube to solve it — you
just need to have *memorized* where every piece needs to go. The solve itself becomes
a purely mechanical process of executing algorithms you have practiced until they are
muscle memory.

---

## What Method Does This Repo Use?

This repo teaches **Old Pochmann (OP)**, the most beginner-friendly blindfolded solving
method. Old Pochmann works by solving one piece at a time, using just a small number of
algorithms that you likely already know from learning to solve the cube normally.

The best introduction to Old Pochmann is this video by JPerm:
- [JPerm - How to Solve a Rubik's Cube Blindfolded](https://www.youtube.com/watch?v=ZZ41gWvltT8)

We strongly recommend watching this video before or alongside working through this repo.
This repo is loosely based on JPerm's tutorial, but adds a structured progression system
on top of it.

> **Note for advanced learners:** The scrambles in Phase 1 of this repo are also useful
> for people learning more advanced blindfolded methods such as Orozco or 3-Style. The
> recognition and tracing skills trained in Phase 1 are method-agnostic.

---

## The Speffz Lettering Scheme

Old Pochmann requires you to assign a letter to each sticker on the cube, so that you
can describe the cube's state as a sequence of letters — your **memo**. This repo uses
the **Speffz** lettering scheme, which is the most widely used standard.

In Speffz, each of the 24 edge stickers and 24 corner stickers on the cube is assigned
a letter from A to X (Y and Z are not used). You will learn what each letter looks like
on the cube as you work through Phase 1 of this repo.

For a visual reference, JPerm's video above includes a clear diagram of the Speffz
lettering scheme.

---

## The Three Algorithms You Need

Old Pochmann requires only three algorithms. You do not need to learn all three at once
— this repo will tell you when to introduce each one.

**T Perm** (used for edges):
```
R U R' U' R' F R2 U' R' U' R U R' F'
```

**Modified Y Perm** (used for corners):
```
R U' R' U' R U R' F' R U R' U' R' F R
```

**Ra Perm** (used for parity):
```
R U R' F' R U2 R' U2 R' F R U R U2 R' U'
```

> **When do you need each algorithm?**
> - Phases 1 and 2A/2B: T Perm and Y Perm only
> - Phase 2C onwards: Ra Perm is introduced for parity

---

## How to Use This Repo

The learning path is structured into two phases:

**Phase 1 - Recognition Training**
Learn to recognize and trace every edge and corner piece on the cube, using a
progressively larger set of letters. Start with edges, then corners.

**Phase 2 - Memo Retention Training**
Practice holding longer and longer sequences of letters in your memory, culminating
in full blindfolded solves.

### How to Progress Through Levels

Each level contains 500 scrambles. You do not need to do all 500. Instead, work through
scrambles until you feel confident — a good rule of thumb is **10 successful solves in
a row** before moving to the next level. That said, trust your own feel. If you feel
ready, move on. If you don't, keep practicing.

There is no timer here. Accuracy and confidence matter more than speed at this stage.

---

## What's Next?

Head to [02 - Phase 1 Overview](phase_1_recog/02_phase1_overview.md) to begin.