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

# BASEDIR = './tests'
# DATA_DIR = os.path.join(BASEDIR, 'dat')


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
    # Unit tests for read_json()
    ###########################################################################

    def test_read_json(self):
        test_file = os.path.join(DATA_DIR, 'test_json.json')
        test_json = {
            "0": ["0", "1", "2"],
            "1": {
                "0": ["0", "1", "2"],
                "1": "0"
            }
        }

        self.assertEqual(test_json, f_utils.read_json(test_file))

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

    ###########################################################################
    # Unit tests for read()
    ###########################################################################

    ###########################################################################
    # Unit tests for read_file()
    ###########################################################################
