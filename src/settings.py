import pygame

#       y
#         ^
#         |
# 20      |		+---+---+---+---+---+---+---+---+---+---+
#         |		|   |   |   |   |   |   |   |   |   |   |
#         |		+---+---+---+---+---+---+---+---+---+---+
#         |		|   |   |   |   |   |   |   |   |   |   |
#         |		+---+---+---+---+---+---+---+---+---+---+
#         |		|   |   |   |   |   |   |   |   |   |   |
#         |		+---+---+---+---+---+---+---+---+---+---+
#		  |		.........................................
#         |                     
#         +-------------------------------------------------------------> x
#                               10

COLUMNS = 10
ROWS = 20

# pixel size
CELL_SIZE = 40

# Dynamic game size
GAME_WIDTH = COLUMNS * CELL_SIZE
GAME_HEIGHT = ROWS * CELL_SIZE

#sidebar size
SIDEBAR_WIDTH = 200
SIDEBAR_PREVIEW_HEIGHT_PERCENT = 0.7
SCORE_HEIGHT_PERCENT = 1 - SIDEBAR_PREVIEW_HEIGHT_PERCENT

#window size
# +---------------------------------------------+
# |                                             |
# |           SIZE (outer box)     20           |
# |           Tetris box       SIDEBAR          |
# |     +--------------+    +-------------+     |
# |     |              |    |             |     |
# |  20 |     ++       | 20 |   PREVIEW   | 20  |
# |     |     +        |    |             |     |
# |     |              |    +-------------+     |
# |     |              |    |             |     |
# |     |      +       |    |   SCORE     |     |
# |     |     ++       |    |             |     |
# |     +--------------+    +-------------+ 20  |
# |            20                               |
# +---------------------------------------------+
# 		20 + GAME_WIDTH + 20 + SIDEBAR_WIDTH + 20

PADDING = 20
WINDOW_WIDTH = GAME_WIDTH + SIDEBAR_WIDTH + PADDING * 3
WINDOW_HEIGHT = GAME_HEIGHT + PADDING * 2

# UI Colors
LINE_COLOR = '#FFFFFF'
GRAY = '#1C1C1C'
PURPLE = '#7b217f'


# 'T': { 'shape': [(0,0),(-1,0),(1,0),(0,-1)]
#
#   -3   -2   -1    0    1    2    3   (Columns)
# +----+----+----+----+----+----+----+
# |    |    |    |    |    |    |    |  3
# +----+----+----+----+----+----+----+
# |    |    |    |    |    |    |    |  2
# +----+----+----+----+----+----+----+
# |    |    |    |    |    |    |    |  1
# +----+----+----+----+----+----+----+
# |    |    | X  |  X |  X |    |    |  0
# +----+----+----+----+----+----+----+
# |    |    |    |  X |    |    |    |  -1 
# +----+----+----+----+----+----+----+
# |    |    |    |    |    |    |    |  -2
# +----+----+----+----+----+----+----+
# |    |    |    |    |    |    |    |  -3
# +----+----+----+----+----+----+----+

TETROMINOS = {
	'T': { 'shape': [(0,0),(-1,0),(1,0),(0,-1)], 'color': PURPLE },
	'O': { 'shape': [(0,0),(0,-1),(1,0),(1,-1)], 'color': PURPLE },
	'J': { 'shape': [(0,0),(0,-1),(0,1),(-1,1)], 'color': PURPLE },
	'L': { 'shape': [(0,0),(0,-1),(0,1),(1,1)], 'color': PURPLE },
	'I': { 'shape': [(0,0),(0,-1),(0,-2),(0,1)], 'color': PURPLE },
	'S': { 'shape': [(0,0),(-1,0),(0,-1),(1,-1)], 'color': PURPLE },
	'Z': { 'shape': [(0,0),(1,0),(0,-1),(-1,-1)], 'color': PURPLE }
}

# spawn tetronimos at the middle of the columns, above visible grid
# to create falling effect
BLOCK_OFFSET = pygame.Vector2(COLUMNS // 2, 5)