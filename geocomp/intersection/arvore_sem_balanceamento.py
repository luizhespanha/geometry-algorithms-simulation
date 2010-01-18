# -*- coding: utf-8 -*-
# Arvore de busca binaria nao balenceada iterativa

from geocomp.common.point import Point
from geocomp.common.segment import Segment
from geocomp.common import prim

class No:
    def __init__(self):
        self.dir = None
        self.esq = None
        self.pai = None
        self.segmento = None
                   
    def RemoveNo(self, segmento):
        p = None #no que sera removido
        f = None 
        q = No.buscarNo(self, segmento)
        if q.esq.segmento == None or q.dir.segmento == None: #no a ser removido nao tem folhos
            p = q
        else: #ajusta os filhos do no a ser removido na arvore
            p = No.Minimo(q.dir)
            q.segmento = p.segmento
        if p.esq.segmento == None:
            f = p.dir
        else:
            f = p.esq
        if f != None:
            f.pai = p.pai
        if p.pai == None:
            self = f
            self.pai = None
        else:
            if p == p.pai.esq:
                p.pai.esq = f
            else:
                p.pai.dir = f
        p = None
        return self
            
    
    def Minimo(self):
        p = self
        while p.esq.segmento != None:
            p = p.esq
        return p
    
           
    def RemovaMin(self):
        if self.esq.segmento == None:
            return self.esq
        self.esq = No.RemovaMin(self.esq)
        self.esq.pai = self
        return self
                              
    def InsereNo(self, segmento):
        q = No() #no que sera inserido
        q.segmento = segmento
        q.dir = No()
        q.dir.pai = q
        q.esq = No()
        q.esq.pai = q
        p = self
        ant = None
        while p.segmento != None: #busca a posicao do novo no na arvore
            ant = p
            if segmento < p.segmento:
                p = p.esq
            else:
                p = p.dir
        if ant == None: #se nao tem anterior entao eh a raiz
            self = q
        else:
            if segmento < ant.segmento:
                ant.esq = q
            else:
                ant.dir = q
            q.pai = ant
        self.pai = None
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
        
                
class ArvoreNaoBalanceada:
    def __init__(self):
        novoNo = No()
        self.raiz = novoNo
        
    def insere(self, segmento):
        self.raiz = No.InsereNo(self.raiz, segmento)    

    def remove(self, segmento):
        self.raiz = No.RemoveNo(self.raiz, segmento)

    def imprime_inordem(self):
        # Adicionado para nao dar pau tentando imprimir arvore vazia
        if self.raiz.segmento != None: No.imprime_inordem(self.raiz)
                
    def sucessor(self, segmento):
        s = No.sucessor(self.raiz, segmento)
        return s

    def predecessor(self, segmento):
        s = No.predecessor(self.raiz, segmento)
        return s

