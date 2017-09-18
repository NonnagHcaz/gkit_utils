from __future__ import absolute_import, division, print_function

import unittest

try:
    # Python 3
    from unittest import mock
except ImportError:
    # Python 2
    import mock

try:
    # Python 2
    from StringIO import StringIO
except ImportError:
    # Python 3
    from io import StringIO

import time

from .context import print_utilities as p_utils

DEFAULT_MSG = 'TEST'
MOCK_TIMESTAMP = '20000101-000000'
MOCK_TIMESTAMP_2 = '20000101-000003'

DEFAULT_PRE = '['
DEFAULT_POST = ']'
DEFAULT_SEP = ':'

TEST_SLEEP = 3


def dummy(*args, **kwargs):
    time.sleep(TEST_SLEEP)


class PrintUtilitiesTests(unittest.TestCase):
    def setUp(self):
        self.out = StringIO()

    def tearDown(self):
        del self.out

    @mock.patch(
        'gkit_utils.time_utilities.get_timestamp', return_value=MOCK_TIMESTAMP)
    def test_timeit(self, mfunc):
        tag = (
            '[{ts}] PROGRAM STARTED...\n\n************************************'
            '************************************\n\n*************************'
            '***********************************************\n[{ts}] PROGRAM E'
            'NDED.\nElapsed:\n\t00:00:{secs}').format(
                ts=MOCK_TIMESTAMP, secs=str(TEST_SLEEP).zfill(2))

        func = dummy
        p_utils.timeit(func, out=self.out, stamped=True)
        self.assertEqual(tag, self.out.getvalue().strip())

    def test_display_divider(self):
        token = '*'
        count = 72
        tag = token * count

        p_utils.display_divider(
            token=token, count=count, pre='', post='', out=self.out)
        self.assertEqual(tag, self.out.getvalue().strip())

    @mock.patch(
        'gkit_utils.time_utilities.get_timestamp', return_value=MOCK_TIMESTAMP)
    def test_display_message_no_stamp(self, mfunc):
        tag = DEFAULT_PRE + DEFAULT_MSG + DEFAULT_POST + DEFAULT_SEP + ' '

        p_utils.display_message(DEFAULT_MSG, tag=DEFAULT_MSG, out=self.out)
        self.assertEqual(tag + DEFAULT_MSG, self.out.getvalue().strip())

    @mock.patch(
        'gkit_utils.time_utilities.get_timestamp', return_value=MOCK_TIMESTAMP)
    def test_display_event_no_stamp(self, mfunc):
        tag = DEFAULT_PRE + 'EVENT' + DEFAULT_POST + DEFAULT_SEP + ' '

        p_utils.display_event(DEFAULT_MSG, out=self.out)
        self.assertEqual(tag + DEFAULT_MSG, self.out.getvalue().strip())

    @mock.patch(
        'gkit_utils.time_utilities.get_timestamp', return_value=MOCK_TIMESTAMP)
    def test_display_error_no_stamp(self, mfunc):
        tag = DEFAULT_PRE + 'ERROR' + DEFAULT_POST + DEFAULT_SEP + ' '

        p_utils.display_error(DEFAULT_MSG, out=self.out)
        self.assertEqual(tag + DEFAULT_MSG, self.out.getvalue().strip())

    @mock.patch(
        'gkit_utils.time_utilities.get_timestamp', return_value=MOCK_TIMESTAMP)
    def test_display_success_no_stamp(self, mfunc):
        tag = DEFAULT_PRE + 'SUCCESS' + DEFAULT_POST + DEFAULT_SEP + ' '

        p_utils.display_success(DEFAULT_MSG, post='', out=self.out)
        self.assertEqual(tag + DEFAULT_MSG, self.out.getvalue().strip())
