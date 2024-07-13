# How to solve the Rubik's Cube blindfolded

The aim of this resource is to teach you how to solve a Rubik's cube blindfolded from a starting place of nothing.
If I do a good job, then you won't even need to know how to solve a Rubik's cube with your eyes open in order to take advantage of this guide!

## Table of Contents

1. How many ways can you scramble a Rubik's cube? How many possible configurations/states of a 3x3x3 cube are there?
2. What does it mean for a piece to be solved?
3. How can you "compress" one of these states into an easily memorizable format or "mnemonic"?
4. How can you solve the cube given a specific "mnemonic"?
  * What "swaps" are needed? (edit this)
  * How can we perform these swaps on a real cube? (edit this)
5. Solving the corners
6. What is parity?

### Chapter 0: What is a Rubik's cube?

#### History

A Rubik's cube is a toy developed in 1974 by Hungarian architect Erno Rubik and released for commercial use in 1980. Many sources refer to it as the best selling toy of all time. Solving it with your eyes open is difficult enough, but solving it blindfolded ("blindsolving") can be seen as even more impressive.

#### Blindsolving, simplified

[Here](https://www.youtube.com/watch?v=R9Q4K8HPeTY) is a video of current World Record holder Tommy Cherry doing some unofficial practice outside. Awesome, right? By watching this video, hopefully you can get an idea of what the actual act of blindsolving looks like.

* First, to prepare, he scrambles the cube and starts the timer.
* Without making any turns of the puzzle, he memorizes what the cube looks like.
* He puts on the blindfold.
* Once the blindfold is fully donned, he starts making turns.
* Once he believes he is done, he stops the timer, and takes off the blindfold.

**How is this possible?**

By the end of this guide, you won't quite be world-record level, but hopefully you will be able to understand a basic method of blindsolving well enough to execute it by yourself at home.

Before you can understand **how** to blindsolve, you first must understand **the underlying math** behind the Rubik's cube.

#### Mechanics: What is a Rubik's cube... *really*?

It is of course accurate to describe the Rubik's cube as a toy - as a phyiscal object which exists in the real world. But in order to figure out how blindsolving is doable, it may be more helpful to think of the cube as an abstract mathematical entity. For those who happen to have an understanding of group theory, it is common to describe the cube as a [group](https://en.wikipedia.org/wiki/Rubik%27s_Cube_group). However, no group theory is necessary to learn how to solve the cube.

At first, the cube may appear to contain 6 sides, each with 9 stickers. This isn't necessarily wrong, but there is a key insight to be made - the stickers do not move independently, they are instead attached to one another. For example, a Rubik's cube with a standard color scheme has a "corner piece" which contains a white, red, and green sticker piece. No matter how many twists and turns of the cube you make, you cannot separate the stickers on this piece. There also will only be one corner piece that contains white, green, and red stickers. In addition, you cannot change the order that they are in. Looking at the cube from the outside, the white-red-green corner will always have a white sticker, then clockwise a red sticker, then a green sticker if you move clockwise still.

Because individual pieces cannot be altered, it makes sense to think of the cube as a collection of pieces, rather than a collection of stickers. So - how many pieces are there?

A careful phyiscal examination of the cube reveals that there are:
* 6 pieces with one sticker ("center pieces")
* 12 pieces with two stickers ("edge pieces")
* 8 pieces with three stickers ("corner pieces")

Adding these up, we get 26 pieces, which are sometimes called "cubies". Why 26? Well, you can think of the cube as being "3 pieces long" in each dimension. Therefore, if we use the forumla for volume of a cube as V = s * s * s, we get V = 3 * 3 * 3 = 27. However, of the 27 pieces we would expect to find, one of them occupies the space in the middle of the cube. This is sometimes called the "core." Disassembling a Rubik's cube reveals that the core is connected to the center pieces by long shafts. I encourage the reader to do a google image search for "Rubik's cube core" if they are interested.

There is a second epiphany one must make in order to solve the cube: the 6 center pieces, located in the center of each of the 6 sides, cannot move. The easiest way to understand this is to hold a phyiscal Rubik's cube yourself and to observe what happens to the center pieces when you make turns. No matter what you do, the white center piece will always be opposite the yellow one, the red center piece will be opposite orange, and blue will oppose green (assuming a standard color scheme). Because the center pieces cannot move, they *determine* where the other pieces belong. For example, you may notice that there exists an edge piece (again - exactly 1 edge piece) that is half orange and half green. This piece belongs in between the green center piece and the orange center piece. That is the only place it belongs. The center pieces therefore give us some helpful information - every piece belongs in one, and only one, place (or "slot"). In addition, this means that every piece is either **solved** or **unsolved** (with the exception of the center pieces, which cannot be altered and are therefore always solved). Our large-scale goal is to "solve the cube" - and the only way to do that is to make sure that each individual piece is solved.

Finally, we need to examine what happens to each piece when we make one turn of the cube. We can see that, no matter how scrambled up the cube gets, each edge is always in between two of the center pieces, and each corner is always in between three center pieces. Therefore, each of the 8 corners always exists within one of the 8 "corner slots" and each of the 12 edges always exist in one of the two "edge slots". However, just because an edge occupies the correct slot, doesn't mean that it is necessarily *solved*. For example, here is an example where the AB edge is in the AB slot, yet is still unsolved due to its orientation.

(insert pic here)

**To summarize:**
* A rubik's cube is made up of 26 pieces.
 * 6 center pieces
 * 12 edge pieces
 * 8 corner pieces
* The center pieces do not move.
 * Therefore, the locations of the center pieces determine where the other pieces should go.
* Each piece "type" can only inhabit the space of other pieces of the same piece type.
