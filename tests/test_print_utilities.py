from __future__ import absolute_import, division, print_function

import unittest

try:
    from unittest import mock
except (ImportError):
    import mock

try:
    from StringIO import StringIO
except (ImportError):
    from io import StringIO

from .context import print_utilities as p_utils
# from .context import time_utilities

DEFAULT_MSG = 'TEST'
MOCK_TIMESTAMP = '20000101-000000'

DEFAULT_PRE = '['
DEFAULT_POST = ']'
DEFAULT_SEP = ':'


def dummy():
    pass


class PrintUtilitiesTests(unittest.TestCase):
    def setUp(self):
        self.out = StringIO()

    def tearDown(self):
        del self.out

    @mock.patch(
        'gkit_utils.time_utilities.get_timestamp', return_value=MOCK_TIMESTAMP)
    def test_timeit(self, mfunc):
        tag = '[{ts}]PROGRAM STARTED...\n\n************************************************************************\n\n************************************************************************\n[{ts}]PROGRAM ENDED.\nElapsed:\n\t0.0000 s'.format(
            ts=MOCK_TIMESTAMP)
        func = dummy
        p_utils.timeit(func, out=self.out)
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
        tag = DEFAULT_PRE + MOCK_TIMESTAMP + DEFAULT_POST + DEFAULT_PRE + DEFAULT_MSG + DEFAULT_POST + DEFAULT_SEP + ' '

        p_utils.display_message(DEFAULT_MSG, tag=DEFAULT_MSG, out=self.out)
        self.assertEqual(tag + DEFAULT_MSG, self.out.getvalue().strip())

    @mock.patch(
        'gkit_utils.time_utilities.get_timestamp', return_value=MOCK_TIMESTAMP)
    def test_display_event_no_stamp(self, mfunc):
        tag = DEFAULT_PRE + MOCK_TIMESTAMP + DEFAULT_POST + DEFAULT_PRE + 'EVENT' + DEFAULT_POST + DEFAULT_SEP + ' '

        p_utils.display_event(DEFAULT_MSG, out=self.out)
        self.assertEqual(tag + DEFAULT_MSG, self.out.getvalue().strip())

    @mock.patch(
        'gkit_utils.time_utilities.get_timestamp', return_value=MOCK_TIMESTAMP)
    def test_display_error_no_stamp(self, mfunc):
        tag = DEFAULT_PRE + MOCK_TIMESTAMP + DEFAULT_POST + DEFAULT_PRE + 'ERROR' + DEFAULT_POST + DEFAULT_SEP + ' '

        p_utils.display_error(DEFAULT_MSG, out=self.out)
        self.assertEqual(tag + DEFAULT_MSG, self.out.getvalue().strip())

    @mock.patch(
        'gkit_utils.time_utilities.get_timestamp', return_value=MOCK_TIMESTAMP)
    def test_display_success_no_stamp(self, mfunc):
        tag = DEFAULT_PRE + MOCK_TIMESTAMP + DEFAULT_POST + DEFAULT_PRE + 'SUCCESS' + DEFAULT_POST + DEFAULT_SEP + ' '

        p_utils.display_success(DEFAULT_MSG, post='', out=self.out)
        self.assertEqual(tag + DEFAULT_MSG, self.out.getvalue().strip())
