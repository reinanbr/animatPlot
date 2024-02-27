import random
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd


def dado():
  valor = random.randint(1,6)
  return str(valor)


def playing(N):
  lances = []

  for l in range(int(N)):
    valor_dado = dado()
    lances.append(valor_dado)

  lista_contada = Counter(lances)



  # pegar porcentagem/frequência
  frequencia = {}
  freq_total = 0
  for face in lista_contada.keys():
    valor = lista_contada[face]
    freq = valor/N
    frequencia[face] = freq


  #fazendo a plotagem
  columns = list(frequencia.keys())
  lines = list(frequencia.values())
  df = pd.DataFrame({"faces":columns,"frequência":lines})

  fig = df.plot(kind='bar',x="faces",legend=False)
  return fig

