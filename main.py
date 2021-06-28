import json
import hashlib

WIKIPEDIA = 'https://en.wikipedia.org/wiki/'


# класс итератора:
class WikipediaCountries:

    def __init__(self, path, links):
        with open(path, encoding='utf-8') as f:
            self.countries = json.load(f)
        self.links = links
        with open(self.links, 'w') as file:
            file.write('')

    def __iter__(self):
        return self

    def __next__(self):
        if not self.countries:
            raise StopIteration
        name = self.countries.pop()['name']['common']
        link = WIKIPEDIA + name.replace(' ', '_')
        with open(self.links, 'a', encoding='utf-8') as file:
            file.write(f'{name} - {link}\n')
        return f'{name} - {link}'


for country in WikipediaCountries('countries.json', 'countries_links.txt'):
    print(country)


# генератор:
def md5_hash(path):
    with open(path, encoding='utf-8') as f:
        for line in f:
            yield hashlib.md5(line.strip().encode('utf-8')).hexdigest()


for i in md5_hash('countries_links.txt'):
    print(i)
