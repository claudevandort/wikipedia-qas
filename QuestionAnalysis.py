from nltk.tag import StanfordPOSTagger
from nltk import chunk
import os


def POStagger(text):
    """
     * Part-of-Speech Tagging
     * Function: use the Stanford tagger and a model already trained in spanish
     * Input: text to tag
     * Output: tagged text
    """
    os.environ['JAVAHOME'] = "/usr/bin/java"
    MODEL = "spanish.tagger"
    TAGGER = "stanford-postagger.jar"

    Tagger = StanfordPOSTagger(MODEL, TAGGER)
    tagged_text = Tagger.tag(text.split())
    return tagged_text


def Chunking(tagged_text):
    """
    * Chuncking
    * Function: partially parse a tagged text,
    *           identifying:
    *               - nominal phrases
    *               - interrogative pronouns
    *               - verbs
    * Input: tagged text
    * Output: syntax tree
    """
    # regex to find nominal phrases, questions and verbs
    grammar = '''
    NP:
       {<da0000>*(<n.*>)*<aq0000>*}
    IP:
       {<pr000000|pt000000>}
    V:
       {<v.*>}
    '''
    chunker = chunk.RegexpParser(grammar)
    tree = chunker.parse(tagged_text)
    return tree


def questionAnalysis(question_text):
    """
    * Question Analysis
    * Function: extract and group key components in a question
    * Input: input text
    * Output: input text's relevant tagged words grouped in a dictionary by tag type (IP, V and NP)
    """
    pos = {'IP': [], 'V': [], 'NP': []}
    tree = Chunking(POStagger(question_text))
    for subtree in tree.subtrees():
        if subtree.label() != 'S':
            pos[subtree.label()] += subtree.leaves()
    return pos

