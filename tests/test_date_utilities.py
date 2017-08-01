import datetime
import unittest

from .context import date_utilities as d_utils


class DateUtilitiesTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    ###########################################################################
    # Unit tests for get_datestamp()
    ###########################################################################

    # Test names are of the format:
    #   test_<func>_<in_fmt>_<out_fmt>_<date>
    #
    # Where:
    #   <func>      Function name being tested.
    #                   (get_datestamp)
    #   <in_fmt>    Date element separator format for input.
    #                   (s=slash, d=dashed, c=contiguous, x=default)
    #   <out_fmt>   Date element separator format for output.
    #                   (s=slash, d=dashed, c=contiguous, x=default)
    #   <date>      Expected return boolean value.
    #                   (y=y2k, x=default)

    def test_get_datestamp_x_x_x(self):
        test_str = datetime.datetime.today().strftime('%Y%m%d')
        self.assertEqual(test_str, d_utils.get_datestamp())

    def test_get_timestamp_x_d_x(self):
        test_str = datetime.datetime.today().strftime('%Y-%m-%d')
        format_str = '%Y-%m-%d'
        self.assertEqual(
            test_str, d_utils.get_datestamp(format_string=format_str))

    def test_get_datestamp_d_x_y(self):
        test_str = '20000101'
        orig_str = '2000-01-01'
        self.assertEqual(test_str, d_utils.get_datestamp(orig_str))

    def test_get_datestamp_s_d_y(self):
        test_str = '2000-01-01'
        orig_str = '01/01/2000'
        format_str = '%Y-%m-%d'
        self.assertEqual(test_str, d_utils.get_datestamp(orig_str, format_str))

    ###########################################################################
    # Unit tests for is_date()
    ###########################################################################

    # Test names are of the format:
    #   test_<func>_<standard>_<format>_<return>_{<bound>}
    #
    # Where:
    #   <func>      Function name being tested.
    #                   (is_date)
    #   <standard>  Date standard tested.
    #                   (i=ISO 8601, n=Non-ISO)
    #   <format>    Date element separator format.
    #                   (s=slash, d=dashed, c=contiguous)
    #   <return>    Expected return boolean value.
    #                   (t=True, f=False)
    #   <bound>     (optional) For False returns, what offending date bound is
    #               being tested.
    #                   (u=upper, l=lower)

    ###########################################################################
    # Non-ISO slash format is_date() tests
    ###########################################################################

    def test_is_date_n_s_t(self):
        test_str = '01/01/2000'
        self.assertTrue(d_utils.is_date(test_str))

    def test_is_date_n_s_f_u(self):
        test_str = '13/32/2000'
        self.assertFalse(d_utils.is_date(test_str))

    def test_is_date_n_s_f_l(self):
        test_str = '00/00/0000'
        self.assertFalse(d_utils.is_date(test_str))

    ###########################################################################
    # Non-ISO dashed format is_date() tests
    ###########################################################################

    def test_is_date_n_d_t(self):
        test_str = '01-01-2000'
        self.assertTrue(d_utils.is_date(test_str))

    def test_is_date_n_d_f_u(self):
        test_str = '13-32-2000'
        self.assertFalse(d_utils.is_date(test_str))

    def test_is_date_n_d_f_l(self):
        test_str = '00-00-0000'
        self.assertFalse(d_utils.is_date(test_str))

    ###########################################################################
    # ISO 8601 dashed format is_date() tests
    ###########################################################################

    def test_is_date_i_s_t(self):
        test_str = '2000/01/01'
        self.assertTrue(d_utils.is_date(test_str))

    def test_is_date_i_s_f_u(self):
        test_str = '2000/13/32'
        self.assertFalse(d_utils.is_date(test_str))

    def test_is_date_i_s_f_l(self):
        test_str = '0000/00/00'
        self.assertFalse(d_utils.is_date(test_str))

    ###########################################################################
    # ISO 8601 dashed format is_date() tests
    ###########################################################################

    def test_is_date_i_d_t(self):
        test_str = '2000-01-01'
        self.assertTrue(d_utils.is_date(test_str))

    def test_is_date_i_d_f_u(self):
        test_str = '2000-13-32'
        self.assertFalse(d_utils.is_date(test_str))

    def test_is_date_i_d_f_l(self):
        test_str = '0000-00-00'
        self.assertFalse(d_utils.is_date(test_str))

    ###########################################################################
    # ISO-8601 contiguous format is_date() tests
    ###########################################################################

    def test_is_date_i_c_t(self):
        test_str = '20000101'
        self.assertTrue(d_utils.is_date(test_str))

    def test_is_date_i_c_f_u(self):
        test_str = '20001332'
        self.assertFalse(d_utils.is_date(test_str))

    def test_is_date_i_c_f_l(self):
        test_str = '00000000'
        self.assertFalse(d_utils.is_date(test_str))
