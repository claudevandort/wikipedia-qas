# Question Answering System based on Wikipedia
## Building the corpus
* Download the Wikipedia dump [here](https://dumps.wikimedia.org/eswiki/).
* Install dependencies with `pip3 install -r requirements.txt`
* Process the compressed dump `python3 make_wiki_corpus.py <wikipedia_dump_file>`.
  * This will generate a `.txt` file for every article in a `corpus` subfolder.
