import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

import unittest
import TestRunner

from os import remove
from os.path import isfile

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


    def test_json_creation(self):
        '''
        Tests that a JSON file gets created.
        '''
        store = StoreAdapter(method='JSON')
        test_path = './testing_json.json'
        store.to_json(
            data = {},
            path = test_path,
            overwrite = self.overwrite
        )
        self.assertTrue(isfile(test_path))


    def test_json_update(self):
        '''
        Tests that the created-for-testing-purposes JSON file gets updated.
        '''
        store = StoreAdapter(method='JSON')
        test_path = './testing_json.json'
        store.to_json(
            data = {},
            path = test_path,
            overwrite = self.overwrite
        )
        test_data = {'update_test': True}
        store.to_json(
            data = test_data,
            path = test_path,
            overwrite = False
        )
        d = store.load_json(test_path)
        self.assertEqual(d, test_data)


    def cleanUp(self):
        try: remove('./testing_json.json')
        except: pass


TestRunner.main()
