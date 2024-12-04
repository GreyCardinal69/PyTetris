from settings import *
from os import path

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
		self.display_surface = pygame.display.get_surface()
		self.surface = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT * SIDEBAR_PREVIEW_HEIGHT_PERCENT))

		# load shape images for previews
		# converting to alpha for pygame 
		self.shape_panels = {shape: pygame.image.load(path.join('..', 'data', f'{shape}.png')).convert_alpha() for shape in TETROMINOS.keys()}

		# create surface engulf rectangle for positioning
		self.rect = self.surface.get_rect(topright = (WINDOW_WIDTH-PADDING,PADDING))

	def display_pieces(self, next_shapes):
		for i, shape in enumerate(next_shapes):
			shape_surface = self.shape_panels[shape]
			height = self.surface.get_height() / 3

			x = self.surface.get_width() / 2
			y = height / 2 + i * height
			rect = shape_surface.get_rect(center = (x,y))
			self.surface.blit(shape_surface,rect )

	def run(self, next_shapes):
		self.surface.fill(GRAY)
		self.display_pieces(next_shapes)
		self.display_surface.blit(self.surface, self.rect)
		pygame.draw.rect(self.display_surface, LINE_COLOR, self.rect, 2, 2)