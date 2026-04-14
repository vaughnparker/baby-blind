# 08 - Phase 2B: Natural Memos, No Parity

## What is Phase 2B?

In Phase 2A, scrambles were constructed to have a specific memo length. In Phase 2B,
scrambles are fully random — but filtered so that parity never occurs and your memo
length falls within a specific range.

This is an important transition. For the first time, you are solving scrambles that
were not specially constructed for you. The cube is in a genuinely random state. The
only concession is that parity has been filtered out, so you still only need the
**T Perm** and **Modified Y Perm**.

---

## What to Expect

Based on analysis of 10,000 random scrambles, the distribution of memo lengths for
a fully random blindfolded solve looks like this:

```
14 letters:  4 solves    (0.04%)
16 letters:  192 solves  (1.92%)
18 letters:  1868 solves (18.68%)
20 letters:  4604 solves (46.04%)
22 letters:  2843 solves (28.43%)
24 letters:  469 solves  (4.69%)
26 letters:  20 solves   (0.20%)
```

Note that memo length is always even. This is a consequence of the cube's permutation
structure — any valid scramble can only be solved with an even total number of swaps,
which means your memo will always have an even number of letters. This is actually a
useful error-checking tool: if you finish tracing and your edge count and corner count
are not both even or both odd, you have made a mistake in tracing and should retrace
before putting on your blindfold.

The vast majority of full solves (over 90%) fall between 18 and 22 letters. Level 4
of Phase 2B — 22 letters — is therefore close to a typical full solve in terms of
memo length.

## The Levels

### Level 1: 16 total letters
Your memo will contain exactly 16 letters in total. This is on the shorter end of
naturally occurring memo lengths.

### Level 2: 18 total letters
Your memo will contain exactly 18 letters in total.

### Level 3: 20 total letters
Your memo will contain exactly 20 total letters. This is the most common memo length
in a fully random solve.

### Level 4: 22 total letters
Your memo will contain exactly 22 letters in total.

---

## How to Use the Scramble Files

The process is the same as in Phase 2A:

1. **Start with a solved cube.**
2. **Apply the scramble** from the file to your cube.
3. **Inspect the cube** and build your memo — edges first, then corners.
4. **Put on your blindfold.**
5. **Solve edges** using the T Perm.
6. **Solve corners** using the Modified Y Perm.
7. **Remove your blindfold** and check if the cube is solved.

Work through the levels in order, starting with
`memo_length_16_scrambles.txt`. Use the **10 successful solves in a row** criterion
before moving to the next level.

---

## What's Next?

Head to [09 - Phase 2C](../phase_2c_parity_guaranteed/09_phase2c_guide.md) to continue.