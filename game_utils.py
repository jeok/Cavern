# Useful functions in a separate module to improve readibility
import pyglet
import pytmx.util_pyglet
from pyglet.window import key

# Not pretty to include these here also but it's messy to pass around such constants
SCREEN_HEIGHT = 480
SCREEN_WIDTH = 640
TILE_SIZE = 16


def create_batch_from_tileset(tiled_map, layer_name):
	""" Function for creating a Sprite batch (pyglet.graphics.Batch) from tileset's
	certain layer. Returns the batch and a list containing the sprites."""
	sprite_list = []
	sprite_batch = pyglet.graphics.Batch()
	for tile in tiled_map.get_layer_by_name(layer_name).tiles():
		sprite_list.append(pyglet.sprite.Sprite(tile[2],
												tile[0] * TILE_SIZE,
												SCREEN_HEIGHT - tile[1] * TILE_SIZE - TILE_SIZE,
												batch=sprite_batch))
	return sprite_batch, sprite_list

def check_keys(keys):
	movedir = "NONE"
	jump_pressed = False
	run_pressed = False

	if keys[key.LEFT]:
		movedir = "LEFT"
	elif keys[key.RIGHT]:
		movedir = "RIGHT"
	else:
		movedir = "NONE"

	if keys[key.SPACE]:
		jump_pressed = True

	if keys[key.LSHIFT]:
		run_pressed = True

	return (movedir, jump_pressed, run_pressed)
