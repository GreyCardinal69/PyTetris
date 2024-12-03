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






