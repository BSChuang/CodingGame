import hlt
import logging

game = hlt.Game("Settler")

logging.info("Starting my Settler bot!")

while True:
    game_map = game.update_map()
    
    command_queue = []

    for ship in game_map.get_me().all_ships():
        if planet.is_owned():
            continue