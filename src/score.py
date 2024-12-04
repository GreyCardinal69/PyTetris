from settings import *
from os import path

class Score:
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
		self.surface = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT * SCORE_HEIGHT_PERCENT - PADDING))
		self.display_surface = pygame.display.get_surface()

		self.font = pygame.font.Font( path.join('..', 'data', 'zekton.ttf') ,25)

		self.height_increment = self.surface.get_height() / 3

		# create surface engulf rectangle for positioning
		self.rect = self.surface.get_rect(bottomright = (WINDOW_WIDTH-PADDING,WINDOW_HEIGHT-PADDING))

		self.score = 0
		self.level = 1
		self.lines = 0

	def display_text(self, pos, text):
		# true for smooth edges
		text_surface = self.font.render( f'{text[0]}: {text[1]}', True, LINE_COLOR)
		text_rect = text_surface.get_rect( center = pos)
		self.surface.blit( text_surface, text_rect)

	def run(self):
		self.surface.fill(GRAY)

		for i, text in enumerate([('Score', self.score), ('Level', self.level), ('Lines', self.lines)]):
			x = self.surface.get_width() / 2
			# top padding + i * padding for each element
			y = self.height_increment / 2 + i * self.height_increment
			self.display_text( (x,y), text )

		self.display_surface.blit(self.surface, self.rect)
		pygame.draw.rect(self.display_surface, LINE_COLOR, self.rect, 2, 2)
		# draw border
		