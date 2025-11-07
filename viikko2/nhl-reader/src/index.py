from rich.console import Console
from rich.table import Table
import requests
from player import Player
# pylint test4
def fetch_players(season):
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    response = requests.get(url, timeout=10).json()
    return [Player(p) for p in response]

def render_table(players, nationality, season):
    table = Table(title=f"Players from {nationality} in season {season}")
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Team", style="magenta")
    table.add_column("Goals", justify="right")
    table.add_column("Assists", justify="right")
    table.add_column("Points", justify="right", style="bold green")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.points())
        )

    console = Console()
    console.print(table)

def main():
    season = input("Valitse kausi: ")
    nationality = input("Valitse kansallisuus: ")

    players = fetch_players(season)
    selected = [p for p in players if p.nationality == nationality]
    sorted_players = sorted(selected, key=lambda p: p.points(), reverse=True)

    render_table(sorted_players, nationality, season)

if __name__ == "__main__":
    main()
