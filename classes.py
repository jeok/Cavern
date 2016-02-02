# This module includes classes for building various game objects
import pyglet
import pytmx.util_pyglet

class Rect():
	"""
	Class for storing rectangular information
	"""
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.topleft = (x, y + height)
		self.topright = (x + width, y + height)
		self.middle = (self.topright[0] / 2, self.topright[1] / 2)
		self.right = self.x + width

	def move(self, x_delta, y_delta):
		self.x = self.x + x_delta
		self.y = self.y + y_delta
		self.topleft = (self.topleft[0] + x_delta, self.topleft[1] + y_delta)
		self.topright = (self.topright[0] + x_delta, self.topright[0] + y_delta)
		self.middle = (self.middle[0] + x_delta, self.middle[1] + y_delta)
		self.right = self.right + x_delta

class Player():
	""" Class for player
	x = position on x plane
	y = -,,- 		y plane
	Different animation states:
	idle
	walk
	run
	jump
	push
	"""
	def __init__ (self, x, y):
		self.speed_x = 0
		self.speed_y = 0
		self.x = x
		self.y = y
		self.size_x = 16
		self.size_y = 16

		self.anim_state = "idle"
		# Create a rectangular for collision detection
		collision_box = Rect(self.x, self.y, self.size_x, self.size_y)


	def move(self, movement_direction, run_pressed, jump_pressed):
		if movement_direction == "NONE":
			self.speed_x = 0
			self.speed_y = 0
		if movement_direction == "LEFT":
			self.speed_x = -1
		elif movement_direction == "RIGHT":
			self.speed_x = 1

	def update(self, collisionmap):
		"""
		Update method which checks if player can move.
		Collision detection works as such:
		See if player's future position is legal according to tilemap's foreground layer (layer 1)
		"""
		# If player's going left, boundaries need to aknowledge player's size_x
		future_x = self.x + self.speed_x
		compensation_x = 0
		if self.speed_x	> 0:
			compensation_x = self.size_x
		if collisionmap.get_tile_gid((future_x + compensation_x) / self.size_x, (480 - self.y) / self.size_y, 1) == 0:
			self.x = future_x


class Camera(object):
	""" Camera class, heavily inspired by:
	https://stackoverflow.com/questions/14354171/add-scrolling-to-a-platformer-in-pygame
	"""
	def __init__(self, camera_func, width, height):
		self.camera_func = camera_func
		self.state = Rect(0, 0, width, height)

	def apply(self, target):
		return target.rect.move(self.state.topleft)

	def update(self, target):
		self.state = self.camera_func(self.state, target.rect)

