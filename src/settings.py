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

# Pixel size
CELL_SIZE = 40

# Dynamic game size
GAME_WIDTH = COLUMNS * CELL_SIZE
GAME_HEIGHT = ROWS * CELL_SIZE

# Sidebar size
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
LINE_COLOR = '#FFFFFF' # Grid color
BACKGROUND_COLOR = '#191919'
ACCCENT_COLOR = '#F2BC57' # Also text color

# Tetromine colors
YELLOW_GOLD = '#F2BC57'
BRIGHT_CYAN = '#00C3E3'
RICH_PURPLE = '#ce006b'
BRIGHT_ORANGE = '#F28D35'
BRIGHT_BLUE = '#2A52F2'
BRIGHT_GREEN = '#4CAF50'
BRIGHT_RED = '#F24444'

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
	'T': { 'shape': [(0,0),(-1,0),(1,0),(0,-1)], 'color': RICH_PURPLE },
	'O': { 'shape': [(0,0),(0,-1),(1,0),(1,-1)], 'color': YELLOW_GOLD },
	'J': { 'shape': [(0,0),(0,-1),(0,1),(-1,1)], 'color': BRIGHT_BLUE },
	'L': { 'shape': [(0,0),(0,-1),(0,1),(1,1)], 'color': BRIGHT_ORANGE },
	'I': { 'shape': [(0,0),(0,-1),(0,-2),(0,1)], 'color': BRIGHT_CYAN },
	'S': { 'shape': [(0,0),(-1,0),(0,-1),(1,-1)], 'color': BRIGHT_GREEN },
	'Z': { 'shape': [(0,0),(1,0),(0,-1),(-1,-1)], 'color': BRIGHT_RED }
}

# Spawn tetronimos at the middle of the columns, above visible grid
# To create falling effect
BLOCK_OFFSET = pygame.Vector2(COLUMNS // 2, -1)
# Block fall speed
UPDATE_START_SPEED = 400
# Frame rate input spam protection
USER_INPUT_COOLDOWN = 200
# Block rotation cooldown
USER_ROTATION_COOLDOWN = 200