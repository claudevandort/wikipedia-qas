import sys
from pathlib import Path
from gensim.corpora import WikiCorpus
from boltons.strutils import slugify


def make_corpus(input_file):
    """Convert Wikipedia xml dump file to text corpus"""

    wiki = WikiCorpus(input_file)
    wiki.metadata = True
    output_folder = '../corpus'
    Path(output_folder).mkdir(parents=True, exist_ok=True)
    for article in wiki.get_texts():
        text = article[0]
        page_id, title = article[1]
        filename = f'{output_folder}/{page_id}-{slugify(title)}.txt'
        with open(filename, 'a') as file:
            file.write(bytes(' '.join(text), 'utf-8').decode('utf-8') + '\n')
            print(f'{page_id} {title}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 make_wiki_corpus.py <wikipedia_dump_file>')
        sys.exit(1)
    input_file = sys.argv[1]
    make_corpus(input_file)
