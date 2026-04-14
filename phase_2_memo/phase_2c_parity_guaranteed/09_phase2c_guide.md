# 09 - Phase 2C: Parity Introduced

## What is Phase 2C?

In Phase 2C, every single scramble has parity. The memo lengths are kept short and
familiar — just 2 or 16 letters total — so that you can focus entirely on one new
challenge: learning to detect and execute parity.

This is where you learn the **Ra Perm**, the third and final algorithm you need for
Old Pochmann.

---

## What is Parity?

Parity is a situation that occurs in roughly half of all blindfolded solves. It is a
consequence of the cube's permutation structure — specifically, it arises when the
edge permutation and corner permutation are both odd.

In practical terms, you will know you have parity by counting your memo letters:

- If your edge memo has an **odd** number of letters, you have parity.
- If your edge memo has an **even** number of letters, you do not have parity.

Your corner memo count will always agree with your edge memo count — both will be odd
(parity) or both will be even (no parity). If one is odd and the other is even, you
have made a mistake in tracing and should retrace before putting on your blindfold.

---

## What to Do When You Have Parity

If you have parity, you must execute the **Ra Perm** after solving your edges and
before solving your corners:

```
R U' R' U' R U R D R' U' R D' R' U2 R' U'
```

The order is:
1. Solve edges (T Perm)
2. Execute Ra Perm
3. Solve corners (Modified Y Perm)

If you do not execute the Ra Perm when you have parity, your corners will not solve
correctly.

---

## A Note on Solve Order

This guide recommends solving edges first, then corners. This is the most common
approach and is what JPerm's tutorial teaches.

However, it is not required. You could solve corners first and edges second. If you
do, parity detection works the same way — just check your corner memo count instead
of your edge memo count. If your corner memo has an odd number of letters, you have
parity, and you must execute the Ra Perm after solving corners and before solving
edges.

Whichever order you choose, be consistent — pick one and stick with it.

---

## The Levels

### Level 1: 2 total letters (parity guaranteed)
Your memo will contain exactly 2 letters in total — 1 edge and 1 corner. This is the
simplest possible parity case. The memo burden is minimal so you can focus entirely
on recognizing parity and executing the Ra Perm correctly.

### Level 2: 16 total letters (parity guaranteed)
Your memo will contain exactly 16 letters in total. This is a more realistic memo
length, similar to Phase 2B Level 1. By this point you should be comfortable
detecting and executing parity.

---

## How to Use the Scramble Files

1. **Start with a solved cube.**
2. **Apply the scramble** from the file to your cube.
3. **Inspect the cube** and build your memo — edges first, then corners.
4. **Count your edge letters** — they will always be odd in this phase.
5. **Put on your blindfold.**
6. **Solve edges** using the T Perm.
7. **Execute the Ra Perm.**
8. **Solve corners** using the Modified Y Perm.
9. **Remove your blindfold** and check if the cube is solved.

Work through the levels in order, starting with
`memo_length_2_scrambles.txt`. Use the **10 successful solves in a row** criterion
before moving to the next level.

---

## What's Next?

Head to [10 - Phase 2D](../phase_2d_full/10_phase2d_guide.md) to continue.