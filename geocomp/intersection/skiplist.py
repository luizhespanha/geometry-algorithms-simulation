# -*- coding: utf-8 -*-
import random

class Skiplist:
    def __init__(self):
        self.nivel = 1
        self.p = 0.6
        self.cabeca = Cabeca(1)
        self.nil = Celula(1, None)
        self.cabeca.ptrs[0] = self.nil

    def nivelRandomico(self):
        level = 1

        while random.random() < self.p:
            level = level + 1

        return level

    def predecessor(self, segmento):
        celula = self.cabeca
        i = self.nivel - 1

        while i >= 0:
            while(celula.ptrs[i] != self.nil and celula.ptrs[i].valor < segmento): 
                celula = celula.ptrs[i]

            i = i - 1

        if celula.ehCabeca() == True: return None
        else: return celula.valor

    def sucessor(self, segmento):
        celula = self.cabeca
        i = self.nivel - 1

        while i >= 0:
            while(celula.ptrs[i] != self.nil and celula.ptrs[i].valor <= segmento): 
                celula = celula.ptrs[i]

            i = i - 1

        prox = celula.ptrs[0]

        if prox.ehNil() == True: return None
        else: 
            return prox.valor

    def remove(self, segmento): 
        update = []
        
        celula = self.cabeca
        i = self.nivel - 1

        while i >= 0:
            while(celula.ptrs[i] != self.nil and celula.ptrs[i].valor < segmento): 
                celula = celula.ptrs[i]
            update.append(celula)
            i = i - 1

        prox = celula.ptrs[0]

        if prox != self.nil and prox.valor == segmento:
            for i in range(0,self.nivel):
                up = update.pop()

                if up.ptrs[i] != prox: 
                    break
                else: 
                    up.ptrs[i] = prox.ptrs[i]

            while self.nivel >= 1 and self.cabeca.ptrs[self.nivel - 1] == self.nil:
                self.nivel = self.nivel - 1

            if self.nivel == 0: self.nivel = 1

            del self.cabeca.ptrs[self.nivel:]


    def insere(self, segmento):
        novoNivel = self.nivelRandomico()

        update = []

        celula = self.cabeca
        i = self.nivel - 1

        while i >= 0:
            while(celula.ptrs[i] != self.nil and celula.ptrs[i].valor < segmento):
                celula = celula.ptrs[i]
           
            update.append(celula)
            i = i - 1


        novaCelula = Celula(novoNivel, segmento)

        if novoNivel > self.nivel:
            self.cabeca.ptrs.extend([novaCelula] * (novoNivel - self.nivel))

            for i in range(self.nivel, novoNivel):
                novaCelula.ptrs[i] = self.nil

            for i in range(0, self.nivel):
                celula = update.pop()
                novaCelula.ptrs[i] = celula.ptrs[i]
                celula.ptrs[i] = novaCelula

            self.nivel = novoNivel

        else :
            for i in range(0, novoNivel):
                celula = update.pop()
                novaCelula.ptrs[i] = celula.ptrs[i]
                celula.ptrs[i] = novaCelula

    def imprime(self):
        print 'Skip list com nivel ' + str(self.nivel)
        x = self.cabeca

        while x != None:
            print 'Celula atual: ' + str(x.valor) + ' @ ' + str(x) + ' eh nil ? ' + str(x.ehNil())
            
            for i, vizinho in enumerate(x.ptrs):
                print '\tvizinho ' + str(i) + ': ' + str(x.ptrs[i])

            print '****\n'
            x = x.ptrs[0]

    def imprime_inordem(self):
        x = self.cabeca

        while x != None:
            if x.ehNil() == False:
                print str(x.valor),
                if x.ptrs[0] != self.nil:
                    print '<',
            
            x = x.ptrs[0]

        print

class Celula:
    def __init__(self, nivel, valor):
        self.ptrs = [None]*nivel
        self.valor = valor

    def ehNil(self):
        return self.valor == None

    def ehCabeca(self):
        return self.__class__.__name__ == 'Cabeca'

class Cabeca(Celula):
    def __init__(self, nivel):
        self.ptrs = [None]*nivel
        self.valor = None


# Abaixo são os testes 
'''
s = Skiplist()
s.insere(3)
s.insere(9)
s.insere(1)
s.insere(5)
s.imprime_inordem()

suc = s.sucessor(3)
print 'Sucessor do 3: ' + str(suc)
pre = s.predecessor(3)
print 'Predecessor do 3: ' + str(pre)

print 'Agora vou remover........... '

s.remove(9)
s.remove(9)
s.remove(9)
s.remove(9)
s.imprime_inordem()
s.remove(5)
s.imprime_inordem()
s.remove(1)
s.imprime_inordem()
s.remove(3)
s.imprime_inordem()


print 'Agora vou inserir 88, 33, 910 e -30 ........... '

s.insere(88)
s.imprime_inordem()
s.insere(33)
s.imprime_inordem()
s.insere(910)
s.imprime_inordem()
s.insere(-30)
s.imprime_inordem()


suc = s.sucessor(33)
print 'Sucessor do 33: ' + str(suc)
pre = s.predecessor(33)
print 'Predecessor do 33: ' + str(pre)

suc = s.sucessor(910)
print 'Sucessor do 910: ' + str(suc)
pre = s.predecessor(910)
print 'Predecessor do 910: ' + str(pre)

suc = s.sucessor(-30)
print 'Sucessor do -30: ' + str(suc)
pre = s.predecessor(-30)
print 'Predecessor do -30: ' + str(pre)
'''
