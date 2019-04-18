# Marvel API
# source from: https://github.com/wrap-away/Marvel-API/ and https://github.com/YZHANG1270/Marvel_KnowledgeGraph/blob/master/marvel_api.ipynb
import os
import pytest
from marvel import Marvel
from marvel.exceptions import MarvelException

# Create a cache file to store json file
CACHE_FNAME = 'marvel_cache.json'

class MarvelHero(object):
    # Constructor
    def __init__(self, charac_diction):
        self.id = charac_diction['id']
        self.name = charac_diction['name']
        self.description = charac_diction['description']
        self.thumbnail = charac_diction['thumbnail']['path']
        self.wiki = charac_diction['urls'][1]['url']

    def __str__(self):
        if self.description:
            return "{}: {}. Learn more here: {}".format(self.name, self.description, self.wiki)
        else:
            return "Find more about {} in {}.".format(self.name, self.wiki)


try:
    cache_file = open(CACHE_FNAME, 'r')
    CACHE_DICTION = json.loads(cache_file.read())
    cache_file.close()
except:
    CACHE_DICTION = {}


PUBLIC_KEY = "3117fd27b59beda1728b443a29c47958"
PRIVATE_KEY = "e9c5465e209f52e14295a581cd2be315c655073b"

m = Marvel(PUBLIC_KEY, PRIVATE_KEY)
character = m.characters
character.all()

instance_list_ticketmaster = []
instance_list_ticketmaster_artists = []

while True:
    name = input("Enter the characters with names that begin with: ")
    hero_list = character.all(nameStartsWith=name)
    try:
        for each_hero in hero_list['data']['results']:
            instance = MarvelHero(each_hero)
            instance_list_ticketmaster.append(instance)
            instance_list_ticketmaster_artists = instance.name
        print("Searching for keyword \"{}\" in Marvel database ...".format(nameStartsWith_input))
    except:
        print("\nSorry, no result matches the keyword. Please try again.")
    else:
        print("Yay! Here is what I found:")
        break
print("==================================================================================")
# Print the concert details
if instance_list_ticketmaster != []:
    # print(instance_list_ticketmaster_artists)
    for i in instance_list_ticketmaster:
        print("\n")
        print(i)
        print("\n")
print("==================================================================================")
