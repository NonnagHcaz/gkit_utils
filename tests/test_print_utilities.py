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

    # @mock.patch(
    #     'gkit_utils.time_utilities.get_timestamp', return_value=MOCK_TIMESTAMP)
    # def test_timeit(self, mfunc):
    #     tag = (
    #         '[{ts}][STARTUP]: PROGRAM STARTED...\n\n**************************'
    #         '**********************************************\n\n***************'
    #         '*********************************************************\n\n'
    #         '[{ts}] PROGRAM ENDED.\nElapsed:\n\t00:00:{secs}').format(
    #             ts=MOCK_TIMESTAMP, secs=str(TEST_SLEEP).zfill(2))

    #     p_utils.timeit(func=dummy, out=self.out, stamped=True)
    #     print('\n' + '#' * 72 + '\n')
    #     print(self.out.getvalue().strip())
    #     print('\n' + '#' * 72 + '\n')
    #     print(tag)
    #     print('\n' + '#' * 72 + '\n')
    #     self.assertEqual(tag, self.out.getvalue().strip())

    def test_print_divider(self):
        token = '*'
        count = 72
        tag = token * count

        p_utils.print_divider(
            token=token, count=count, pre='', post='', out=self.out)
        self.assertEqual(tag, self.out.getvalue().strip())

    @mock.patch(
        'gkit_utils.time_utilities.get_timestamp', return_value=MOCK_TIMESTAMP)
    def test_print_message(self, mfunc):
        tag = (
            DEFAULT_PRE + MOCK_TIMESTAMP + DEFAULT_POST +
            DEFAULT_PRE + DEFAULT_MSG + DEFAULT_POST + DEFAULT_SEP + ' ')

        p_utils.print_message(
            DEFAULT_MSG, tags=[DEFAULT_MSG], out=self.out, stamped=True)
        self.assertEqual(tag + DEFAULT_MSG, self.out.getvalue().strip())

    @mock.patch(
        'gkit_utils.time_utilities.get_timestamp', return_value=MOCK_TIMESTAMP)
    def test_print_event(self, mfunc):
        tag = (
            DEFAULT_PRE + MOCK_TIMESTAMP + DEFAULT_POST +
            DEFAULT_PRE + 'EVENT' + DEFAULT_POST + DEFAULT_SEP + ' ')

        p_utils.print_event(DEFAULT_MSG, out=self.out, stamped=True)
        self.assertEqual(tag + DEFAULT_MSG, self.out.getvalue().strip())

    @mock.patch(
        'gkit_utils.time_utilities.get_timestamp', return_value=MOCK_TIMESTAMP)
    def test_print_error(self, mfunc):
        tag = (
            DEFAULT_PRE + MOCK_TIMESTAMP + DEFAULT_POST +
            DEFAULT_PRE + 'ERROR' + DEFAULT_POST + DEFAULT_SEP + ' ')

        p_utils.print_error(DEFAULT_MSG, out=self.out, stamped=True)
        self.assertEqual(tag + DEFAULT_MSG, self.out.getvalue().strip())

    @mock.patch(
        'gkit_utils.time_utilities.get_timestamp', return_value=MOCK_TIMESTAMP)
    def test_print_success(self, mfunc):
        tag = (
            DEFAULT_PRE + MOCK_TIMESTAMP + DEFAULT_POST +
            DEFAULT_PRE + 'SUCCESS' + DEFAULT_POST + DEFAULT_SEP + ' ')

        p_utils.print_success(DEFAULT_MSG, post='', out=self.out, stamped=True)
        self.assertEqual(tag + DEFAULT_MSG, self.out.getvalue().strip())

    @mock.patch(
        'gkit_utils.time_utilities.get_timestamp', return_value=MOCK_TIMESTAMP)
    def test_print_startup(self, mfunc):
        tag = (
            DEFAULT_PRE + MOCK_TIMESTAMP + DEFAULT_POST +
            DEFAULT_PRE + 'STARTUP' + DEFAULT_POST + DEFAULT_SEP + ' ')

        p_utils.print_startup(DEFAULT_MSG, out=self.out, stamped=True)
        self.assertEqual(tag + DEFAULT_MSG, self.out.getvalue().strip())
