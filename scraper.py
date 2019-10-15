# -*- coding: utf-8 -*-
import wikipedia
from boltons.strutils import slugify

scraped = []


def scrape(queue):
    # Breath-first search
    while len(queue) > 0:
        title = queue.pop(0)
        if title in scraped:
            continue
        scraped.append(title)
        links, summary, content = None, None, None
        try:
            links = wikipedia.page(title).links
            summary = wikipedia.summary(title)
            content = wikipedia.page(title).content
        except:
            continue
        queue += [link for link in links if link[:1].isalpha()]
        with open("corpus/{0:03d}-{1}.txt".format(len(scraped), slugify(title)), 'a') as file:
            file.write(title)
            file.write("\n")
            file.write(summary)
            file.write("\n")
            file.write(content)
            file.write("\n\n")
        print("{} {}".format(title, len(queue)))


def main():
    wikipedia.set_lang("es")
    seed = "Inteligencia Artificial"
    q = [seed]
    scrape(q)


if __name__ == "__main__":
    main()