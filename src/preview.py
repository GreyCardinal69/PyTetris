from settings import *

class Preview:
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
		self.surface = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT * SIDEBAR_PREVIEW_HEIGHT_PERCENT))
		self.display_surface = pygame.display.get_surface()

		# create surface engulf rectangle for positioning
		self.rect = self.surface.get_rect(topright = (WINDOW_WIDTH-PADDING,PADDING))

	def run(self):
		self.display_surface.blit(self.surface, self.rect)