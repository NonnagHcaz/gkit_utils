import unittest
import os
import shutil

try:
    # Python 3
    from unittest import mock
except ImportError:
    # Python 2
    import mock

from .context import file_utilities as f_utils
from .context import BASEDIR, DATA_DIR

DEFAULT_TXT = 'Hello, World!\n!dlroW ,olleH\n'

DEFAULT_JSON = {"0": ["0", "1", "2"], "1": {"0": ["0", "1", "2"], "1": "0"}}

DEFAULT_CSV_Y = [{
    'a': '0',
    'b': '1',
    'c': 'd'
}, {
    'a': '1',
    'b': '2',
    'c': 'e'
}]
DEFAULT_CSV_N = [{
    0: 'a',
    1: 'b',
    2: 'c'
}, {
    0: '0',
    1: '1',
    2: 'd'
}, {
    0: '1',
    1: '2',
    2: 'e'
}]


class FileUtilitiesTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_mkdir_p(self):
        test_dir = os.path.join(BASEDIR, 'test_dir')
        f_utils.mkdir_p(test_dir)
        self.assertTrue(os.path.isdir(test_dir))
        shutil.rmtree(test_dir)

    ###########################################################################
    ###########################################################################
    ###########################################################################
    # Unit tests for read methods
    ###########################################################################
    ###########################################################################
    ###########################################################################

    ###########################################################################
    # Unit tests for read_json()
    ###########################################################################

    def test_read_json(self):
        test_file = os.path.join(DATA_DIR, 'test_json.json')
        self.assertEqual(DEFAULT_JSON, f_utils.read_json(test_file))

    @mock.patch('warnings.warn')
    def test_read_json_fnfex(self, mfunc):
        test_file = os.path.join(DATA_DIR, 'nofile.json')
        f_utils.read_json(test_file)
        self.assertTrue(mfunc.called)

    @mock.patch('warnings.warn')
    def test_read_json_jdex(self, mfunc):
        test_file = os.path.join(DATA_DIR, 'test_csv.csv')
        f_utils.read_json(test_file)
        self.assertTrue(mfunc.called)

    ###########################################################################
    # Unit tests for read_csv()
    ###########################################################################

    def test_read_csv_y_c(self):
        test_file = os.path.join(DATA_DIR, 'test_csv_c.csv')
        self.assertEqual(DEFAULT_CSV_Y,
                         f_utils.read_csv(
                             test_file, headings=True, delimiter=','))

    def test_read_csv_n_p(self):
        test_file = os.path.join(DATA_DIR, 'test_csv_p.csv')
        self.assertEqual(DEFAULT_CSV_N,
                         f_utils.read_csv(
                             test_file, headings=False, delimiter='|'))

    ###########################################################################
    # Unit tests for read_file()
    ###########################################################################

    def test_read_file_as_json(self):
        test_file = os.path.join(DATA_DIR, 'test_json.json')
        self.assertEqual(DEFAULT_JSON, f_utils.read_file(test_file))

    def test_read_file_as_txt(self):
        test_file = os.path.join(DATA_DIR, 'test_txt.txt')
        self.assertEqual(DEFAULT_TXT, f_utils.read_file(test_file))

    ###########################################################################
    # Unit tests for read()
    ###########################################################################

    def test_read_as_txt(self):
        test_file = os.path.join(DATA_DIR, 'test_txt.txt')
        self.assertEqual(DEFAULT_TXT, f_utils.read(test_file))

    def test_read_as_json(self):
        test_file = os.path.join(DATA_DIR, 'test_json.json')
        self.assertEqual(DEFAULT_JSON, f_utils.read(test_file))

    def test_read_as_csv(self):
        test_file = os.path.join(DATA_DIR, 'test_csv_p.csv')
        self.assertEqual(DEFAULT_CSV_Y,
                         f_utils.read(test_file, headings=True, delimiter='|'))

    ###########################################################################
    ###########################################################################
    ###########################################################################
    # Unit tests for read methods
    ###########################################################################
    ###########################################################################
    ###########################################################################

    ###########################################################################
    # Unit tests for write_json()
    ###########################################################################

    def test_write_json(self):
        test_file = os.path.join(DATA_DIR, 'test_json_write.json')
        f_utils.write_json(test_file, DEFAULT_JSON, sort_keys=True)
        self.assertEqual(DEFAULT_JSON, f_utils.read_json(test_file))
        os.remove(test_file)

    ###########################################################################
    # Unit tests for write_csv()
    ###########################################################################

    def test_write_csv(self):
        test_file = os.path.join(DATA_DIR, 'test_csv_write.csv')
        f_utils.write_csv(test_file, DEFAULT_CSV_Y)
        self.assertEqual(DEFAULT_CSV_Y,
                         f_utils.read_csv(
                             test_file, headings=True, delimiter=','))
        os.remove(test_file)

    ###########################################################################
    # Unit tests for write_file()
    ###########################################################################

    def test_write_as_json(self):
        test_file = os.path.join(DATA_DIR, 'test_json_write.json')
        f_utils.write_file(test_file, DEFAULT_JSON, sort_keys=True)
        self.assertEqual(DEFAULT_JSON, f_utils.read_json(test_file))
        os.remove(test_file)

    def test_write_as_csv(self):
        test_file = os.path.join(DATA_DIR, 'test_csv_write.csv')
        f_utils.write_file(test_file, DEFAULT_CSV_Y)
        self.assertEqual(DEFAULT_CSV_Y,
                         f_utils.read_csv(
                             test_file, headings=True, delimiter=','))
        os.remove(test_file)
