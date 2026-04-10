# Memo Length Distribution Analysis

## Methodology

We generated 10,000 random scrambles using `new_scrambled_cube()` and solved each one using
`solve_cube()`. The solution string format is `<edge_memo><separator><corner_memo>`, where the
separator is `.` for no parity and `|` for parity. We then measured the edge memo length, corner
memo length, total memo length, and whether parity was present.

## Results (10,000 samples)

### Total memo length
- Min: 14
- Max: 26
- Mean: 20.32

### Edge memo length
- Min: 6
- Max: 17
- Mean: 12.15

### Corner memo length
- Min: 4
- Max: 13
- Mean: 8.16

### Parity
- 5014/10000 solves had parity (50.1%)

### Distribution of total memo length
```
 14:  (4)
 15:  (0)
 16:  (192)
 17:  (0)
 18: ######### (1868)
 19:  (0)
 20: ####################### (4604)
 21:  (0)
 22: ############## (2843)
 23:  (0)
 24: ## (469)
 25:  (0)
 26:  (20)
```

## Key Observations

1. **Total memo length is always even.** No odd totals appear in the distribution at all. This
makes sense because Old Pochmann always solves pieces in pairs — each swap involves 2 pieces —
so the total memo length must always be even.

2. **The distribution is roughly bell-shaped**, peaking at 20 letters total, which represents
the "typical" full solve.

3. **Parity occurs in almost exactly 50% of solves**, which is consistent with theoretical
expectations.

4. **The vast majority of solves (over 90%) fall between 18 and 22 total letters.** The extremes
(14 and 26) are very rare.

## Implications for Phase 2 Level Design

Based on this data, a natural progression for Phase 2 (memo retention training) might be:

```
Level 1:  2-4  total letters  (very short, almost solved cube)
Level 2:  6-8  total letters
Level 3:  10-12 total letters
Level 4:  14-16 total letters
Level 5:  18-20 total letters (approaching typical full solve)
Level 6:  22-26 total letters (full difficulty)
```

Parity should be avoided in the early levels (1-3) since it adds execution complexity on top
of memo complexity. It can be gradually introduced in levels 4 and above, once the student
is comfortable holding a longer memo.

Note that 6 is an arbitrary number of levels here — the actual number should be tuned based
on student feedback and experience.
