from main_class import tileProblem, singleTile

class commonDivisorProblem(tileProblem):
    """
    Problem subclass for puzzles where every tile has a known
    common divisor.

    MAKE SURE the common divisor is correct for the set of tiles,
    as otherwise, you may get a false negative solution
    """

    def __init__(self, tile_list, grid, common_divisor = 1):
        super().__init__(tile_list, grid)
        self.common_divisor = common_divisor

    def is_it_possible(self):
        """
        This version of the method verifies if every connected
        set of empty spaces in the game has a number of cells
        that is a multiple of the common divisor.
        """
        if self.common_divisor == 1:
            # without a common divisor greater than 1, this method cannot help
            return True

            
        visited = [[False for _ in range(len(self.grid[0]))] for _ in range(len(self.grid))]
        # no diagonal directions, because all tiles have to be orthogonally connected
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        # scan the matrix for empty spaces to start the search in
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if not visited[i][j] and self.game[i][j] == '-':
                    # found an empty space, start counting via DFS
                    count = 1
                    visited[i][j] = True
                    # yes, I know this is being used as a stack rather than a queue
                    queue = [[i,j]]
                    while queue:
                        cell = queue.pop()
                        for direction in directions:
                            next_one = [cell[0] + direction[0], cell[1] + direction[1]]
                            if next_one[0] < 0 or next_one[1] < 0 or next_one[0] >= len(self.grid) or next_one[1] >= len(self.grid[0]):
                                # out of bounds
                                continue
                            if not visited[next_one[0]][next_one[1]] and self.game[next_one[0]][next_one[1]] == '-':
                                # adjacent empty cell found, add up counter and stack it
                                visited[next_one[0]][next_one[1]] = True
                                count += 1
                                queue.append(next_one)
                    # at the end of the while loop, "count" will contain the amount of empty cells in the connected component
                    if count % self.common_divisor:
                        if self.verbose:
                            print(f"Infeasibility found: empty space of size {count}")
                        return False
        return True

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

    problem = commonDivisorProblem(usable_pieces, usable_grid, 6)
    problem.print_all_tiles()
    problem.solve()
