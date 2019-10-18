# *******************************************
# Autor:  John Atkinson
# Fecha: 08/09/18
# Contenido:
#     Funciones para realizar Part-of-Speech (POS) tagging para textos en Espanol
#     Note que el tagset utilizado lo puede ver acá:
#       https://nlp.stanford.edu/software/spanish-faq.shtml#tagset

# *******************************************
# IMPORTANTE instalar:
#    (1) JAVA (si es que no está instalado:
#       http://www.oracle.com/technetwork/es/java/javase/downloads/jre8-downloads-2133155.html
#    (2) Setear ruta (PATH) a Java
# *******************************************

from nltk.tag import StanfordPOSTagger
import os


# ************************************************************
# Función: POStagger(texto)
# Objetivo: Realizar POS tagging de un texto en Español
# Salida: retorna texto etiquetado
# ************************************************************
def POStagger(texto):
    # Colocar la ruta donde se encuentra JAVA (JRE)
    JAVA_PATH = "/usr/bin/java"
    os.environ['JAVAHOME'] = JAVA_PATH
    TRAINED_MODEL = "spanish.tagger"
    TAGGER_JAVA = "stanford-postagger.jar"

    # Utilizar POS Tagger ya entrenado por el Stanford Tagger
    Tagger = StanfordPOSTagger(TRAINED_MODEL, TAGGER_JAVA)
    # Separar (split) oraciones a etiquetar
    tagged_text = Tagger.tag(texto.split())
    return tagged_text

