# Cavern - a short exploration game by Valtteri Talvensaari (Haltija) and Janne Körkkö (jeok)
# Written in Python3 utilizes Pyglet heavily

import pyglet
from pyglet.window import key
import pytmx.util_pyglet
import game_utils
import classes


SCREEN_HEIGHT = 480
SCREEN_WIDTH = 640
TILE_SIZE = 16

# Initialize window
window = pyglet.window.Window(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

# Create KeyStateHandler for holding keyboard state and push it to window's event stack
keys = key.KeyStateHandler()
window.push_handlers(keys)


# Load resources below

# Load tileset
tileset = pyglet.resource.image("tileset1.png")
# Load tilemap
tiled_map = pytmx.util_pyglet.load_pyglet("testlevel1.tmx")
# Load image used for player sprite
player_image = pyglet.resource.image("player.png")

# Separate each tile from a map layer and create a sprite from it
# Each sprite is added to a list
batch_bg, sprites_bg = game_utils.create_batch_from_tileset(tiled_map, "Background")
batch_fg, sprites_fg = game_utils.create_batch_from_tileset(tiled_map, "Foreground")

# Init player
# Player object that has all sorts of fun attributes
player = classes.Player(TILE_SIZE * 2, SCREEN_HEIGHT - TILE_SIZE * 5)
# Player sprite
player_sprite = pyglet.sprite.Sprite(player_image, player.x, player.y)

fps_display = pyglet.clock.ClockDisplay()

#Define events

@window.event
def on_key_press(symbol, modifiers):
	movedir = "NONE"
	jump_pressed = False
	run_pressed = True

	if symbol == key.LEFT:
		movedir = "LEFT"
	elif symbol == key.RIGHT:
		movedir = "RIGHT"
	else:
		movedir = "NONE"

	if symbol == key.SPACE:
		jump_pressed = True

	if modifiers == key.LSHIFT:
		run_pressed = True


	player.move(movedir, jump_pressed, run_pressed)


def update(dt):
	# Things that need to be checked:
	# player movement
	# camera movement
	player.update()
	player_sprite.x = player.x

pyglet.clock.schedule_interval(update, 1/60.0)

@window.event
def on_draw():
	# What to do when drawing a window:
	window.clear()
	batch_bg.draw()
	batch_fg.draw()
	player_sprite.draw()
	fps_display.draw()

pyglet.app.run()

