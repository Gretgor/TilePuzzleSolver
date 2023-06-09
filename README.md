=============
TILE PUZZLE SOLVER
=============

This program was created to solve simple tile-fitting puzzles, in which the goal is to fit all available tiles onto a board. A proper description of the puzzle is as follows:

> Given:
- A board (called a "grid" in the program), represented by a matrix of characters, where '-' indicates an empty cell and '#' indicates a blocked cell.
- A set of "tiles":
  - Every tile is comprised of a series of orthogonally connected cells, represented by a matrix where '-' denotes an empty (not contained in the tile) cell and '#' represents a piece of the tile.
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
SUBCLASSES
====

> File "common_divisor.py": a subclass of the tileProblem class, called **commonDivisorProblem**, with a bounding heuristic associated with a common divisor.

If a tile problem is such that a common divisor is known for the sizes of the tiles, and the total number of empty spaces in the grid is equal to the sum of the number of cells in every tile, then it is possible to apply the following bounding heuristic:
- If the current state of the game is such that there exists a connected component of empty spaces whose length is not a multiple of the known common divisor, then it is impossible to reach a solved state without replacing or moving an already placed tile.

The proof of the validity of that bound is simple: since every new tile added to the current state of the game has to be placed entirely within one of the connected components (tiles must be orthogonally connected), then the connected component whose size does not match the common divisor cannot have an integer number of tiles in it. A more ellaborate proof is left as an exercise for the more formally inclined.

That bounding heuristic is applied by doing a simple depth-first-search (DFS) over the current state of the game in the is_it_possible method. The example problem for this subclass is equal to the one for the main class, since every tile is of size 6.

====
KNOWN ISSUES
====

Any puzzle containing more than 30 tiles will not work, as the list of symbols in the tileProblem class is limited.
- This can be solved by extending the tile_symbols list in the tileProblem class.

No input validation is done. It is imperative that the user knows what they are doing before using the solver.
