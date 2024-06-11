# baby-blind
Baby (read:beginner) 3BLD solver

This will hopefully be a program that can be used to teach the user how to solve a 3x3 Rubik's cube blindfolded. The end goal is a script that prompts the user with scrambles that are "easy" in several levels.

For example, level 1 might be scrambles that expect you to just solve the edges, and the edge memo might only use "easy letters". A hypothetical letter difficulty system might go like this:

```
Edge Letters: A_CD EFGH IJKL _NOP QRST UVWX

Level 1: ACD
Level 2: ACD UVWX
Level 3: ACD UVWX LR JT
Level 4: ACD UVWX LR JT FH NP
Level 5: ACD UVWX LR JT FH NP EIQ
Level 6: ACD UVWX LR JT FH NP EIQ KS GO
```

An alternative lettering scheme might be based purely on sticker color:
```
Level 1: ACD
Level 2: ACD UVWX
Level 3: ACD UVWX EFGH
Level 4: ACD UVWX EFGH IJKL
Level 5: ACD UVWX EFGH IJKL NOP
Level 6: ACD UVWX EFGH IJKL NOP QRST
```

Future work:
* First we need to make a solver which prints solutions in a specific format.
* Next, we have to generate lots of these scrambles, and then filter them down to scrambles whose edge solutions ONLY contain the letters that we are interested in (for example, level 2 will only give scrambles that require a solver to memorize letters in the set [ACD UVWX]).
* This will likely not be sufficient for the smaller levels. Even if we generate 1,000,000 scrambles, it is unlikely that all the edges in the bottom two layers are solved. We will need to employ some sort of actually intelligent algorithm (potentially Kociemba's algorithm) in order to intelligently generate scrambles that have a reduced subset of letters to memo.
* In the far future, I would like this github repo to be a sufficient resource for new cubers learning to start blind solving, starting from the absolute basics and moving very, very slowly.

### The vision

The vision is

1. The human picks a level
2. The computer generates a random string of letters from the letter set of the selected level
3. The computer simplifies that random string until it is something you would actually memorize
4. The computer finds the scrambled cube that would result from applying those letters backwards
5. The computer converts that scrambled cube into a friendlier format
6. The computer applies kociembas algorithm, or some other algorithm, to find the scamble sequence that results in that cube
7. The computer gives the human the scramble sequence
8. The human applies the scramble sequence, and then either types it back to the computer or just solves the cube and times themselves.
9. This process repeats dozens or hundreds of times until the human feels that they are confident with all of the letters in the level, and then the human manually chooses to advance to the next level.
