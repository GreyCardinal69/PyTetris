from settings import *
from random import *
from timer import Timer
from pygame import mixer 
from os import path

# main tetris display
class Game:
	def __init__(self, get_next_shape, update_score):
		self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
		# fetch main window aka main.py
		self.display_surface = pygame.display.get_surface()
		self.rect = self.surface.get_rect(topleft = (PADDING, PADDING))
		self.sprites = pygame.sprite.Group()
		# function in MAIN
		self.get_next_shape = get_next_shape
		self.update_score = update_score

		# Create overlay surface for grid transparency
		self.line_surface = self.surface.copy()
		# fill with full green that wont be used
		self.line_surface.fill((0,255,0))
		# hide specific color
		self.line_surface.set_colorkey((0,255,0))
		# set transparent
		self.line_surface.set_alpha(120)

		# data and score
		self.current_score = 0
		self.best_score = 0
		self.current_lines = 0
		self.current_level = 1

		self.game_data = [[ 0 for x in range(COLUMNS)] for y in range(ROWS)]
		self.tetromino = Tetromino(choice(list(TETROMINOS.keys())), self.sprites, self.create_static_tetromino, self.game_data)

		self.down_speed = UPDATE_START_SPEED
		self.hastened_down_speed = self.down_speed * 0.2
		self.down_press = False
		# timer
		self.timers = {
			'vertical': Timer(self.down_speed, True, self.move_blocks_down),
			'horizontal': Timer(USER_INPUT_COOLDOWN),
			'rotation': Timer(USER_ROTATION_COOLDOWN)
		}
		self.timers['vertical'].activate()

	def create_static_tetromino(self):
		self.check_gameover()
		# Create new block on border hit
		self.check_full_row()
		self.tetromino = Tetromino( self.get_next_shape(), self.sprites, self.create_static_tetromino, self.game_data)


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

	def calculate_score(self, num_cleared_lines):
		self.current_lines += num_cleared_lines
		self.current_score +=( 100 * num_cleared_lines ) * num_cleared_lines

		# update level for each 10 cleared lines
		if self.current_lines / 10 > self.current_level:
			self.current_level = min( 10, self.current_level + 1 )
			self.down_speed *= 0.75
			self.hastened_down_speed = self.down_speed * 0.3
			self.timers['vertical'].duration = self.down_speed
		self.update_score( self.current_lines, self.current_score, self.current_level)

	def check_gameover(self):
		delete_rows = []
		# get indexes
		for i, row in enumerate(self.game_data):
			delete_rows.append(i)
		game_over = False
		for delete_row in delete_rows:
			for block in self.game_data[delete_row]:
				# pygame method to kill sprite
				if block != 0 and int(block.pos.y) <= 0:
					game_over = True
					break
		if game_over:
			for delete_row in delete_rows:
				for block in self.game_data[delete_row]:
					# pygame method to kill sprite
					if block != 0:
						block.kill()
			self.game_data = [[ 0 for x in range(COLUMNS)] for y in range(ROWS)]
			self.current_lines = 0
			self.current_level = 1
			self.current_score = 0
			self.update_score( self.current_lines, self.current_score, self.current_level)
			game_over = False

	# Row filled with blocks, clear it
	def check_full_row(self):
		delete_rows = []
		# get indexes
		for i, row in enumerate(self.game_data):
			if all(row):
				delete_rows.append(i)
		if delete_rows:
			for delete_row in delete_rows:
				for block in self.game_data[delete_row]:
					# pygame method to kill sprite
					block.kill()

				# move blocks down
				for row in self.game_data:
					for block in row:
						if block and block.pos.y < delete_row:
							block.pos.y += 1 # not 0 in grid
			self.game_data = [[ 0 for x in range(COLUMNS)] for y in range(ROWS)]

			for block in self.sprites:
				self.game_data[int(block.pos.y)][int(block.pos.x)] = block
		# update score
		self.calculate_score(len(delete_rows))

	def user_input(self):
		keys = pygame.key.get_pressed()

		if not self.timers['horizontal'].active:
			if keys[pygame.K_LEFT]:
				self.tetromino.move_horizontal(-1)
				self.timers['horizontal'].activate()
			elif keys[pygame.K_RIGHT]:
				self.tetromino.move_horizontal(1)
				self.timers['horizontal'].activate()

			if not self.timers['rotation'].active:
				if keys[pygame.K_UP]:
					self.tetromino.rotate()
					self.timers['rotation'].activate()

			if not self.down_press and keys[pygame.K_DOWN]:
				self.down_press = True
				self.timers['vertical'].duration = self.hastened_down_speed
			if self.down_press and not keys[pygame.K_DOWN]:
				self.down_press = False
				self.timers['vertical'].duration = self.down_speed

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
	def __init__(self, shape, group, create_new, game_data):
		self.block_positions = TETROMINOS[shape]['shape']
		self.color = TETROMINOS[shape]['color']
		self.create_new = create_new
		self.game_data = game_data
		self.shape = shape

		self.blocks = [Block(group, pos,self.color) for pos in self.block_positions]

	def rotate(self):
		# square shape, doesnt need rotation
		if self.shape != 'O':
			# pivot point is the center (0,0) point block
			# we rotate 90 deg around pivot
			pivot = self.blocks[0].pos

			new_block_positions = [block.rotate(pivot) for block in self.blocks]

			# check for out of bounds
			for pos in new_block_positions:
				#horizontal
				if pos.x < 0 or pos.x >= COLUMNS:
					return

				#game field bound violation
				if self.game_data[int(pos.y)][int(pos.x)]:
					return

				#vertical
				if pos.y > ROWS:
					return

			# access to index
			for i, block in enumerate(self.blocks):
				block.pos = new_block_positions[i]

	def move_blocks_down(self):
		if not self.calculate_vertical_move_collission(self.blocks,1):
			for block in self.blocks:
				block.pos.y += 1
		else:
			for block in self.blocks:
				# or just 1
				self.game_data[int(block.pos.y)][int(block.pos.x)] = block

				mixer.init() 
				mixer.music.load(path.join("..","sound","land.ogg")) 
				mixer.music.set_volume(0.7) 
				mixer.music.play() 

			self.create_new()

	def calculate_vertical_move_collission(self, blocks, amount):
		collissions = [block.vertical_collide(int(block.pos.y + amount), self.game_data) for block in self.blocks]
		return True if any(collissions) else False

	def move_horizontal(self, val):
		if not self.calculate_horizontal_move_collission(self.blocks,val):
			for block in self.blocks:
				block.pos.x += val

	def calculate_horizontal_move_collission(self, blocks, amount):
		collissions = [block.horizontal_collide(int(block.pos.x + amount), self.game_data) for block in self.blocks]
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
#  0		 +------+------+------+------+------+------+------+------+------+------+
#		    | (0,0)| (0,1)| (0,2)| (0,3)| (0,4)| (0,5)| (0,6)| (0,7)| (0,8)| (0,9)|
#		    +------+------+------+------+------+------+------+------+------+------+
#  1		 | (1,0)| (1,1)| (1,2)| (1,3)| (1,4)| (1,5)| (1,6)| (1,7)| (1,8)| (1,9)|
#		    +------+------+------+------+------+------+------+------+------+------+
#  2		 | (2,0)| (2,1)| (2,2)| (2,3)| (2,4)| (2,5)| (2,6)| (2,7)| (2,8)| (2,9)|
#		    +------+------+------+------+------+------+------+------+------+------+
#  3		 | (3,0)| (3,1)| (3,2)| (3,3)| (3,4)| (3,5)| (3,6)| (3,7)| (3,8)| (3,9)|
#		    +------+------+------+------+------+------+------+------+------+------+
#  4		 | (4,0)| (4,1)| (4,2)| (4,3)| (4,4)| (4,5)| (4,6)| (4,7)| (4,8)| (4,9)|
#		    +------+------+------+------+------+------+------+------+------+------+
#  5		 | (5,0)| (5,1)| (5,2)| (5,3)| (5,4)| (5,5)| (5,6)| (5,7)| (5,8)| (5,9)|
#		    +------+------+------+------+------+------+------+------+------+------+
#  ...       | ...  | ...  | ...  | ...  | ...  | ...  | ...  | ...  | ...  | ...  |
# 19		 |(19,0)|(19,1)|(19,2)|(19,3)|(19,4)|(19,5)|(19,6)|(19,7)|(19,8)|(19,9)|
#		    +------+------+------+------+------+------+------+------+------+------+

		# POSITION IN MATRIX INDEX * CELL_SIZE
		# Convert pos to Vector2 for tetromino creation later
		self.pos = pygame.Vector2(pos) + BLOCK_OFFSET
		self.rect = self.image.get_rect(topleft = self.pos * CELL_SIZE)

	def update(self):
		self.rect.topleft = self.pos * CELL_SIZE

	def rotate(self, pivot):
		# get distance for rotation
		distance = self.pos - pivot
		rotated = distance.rotate(90)
		new_pos = pivot + rotated
		return new_pos

	def horizontal_collide(self, x, game_data):
		if not 0 <= x < COLUMNS:
			# if outside borders, return true
			return True

		# check collisions with others
		if game_data[int(self.pos.y)][x]:
			return True

	def vertical_collide(self, y, game_data):
		if y >= ROWS:
			# if outside borders, return true
			return True
		if y >= 0 and game_data[y][int(self.pos.x)]:
			return True























