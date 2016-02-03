# Useful functions in a separate module to improve readibility
import pyglet
import pytmx.util_pyglet
from pyglet.window import key

# Not pretty to include these here also but it's messy to pass around such
# constants
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
                                                SCREEN_HEIGHT -
                                                tile[1] * TILE_SIZE -
                                                TILE_SIZE,
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

    if keys[key.UP]:
        jump_pressed = True
    else:
        jump_pressed = False

    if keys[key.LSHIFT]:
        run_pressed = True

    return (movedir, jump_pressed, run_pressed)

def check_collision(player_object, collisionmap, movedir):
    """ Function for checking player collision. Checks player's rectangle's
    different sides' coordinates depending on move direction."""
    test_x_left = player_object.collision_box.x + player_object.speed_x
    test_x_right = player_object.collision_box.right + player_object.speed_x
    test_y_top = player_object.collision_box.y + player_object.collision_box.height
    test_y_bottom = player_object.collision_box.y

    # Check if player is jumping
    if movedir == "UP":
        test_y_top += player_object.speed_y
        test_y_bottom += player_object.speed_y

    # Generate coordinates that are checked from collisionmap
    x_coord_left = test_x_left / collisionmap.tilewidth
    x_coord_right = test_x_right / collisionmap.tilewidth
    y_coord_top = (collisionmap.height * collisionmap.tileheight -
        test_y_top) / collisionmap.tileheight
    y_coord_bottom = (collisionmap.height * collisionmap.tileheight -
        test_y_bottom) / collisionmap.tileheight

    # Corner checks
    top_right = collisionmap.get_tile_gid(x_coord_right, y_coord_top, 1)
    top_left = collisionmap.get_tile_gid(x_coord_left, y_coord_top, 1)
    bottom_right = collisionmap.get_tile_gid(x_coord_right, y_coord_bottom, 1)
    bottom_left = collisionmap.get_tile_gid(x_coord_left, y_coord_bottom, 1)

    # If there's anything but 0 in GIDs' of those tiles, return True because collision happened
    if top_right == 0 and top_left == 0 and bottom_right == 0 and bottom_left == 0:
        return False
    else:
        return True




    
