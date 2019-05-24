# sliding-tiles
A simple sliding puzzle game, featuring famous surrealist paintings

- This is a modification of the awesome Sliding Puzzle game by Al Sweigart, https://inventwithpython.com/pygame/chapter4.html

- This modification was created by Ryan Welfle and Lorenzo Baitwa

- This modification was created using Spyder 3.3.2, and thus would best be run via that environment



Welcome to the Sliding Tiles: README!

Thank you for choosing to play “Sliding Tiles”!
There are a few things you need you need to know to get this game up and running ...
- Get either the ‘Sliding Tiles (windows) - R.Welfle - L.Baitwa.py’ or the 'Sliding Tiles (osx) - R.Welfle - L.Baitwa.py' file downloaded onto your computer (depending on with operating system you're using)
- Download and unzip the 'slidingimagesandmusic.zip' file, and put the contents in the same directory as the main program PY file
- Before you open the game via the pertinent PY file, make sure that you have the ‘pygame’ module installed on your computer, as this program will not work without it; you can install it by opening a Terminal window (for OSX) or Command Prompt window (for Windows) and typing the command ‘pip install pygame’
- Once ‘pygame’ is successfully installed, the best way to open the program is open up Spyder (if you have it) and drag-and-drop the PY file from the folder that represents your operating system into Spyder
- To start the game, press F5 or click on the ‘Run File’ button in Spyder; a window should open up revealing the game!

Now that the ‘Sliding Tiles’ window has opened, here is how you can navigate the program (!) ...
- The opening window screen will show the “solved” screen state of one of two images that you can play the game with; this image is a version of a 1964 painting by Rene Magritte called “The Son of Man”; you can play around with sliding the tiles on this opening screen, but this hardly constitutes as playing the actual game itself
- You can shuffle the tiles around by either clicking on the tiles adjacent to an empty space, or by using the arrow keys on your keyboard, or by using the W-A-S-D letter keys on your keyboard
￼
- If you click on the ‘Image #1 Easy Game’ button, the Rene Magritte image will randomly shuffle its tiles 100 times; from there on in it is your goal to shuffle the image back to its original state
- If you click on the ‘Image #1 Hard Game’ button, the Rene Magritte image will randomly shuffle its tiles 350 times, and you must shuffle the image back to its original state
- If you click on the ‘Image #2 Easy Game’ button, the tiled image will change in a version of a 1921 painting by Max Ernst called “The Elephant Celebes” (that is, if that image is not there already); from there the Max Ernst image will randomly shuffle its tiles 100 times, and you must shuffle the image back to its original state
- If you click on the ‘Image #2 Hard Game’ button, the Max Ernst image will randomly shuffle its tiles 350 times, and you must shuffle the image back to its original state
- While in the middle of a game, you have four options to the right-hand side of the puzzle: ‘Reset Last Five’, ‘Reset All’, ‘Solve 20 Moves’, and ‘Solve All’
- If you select ‘Reset Last Five’ in the middle of a game, the game will undo the last five tiles slides that you made during the game-play; if you have made less than five tile slides in total, like three slides for example, then the game will undo those three slides
- If you select ‘Reset All’ in the middle of a game, the game will undo all of the tile slides that you made during the game-play
- If you select ‘Solve 20 Moves’ in the middle of a game, the game will get you twenty correct moves closer to solving the puzzle (think of this as a ‘help function’); for ‘easy’ games, you can press this button a maximum of 5 times before the puzzle ends up being solved; for ‘hard’ games, you can press this button a maximum of 18 times before the puzzle ends up being solved
- If you select “Solve All” in the middle of a game, the game will solve the puzzle completely right before your very eyes!
- WINDOWS VERSION ONLY! ​There is also the option to stop and start the game’s background music; to start the game’s background music (which will play on an infinite loop until stopped) press the ‘Play Background Music’ button; to stop the game’s background music press the ‘Stop Background Music’ button
