class Laskin:
    def __init__(self, io):
        self._io = io

    def suorita(self):
        while True:
            try:
                luku1 = int(self._io.lue("Luku 1:"))
            except IndexError:
                return

            if luku1 == -9999:
                continue  # Siirry seuraavaan laskuun

            try:
                luku2 = int(self._io.lue("Luku 2:"))
            except IndexError:
                return

            if luku2 == -9999:
                continue  # Siirry seuraavaan laskuun

            vastaus = self._laske_summa(luku1, luku2)
            self._io.kirjoita(f"Summa: {vastaus}")

    def _laske_summa(self, luku1, luku2):
        return luku1 + luku2
