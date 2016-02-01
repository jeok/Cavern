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
player_sprite = pyglet.sprite.Sprite(player_image, player.x - player.size_x / 2 , player.y)

fps_display = pyglet.clock.ClockDisplay()

#Define events


#ITS FROM HELL


def update(dt):
	# Things that need to be checked:
	# player movement
	# camera movement
	keyboard_input = game_utils.check_keys(keys)
	player.move(keyboard_input[0], keyboard_input[1], keyboard_input[2])
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

