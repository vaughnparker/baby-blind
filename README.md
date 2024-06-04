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
