from copy import deepcopy


class singleTile():
    """
    Class defining single tiles.
    """
    
    def __init__(self, tile, can_mirror = True):
        """
        - set arguument "can_mirror" to False to make a no-mirror tile
        """
        self.rows = len(tile)
        self.cols = len(tile[0])
        self.tile = []
        self.tile.append(tile)
        self.can_mirror = can_mirror
        self.get_all_rotations()

    @staticmethod
    def rotate_90_degrees(tile):
        """
        Rotates the character matrix 'tile' by 90 degrees clockwise.
        """
        new_tile = [['-' for _ in range(len(tile))] for _ in range(len(tile[0]))]
        for i in range(len(tile)):
            for j in range(len(tile[0])):
                new_tile[j][len(tile)-i-1] = tile[i][j]
        return new_tile

    @staticmethod
    def mirror(tile):
        """
        Mirrors a tile along the x axis.
        """
        new_tile = [['-' for _ in range(len(tile[0]))] for _ in range(len(tile))]
        for i in range(len(tile)):
            for j in range(len(tile[0])):
                new_tile[len(tile)-i-1][j] = tile[i][j]
        return new_tile
    
    def get_all_rotations(self):
        """
        Given the matrix passed as a creation argument for the tile, 
        creates all rotations and mirrored rotations of the tile.
        """
        # get 90 degrees
        new_tile = self.rotate_90_degrees(self.tile[0])
        self.tile.append(new_tile)

        # get 180 degrees
        newer_tile = self.rotate_90_degrees(new_tile)
        self.tile.append(newer_tile)

        # get 270 degrees
        newest_tile = self.rotate_90_degrees(newer_tile)
        self.tile.append(newest_tile)

        # if the tile is set to not mirror, do not add the mirror forms
        if not self.can_mirror:
            return

        # mirror
        for i in range(4):
            mirrored_tile = self.mirror(self.tile[i])
            self.tile.append(mirrored_tile)

    def __len__(self):
        return len(self.tile[0])*len(self.tile[0][0])

    def print_all_forms(self):
        """
        Prints all rotations and mirrored rotations for the tile
        """
        for tile in self.tile:
            for row in tile:
                print(''.join(row))
            print('NEXT =========')

    def __str__(self):
        string = ""
        for row in self.tile[0]:
            string += ''.join(row) + '\n'
        return string

        
       
class tileProblem():
    """
    Class containing the tile problem and solver
    """
    
    def __init__(self, tile_list, grid):
        """
        Class attributes:
        -tile_symbols: symbols that will be printed in lieu of '#' when tiles are placed
        -grid: the basic grid as recieved in the input
        -game: saves the current state of the grid with the tiles inserted into it
        -verbose: set to True in order to print the current state of the board for every new move
        """
        self.tile_symbols = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
                             'Q','R','S','T','U','V','W','X','Y','Z','@','1','2','3']
        self.grid = grid
        self.game = deepcopy(grid)
        self.verbose = True
        self.tile_list = self.order_tiles(tile_list)

    def order_tiles(self, tile_list):
        """
        - determines the order in which the tiles will be checked for a position.
        - can be changed in subclasses for order heuristics.
        - this is not made into a static method because subclasses may want to use grid 
          information to determine the order.
        """
        return list(sorted(tile_list,key=lambda x: -len(x)))

    def print_all_tiles(self):
        """
        Prints one form of every tile
        """
        for tile in self.tile_list:
            print(tile)
            print("============")

    def print_game(self):
        """
        Prints the current game state
        """
        for line in self.game:
            print(''.join(line))
        print('')

    def is_it_possible(self):
        """
        Dummy function for bounding conditions.
        To be changed in subclasses in case there is a simple 
        way to determine that a certain configuration does 
        not lead to a solution.
        """
        return True

    def try_for_piece(self, index):
        """
        Attempts to insert the piece at index 'index' in the list of tiles.
        - Attempts every one of the possible configurations for the tile
        - Attempts every possible position
        - Once a valid position is selected, makes a recursive call for index + 1
        """
        if self.verbose:
            self.print_game()
        if index >= len(self.tile_list):
            # all tiles are in, problem solved
            return True

        if not self.is_it_possible():
            return False

        # the 'for' below gets every possible rotation of the tile, one by one
        for matrix in self.tile_list[index].tile:
            # gets every eligible position in the grid
            for i in range(len(self.grid) - len(matrix) + 1):
                for j in range(len(self.grid[0]) - len(matrix[0]) + 1):
                    # checks if it is possible to insert the tile in that position
                    can_try = True
                    for k in range(len(matrix)):
                        if not can_try:
                            break
                        for l in range(len(matrix[0])):
                            if self.game[i + k][j + l] != '-' and matrix[k][l] != '-':
                                can_try = False
                                break

                    # it is possible! Try fitting
                    if can_try:
                        # insert tile into position
                        for k in range(len(matrix)):
                            for l in range(len(matrix[0])):
                                if matrix[k][l] != '-':
                                    self.game[i + k][j + l] = self.tile_symbols[index]
                        value = self.try_for_piece(index + 1)
                        if value:
                            return True
                        # if recursive call did not lead to the solution, removes the tile 
                        # from the position
                        for k in range(len(matrix)):
                            for l in range(len(matrix[0])):
                                if matrix[k][l] != '-':
                                    self.game[i + k][j + l] = '-'
                        
            
        return False

    def solve(self, verbose = True):
        """
        Starts the solving process.
        - Outputs "SOLVED" if the problem is solvable, alongside the solved game.
        - Outputs "SOLUTION NOT FOUND" if the problem is not solvable.
        """
        self.game = deepcopy(self.grid)
        self.verbose = verbose
        success = self.try_for_piece(0)
        if success:
            print("===============")
            self.print_game()
            print("SOLVED")
        else:
            print("SOLUTION NOT FOUND")

if __name__ == '__main__':
    grid = [
    '#############',
    '#####---#####',
    '#-----#-----#',
    '#-#-#---#-#-#',
    '#-----#-----#',
    '##-#-----#-##',
    '##-#-###-#-##',
    '##-#-----#-##',
    '#-----#-----#',
    '#-#-#---#-#-#',
    '#-----#-----#',
    '#####---#####',
    '#############']

    usable_grid = []
    for line in grid:
        usable_grid.append(list(line))

    pieces = [
        [
        '#-',
        '##',
        '-#',
        '##'
        ],
        [
        '-#',
        '##',
        '-#',
        '##'
        ],
        [
        '-##',
        '-#-',
        '-#-',
        '##-'
        ],
        [
        '#-',
        '#-',
        '##',
        '-#',
        '-#'       
        ],
        [
        '--#',
        '###',
        '--#',
        '--#'
        ],
        [
        '###',
        '#-#',        
        '--#'
        ],
        [
        '###',
        '#--',
        '#--',
        '#--'
        ],
        [
        '-#-',
        '###',
        '#-#'
        ],
        [
        '-##',
        '##-',
        '#--',
        '#--'
        ],
        [
        '-#',
        '-#',
        '-#',
        '##',
        '#-'
        ],
        [
        '-##',
        '-#-',
        '##-',
        '#--'
        ],
        [
        '-###',
        '-#--',
        '##--'
        ],
        [
        '----#',
        '#####'
        ]
    ]

    usable_pieces = []
    for piece in pieces:
        new_piece = []
        for line in piece:
            new_piece.append(list(line))
        tile = singleTile(new_piece)
        usable_pieces.append(tile)

    problem = tileProblem(usable_pieces, usable_grid)
    problem.print_all_tiles()
    problem.solve()
