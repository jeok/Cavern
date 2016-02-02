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
		self.topleft = (self.x, self.y + self.height)
		self.topright = (self.x + self.width, self.y + self.height)
		self.middle = (self.topright[0] / 2, self.topright[1] / 2)
		self.right = self.x + self.width

	def updateposition(self, new_x, new_y):
		self.x = new_x
		self.y = new_y
		self.topleft = (self.x, self.y + self.height)
		self.topright = (self.x + self.width, self.y + self.height)
		self.middle = (self.topright[0] / 2, self.topright[1] / 2)
		self.right = self.x + self.width

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
		# Create a rectangle for collision detection
		self.collision_box = Rect(self.x, self.y, self.size_x, self.size_y)


	def move(self, movement_direction, jump_pressed, run_pressed):
		if movement_direction == "NONE":
			self.speed_x = 0
		if movement_direction == "LEFT":
			self.speed_x = -1
		elif movement_direction == "RIGHT":
			self.speed_x = 1
		if jump_pressed:
			self_speed_y = 30
			print(jump_pressed)

	def update(self, collisionmap, GRAVITY):
		"""
		Update method which checks if player can move.
		Collision detection works as such:
		See if player's future position is legal according to tilemap's foreground layer (layer 1)
		"""

		#print(self.speed_y)
		if self.speed_y > -5:
			self.speed_y += GRAVITY

		# If player's going left, boundaries need to aknowledge player's size_x
		if self.speed_x > 0:
			test_x = self.collision_box.right + self.speed_x
			if collisionmap.get_tile_gid(test_x / collisionmap.tilewidth,
					(collisionmap.height * collisionmap.tileheight - self.collision_box.y) / collisionmap.tileheight , 1) == 0:
				self.x += self.speed_x
		elif self.speed_x < 0:
			test_x = self.collision_box.x + self.speed_x
			if collisionmap.get_tile_gid(test_x / collisionmap.tilewidth,
					(collisionmap.height * collisionmap.tileheight - self.collision_box.y) / collisionmap.tileheight, 1) == 0:
				self.x += self.speed_x

		if self.speed_y < 0:
			test_y = self.collision_box.y + self.speed_y
			if collisionmap.get_tile_gid(self.x / collisionmap.tilewidth,
					(collisionmap.height * collisionmap.tileheight - test_y) / collisionmap.tileheight, 1) == 0:
				self.y += self.speed_y
			elif (collisionmap.get_tile_gid(self.x / collisionmap.tilewidth,
					(collisionmap.height * collisionmap.tileheight - test_y) / collisionmap.tileheight, 1) == 1) and (collisionmap.get_tile_gid(self.x / collisionmap.tilewidth, (collisionmap.height * collisionmap.tileheight - self.y) / collisionmap.tileheight, 1) == 0):
				self.speed.y = self.y % collisionmap.tileheight
				self.y += self.speed_y

#		if self.speed_y > 0:
#			self.x += self.speed_y
#			test_y = self.collision_box.y + self.collision_box.height + self.speed_y
#			if collisionmap.get_tile_gid(self.x / collisionmap.tilewidth,
#					(collisionmap.height * collisionmap.tileheight - test_y) / collisionmap.tileheight, 1) == 0:
#				self.y += self.speed_y
#			elif (collisionmap.get_tile_gid(self.x / collisionmap.tilewidth,
#					(collisionmap.height * collisionmap.tileheight - test_y) / collisionmap.tileheight, 1) == 1) and (collisionmap.get_tile_gid(self.x / collisionmap.tilewidth, (collisionmap.height * collisionmap.tileheight - self.y) / collisionmap.tileheight, 1) == 0):
#				self.speed.y = collisionmap.tileheight - ((self.collision_box.y + self.collision_box.height) % collisionmap.tileheight)
#				self.y += self.speed_y

		self.collision_box.updateposition(self.x, self.y)

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

