class Summa:
	def __init__(self, sovellus, lue_syote):
		self._sovellus = sovellus
		self._lue_syote = lue_syote
		self._edellinen = None

	def suorita(self):
		try:
			arvo = int(self._lue_syote())
		except Exception:
			arvo = 0
		self._edellinen = self._sovellus.arvo()
		self._sovellus.plus(arvo)

	def kumoa(self):
		if self._edellinen is None:
			return
		self._sovellus.aseta_arvo(self._edellinen)

class Erotus:
	def __init__(self, sovellus, lue_syote):
		self._sovellus = sovellus
		self._lue_syote = lue_syote
		self._edellinen = None

	def suorita(self):
		try:
			arvo = int(self._lue_syote())
		except Exception:
			arvo = 0
		self._edellinen = self._sovellus.arvo()
		self._sovellus.miinus(arvo)

	def kumoa(self):
		if self._edellinen is None:
			return
		self._sovellus.aseta_arvo(self._edellinen)

class Nollaus:
	def __init__(self, sovellus, lue_syote):
		self._sovellus = sovellus
		self._lue_syote = lue_syote
		self._edellinen = None

	def suorita(self):
		self._edellinen = self._sovellus.arvo()
		self._sovellus.nollaa()

	def kumoa(self):
		if self._edellinen is None:
			return
		self._sovellus.aseta_arvo(self._edellinen)

