from geocomp.common.point import Point
from geocomp.common.segment import Segment

# determina um ponto evento, basicamente um wrapper c/ tipo e id do segmento pertencente "pendurados"
class PontoEvento:
    def __init__(self, ponto, tipo, id_segmento):
        self.ponto = ponto
        self.tipo = tipo
        self.id_segmento = id_segmento

    def __repr__(self): # imprime uma representacao legivel de ponto evento
        if (self.tipo == 'esquerdo'):
            return '(' + str(self.ponto) + ',' + str(self.id_segmento) + ', E)'
        elif (self.tipo == 'direito'):
            return '(' + str(self.ponto) + ',' + str(self.id_segmento) + ', D)'
        else:
            return '(' + str(self.ponto) + ',' + str(self.id_segmento) + ', UNKW)'

    def __cmp__(self, other): # compara dois pontos eventos
        if self.ponto.x < other.ponto.x: return -1
        elif self.ponto.x > other.ponto.x: return 1

        else: # self e other tem mesma X-coordenada
            if self.tipo == 'esquerdo' and other.tipo == 'direito':
                return -1

            elif other.tipo == 'esquerdo' and self.tipo == 'direito':
                return 1

            else: # os dois sao esquerdos ou os dois sao direitos                
                if self.ponto.y < other.ponto.y: return -1
                elif self.ponto.y > other.ponto.y: return 1
                else: return 0