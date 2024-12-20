import pygame

class Timer:
	def __init__(self, duration, repeat = False, func = None):
		self.repeat = repeat
		self.func = func
		self.duration = duration

		self.start_time = 0
		self.active = False

	def activate(self):
		self.active = True
		# Get elapsed time since start of game
		self.start_time = pygame.time.get_ticks()

	def deactivate(self):
		self.active = False
		self.start_time = 0

	def update(self):
		current_time = pygame.time.get_ticks()
		# If more than duration amount of ms passed since start time,
		# The timer has elapsed
		if current_time - self.start_time >= self.duration and self.active:
			if self.func and self.start_time != 0:
				self.func()
			# Reset
			self.deactivate()

			if self.repeat:
				self.activate()