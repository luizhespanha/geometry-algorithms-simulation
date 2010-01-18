# -*- coding: utf-8 -*-
from geocomp.common.point import Point
from geocomp.common.segment import Segment
from geocomp.common import prim
from geocomp.common import control
from geocomp import config
from skiplist import *
from arvore import *
from arvore_sem_balanceamento import *
from ponto_evento import PontoEvento

cores = {  "passado": config.COLOR_ALT4,
           "presente": config.COLOR_ALT5,
           "intersectado": config.COLOR_ALT6,
           "vizinho": config.COLOR_HI_SEGMENT # vizinho significa 'predecessor' ou 'sucessor'
        }

x_linha_varredura = float('-inf') # variavel global, usada em prim.compara_segmentos(x,s1,s2)

def destaca_segs(lista_segs, string_cor): # pinta segmentos com cores do passado, presente, vizinho ou intersectado
    global cores
    control.freeze_update ()

    for seg in lista_segs:
        if seg != None:
            seg.hilight2(cores[string_cor])

    control.thaw_update ()

def shamos_hoey(segmentos, estrutura):
    global cores

    if len(segmentos) == 0: return None

    # Abaixo, redefinimos as funcoes de comparacao de segmentos para nosso proposito
    Segment.__lt__ = lambda s1, s2: prim.compara_segmentos(x_linha_varredura, s1, s2) == -1
    Segment.__ge__ = lambda s1, s2: prim.compara_segmentos(x_linha_varredura, s1, s2) >= 0

    E = [] # inicializa fila de eventos

    for i, segmento in enumerate(segmentos):
        # se e_x > d_x, entao inverte os pontos que determinam o segmento 
        # (pontos da esquerda nao podem ter x-coordenada maior que pontos da direita)
        if (segmento.init.x > segmento.to.x): 
            segmento.reverse()

        # tambem inverte se for segmento vertical com inicio (init) com menor y-coordenada do que fim (to)
        elif (segmento.init.x == segmento.to.x and segmento.init.y < segmento.to.y):
            segmento.reverse()

        segmento.id = i
        segmento.intersected = False
        # coloca na fila de eventos E
        E.append(PontoEvento(segmento.init, 'esquerdo', i))
        E.append(PontoEvento(segmento.to, 'direito', i))

    E.sort() # ordena pontos eventos por x-coordenada

    global x_linha_varredura

    pred,suc = None, None

    for ponto_evento in E:
        x_linha_varredura = ponto_evento.ponto.x

        #Remove o destaque da iteracao passada
        destaca_segs( [pred, suc], 'presente')

        seg = segmentos[ponto_evento.id_segmento]
        pred = estrutura.predecessor(seg)
        suc = estrutura.sucessor(seg)

        #Destaca os segmentos que serao analisados
        destaca_segs( [pred, suc], 'vizinho')

        if ponto_evento.tipo == 'esquerdo':
            destaca_segs([seg], 'presente')
            estrutura.insere(seg)
            if pred != None:
                if prim.inter(seg,pred) == True: # Detectou interseccao do seg com o pred
                    destaca_segs([seg,pred], 'intersectado')
                    seg.intersected, pred.intersected = True, True
                    break

            if suc != None:
                if prim.inter(seg,suc) == True: # Detectou interseccao do seg com o suc
                    destaca_segs([seg,suc], 'intersectado')
                    seg.intersected, suc.intersected = True, True
                    break

        elif ponto_evento.tipo == 'direito':
            destaca_segs([seg], 'passado')
            estrutura.remove(seg)
            if (pred != None and suc != None):
                if prim.inter(pred,suc) == True: # Detectou interseccao do pred com o suc
                    destaca_segs([pred,suc], 'intersectado')
                    pred.intersected, suc.intersected = True, True
                    break

        linha_varredura_plotada_id = control.gui.plot_vert_line (x_linha_varredura, config.COLOR_LINE_SPECIAL, 1) # plota a linha de varredura
        control.sleep() # dorme
        control.gui.plot_delete(linha_varredura_plotada_id) # desplota a linha de varredura

    if estrutura.__class__.__name__ == 'Skiplist':
        ret = Segment() # pequeno hack, porque resolvemos um problema de decisão, e não temos nada (nenhum polígono, por exemplo) para retornar
                        # e para o algoritmo de Skip List queremos devolver essa informacao extra abaixo
        ret.extra_info = 'SL: p = ' + str(estrutura.p) + ' nivelmax = '  + str(estrutura.maxnivel) + ' (media de niveis = ' + str( (estrutura.somaniveis / (2*len(segmentos)))) + ')'
        return ret

def shamos_hoeyABBB(segmentos):
    estrutura = Arvore()
    return shamos_hoey(segmentos, estrutura)

def shamos_hoeyABB(segmentos):
    estrutura = ArvoreNaoBalanceada()
    return shamos_hoey(segmentos, estrutura)

def shamos_hoeySL(segmentos):
    estrutura = Skiplist()
    return shamos_hoey(segmentos, estrutura)
