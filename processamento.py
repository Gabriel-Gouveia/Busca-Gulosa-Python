from grafo import Grafo
from gulosa import Gulosa

meuGrafo = Grafo()

busca_gulosa = Gulosa(meuGrafo.bucharest)
busca_gulosa.buscar(meuGrafo.arad)

print(busca_gulosa.encontrado)