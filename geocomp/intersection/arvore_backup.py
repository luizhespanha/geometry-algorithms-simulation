# -*- coding: utf-8 -*-
# Arvore de busca

#trocar pelas classes no common
class Ponto:
    self.x = None
    self.y = None
    
class Segmento:
    self.id = None
    self.e = None
    self.d = None

class No:
    def __init__(self):
        self.dir = None
        self.esq = None
        #self.valor = None
        self.rubro = False
        self.pai = None
        self.segmento = None
        
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
    
    def FixUp(self):
        if self.dir != None and self.dir.rubro == True and self.esq != self.esq.rubro == False:
            self = No.RotacioneEsq(self)
        if self.esq != None and self.esq.rubro == True and self.dir != None and self.dir.rubro == True:
            No.TroqueCores(self)
        return self
    
    def RemoveNo(self, valor):
        self = No.RemoveNoRec(self, valor)
        self.rubro = False        
        return self
    
#    def Minimo(self):
#        p = self
#        while p.esq.valor != None:
#            p = p.esq
#        return p.valor
    
    def RemoveNoRec(self, valor):
        if valor < self.valor:
            if self.esq.rubro == False and self.esq.esq.rubro == False:
                self = No.MovaRubroEsq(self)
            self.esq = No.RemoveNoRec(self.esq, valor)
            self.esq.pai = self
        else:
            if self.esq.rubro == True:
                self = No.RotacioneDir(self)
            if valor == self.valor and self.dir.valor == None:
                p = No()
                p.esq = No()
                p.esq.pai = p
                p.dir = No()
                p.dir.pai = p
                return p
            if self.dir.rubro == False and self.dir.esq.rubro == False:
                self = No.MovaRubroDir(self)
            if valor == self.valor:
                self.valor = No.Minimo(self.dir)
                self.dir = No.RemovaMin(self.dir)
                self.dir.pai = self
            else:
                self.dir = No.RemoveNoRec(self.dir, valor)
                self.dir.pai = self
        self = No.FixUp(self)
        return self
               
    def RemovaMin(self):
        if self.esq.valor == None:
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
                      
#    def InsereNo(self, valor):
#        self = No.InsereNoRec(self, valor)
#        self.rubro = False
#        self.pai = None
#        return self
#      
#    def InsereNoRec(self, valor):
#        if self.valor == None:
#            self.valor = valor
#            self.rubro = True
#            self.dir = No()
#            self.dir.pai = self
#            self.esq = No()
#            self.esq.pai = self
#            self.pai = None
#            return self
#        else:
#            if valor < self.valor:
#                self.esq = No.InsereNoRec(self.esq, valor)
#                self.esq.pai = self
#            else:
#                self.dir = No.InsereNoRec(self.dir, valor)
#                self.dir.pai = self                
#            if self.dir.rubro == True and self.esq.rubro == False:
#                self = No.RotacioneEsq(self)
#            if self.esq.rubro == True and self.esq.esq.rubro == True:
#                self = No.RotacioneDir(self)
#            if self.esq.rubro == True and self.dir.rubro == True:
#                No.TroqueCores(self)
#            return self
        
    def InsereNo(self, segmento):
        self = No.InsereNoRec(self, segmento)
        self.rubro = False
        self.pai = None
        return self
      
    def InsereNoRec(self, segmento):
        if self.segmento == None:
            #self.valor = valor
            self.rubro = True
            self.dir = No()
            self.dir.pai = self
            self.esq = No()
            self.esq.pai = self
            self.pai = None
            self.segmento = segmento
            return self
        else:
            if segmento.e.y > self.segmento.e.y:
                self.esq = No.InsereNoRec(self.esq, segmento)
                self.esq.pai = self
            else:
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
        if no.esq.valor != None: self.imprime_inordem_rec(no.esq)
        if no.valor != None: print str(no.valor) + ' < ',
        if no.dir.valor != None: self.imprime_inordem_rec(no.dir)
        
    def imprime(self, tipo):
        print str(self.valor) + ' do tipo ' + tipo + ' o meu pai eh '
        if self.pai != None: print str(self.pai.valor) 
        else: print 'None'
        if (self.esq.valor != None): No.imprime(self.esq, 'esq')
        if (self.dir.valor != None): No.imprime(self.dir, 'dir')
        
    def buscarNo(self, valor):
        if self.valor == None: return self
        else:
            x = self
            while x.valor != None and x.valor != valor:
                if x.valor < valor:
                    x = x.dir
                else:
                    x = x.esq
            return x
        
    def noSucessor(self, valor):
      no = No.buscarNo(self, valor)

      if no.valor == None or no.dir.valor == None:
          y = no.pai
          x = no
          while(y != None and y.dir == x):
              x = y
              y = y.pai
          return y
      else:
          return No.menorElemento(self, no.dir)

    def sucessor(self, valor):
        no = No.noSucessor(self, valor)
        if no == None: return None
        else: return no.valor

    def noPredecessor(self, valor):
        no = No.buscarNo(self, valor)

        if no.valor == None or no.esq.valor == None:
            y = no.pai
            x = no
            while(y != None and y.esq == x):
                x = y
                y = y.pai
            return y
        else:
            return No.maiorElemento(self, no.esq)

    def predecessor(self, valor):
        no = No.noPredecessor(self, valor)
        if no == None: return None
        else: return no.valor
        
    def menorElemento(self, subArvoreEnraizadaEm):
        y = subArvoreEnraizadaEm        
        if y.valor == None: return y

        while y.esq.valor != None:
            y = y.esq

        return y

    def maiorElemento(self, subArvoreEnraizadaEm):
        y = subArvoreEnraizadaEm
        if y.valor == None: return y

        while y.dir.valor != None:
            y = y.dir

        return y
        
                
class Arvore:
    def __init__(self):
        novoNo = No()
        self.raiz = novoNo
        
    def insereNo(self, valor):
        self.raiz = No.InsereNo(self.raiz, valor)     

    def buscaNo(self, valor):
        return No.buscarNo(self.raiz, valor)

    def removeNo(self, valor):
        self.raiz = No.RemoveNo(self.raiz, valor)

    def imprime_inordem(self):
        No.imprime_inordem(self.raiz)
        
    def imprimir(self):
        No.imprime(self.raiz, 'raiz')
        
    def valorDoSucessor(self, valor):
        r = No.noSucessor(self.raiz, valor)
        if r != None:
            return r.valor
        else:
            return None
        
    def valorDoPredecessor(self, valor):
        r = No.noPredecessor(self.raiz, valor)
        if r != None:
            return r.valor
        else:
            return None
        
a = Arvore()
a.insereNo(1)
a.insereNo(10)
a.insereNo(15)
a.insereNo(5)
a.insereNo(2)

a.imprimir()

print '--------------------'

a.removeNo(10)

a.removeNo(2)

a.imprimir()

print '--------------------'

a.insereNo(12)

a.insereNo(8)

a.insereNo(2)

a.removeNo(5)

a.insereNo(20)

a.imprimir()

print '-------------------'

print a.valorDoPredecessor(3)

print a.valorDoSucessor(18)

print a.buscaNo(50).valor

print a.buscaNo(20).valor

