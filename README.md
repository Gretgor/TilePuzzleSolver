=============
TILE PUZZLE SOLVER
=============

This program was created to solve simple tile-fitting puzzles, in which the goal is to fit all available tiles onto a board. A proper description of the puzzle is as follows:

> Given:
- A board (called a "grid" in the program), represented by a matrix of characters, where '-' indicates an empty cell and '#' indicates a blocked cell.
- A set of "tiles":
  - Every tile is comprised of a series of orthogonally adjacent cells, represented by a matrix where '-' denotes an empty (not contained in the tile) cell and '#' represents a piece of the tile.
> Find:
  - A way to fit every tile into the board such that:
    - No tile intersects a blocked cell of the board.
    - No tile intersects another tile.
    - The game is discrete: cells are either occupied or unoccupied, no half-occupation allowed. The number of cells of a tile is equal to the number of cells it occupies in the grid.
    - Tiles can be turned 90, 180 and 270 degrees, and also mirrored, but cannot be placed diagonally.
      - Specific tiles can be set to "not mirrorable" in case it is a necessary rule, or to save time in case the mirror forms are isomorphic to normal forms.

=====
PROGRAM STRUCTURE
=====

File "main_class.py": ccontains the main tile and problem classes, as well as the solver.

- Class "singleTile": the class used to represent every single tile in a set of tiles. Its creation routine recieves a single sample matrix of the tile, and creates all possible configurations for said tile (i.e. all rotations and mirrored rotations).
- Class "tileProblem": the class that houses the problem itself, including its grid and set of tiles, as well as the simple solving algorithm.
  - Solving algorithm: the solving algorithm is a simple recursive method which attempts to fit every piece, starting from the largest one, one by one. Without anything added into the is_it_possible method, the algorithm is a simple brute-force, attempting every possible configuration for every tile until finding a proper one. 
    - Heuristics for bounding can be added in subclasses via the is_it_possible method.
    - Heuristics for the order in which tiles are to be attempted can be added via the 'order_tiles' method.

====
KNOWN ISSUES
====

Any puzzle containing more than 30 tiles will not work, as the list of symbols in the tileProblem class is limited.
- This can be solved by extending the tile_symbols list in the tileProblem class.

No input validation is done. It is imperative that the user knows what they are doing before using the solver.
