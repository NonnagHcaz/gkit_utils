import unittest
import os

try:
    from unittest import mock
except ImportError:
    import mock

from .context import config_reader

BASEDIR = './tests'
DATA_DIR = os.path.join(BASEDIR, 'dat')


class ConfigReaderTests(unittest.TestCase):

    def setUp(self):
        self.test_file = os.path.join(DATA_DIR, 'test_ini.ini')

    def tearDown(self):
        pass

    def test_read_config(self):
        test_heads = ['a', 'b', 'c']
        test_dict = {'a': '1', 'b': '2', 'c': 'd'}
        self.assertEqual(test_dict, config_reader.ConfigReader().read_config(self.test_file, test_heads))

    @mock.patch('warnings.warn')
    def test_read_config_bad(self, mfunc):
        test_heads = ['a', 'b', 'd']
        test_dict = {'a': '1', 'b': '2', 'd': None}
        self.assertEqual(test_dict, config_reader.ConfigReader().read_config(self.test_file, test_heads))
        self.assertTrue(mfunc.called)
