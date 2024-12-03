from settings import *

# main tetris display
class Game:
	def __init__(self):
		self.surface = pygame.Surface((GAME_WIDTH,GAME_HEIGHT))
		# fetch main window aka main.py
		self.display_surface = pygame.display.get_surface()

	def run(self):
		# put this surface on main
		self.display_surface.blit(self.surface, (PADDING,PADDING))





























