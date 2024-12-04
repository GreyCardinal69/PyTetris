from settings import *
from sys import exit

# Components
from game import Game
from score import Score
from preview import Preview
from random import choice

class Main:
	def __init__(self):
		pygame.init()
		self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		# set window name
		# create clock for time control
		self.clock = pygame.time.Clock()
		pygame.display.set_caption('Tetris')

		# get 3 random shapes
		self.next_shapes = [choice(list(TETROMINOS.keys())) for shape in range(3)]
		print(self.next_shapes)
		# Create primary game
		self.game = Game(self.get_next_shape, self.update_score)
		# create score panel
		self.score = Score()
		# create preview panel
		self.preview = Preview()

	def update_score(self, lines, score, level):
		self.score.lines = lines
		self.score.score = score
		self.score.level = level

	def get_next_shape(self):
		# get top element
		next = self.next_shapes.pop(0)
		self.next_shapes.append(choice(list(TETROMINOS.keys())))
		return next

	def run(self):
		while True:
			# check events to avoid static window
			for event in pygame.event.get():
				# exit application
				if event.type == pygame.QUIT:
					pygame.quit()
					# import sys exit to avoid error on line 19 after pygame.quit()
					exit()

			self.display_surface.fill(GRAY)
			self.game.run()
			self.score.run()
			self.preview.run(self.next_shapes)
			pygame.display.update()
			self.clock.tick(60)

if __name__ == '__main__':
	main = Main()
	main.run()








