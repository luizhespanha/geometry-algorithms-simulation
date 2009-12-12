"""Algoritmos para o Problema da detecao de interseccao:

"""
import shamos_hoey
import shamos_hoeySL

# cada entrada deve ter:
#  [ 'nome-do-modulo', 'nome-da-funcao', 'nome do algoritmo' ]
children = ( 
	( 'shamos_hoey', 'Shamos_Hoey', 'Shamos e Hoey' ),       
	( 'shamos_hoeySL', 'Shamos_HoeySL', 'Shamos e Hoey SL' )
)

#children = algorithms

#__all__ = [ 'graham', 'gift' ]
__all__ = map (lambda a: a[0], children)
