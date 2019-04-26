from SI507_finalProject import *
import unittest
import csv

# testing instances
class Testcase1(unittest.TestCase):
    def searching(self):
        name = 'iron'
        result = searching_hero(name)
        self.searching = superhero_list
        self.assertIsInstance(self.searching)

    def test_csv(self):
        self.superhero_file = open('all_superhero.csv','r')
        self.row_reader = self.superhero_file.readlines()

        # print(self.row_reader[0]) # For debug
        # print(self.row_reader[1]) # For debug

        self.assertTrue(self.row_reader[0], "Testing that there is a Title")
        self.assertTrue(self.row_reader[1], "Testing that there is a value")

        self.superhero_file.close()

# class Testcase2(unittest.TestCase):
#     def website(self):
#

class PartThree(unittest.TestCase):
    def setUp(self):
        self.movie_instance = Movie()
        self.distributor_instance = Distributor()
        self.character_instance = Character()

    def test_instances(self):
        self.assertIsInstance(self.movie_instance, Movie, "testing if instance is of class Movie")
        self.assertIsInstance(self.distributor_instance, Distributor, "testing if instance is of class Distributor")
        self.assertIsInstance(self.character_instance, Character, "testing if instance is of class Character")

class PartTwo(unittest.TestCase):
    def setUp(self):
        self.movie_instance = Movie(title = "Iron Man 2")
        self.distributor_instance = Distributor(name = "distributor")
        self.character_instance = Character(name = "Iron Man")


    def test_instances(self):
        self.assertEqual(self.movie_instance.title, "Iron Man 2")
        self.assertEqual(self.distributor_instance.name, "distributor")
        self.assertEqual(self.character_instance.name, "Iron Man")


if __name__ == "__main__":
    unittest.main(verbosity=3)
