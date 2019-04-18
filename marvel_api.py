# Marvel API
from marvel import Marvel
import json
import requests

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
            return "ID: {} - {}: {}.\nLearn more here: {}".format(self.id, self.name, self.description, self.wiki)
        else:
            return "ID: {} - Find more about {} in {}.".format(self.id, self.name, self.wiki)

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

instance_list = []

def get_hero_data_with_caching(name):
    if name in CACHE_DICTION:
        return CACHE_DICTION[name]
    else:
        python_object = character.all(nameStartsWith=name)

        cache_file_object = open(CACHE_FNAME, 'w')
        CACHE_DICTION[name] = python_object
        cache_file_object.write(json.dumps(CACHE_DICTION))
        cache_file_object.close()
        return CACHE_DICTION[name]

# Part 1: search superhero with keyword

while True:
    name = input("Enter the characters with names that begin with: ")
    hero_list = get_hero_data_with_caching(name)

    try:
        for superhero in hero_list['data']['results']:
            instance = MarvelHero(superhero)
            instance_list.append(instance)
        print("Searching for keyword \"{}\" in Marvel database ...".format(name))
    except:
        print("\nSorry, no result matches the keyword. Please try again.")
    else:
        if instance_list != []:
            print("Yay! Here is what I found:")
            print("==================================================================================")
            for i in instance_list:
                print("\n")
                print(i)
            break
        else:
            print("\nSorry, no result matches the keyword. Please try again.")

print("==================================================================================")


# Part 2: dump all the superhero into one database


# print("\n=============== CSV =================\n")
#
# character.all()
#
#
# # Step 9:
# # Make a CSV file called "all_superhero.csv"
#
# csv_file = open("all_superhero.CSV", "w")
# csv_file.write("ID,Name,Description,Link,Photo\n")
# for hero in instance_list_ticketmaster:
#     csv_file.write("{},{},{},{},{}\n".format(event.eventname, event.date, event.time, event.artists_string_grammar(), event.eventlink))
# csv_file.write("\n")
# csv_file.write("Artist,Track,Album,Length,Release Date\n")
# for artist in itunes_results_master:
#     for song in artist:
#         csv_file.write("{},{},{},{},{}\n".format(song.artists.replace(',', '&'), song.song.replace(',', ''), song.collection.replace(',', '&'), song.normallength(), song.date))
# csv_file.close()
# print("The CSV file is created successfully. Open the file and Listen to the top 10 songs we have sorted for you.\nLet's start from the latest one! Enjoy!")
