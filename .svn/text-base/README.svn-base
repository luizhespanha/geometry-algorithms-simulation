Esse programa implementa os seguintes algoritmos para o problema do
fecho convexo planar:

- Graham
- Embrulho para Presente
- Quickhull
- Mergehull
- Incremental
- Incremental Probabilístico
- Algoritmo ótimo proposto por Chan[1]
- Algoritmo ótimo propost por Bhattacharya e Sen[2]

Existem três "front-ends" ({cli,tk,g}geocomp.py). Para rodar qualquer um
deles, você vai precisar de Python (testado com as versões 1.5.2 e 2.1).
Além disso, tkgeocomp.py precisa do módulo padrão de Tk que acompanha a
distribuição de Python e ggeocomp.py precisa de gnome-python (testado
com a versão 1.4.1)

O arquivo geocomp/config.py pode ser alterado para mudar cores, tamanho
da janela, largura da linha, etc.

O programa tenta carregar automaticamente o primeiro arquivo do
diretório "dados". Depois disso, é possível abrir arquivos em outros
diretórios, usando o "menu" na parte superior esquerda da tela.

Depois de rodar um algoritmo, o programa mostra o número de operações
primitivas realizadas pelo algoritmo ao lado do seu botão. Alguns
algoritmos podem retornar informações adicionais que são mostradas na
parte inferior da janela.

O tempo entre dois passos de um algoritmo pode ser alterado
dinamicamente durante a sua execução e também é possível executar apenas
uma pequena parte do algoritmo passo a passo, bastando para isso usar
o botão "passo a passo". Algumas vezes, é desejável apenas medir a
eficiência de um algoritmo para uma determinada entrada. Como qualquer
algoritmo leva mais tempo desenhando do que fazendo conta, é possível,
antes de iniciar um algoritmo, apertar o botão "esconder" para não
desenhar nada na tela, permitindo que o algoritmo rode bem mais rápido.

O front-end tkgeocomp.py permite salvar a imagem que está desenhada
em um determinado instante na tela, bastando para isso apertar o botão
"imprimir". O formato da imagem criada é .eps (Encapsulated Postscript).

O front-end ggeocomp.py permite dar um zoom em uma determinada área da
tela - infelizmente esse zoom não é muito útil porque os pontos
continuam sendo desenhados na mesma proporção.

O front-end cligeocomp.py pode ser usado para rodar os algoritmos não
interativamente. Ele pode ser chamado como:
	cligeocomp geocomp/convexhull/graham.py dados/ptos*
para rodar o algoritmo de Graham em todos os arquivos dados/ptos*, ou
como
	cligeocomp -a dados/ptos2.pts geocomp/convexhull/graham.py \
			geocomp/convexhull/quickhull.py
para rodar os algortimos de Graham e Quickhull dando dados/ptos2.pts de
entrada. (dica: para rodar todos os algoritmos de fecho convexo, use
	cligeocomp -a dados/ptos2.pts geocomp.convexhull/[^_]*.py
  [^_]*.py vai pegar todos os arquivo que acabam em ".py" e que não
começam com "_")


Acrescentando novos algoritmos/problemas
========================================
Para acrescentar um novo algoritmo de, por exemplo, fecho convexo:
- escreva seu algoritmo no arquivo geocomp/convexhull/novo_alg.py, numa
  função Novo_alg
- edite geocomp/convexhull/__init__.py colocando uma linha
	import novo_alg
  e adicione um item 
  ('novo_alg', 'Novo_alg', 'um nome para aparecer na interface grafica')
  à variável children

Para colocar um novo problema:
- crie um diretório geocomp/novo_problema
- crie geocomp/novo_problema/__init__.py , no mesmo estilo de
  geocomp/convexhull/__init__.py :
  - uma linha "import foo" para cada arquivo foo.py
  - uma lista "children" que possui um item 
  ( 'foo', 'Funcao_de_Foo', 'Nome para a interface grafica')
    para cada arquivo foo.py em geocomp/convexhull/
- edite geocomp/__init__.py e coloque uma linha:
	import novo_problema
  e coloque um item
  ( 'novo_problema', None, 'Um nome para a interface grafica')
  na variável children

Se o novo problema possuir uma entrada que não seja um conjunto de
pontos, será necessário alterar, pelo menos geocomp/common/io.py e
geocomp/common/guicontrol.py (função run_algorithm) para que tudo
funcione.

Quaisquer dúvidas, entre em contato comigo

alexis@ime.usp.br
