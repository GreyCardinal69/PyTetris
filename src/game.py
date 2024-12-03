from settings import *
from random import *
from timer import Timer

# main tetris display
class Game:
	def __init__(self):
		self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
		# fetch main window aka main.py
		self.display_surface = pygame.display.get_surface()
		self.rect = self.surface.get_rect(topleft = (PADDING, PADDING))
		self.sprites = pygame.sprite.Group()

		# Create overlay surface for grid transparency
		self.line_surface = self.surface.copy()
		# fill with full green that wont be used
		self.line_surface.fill((0,255,0))
		# hide specific color
		self.line_surface.set_colorkey((0,255,0))
		# set transparent
		self.line_surface.set_alpha(120)

		self.tetromino = Tetromino(choice(list(TETROMINOS.keys())), self.sprites, self.create_static_tetromino)

		# timer
		self.timers = {
			'vertical': Timer(UPDATE_START_SPEED, True, self.move_blocks_down),
			'horizontal': Timer(USER_INPUT_COOLDOWN)
		}
		self.timers['vertical'].activate()

	def create_static_tetromino(self):
		self.tetromino = Tetromino( choice(list(TETROMINOS.keys())) , self.sprites, self.create_static_tetromino)


	def run(self):

		self.user_input()
		self.update_timers()
		self.sprites.update()

		# put this surface on main
		self.surface.fill(GRAY)
		self.sprites.draw(self.surface)

		self.draw_grid() 
		self.display_surface.blit(self.surface, (PADDING,PADDING))
		# draw border around main surface
		pygame.draw.rect(self.display_surface, LINE_COLOR, self.rect, 2, 2)

	def move_blocks_down(self):
		self.tetromino.move_blocks_down()

	def update_timers(self):
		for timer in self.timers.values():
			timer.update()

	def user_input(self):
		keys = pygame.key.get_pressed()

		if not self.timers['horizontal'].active:
			if keys[pygame.K_LEFT]:
				self.tetromino.move_horizontal(-1)
				self.timers['horizontal'].activate()
			elif keys[pygame.K_RIGHT]:
				self.tetromino.move_horizontal(1)
				self.timers['horizontal'].activate()

	def draw_grid(self):

		for col in range(1, COLUMNS):
			# move each column line to CELL_SIZE * index, from 1 to avoid line at border
			x = col * CELL_SIZE
			pygame.draw.line(self.line_surface, LINE_COLOR, (x,0), (x,self.surface.get_height()), 1 )

		for row in range(1, ROWS):
			y = row * CELL_SIZE
			pygame.draw.line(self.line_surface, LINE_COLOR, (0,y), (self.surface.get_width(), y), 1)
		self.surface.blit(self.line_surface, (0,0))


class Tetromino:
	def __init__(self, shape, group, create_new):
		self.block_positions = TETROMINOS[shape]['shape']
		self.color = TETROMINOS[shape]['color']
		self.create_new = create_new

		self.blocks = [Block(group, pos,self.color) for pos in self.block_positions]

	def move_blocks_down(self):
		if not self.calculate_vertical_move_collission(self.blocks,1):
			for block in self.blocks:
				block.pos.y += 1
		else:
			self.create_new()

	def calculate_vertical_move_collission(self, blocks, amount):
		collissions = [block.vertical_collide(int(block.pos.y + amount)) for block in self.blocks]
		return True if any(collissions) else False

	def move_horizontal(self, val):
		if not self.calculate_horizontal_move_collission(self.blocks,val):
			for block in self.blocks:
				block.pos.x += val

	def calculate_horizontal_move_collission(self, blocks, amount):
		collissions = [block.horizontal_collide(int(block.pos.x + amount)) for block in self.blocks]
		return True if any(collissions) else False

# All sprites belong to a group which renders them
class Block(pygame.sprite.Sprite):
	def __init__(self, group, pos, color ):
		# initiate into group
		super().__init__(group)
		self.image = pygame.Surface((CELL_SIZE,CELL_SIZE))
		self.image.fill(color)

		#position
		#      Columns:   0      1      2      3      4      5      6      7      8      9
# Rows
#  0         +------+------+------+------+------+------+------+------+------+------+
#            | (0,0)| (0,1)| (0,2)| (0,3)| (0,4)| (0,5)| (0,6)| (0,7)| (0,8)| (0,9)|
#            +------+------+------+------+------+------+------+------+------+------+
#  1         | (1,0)| (1,1)| (1,2)| (1,3)| (1,4)| (1,5)| (1,6)| (1,7)| (1,8)| (1,9)|
#            +------+------+------+------+------+------+------+------+------+------+
#  2         | (2,0)| (2,1)| (2,2)| (2,3)| (2,4)| (2,5)| (2,6)| (2,7)| (2,8)| (2,9)|
#            +------+------+------+------+------+------+------+------+------+------+
#  3         | (3,0)| (3,1)| (3,2)| (3,3)| (3,4)| (3,5)| (3,6)| (3,7)| (3,8)| (3,9)|
#            +------+------+------+------+------+------+------+------+------+------+
#  4         | (4,0)| (4,1)| (4,2)| (4,3)| (4,4)| (4,5)| (4,6)| (4,7)| (4,8)| (4,9)|
#            +------+------+------+------+------+------+------+------+------+------+
#  5         | (5,0)| (5,1)| (5,2)| (5,3)| (5,4)| (5,5)| (5,6)| (5,7)| (5,8)| (5,9)|
#            +------+------+------+------+------+------+------+------+------+------+
#  ...       | ...  | ...  | ...  | ...  | ...  | ...  | ...  | ...  | ...  | ...  |
# 19         |(19,0)|(19,1)|(19,2)|(19,3)|(19,4)|(19,5)|(19,6)|(19,7)|(19,8)|(19,9)|
#            +------+------+------+------+------+------+------+------+------+------+

		# POSITION IN MATRIX INDEX * CELL_SIZE
		# Convert pos to Vector2 for tetromino creation later
		self.pos = pygame.Vector2(pos) + BLOCK_OFFSET
		self.rect = self.image.get_rect(topleft = self.pos * CELL_SIZE)

	def update(self):
		self.rect.topleft = self.pos * CELL_SIZE

	def horizontal_collide(self, x):
		if not 0 <= x < COLUMNS:
			# if outside borders, return true
			return True

	def vertical_collide(self, y):
		if not y < ROWS:
			# if outside borders, return true
			return True























