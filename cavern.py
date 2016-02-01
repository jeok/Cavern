# Cavern - a short exploration game by Valtteri Talvensaari (Haltija) and Janne Körkkö (jeok)
# Written in Python3 utilizes Pyglet heavily

import pyglet
import pytmx.util_pyglet
import gameobj

SCREEN_HEIGHT = 480
SCREEN_WIDTH = 640
TILE_SIZE = 16

# Initialize window
window = pyglet.window.Window(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

# Load resources below

# Load tileset
tileset = pyglet.resource.image("tileset1.png")
# Load tilemap
tiled_map = pytmx.util_pyglet.load_pyglet("testlevel1.tmx")
# Load image used for player sprite
player_image = pyglet.resource.image("player.png")

# Empty batches for sprites separated by their layers
batch_bg = pyglet.graphics.Batch()
batch_fg = pyglet.graphics.Batch()
batch_obj = pyglet.graphics.Batch()

# Empty lists for saving sprites
bg_images = []
fg_images = []
obj_images = []

# Separate each tile from a map layer and create a sprite from it
# Each sprite is added to a list
for tile in tiled_map.get_layer_by_name("Background").tiles():
	bg_images.append(pyglet.sprite.Sprite(tile[2], tile[0] * TILE_SIZE, SCREEN_HEIGHT - tile[1] * TILE_SIZE - TILE_SIZE, batch=batch_bg))

for tile in tiled_map.get_layer_by_name("Foreground").tiles():
	fg_images.append(pyglet.sprite.Sprite(tile[2], tile[0] * TILE_SIZE, SCREEN_HEIGHT - tile[1] * TILE_SIZE - TILE_SIZE, batch=batch_fg))

# Init player
# Player object that has all sorts of fun attributes
player = gameobj.Player(TILE_SIZE * 2, SCREEN_HEIGHT - TILE_SIZE * 5)
# Player sprite
player_sprite = pyglet.sprite.Sprite(player_image, player.x, player.y)

fps_display = pyglet.clock.ClockDisplay()

def update(dt):
	# Things that need to be checked:
	# player movement
	# camera movement
	pass

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

