from rich.console import Console
from rich.table import Table
import requests
from player import Player

def main():
    season = input("Valiste kausi (2018-19, 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26): ")
    nationality = input("Valitse kansallisuus (USA, FIN, CAN, SWE, CZE, RUS, SLO, FRA, GBR, SVK, DEN, NED,  AUT, BLR, GER, SUI, NOR, UZB, LAT, AUS): ")
    
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    response = requests.get(url).json()

    players = [Player(p) for p in response]

    
    def by_points(player: Player):
        return player.points()
    
    selected = [p for p in players if p.nationality == nationality]
    
    sorted_players = sorted(selected, key=by_points, reverse=True)
    
    table = Table(title=f"Players from {nationality} in season {season}")

    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Team", style="magenta")
    table.add_column("Goals", justify="right")
    table.add_column("Assists", justify="right")
    table.add_column("Points", justify="right", style="bold green")

    for player in sorted_players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.points())
        )

    console = Console()
    console.print(table)
        
if __name__ == "__main__":
    main()
