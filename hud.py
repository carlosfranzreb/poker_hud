""" Shows the stats of the players. """

import os
import glob

from player import Player


players = list()

# Get last file of the folder, which can be found by name
file_list = glob.glob('./hands/elketefuka/*.txt')
file = max(file_list, key=os.path.getctime)  # latest file

# Get players and store them in a list, which will be updated when necessary
with open(file) as f:
    hands = f.read()

hands = hands.split('\n')
line_count = len(hands)  # important when updating, to skip old lines
reading_players = False  # True when first line with a player in it appears
for line in hands:
    if 'Seat' in line:  # player name is displayed in this line
        if not reading_players:  # skip first hit, which contains info about the table
            reading_players = True
        else:
            words = line.split(' ')  # username at index 2
            new_player = True
            for player in players:  # check if the player is new
                if player.username == words[2]:
                    new_player = False
                    break
            if new_player:
                players.append(Player(words[2]))
    elif reading_players:  # all lines with players have been read
        break

        
for player in players:
    print(player.username)
    

# Keep track of the number of hands per player

# Update the VPIP