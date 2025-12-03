class Summa:
	def __init__(self, sovellus, lue_syote):
		self._sovellus = sovellus
		self._lue_syote = lue_syote

	def suorita(self):
		try:
			arvo = int(self._lue_syote())
		except Exception:
			arvo = 0
		self._edellinen = self._sovellus.arvo()
		self._sovellus.plus(arvo)

class Erotus:
	def __init__(self, sovellus, lue_syote):
		self._sovellus = sovellus
		self._lue_syote = lue_syote

	def suorita(self):
		try:
			arvo = int(self._lue_syote())
		except Exception:
			arvo = 0
		self._edellinen = self._sovellus.arvo()
		self._sovellus.miinus(arvo)

class Nollaus:
	def __init__(self, sovellus, lue_syote):
		self._sovellus = sovellus
		self._lue_syote = lue_syote

	def suorita(self):
		self._edellinen = self._sovellus.arvo()
		self._sovellus.nollaa()

