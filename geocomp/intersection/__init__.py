"""Algoritmos para o Problema da detecao de interseccao:

"""
import shamos_hoey
import brute

# cada entrada deve ter:
#  [ 'nome-do-modulo', 'nome-da-funcao', 'nome do algoritmo' ]
children = ( 
	( 'shamos_hoey', 'shamos_hoeyABBB', 'Shamos e Hoey Arvore Balanceada' ),
	( 'shamos_hoey', 'shamos_hoeyABB', 'Shamos e Hoey Arvore' ),
	( 'shamos_hoey', 'shamos_hoeySL', 'Shamos e Hoey Skip List' ),
	( 'brute', 'Brute_Force', 'Forca Bruta' )
)

#children = algorithms

#__all__ = [ 'graham', 'gift' ]
__all__ = map (lambda a: a[0], children)
