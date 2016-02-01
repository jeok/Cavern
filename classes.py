# This module includes classes for building various game objects
import pyglet

class Rect():
	"""
	Class for storing rectangular information
	"""
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.coordinates = []
		self.topleft = (x, y + height)
		self.topright = (x + width, y + height)
		self.middle = (self.topright[0] / 2, self.topright[1] / 2)

		for n in range(self.y, height + 1):
			for m in range(self.x, width + 1):
				self.coordinates.append((x, y))

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
		self.anim_state = "idle"
		#print("Player succesfully created")

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
