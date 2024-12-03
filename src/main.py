from settings import *
from sys import exit

# Components
from game import Game
from score import Score
from preview import Preview

class Main:
	def __init__(self):
		pygame.init()
		self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		# set window name
		# create clock for time control
		self.clock = pygame.time.Clock()
		pygame.display.set_caption('Tetris')

		# Create primary game
		self.game = Game()
		# create score panel
		self.score = Score()
		# create preview panel
		self.preview = Preview()

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
			self.preview.run()
			pygame.display.update()
			self.clock.tick(60)

if __name__ == '__main__':
	main = Main()
	main.run()








