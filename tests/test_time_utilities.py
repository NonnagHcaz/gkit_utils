import unittest
import datetime
import time

from .context import time_utilities as t_utils


class TimeUtilitiesTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    ###########################################################################
    # Unit tests for get_timestamp()
    ###########################################################################

    # Test names are of the format:
    #   test_<func>_<in_fmt>_<out_fmt>_<date>
    #
    # Where:
    #   <func>      Function name being tested.
    #                   (get_timestamp)
    #   <in_fmt>    Date element separator format for input.
    #                   (s=slash, d=dashed, c=contiguous, x=default)
    #   <out_fmt>   Date element separator format for output.
    #                   (s=slash, d=dashed, c=contiguous, x=default)
    #   <date>      Expected return boolean value.
    #                   (y=y2k, x=default)

    def test_get_timestamp_s_d_y(self):
        test_fmt = '%Y-%m-%d %H:%M:%S'
        orig_fmt = '%d/%m/%Y %H:%M:%S'
        test_str = '2000-01-01 00:00:00'
        orig_str = datetime.datetime.strptime('01/01/2000 00:00:00', orig_fmt)
        self.assertEqual(test_str, t_utils.get_timestamp(orig_str, test_fmt))

    ###########################################################################
    # Unit tests for get_timestamp()
    ###########################################################################

    def test_get_elapsed(self):
        format_str = '%Y-%m-%d %H:%M:%S'
        start_str = '2000-01-01 00:00:00'
        end_str = '2000-01-01 00:00:10'
        start_time = time.mktime(time.strptime(start_str, format_str))
        end_time = time.mktime(time.strptime(end_str, format_str))
        pre = 0
        post = 0
        self.assertEqual('10',
                         t_utils.get_elapsed(start_time, end_time, pre, post))
