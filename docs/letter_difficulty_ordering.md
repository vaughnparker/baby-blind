# Baby Blind - Letter Difficulty Ordering

This document describes the letter difficulty ordering for edges and corners in the Baby Blind system.
The letter scheme used is the Speffz lettering scheme.
Buffers are excluded from all levels.

- Edge buffers: B, M
- Corner buffers: A, E, R

---

## Edges

Setup moves use the Old Pochmann method with a Y perm.

### Level 1 (new): A C D
Reasoning: U face (top layer) edges, U face stickers

```
A: Lw2 D' L2
C: Lw2 D L2
D: no setup moves
```

### Level 2 (new): U V W X
Reasoning: D face (bottom layer) edges, D face stickers

```
U: D' L2
V: D2 L2
W: D L2
X: L2
```

### Level 3 (new): L R J T
Reasoning: front and back sides of middle layer edges

```
L: L'
R: L
J: Dw2 L
T: Dw2 L'
```

### Level 4 (new): F H N P
Reasoning: left and right sides of middle layer edges

```
F: Dw' L
H: Dw L'
N: Dw L
P: Dw' L'
```

### Level 5 (new): E I Q
Reasoning: non-U face stickers of top layer edges

```
E: L Dw' L
I: Lw D' L2
Q: Lw' D L2
```

### Level 6 (new): K S G O
Reasoning: non-D face stickers of bottom layer edges

```
K: Lw D L2
S: Lw' D' L2
G: L' Dw' L
O: D2 L' Dw' L
```

---

## Corners

Setup moves use the Old Pochmann method with a Y perm.

### Level 1 (new): U V W X
Reasoning: D face stickers of D face corners (0 moves or single D move setup)

```
U: D
V: no setup moves
W: D'
X: D2
```

### Level 2 (new): B C D
Reasoning: U face stickers of U face corners

```
B: R2
C: F2 D
D: F2
```

### Level 3 (new): I J Q
Reasoning: front and back face stickers of U face corners

```
I: F R'
J: R'
Q: R D'
```

### Level 4 (new): F M N
Reasoning: left and right face stickers of U face corners

```
F: F' D
M: F
N: R' F
```

### Level 5 (new): K L S T
Reasoning: front and back face stickers of D face corners

```
K: F' R'
L: F2 R'
S: D F'
T: R
```

### Level 6 (new): G H O P
Reasoning: left and right face stickers of D face corners

```
G: F'
H: D' R
O: R2 F
P: R F
```