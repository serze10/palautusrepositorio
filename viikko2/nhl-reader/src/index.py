import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    players = [Player(player_dict) for player_dict in response]
    
    fin_players = [p for p in players if p.nationality == "FIN"]
    
    def by_points(player: Player):
        return player.points()
    
    sorted_players = sorted(fin_players, key=by_points, reverse=True)

    
    print("Players from FIN:\n")
    for player in sorted_players:
        print(player)
        
        
if __name__ == "__main__":
    main()
