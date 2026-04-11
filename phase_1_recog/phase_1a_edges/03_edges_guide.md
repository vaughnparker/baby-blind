# 03 - Phase 1A: Edges

## The Edge Buffer

In Old Pochmann edges, the buffer is the **UR edge** (the edge between the U face and
the R face). In Speffz, this edge has two stickers: **B** (the U face sticker) and
**M** (the R face sticker). Because this is the buffer, you will never memorize B or M
— they are excluded from all edge levels.

This leaves 22 edge letters to learn: A C D E F G H I J K L N O P Q R S T U V W X.

---

## The Edge Levels

You will work through 6 levels. Each level introduces a new set of letters on top of
the previous level. By the end of Level 6, you will be comfortable with all 22 edge
letters.

### Level 1: A C D
**New letters:** A C D

**Reasoning:** These are the U face stickers of the top layer edges.

```
A: Lw2 D' L2
C: Lw2 D L2
D: no setup moves
```

### Level 2: U V W X
**New letters:** U V W X

**Reasoning:** These are the D face stickers of the bottom layer edges.

```
U: D' L2
V: D2 L2
W: D L2
X: L2
```

### Level 3: L R J T
**New letters:** L R J T

**Reasoning:** These are the front and back face stickers of the middle layer edges.

```
L: L'
R: L
J: Dw2 L
T: Dw2 L'
```

### Level 4: F H N P
**New letters:** F H N P

**Reasoning:** These are the left and right face stickers of the middle layer edges.

```
F: Dw' L
H: Dw L'
N: Dw L
P: Dw' L'
```

### Level 5: E I Q
**New letters:** E I Q

**Reasoning:** These are the non-U face stickers of the top layer edges.

```
E: L Dw' L (alternative: L' Dw L')
I: Lw D' L2
Q: Lw' D L2
```

### Level 6: K S G O
**New letters:** K S G O

**Reasoning:** These are the non-D face stickers of the bottom layer edges.

```
K: Lw D L2
S: Lw' D' L2
G: L' Dw' L (alternatives: L Dw L' or D Lw D L2)
O: D2 L' Dw' L (alternative: D' Lw D L2 or D Lw' D' L2)
```

---

## Full Edge Setup Move Reference

For convenience, here is the complete list of edge setup moves:

```
A: Lw2 D' L2
B: buffer (you can't swap with B)
C: Lw2 D L2
D: no setup moves
E: L Dw' L (alternative: L' Dw L')
F: Dw' L
G: L' Dw' L (alternatives: L Dw L' or D Lw D L2)
H: Dw L'
I: Lw D' L2
J: Dw2 L
K: Lw D L2
L: L'
M: buffer (you can't swap with M)
N: Dw L
O: D2 L' Dw' L (alternative: D' Lw D L2 or D Lw' D' L2)
P: Dw' L'
Q: Lw' D L2
R: L
S: Lw' D' L2
T: Dw2 L'
U: D' L2
V: D2 L2
W: D L2
X: L2
```

---

## What's Next?

Work through the scramble files in this folder, starting with
`edges_level_1_scrambles.txt`. When you have completed 10 successful solves in a row
at Level 6, you are ready to move on.

Head to [04 - Phase 1B: Corners](../phase_1b_corners/04_corners_guide.md) to continue.