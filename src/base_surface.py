from settings import *

class BaseSurface:
    def __init__(self, width, height, position_func):
        """
            width (int): The width of the surface.
            height (int): The height of the surface.
            position_func (function): A function that determines the surface's rectangle position.
        """
        # Create surface
        self.surface = pygame.Surface((width, height))
        self.display_surface = pygame.display.get_surface()

        # Set rect
        self.rect = position_func(self.surface.get_rect())

    def run(self):
        """Blit the surface onto the main display surface."""
        self.display_surface.blit(self.surface, self.rect)