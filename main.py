
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
from QuestionAnalysis import POStagger
import nltk
from QuestionAnalysis import questionAnalysis


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
    # Document Retrieval





if __name__ == "__main__":
    main()