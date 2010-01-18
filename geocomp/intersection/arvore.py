# -*- coding: utf-8 -*-
# Arvore de busca binaria rubro negra 2-3 recursiva

from geocomp.common.point import Point
from geocomp.common.segment import Segment
from geocomp.common import prim

class No:
    def __init__(self):
        self.dir = None
        self.esq = None
        self.rubro = False
        self.pai = None
        self.segmento = None
        
    #troca as cores do pai e do seus filhos
    def TroqueCores(self):
        if self.rubro == True:
            self.rubro = False
        else:
            self.rubro = True
        if self.esq.rubro == True:
            self.esq.rubro = False
        else:
            self.esq.rubro = True
        if self.dir.rubro == True:
            self.dir.rubro = False
        else:
            self.dir.rubro = True
      
    #faz uma rotacao a esquerda     
    def RotacioneEsq(self):
        q = self.dir
        self.dir = q.esq
        q.esq.pai = self
        q.esq = self
        q.pai = self.pai
        self.pai = q
        q.rubro = self.rubro
        self.rubro = True
        return q    
    
    #faz uma rotacao a direita
    def RotacioneDir(self):
        q = self.esq
        self.esq = q.dir
        q.dir.pai = self
        q.dir = self
        q.pai = self.pai
        self.pai = q
        q.rubro = self.rubro
        self.rubro = True
        return q
    
    #ajusta a arvore para manter as propriedades
    def FixUp(self):
        if self.dir != None and self.dir.rubro == True and self.esq != self.esq.rubro == False:
            self = No.RotacioneEsq(self)
        if self.esq != None and self.esq.rubro == True and self.dir != None and self.dir.rubro == True:
            No.TroqueCores(self)
        return self
    
    def RemoveNo(self, segmento):
        self = No.RemoveNoRec(self, segmento)
        self.rubro = False  #raiz eh sempre negra      
        return self
    
    def Minimo(self):
        p = self
        while p.esq.segmento != None:
            p = p.esq
        return p.segmento
    
    #busca o segmento a ser removida recursivamente na arvore e quando o encontra
    #remove fazendo os ajustes necessarios para manter as propriedades da arvore
    def RemoveNoRec(self, segmento):
        if segmento < self.segmento: #segmento a esquerda
            if self.esq.rubro == False and self.esq.esq.rubro == False:
                self = No.MovaRubroEsq(self)
            self.esq = No.RemoveNoRec(self.esq, segmento)
            self.esq.pai = self
        else: #segmento a direita
            if self.esq.rubro == True:
                self = No.RotacioneDir(self)
            if segmento.id == self.segmento.id and self.dir.segmento == None:
                p = No()
                p.esq = No()
                p.esq.pai = p
                p.dir = No()
                p.dir.pai = p
                return p
            if self.dir.rubro == False and self.dir.esq.rubro == False:
                self = No.MovaRubroDir(self)
            if segmento.id == self.segmento.id:
                self.segmento = No.Minimo(self.dir)
                self.dir = No.RemovaMin(self.dir)
                self.dir.pai = self
            else:
                self.dir = No.RemoveNoRec(self.dir, segmento)
                self.dir.pai = self
        self = No.FixUp(self)
        return self
               
    def RemovaMin(self):
        if self.esq.segmento == None:
            return self.esq
        if self.esq.rubro == False and self.esq.esq.rubro == False:
            self = No.MovaRubroEsq(self)
        self.esq = No.RemovaMin(self.esq)
        self.esq.pai = self
        self = No.FixUp(self)
        return self
        
    def MovaRubroEsq(self):
        No.TroqueCores(self)
        if self.dir.esq.rubro == True:
            self.dir = No.RotacioneDir(self.dir)
            self.dir.pai = self
            self = No.RotacioneEsq(self)
            No.TroqueCores(self)
        return self
    
    def MovaRubroDir(self):
        No.TroqueCores(self)
        if self.esq.esq.rubro == True:
            self = No.RotacioneDir(self)
            No.TroqueCores(self)
            self.dir = No.RotacioneEsq(self.dir)
            self.dir.pai = self
        return self 
                              
    def InsereNo(self, segmento):
        self = No.InsereNoRec(self, segmento)
        self.rubro = False #raiz eh sempre nregra
        self.pai = None #pai da raiz eh sempre NIL
        return self
    
    #insere um novo segmento na posicao correta e faz os ajustes necessarios
    #para manter as propriedades da arvore
    def InsereNoRec(self, segmento):
        if self.segmento == None:
            self.rubro = True
            self.dir = No()
            self.dir.pai = self
            self.esq = No()
            self.esq.pai = self
            self.pai = None
            self.segmento = segmento
            return self
        else:
            if segmento < self.segmento: #segmento a esquerda
                self.esq = No.InsereNoRec(self.esq, segmento)
                self.esq.pai = self
            else: #segmento a direita
                self.dir = No.InsereNoRec(self.dir, segmento)
                self.dir.pai = self                
            if self.dir.rubro == True and self.esq.rubro == False:
                self = No.RotacioneEsq(self)
            if self.esq.rubro == True and self.esq.esq.rubro == True:
                self = No.RotacioneDir(self)
            if self.esq.rubro == True and self.dir.rubro == True:
                No.TroqueCores(self)
            return self        
        
    def imprime_inordem(self):
        self.imprime_inordem_rec(self)
        print ''

    def imprime_inordem_rec(self, no):
        if no.esq.segmento != None: self.imprime_inordem_rec(no.esq)
        if no.segmento != None: print str(no.segmento.id) + ' < ',
        if no.dir.segmento != None: self.imprime_inordem_rec(no.dir)
                
    def buscarNo(self, segmento):
        if self.segmento == None: return self
        else:
            x = self
            while x.segmento != None and x.segmento.id != segmento.id:
                if segmento < x.segmento:
                    x = x.esq
                else:
                    x = x.dir
            return x
        
    def noSucessor(self, segmento):
      no = No.buscarNo(self, segmento)

      if no.segmento == None or no.dir.segmento == None:
          y = no.pai
          x = no
          while(y != None and y.dir == x):
              x = y
              y = y.pai
          return y
      else:
          return No.menorElemento(self, no.dir)

    def sucessor(self, segmento):
        no = No.noSucessor(self, segmento)
        if no == None: return None
        else: return no.segmento

    def noPredecessor(self, segmento):
        no = No.buscarNo(self, segmento)

        if no.segmento == None or no.esq.segmento == None:
            y = no.pai
            x = no
            while(y != None and y.esq == x):
                x = y
                y = y.pai
            return y
        else:
            return No.maiorElemento(self, no.esq)

    def predecessor(self, segmento):
        no = No.noPredecessor(self, segmento)
        if no == None: return None
        else: return no.segmento
        
    def menorElemento(self, subArvoreEnraizadaEm):
        y = subArvoreEnraizadaEm        
        if y.segmento == None: return y

        while y.esq.segmento != None:
            y = y.esq

        return y

    def maiorElemento(self, subArvoreEnraizadaEm):
        y = subArvoreEnraizadaEm
        if y.segmento == None: return y

        while y.dir.segmento != None:
            y = y.dir

        return y
        
                
class Arvore:
    def __init__(self):
        novoNo = No()
        self.raiz = novoNo
        
    def insere(self, segmento):
        self.raiz = No.InsereNo(self.raiz, segmento)    

    def remove(self, segmento):
        self.raiz = No.RemoveNo(self.raiz, segmento)

    def imprime_inordem(self):
        No.imprime_inordem(self.raiz)
                
    def predecessor(self, segmento):
        s = No.predecessor(self.raiz, segmento)
        return s

    def sucessor(self, segmento):
        s = No.sucessor(self.raiz, segmento)
        return s
