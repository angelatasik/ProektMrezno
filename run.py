from player import Player
import sys

if len(sys.argv) != 2:
    print ("Vnesi vo sleden redosled: script_name.py, player name (ex. Player1)")
    exit()

player_name = str(sys.argv[1])

if __name__ == "__main__":
    p = Player(player_name)
    p.run()