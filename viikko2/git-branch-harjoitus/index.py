# tehdän alussa importit

from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan ohjelma") #lisätty mainissa

x = int(input("luku 1: "))
y = int(input("luku 2: "))
print(f"{summa(x, y)}")
print(f"{erotus(x, y)}")

logger("lopetetaan")
