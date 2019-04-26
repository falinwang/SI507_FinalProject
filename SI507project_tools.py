# Marvel API
from marvel import Marvel
import json
import requests
import csv


# Create a cache file to store json file

class MarvelHero(object):
    # Constructor
    def __init__(self, charac_diction):
        self.id = charac_diction['id']
        self.name = charac_diction['name']
        self.description = charac_diction['description']
        self.thumbnail = charac_diction['thumbnail']['path']
        self.detail = charac_diction['urls'][0]['url']

    def __str__(self):
        return '{},{},{},{},{}'.format(self.id, self.name, self.description, self.thumbnail, self.detail)


PUBLIC_KEY = "3117fd27b59beda1728b443a29c47958"
PRIVATE_KEY = "e9c5465e209f52e14295a581cd2be315c655073b"
m = Marvel(PUBLIC_KEY, PRIVATE_KEY)
character = m.characters

def get_hero_data_with_caching(name):
    CACHE_FNAME = 'marvel_cache.json'
    try:
        cache_file = open(CACHE_FNAME, 'r')
        CACHE_DICTION = json.loads(cache_file.read())
        cache_file.close()
    except:
        CACHE_DICTION = {}

    if name in CACHE_DICTION:
        return CACHE_DICTION[name]
    else:
        python_object = character.all(nameStartsWith=name)

        cache_file_object = open(CACHE_FNAME, 'w')
        CACHE_DICTION[name] = python_object
        cache_file_object.write(json.dumps(CACHE_DICTION))
        cache_file_object.close()
        return CACHE_DICTION[name]

# Search superhero with keyword and then output into a csv file

def searching_hero(name):
    superhero_list = []
    another_lst=[]
    hero_list = get_hero_data_with_caching(name)

    try:
        for superhero in hero_list['data']['results']:
            instance = MarvelHero(superhero)
            superhero_list.append(instance)
        print("Searching for keyword \"{}\" in Marvel database.".format(name))
    except:
        print("\nSorry, no result matches the keyword. Please try again.")
    # Part 2: dump all the superhero into one database
    # Make a CSV file called "all_superhero.csv"
    with open('all_superhero.csv', mode='w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(['ID', 'Name', 'Description', 'Photo', 'Link'])
        for hero in superhero_list:
        # writer.writerow(superhero_list)
            csv_file.write("{},{},{},{},{}\n".format(hero.id,hero.name,hero.description.strip().replace(',', '').replace('\n','').replace('\r', ' '),hero.thumbnail,hero.detail.replace(',', '')))
        csv_file.write("\n")


# put the data in csv into db
