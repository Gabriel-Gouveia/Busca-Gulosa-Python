

class Gulosa:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False

    def buscar(self, atual):
        print('------')
        print('Atual: {}'.format(atual.rotulo))
        atual.visitado = True

        if atual == self.objetivo:
            self.encontrado = True            
        else:
            # Lista ordenada de acordo com a distância até Bucareste
            arrayOrdenado = sorted(atual.adjacentes, 
            key=lambda x: x.vertice.distancia_objetivo)

            # Lista com os adjacentes do vértice atual, contanto que os 
            # vértices não tenham sido visitados.
            arrayFiltrado = []
            
            for adjacente in arrayOrdenado:
                if adjacente.vertice.visitado == False:
                    arrayFiltrado.append(adjacente)

            print(arrayFiltrado)

            if arrayFiltrado[0] != None:
                self.buscar(arrayFiltrado[0].vertice)
