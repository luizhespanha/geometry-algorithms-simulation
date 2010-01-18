from geocomp.common.segment import Segment
from geocomp.common import prim
from geocomp.common import control
from geocomp import config

#Algoritmo forca-bruta para encontrar a interseccao de segmentos
#Complexidade: O(n2)
def Brute_Force(segmentos):
    
    cores = (config.COLOR_ALT1, config.COLOR_ALT7, config.COLOR_ALT6)
    
    for segmento in segmentos:
        segmento.intersected = False
    
    for i in range (len(segmentos)):
        control.freeze_update ()
        hii = segmentos[i].hilight2 (cores[1])
        control.thaw_update ()
        control.sleep()
        for j in range (i + 1, len (segmentos)):
            control.freeze_update ()
            hij = segmentos[j].hilight2(cores[0])
            control.thaw_update ()
            control.sleep()
            if prim.inter(segmentos[i],segmentos[j]):
                control.freeze_update ()
                segmentos[i].hilight2 (cores[2])
                segmentos[j].hilight2 (cores[2])
                segmentos[i].intersected = True
                segmentos[j].intersected = True
                control.thaw_update ()
            segmentos[j].unhilight (hij)
        segmentos[i].unhilight (hii)