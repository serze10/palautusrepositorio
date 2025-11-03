import unittest
from statistics_service import StatisticsService
from player import Player
from statistics_service import SortBy


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),   # 16
            Player("Lemieux", "PIT", 45, 54),  # 99
            Player("Kurri",   "EDM", 37, 53),  # 90
            Player("Yzerman", "DET", 42, 56),  # 98
            Player("Gretzky", "EDM", 35, 89)   # 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_loytyy(self):
        player = self.stats.search("Gretzky")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Gretzky")

    def test_search_ei_loydy(self):
        player = self.stats.search("Selänne")
        self.assertIsNone(player)

    def test_team_palauttaa_oikeat_pelaajat(self):
        edm_players = self.stats.team("EDM")
        self.assertEqual(len(edm_players), 3)
        self.assertTrue(all(player.team == "EDM" for player in edm_players))

    def test_team_palauttaa_tyhjan_listan(self):
        empty_team = self.stats.team("XYZ")
        self.assertEqual(empty_team, [])

    def test_top_palauttaa_oikean_maaran(self):
        top_players = self.stats.top(3)
        self.assertEqual(len(top_players), 3)

    def test_top_palauttaa_oikeat_pisteet_jarjestyksessa(self):
        top_players = self.stats.top(3)
        points = [player.points for player in top_players]
        self.assertEqual(points, sorted(points, reverse=True))

    def test_top_palauttaa_kaikki_jos_pyydetaan_liikaa(self):
        top_players = self.stats.top(10)
        self.assertEqual(len(top_players), 5)  # stubissa vain 5 pelaajaa

    def test_top_järjestää_pisteiden_perusteella(self):
        top_players = self.stats.top(2, SortBy.POINTS)
        self.assertEqual(top_players[0].name, "Gretzky")  # 124
        self.assertEqual(top_players[1].name, "Lemieux")  # 99

    def test_top_järjestää_maalien_perusteella(self):
        top_players = self.stats.top(2, SortBy.GOALS)
        self.assertEqual(top_players[0].name, "Lemieux")  # 45
        self.assertEqual(top_players[1].name, "Yzerman")  # 42

    def test_top_järjestää_syöttöjen_perusteella(self):
        top_players = self.stats.top(2, SortBy.ASSISTS)
        self.assertEqual(top_players[0].name, "Gretzky")  # 89
        self.assertEqual(top_players[1].name, "Yzerman")  # 56

    def test_top_toimii_ilman_sortby_parametria(self):
        top_players = self.stats.top(1)
        self.assertEqual(top_players[0].name, "Gretzky")  # oletus: POINTS
