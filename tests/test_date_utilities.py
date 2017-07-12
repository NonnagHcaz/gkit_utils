import unittest

from .context import date_utilities as d_utils


class DateUtilitiesTests(unittest.TestCase):


    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_datestamp_now_default(self):
        test_str = '20170712'
        self.assertEqual(test_str, d_utils.get_datestamp())

    def test_get_timestamp_now_iso8601(self):
        test_str = '2017-07-12'
        format_str = '%Y-%m-%d'
        self.assertEqual(test_str, d_utils.get_datestamp(format_string=format_str))

    def test_get_datestamp_mil_default(self):
        test_str = '20000101'
        orig_str = '2000-01-01'
        self.assertEquals(test_str, d_utils.get_datestamp(orig_str))

    def test_get_datestamp_mil_iso8601(self):
        test_str = '2000-01-01'
        orig_str = '20000101'
        format_str = '%Y-%m-%d'
        self.assertEquals(test_str, d_utils.get_datestamp(orig_str, format_str))


    ###########################################################################
    # Method tests for is_date()
    ###########################################################################

    # Test names are of the format:
    #   test_<func>_<standard>_<format>_<return>_{<bound>}
    #
    # Where:
    #   <func>      Function name being tested. (is_date)
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
