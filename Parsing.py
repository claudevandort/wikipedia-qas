# ***********************************************************************
# Autor:  John Atkinson
# Fecha: 06/09/2018
# Contenido:
#     Análisis sintáctico de oraciones simples en Espanol a partir de una CFG.
#     La gramática se encuentra en archivo "airline.cfg"
# ***********************************************************************

import nltk
from nltk.parse import ChartParser
from POS import *


# ************************************************************
# Función: Parsing(gramatica,oracion)
# Objetivo: Realizar chart parsing de una oracion en Espanol dada una gramática
# Salida: Muestra árboles sintácticos posibles
# ************************************************************
def Parsing(gram, oracion):
    Parser = ChartParser(gram)
    Trees = Parser.parse(oracion)
    for Arbol in Trees:
        print(Arbol)
        # Arbol.draw()
        getNodes(Arbol)


# ************************************************************
# Función: getNodes(parent)
# Objetivo: Muestra el detalle de los nodos de un arvbol sintactico
# ************************************************************
def getNodes(parent):
    RAIZ = "S"
    for node in parent:
        if type(node) is nltk.Tree:
            if node.label() == RAIZ:
                print("======== Sentence =========")
                print("Oración:", " ".join(node.leaves()))
            else:
                print("Constituyente:", node.label())
                print("Hojas:", node.leaves())
            getNodes(node)
        else:
            print("Palabra:", node)


# ************************************************************
# Función: Chuking(texto)
# Objetivo: Realizar parsing parcial para algunos grupos sintácticos
# Salida: Muestra oraciones que calzan con expresion definida
# ************************************************************
def Chunking(texto):
    tagged = POStagger(texto)  # Función que está en programa "POS-tagging.py"
    # Definir Frase Nominal (FN) como: articulo* nombre* adjetivo*
    # * significa 0 o más veces
    grammar = '''                                                                                                              
    FN:
       {<da0000>*(<n.*>)*<aq0000>*}
    Q:
       {<pr000000|pt000000>}
    V:
       {<v.*>}
    '''
    chunker = nltk.chunk.RegexpParser(grammar)
    Arbol = chunker.parse(tagged)
    """
    for subarbol in Arbol.subtrees():
        if subarbol.label() == 'FN':
            print(subarbol)
    """
    return Arbol

