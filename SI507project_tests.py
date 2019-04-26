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



if __name__ == "__main__":
    unittest.main(verbosity=3)
