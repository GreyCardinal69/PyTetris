from settings import *
from base_surface import BaseSurface

class Score(BaseSurface):
    def __init__(self):
    	#window size
		# +---------------------------------------------+
		# |                                             |
		# |           SIZE (outer box)     20           |
		# |           Tetris box       SIDEBAR          |
		# |     +--------------+    +-------------+     |
		# |     |              |    |             |     |
		# |  20 |     ++       | 20 |   PREVIEW   | 20  |
		# |     |     +        |    |     .7%     |     |
		# |     |              |    |		      |
		# |     |              |    +------------ +
		# |     |      +       |    |SCORE .3%    |     |
		# |     |     ++       |    |             |     |
		# |     +--------------+    +-------------+ 20  |
		# |            20                               |
		# +---------------------------------------------+
		# 		20 + GAME_WIDTH + 20 + SIDEBAR_WIDTH + 20
        super().__init__(
            width=SIDEBAR_WIDTH,
            height=(GAME_HEIGHT * SCORE_HEIGHT_PERCENT - PADDING),
            position_func=lambda rect: rect.move(
                WINDOW_WIDTH - PADDING - rect.width, WINDOW_HEIGHT - PADDING - rect.height
            )
        )