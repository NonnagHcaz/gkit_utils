import unittest
import os

try:
    # Python 3
    from unittest import mock
except ImportError:
    # Python 2
    import mock

from .context import config_reader
from .context import DATA_DIR


class ConfigReaderTests(unittest.TestCase):
    def setUp(self):
        self.test_file = os.path.join(DATA_DIR, 'test_ini.ini')

    def tearDown(self):
        pass

    def test_read_config(self):
        test_heads = ['a', 'b', 'c']
        test_dict = {'a': '1', 'b': '2', 'c': 'd'}
        self.assertEqual(test_dict,
                         config_reader.ConfigReader().read_config(
                             self.test_file, test_heads))

    @mock.patch('warnings.warn')
    def test_read_config_bad(self, mfunc):
        test_heads = ['a', 'b', 'd']
        test_dict = {'a': '1', 'b': '2', 'd': None}
        self.assertEqual(test_dict,
                         config_reader.ConfigReader().read_config(
                             self.test_file, test_heads))
        self.assertTrue(mfunc.called)
