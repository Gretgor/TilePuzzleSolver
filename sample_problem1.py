from main_class import tileProblem, singleTile
from common_divisor import commonDivisorProblem

grid = [
    '#############',
    '##---###---##',
    '##-#-----#-##',
    '##-#-###-#-##',
    '##-#-----#-##',
    '#-----#-----#',
    '#-###-#-###-#',
    '#-----#-----#',
    '##-#-----#-##',
    '##-#-###-#-##',
    '##-#-----#-##',
    '##---###---##',
    '#############'    
    ]

usable_grid = []
for line in grid:
    usable_grid.append(list(line))

tiles = [
        [
        '##-',
        '#--',
        '#--',
        '#--',
        '###'
        ],
        [
        '##',
        '#-',
        '#-',
        '#-',
        '##',
        '-#'
        ],
        [
        '-#-',
        '-#-',
        '-#-',
        '-#-',
        '###',
        '--#'
        ],
        [
        '-##',
        '-#-',
        '-#-',
        '-#-',
        '###'
        ],
        [
        '#---',
        '#---',
        '####',
        '-#--',
        '-#--'
        ],
        [
        '-#---',
        '-#---',
        '-#---',
        '#####'
        ],
        [
        '-###',
        '-#--',
        '-#--',
        '##--',
        '-#--'
        ],
        [
        '##-',
        '#--',
        '###',
        '-#-',
        '-#-'
        ],
        [
        '-#-',
        '###',
        '#--',
        '###'
        ]
    ]

usable_pieces = []
for piece in tiles:
    new_piece = []
    for line in piece:
        new_piece.append(list(line))
    tile = singleTile(new_piece)
    usable_pieces.append(tile)

problem = commonDivisorProblem(usable_pieces, usable_grid, 8, find_all = True)
problem.print_all_tiles()
problem.solve(verbose = False)
