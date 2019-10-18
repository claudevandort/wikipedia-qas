
"""
 * Query Reformulation
    Simple string-based manipulations
 * N-Gram Mining
    N-Gram extraction from corpora
 * N-Gram Filtering
    weight according to how well they match the answer type
 * N-Gram Tiling
 *

"""
from POS import POStagger
import nltk
from Parsing import Chunking


def questionAnalysis(question_text):
    pos = {'Q': [], 'V': [], 'FN': []}
    Arbol = Chunking(question_text)
    for subarbol in Arbol.subtrees():
        if subarbol.label() != 'S':
            pos[subarbol.label()] += subarbol.leaves()
    return pos


def main():
    """
    * Question Analysis
    * Document Retrieval
    * Answer Extraction
    * Answer Evaluation
    * Answer Display
    """

    # Question Analysis
    pos = questionAnalysis(input("Pregunte: "))




if __name__ == "__main__":
    main()