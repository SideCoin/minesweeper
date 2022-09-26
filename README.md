# Minesweeper 9x9.

### Made by **Regan Yang**. 

Currently isn't optimized for board size changes as I hard coded things to fit the 9x9 board. In the future, I will update this to include GUI, maybe Tkinter? 
The motivation behind this project was to teach myself Python as well as learn how to play minesweeper. Turns out, minesweeper isn't as complex as I thought, but implementing it had some interesting challenges! 
## Rules: 
1) When a square is selected, it will check its surroundings top, bottom
left, right, and diagonals for bombs and indicate number of bombs. 
2) In case where there's no bombs, will check its neighbor squares for bombs, 
repeats if there's no bombs. Ends when all squares have at least 1 bomb as a neighbor
3) The first selected square will never contain a bomb.
4) Game is lost if selected square is a bomb.
5) All ' ' spaces will represent empty squares, numerical squares and 's' will represent selected squares.
's' squares means there are no neighboring bombs.
Squares with no neighboring bombs in rule 2) will also be considered selected squares.
'x' will represent bombs, this will only show when the game is lost. The user may use "flags" to represent squares where the user thinks is a bomb. All flags
will be represented as "F" on the board. Flags are optional!
6) TO INPUT SQUARES, MUST BE NUMERICAL FORMAT. e.g
Select square at [6][6], input must be 66 
FOR SQUARES on the 0th row, single digit or coordinate style e.g 06, 05
7) To win, all available squares have to be bombs

