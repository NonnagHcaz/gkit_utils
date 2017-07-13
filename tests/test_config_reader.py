import unittest
import os

from .context import config_reader

BASEDIR = './tests'
DATA_DIR = os.path.join(BASEDIR, 'dat')


class ConfigReaderTests(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_read_config(self):
        test_file = os.path.join(DATA_DIR, 'test_ini.ini')
        test_heads = ['a', 'b', 'c']
        test_dict = {'a': '1', 'b': '2', 'c': 'd'}
        self.assertEqual(test_dict, config_reader.ConfigReader().read_config(test_file, test_heads))
