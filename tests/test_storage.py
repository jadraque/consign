import sys
import unittest
import TestRunner

from os import path, remove
from os.path import isfile
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from consign.api import csv, json
from consign.adapters import StoreAdapter


class TestStringMethods(unittest.TestCase):
    

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)


    def setUp(self):
        self.delimiter = None
        self.overwrite = True
        self.provider = None
        self.connection_string = None
        self.container_name = None


    def test_csv_creation(self):
        '''
        Tests that a CSV file gets created.
        '''
        data = []
        test_path = './testing_csv.csv'
        csv(data, test_path)
        self.assertTrue(isfile(test_path))


    def test_json_creation(self):
        '''
        Tests that a JSON file gets created.
        '''
        data = {}
        test_path = './testing_json.json'
        json(data, test_path)
        self.assertTrue(isfile(test_path))


    def test_json_update(self):
        '''
        Tests that a JSON file gets updated.
        '''
        data = {}
        test_path = './testing_json.json'
        json(data, test_path)

        updated_data = {'update_test': True}
        json(updated_data, test_path, overwrite=False)

        store = StoreAdapter(method='JSON')
        d = store.load_json(test_path)
        self.assertEqual(d, updated_data)


    def tearDown(self):
        try: remove('./testing_json.json')
        except: pass
        try: remove('./testing_csv.csv')
        except: pass

TestRunner.main()
