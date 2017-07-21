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

DEFAULT_CSV_R = [{
    '0': 'a',
    '1': 'b',
    '2': 'c'
}, {
    '0': '0',
    '1': '1',
    '2': 'd'
}, {
    '0': '1',
    '1': '2',
    '2': 'e'
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
    # Unit tests for read_config()
    ###########################################################################

    def test_read_config(self):
        test_dict = {'a': '1', 'b': '2', 'c': 'd'}
        self.assertEqual(
            test_dict,
            f_utils.read_config(os.path.join(DATA_DIR, 'test_ini.ini')))

    @mock.patch('warnings.warn')
    def test_read_config_bad(self, mfunc):
        test_heads = ['a', 'b', 'd']
        f_utils.read_config(os.path.join(DATA_DIR, 'test_ini.ini'), test_heads)
        self.assertTrue(mfunc.called)

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

    def test_write_file_as_json(self):
        test_file = os.path.join(DATA_DIR, 'test_json_write.json')
        f_utils.write_file(test_file, DEFAULT_JSON, sort_keys=True)
        self.assertEqual(DEFAULT_JSON, f_utils.read_json(test_file))
        os.remove(test_file)

    def test_write_file_as_csv(self):
        test_file = os.path.join(DATA_DIR, 'test_csv_write.csv')
        f_utils.write_file(test_file, DEFAULT_CSV_Y)
        self.assertEqual(DEFAULT_CSV_Y,
                         f_utils.read_csv(
                             test_file, headings=True, delimiter=','))
        os.remove(test_file)

    def test_write_file_as_txt(self):
        test_file = os.path.join(DATA_DIR, 'test_txt_write.txt')
        f_utils.write_file(test_file, DEFAULT_TXT)
        self.assertEqual(DEFAULT_TXT, f_utils.read_file(test_file))
        os.remove(test_file)

    ###########################################################################
    # Unit tests for write()
    ###########################################################################

    def test_write_as_json(self):
        test_file = os.path.join(DATA_DIR, 'test_json_write.json')
        f_utils.write(test_file, DEFAULT_JSON, sort_keys=True)
        self.assertEqual(DEFAULT_JSON, f_utils.read_json(test_file))
        os.remove(test_file)

    def test_write_as_csv_c(self):
        test_delim = ','
        test_file = os.path.join(DATA_DIR, 'test_csv_write_c.csv')
        f_utils.write(test_file, DEFAULT_CSV_Y, delimiter=test_delim)
        self.assertEqual(DEFAULT_CSV_Y,
                         f_utils.read_csv(
                             test_file, headings=True, delimiter=test_delim))
        os.remove(test_file)

    def test_write_as_csv_p(self):
        test_delim = '|'
        test_file = os.path.join(DATA_DIR, 'test_csv_write_p.csv')
        f_utils.write(test_file, DEFAULT_CSV_Y, delimiter=test_delim)
        self.assertEqual(DEFAULT_CSV_Y,
                         f_utils.read_csv(
                             test_file, headings=True, delimiter=test_delim))
        os.remove(test_file)

    def test_write_as_txt(self):
        test_file = os.path.join(DATA_DIR, 'test_txt_write.txt')
        f_utils.write(test_file, DEFAULT_TXT)
        self.assertEqual(DEFAULT_TXT, f_utils.read_file(test_file))
        os.remove(test_file)

    ###########################################################################
    # Unit tests for convert_delimiter_inline()
    ###########################################################################

    def test_convert_delim_in(self):
        old_delim = ','
        new_delim = '|'
        test_file = os.path.join(DATA_DIR, 'test_csv_conv.csv')
        f_utils.write(test_file, DEFAULT_CSV_Y, delimiter=old_delim)
        f_utils.convert_delimiter_inline(
            test_file, old_delimiter=old_delim, new_delimiter=new_delim)

        self.assertEqual(DEFAULT_CSV_Y,
                         f_utils.read_csv(
                             test_file, headings=True, delimiter=new_delim))
        os.remove(test_file)

    ###########################################################################
    # Unit tests for prepend_headings()
    ###########################################################################

    # def test_prepend_headings_y(self):
    #     test_file = os.path.join(DATA_DIR, 'test_csv_prepend_n.csv')
    #     test_delim = '|'
    #     f_utils.write(test_file, DEFAULT_CSV_Y, delimiter=test_delim)
    #     f_utils.prepend_headings(
    #         test_file, ['a', 'b', 'c'], delimiter=test_delim)

    #     self.assertEqual(DEFAULT_CSV_Y,
    #                      f_utils.read_csv(
    #                          test_file, headings=True, delimiter=test_delim))
    #     os.remove(test_file)

    # def test_prepend_headings_n(self):
    #     test_file = os.path.join(DATA_DIR, 'test_csv_prepend_y.csv')
    #     test_delim = '|'
    #     f_utils.write(test_file, DEFAULT_CSV_Y, delimiter=test_delim)
    #     f_utils.prepend_headings(test_file, [0, 1, 2], delimiter=test_delim)

    #     self.assertEqual(DEFAULT_CSV_R,
    #                      f_utils.read_csv(
    #                          test_file, headings=True, delimiter=test_delim))
    #     os.remove(test_file)

    ###########################################################################
    # Unit tests for batch_prepend_headings()
    ###########################################################################

    # def test_batch_prepend_headings_y(self):
    #     test_dir = os.path.join(DATA_DIR, 'batch')
    #     f_utils.mkdir_p(test_dir)
    #     test_file1 = os.path.join(test_dir, 'test_csv_bprepend1_n.csv')
    #     test_file2 = os.path.join(test_dir, 'test_csv_bprepend2_n.csv')
    #     test_delim = '|'
    #     f_utils.write(test_file1, DEFAULT_CSV_Y, delimiter=test_delim)
    #     f_utils.write(test_file2, DEFAULT_CSV_Y, delimiter=test_delim)
    #     f_utils.batch_prepend_headings(
    #         test_dir, ['a', 'b', 'c'], delimiter=test_delim)

    #     self.assertEqual(DEFAULT_CSV_Y,
    #                      f_utils.read_csv(
    #                          test_file1, headings=True, delimiter=test_delim))
    #     self.assertEqual(DEFAULT_CSV_Y,
    #                      f_utils.read_csv(
    #                          test_file2, headings=True, delimiter=test_delim))
    #     shutil.rmtree(test_dir)

    # def test_batch_prepend_headings_n(self):
    #     test_dir = os.path.join(DATA_DIR, 'batch')
    #     f_utils.mkdir_p(test_dir)
    #     test_file1 = os.path.join(test_dir, 'test_csv_bprepend1_n.csv')
    #     test_file2 = os.path.join(test_dir, 'test_csv_bprepend2_n.csv')
    #     test_delim = '|'
    #     f_utils.write(test_file1, DEFAULT_CSV_Y, delimiter=test_delim)
    #     f_utils.write(test_file2, DEFAULT_CSV_Y, delimiter=test_delim)
    #     f_utils.batch_prepend_headings(
    #         test_dir, [0, 1, 2], delimiter=test_delim)

    #     self.assertEqual(DEFAULT_CSV_R,
    #                      f_utils.read_csv(
    #                          test_file1, headings=True, delimiter=test_delim))
    #     self.assertEqual(DEFAULT_CSV_R,
    #                      f_utils.read_csv(
    #                          test_file2, headings=True, delimiter=test_delim))
    #     shutil.rmtree(test_dir)
