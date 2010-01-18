# -*- coding: utf-8 -*-
import random

# Skip List implementada conforme artigo de William Pugh:
# "Skip Lists: A Probabilistic Alternative to Balanced Trees"
class Skiplist:
    def __init__(self):
        self.nivel = 1
        self.maxnivel = 1
        self.somaniveis = 1 # usado para calcularmos media de niveis

        self.p = 0.25
        self.cabeca = Cabeca(1)
        self.nil = Celula(1, None)
        self.cabeca.ptrs[0] = self.nil # cabeca comeca apontando p/ sentinela 'nil'

    def nivelRandomico(self):
        level = 1

        while random.random() < self.p:
            level = level + 1

        return level

    def predecessor(self, segmento):
        # iteramos na lista, procurando 'segmento'
        celula = self.cabeca
        i = self.nivel - 1

        while i >= 0: # vai ate' o nivel 0 
            while(celula.ptrs[i] != self.nil and celula.ptrs[i].valor < segmento): 
                celula = celula.ptrs[i]

            i = i - 1
        
        # celula aponta para a cabeca ou para o maior elemento que e' menor que 'segmento'
        if celula.ehCabeca() == True: return None # 'segmento' e' o primeiro element da lista
        else: return celula.valor # predecessor proprio

    def sucessor(self, segmento):
        # iteramos na lista, procurando 'segmento'
        celula = self.cabeca
        i = self.nivel - 1

        while i >= 0: # vai ate' o nivel 0
            while(celula.ptrs[i] != self.nil and celula.ptrs[i].valor < segmento): 
                celula = celula.ptrs[i]

            i = i - 1

        # celula aponta para a cabeca ou para o maior elemento que e' menor que 'segmento'
        prox = celula.ptrs[0]
        if prox.ehNil() == False and prox.valor.id == segmento.id: 
            prox = prox.ptrs[0] # se o proximo for o proprio segmento, passamos por ele

        if prox.ehNil() == True: return None # chegou no self.nil
        else: 
            return prox.valor # sucessor proprio

    def remove(self, segmento): 
        update = []
        
        celula = self.cabeca
        i = self.nivel - 1

        while i >= 0:
            while(celula.ptrs[i] != self.nil and celula.ptrs[i].valor < segmento): 
                celula = celula.ptrs[i]
            update.append(celula)
            i = i - 1

        prox = celula.ptrs[0] # prox possui valor maior ou igual a segmento

        if prox != self.nil and prox.valor == segmento:
            for i in range(0,self.nivel): # como removeremos, atualizamos quem apontava para 'segmento'
                up = update.pop() # no estilo 'pilha'

                if up.ptrs[i] != prox: # iesimo apontador de up nao aponta para 'segmento'
                    break
                else: 
                    up.ptrs[i] = prox.ptrs[i]

            while self.nivel >= 1 and self.cabeca.ptrs[self.nivel - 1] == self.nil: 
                # remocao causou diminuicao do nivel
                self.nivel = self.nivel - 1

            if self.nivel == 0: self.nivel = 1
            del self.cabeca.ptrs[self.nivel:] # desaloca os apontadores a mais da cabeca (que estao apontando para self.nil)

        self.somaniveis = self.somaniveis + self.nivel

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

        # celula.ptrs[0] apontara para novaCelula
        novaCelula = Celula(novoNivel, segmento)

        if novoNivel > self.nivel:
            # aumentou o nivel da skiplist
            self.cabeca.ptrs.extend([novaCelula] * (novoNivel - self.nivel))

            for i in range(self.nivel, novoNivel):
                novaCelula.ptrs[i] = self.nil # niveis grandes apontando para self.nil

            for i in range(0, self.nivel):
                # quem apontava para algum sucessor de novaCelula passa a pontar para novaCelula
                celula = update.pop()
                novaCelula.ptrs[i] = celula.ptrs[i]
                celula.ptrs[i] = novaCelula # inicializa apontadores de novaCelula

            self.nivel = novoNivel

        else :
            for i in range(0, novoNivel):
                # quem apontava para algum sucessor de novaCelula passa a pontar para novaCelula
                celula = update.pop()
                novaCelula.ptrs[i] = celula.ptrs[i]
                celula.ptrs[i] = novaCelula # inicializa apontadores de novaCelula

        self.somaniveis = self.somaniveis + self.nivel
        self.maxnivel = max(self.maxnivel, self.nivel)

    def imprime(self): # funcao boa para visualizar estado da SL
        print 'Skip list com nivel ' + str(self.nivel)
        x = self.cabeca

        while x != None:
            if x.ehNil(): t = 'None'
            else: t = str(x.valor.id) + ' ' + str(x.valor)

            print 'Celula atual: ' + str(t) + ' @ ' + str(x) + ' eh nil ? ' + str(x.ehNil())
            
            for i, vizinho in enumerate(x.ptrs):
                print '\tvizinho ' + str(i) + ': ' + str(x.ptrs[i])

            print '****\n'
            x = x.ptrs[0]

    def imprime_inordem(self):
        x = self.cabeca

        while x != None:
            if x.ehNil() == False:
                print str(x.valor.id),
                if x.ptrs[0] != self.nil:
                    print '<',
            
            x = x.ptrs[0]

        print

class Celula: 
    # Celula nao precisa guardar seu proprio nivel, apenas valor (sera um segmento) 
    # e ponteiros para proximas celulas
    def __init__(self, nivel, valor):
        self.ptrs = [None]*nivel
        self.valor = valor

    def ehNil(self):
        return self.valor == None

    def ehCabeca(self):
        return self.__class__.__name__ == 'Cabeca'

class Cabeca(Celula): # Cabeca herda de Celula, reescrevendo o construtor
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
