# Marvel API
from marvel import Marvel
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
character.all()

instance_list = []

while True:
    name = input("Enter the characters with names that begin with: ")
    hero_list = character.all(nameStartsWith=name)
    try:
        for each_hero in hero_list['data']['results']:
            instance = MarvelHero(each_hero)
            instance_list.append(instance)
        print("Searching for keyword \"{}\" in Marvel database ...".format(name))
    except:
        print("\nSorry, no result matches the keyword. Please try again.")
    else:
        print("Yay! Here is what I found:")
        break
print("==================================================================================")
# Print the concert details
if instance_list != []:
    # print(instance_list_ticketmaster_artists)
    for i in instance_list:
        print("\n")
        print(i)
print("==================================================================================")

# print("\n=============== CSV =================\n")
## Step 9:
## Make a CSV file called "event_media.csv"

# csv_file = open("hero_media.CSV", "w")
# csv_file.write("Concert,Date,Time,Lineup,Link\n")
# for event in instance_list_ticketmaster:
#     csv_file.write("{},{},{},{},{}\n".format(event.eventname, event.date, event.time, event.artists_string_grammar(), event.eventlink))
# csv_file.write("\n")
# csv_file.write("Artist,Track,Album,Length,Release Date\n")
# for artist in itunes_results_master:
#     for song in artist:
#         csv_file.write("{},{},{},{},{}\n".format(song.artists.replace(',', '&'), song.song.replace(',', ''), song.collection.replace(',', '&'), song.normallength(), song.date))
# csv_file.close()
# print("The CSV file is created successfully. Open the file and Listen to the top 10 songs we have sorted for you.\nLet's start from the latest one! Enjoy!")
