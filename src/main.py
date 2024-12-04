from settings import *
from sys import exit
from os import path
from random import choice

# Components
from game import Game
from score import Score
from preview import Preview

class Main:
	def __init__(self):
		pygame.init()
		self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		# Set window name
		# Create clock for time control
		self.clock = pygame.time.Clock()
		# App name
		pygame.display.set_caption('Tetris')

		# Set app icon
		programIcon = pygame.image.load(path.join('..', 'data', 'icon.png'))
		pygame.display.set_icon(programIcon)

		# Get 3 random shapes
		self.next_shapes = [choice(list(TETROMINOS.keys())) for shape in range(3)]
		
		# Create primary game
		self.game = Game(self.get_next_shape, self.update_score)
		# Create score panel
		self.score = Score()
		# Create preview panel
		self.preview = Preview()

	def update_score(self, lines, score, level):
		self.score.lines = lines
		self.score.score = score
		self.score.level = level

	def get_next_shape(self):
		# Get top element
		next = self.next_shapes.pop(0)
		self.next_shapes.append(choice(list(TETROMINOS.keys())))
		return next

	def run(self):
		while True:
			# Check events to avoid static window
			for event in pygame.event.get():
				# Exit application
				if event.type == pygame.QUIT:
					pygame.quit()
					# Import sys exit to avoid error on line 19 after pygame.quit()
					exit()

			self.display_surface.fill(BACKGROUND_COLOR)
			self.game.run()
			self.score.run()
			# Send next shapes to preview panel
			self.preview.run(self.next_shapes)
			pygame.display.update()
			self.clock.tick(60)

if __name__ == '__main__':
	main = Main()
	main.run()