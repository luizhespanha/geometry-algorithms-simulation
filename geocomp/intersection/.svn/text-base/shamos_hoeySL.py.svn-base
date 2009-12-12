# -*- coding: utf-8 -*-
from geocomp.common.point import Point
from geocomp.common.polygon import Polygon
from geocomp.common.segment import Segment
from geocomp.common import prim
from geocomp.common import control
from geocomp import config
from geocomp.common.guiprim import *
from skiplist import *

x_linha_varredura = float('-inf') # variavel global. talvez mudemos depois

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

# Compara, na abcissa x, se o segmento1 "e' menor" do que o segmento2 (ordem total da ABBB)
def compara_segmentos(x, segmento1, segmento2):
    e1x,e1y = segmento1.init.x , segmento1.init.y
    d1x,d1y = segmento1.to.x , segmento1.to.y

    y1 = - (e1x * d1y + e1y * x) + d1y * x + e1y * d1x
    y1 = y1 / (d1x - e1x)

    e2x,e2y = segmento2.init.x , segmento2.init.y
    d2x,d2y = segmento2.to.x , segmento2.to.y

    y2 = - (e2x * d2y + e2y * x) + d2y * x + e2y * d2x
    y2 = y2 / (d2x - e2x)

    # lembre que a ordem da linha de varredura e' de cima para baixo. 
    # a principio, abaixo parece que o 1 esta' invertido com o -1, mas e' assim mesmo
    if (y1 < y2): return 1
    elif(y1 > y2): return -1
    else: return 0

def Shamos_HoeySL(segmentos):
    
    cores = (config.COLOR_ALT6,)
    
    for segmento in segmentos:
        segmento.intersected = False

    if len(segmentos) == 0: return None
    print 'Recebido ' + str(len(segmentos)) + ' segmentos'
    print 'Lista de segmentos: ' + str(segmentos)

    # Abaixo, redefinimos as funcoes de comparacao de segmentos para nosso proposito
    Segment.__lt__ = lambda s1, s2: compara_segmentos(x_linha_varredura, s1, s2) == -1
    Segment.__ge__ = lambda s1, s2: compara_segmentos(x_linha_varredura, s1, s2) >= 0

    E = [] # inicializa fila de eventos

    for i, segmento in enumerate(segmentos):
        # se e_x > d_x, entao inverte os pontos que determinam o segmento 
        # (pontos da esquerda nao podem ter x-coordenada maior que pontos da direita)
        if (segmento.init.x > segmento.to.x): 
            segmento.reverse()

        segmento.id = i
        # coloca na fila de eventos E
        E.append(PontoEvento(segmento.init, 'esquerdo', i))
        E.append(PontoEvento(segmento.to, 'direito', i))
        
    E.sort()
    print 'Fila de eventos E: ' + str(E)

    sl = Skiplist()
    global x_linha_varredura

    pred = None
    suc = None

    for ponto_evento in E:
        x_linha_varredura = ponto_evento.ponto.x

        seg = segmentos[ponto_evento.id_segmento]

#        print 'Processando seg ' + str(seg), 

        #Remove o destaque da iteracao passada
        control.freeze_update ()
        if pred != None:
            pred.unhilight (hia)
        if suc != None:
            suc.unhilight (hib)
        control.thaw_update ()

        pred = sl.predecessor(seg)
        suc = sl.sucessor(seg)

#        print ' , tem pred = ' + str(pred) + ' e suc ' + str(suc)
      
        #Destaca os segmentos que serao analisados
        control.freeze_update ()
        if pred != None:
            hia = pred.hilight2 ()
        if suc != None:
            hib = suc.hilight2 ()
        control.thaw_update ()

        if ponto_evento.tipo == 'esquerdo':
            sl.insere(seg)
            if pred != None and prim.inter(seg,pred):
                print 'Detectei intersecao do ' + str(seg.id) + ' com ' + str(pred.id)
                control.freeze_update ()
                seg.hilight2 (cores[0])
                pred.hilight2 (cores[0])
                seg.intersected = True
                pred.intersected = True
                control.thaw_update ()

            if suc != None and prim.inter(seg,suc):
                print 'Detectei intersecao do ' + str(seg.id) + ' com ' + str(suc.id)
                control.freeze_update ()
                seg.hilight2 (cores[0])
                suc.hilight2 (cores[0])
                seg.intersected = True
                suc.intersected = True
                control.thaw_update ()

        elif ponto_evento.tipo == 'direito':
            sl.remove(seg)
            if (pred != None and suc != None and prim.inter(pred,suc)):
                print 'Detectei intersecao do ' + str(pred.id) + ' com o ' + str(suc.id)
                control.freeze_update ()
                pred.hilight2 (cores[0])
                suc.hilight2 (cores[0])
                pred.intersected = True
                suc.intersected = True
                control.thaw_update ()

#        print
#        sl.imprime_inordem()
#        print

        linha_varredura_plotada_id = control.gui.plot_vert_line (x_linha_varredura, config.COLOR_LINE_SPECIAL, 1)
        control.sleep()
        control.gui.plot_delete(linha_varredura_plotada_id)

    #Remove o destaque da ultima iteracao
    control.freeze_update ()
    if pred != None:
        pred.unhilight (hia)
    if suc != None:
        suc.unhilight (hib)
    control.thaw_update ()
        
