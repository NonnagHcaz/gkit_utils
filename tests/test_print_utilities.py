from __future__ import absolute_import, division, print_function

import os
import sys
import unittest

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from .context import print_utilities as p_utils

DEFAULT_MSG = 'TEST'


class PrintUtilityTests(unittest.TestCase):
    def setUp(self):
        self.out = StringIO()

    def tearDown(self):
        del self.out

    def test_display_divider(self):
        token = '*'
        count = 72
        pre = ''
        post = ''
        tag = pre + token * count + post

        p_utils.display_divider(token=token, count=count, pre=pre, post=post, out=self.out)
        self.assertEqual(tag, self.out.getvalue().strip())

    def test_display_message_no_stamp(self):
        pre = '['
        post = ']'
        sep = ':'
        tag = pre + DEFAULT_MSG + post + sep + ' '

        p_utils.display_message(DEFAULT_MSG, tag=DEFAULT_MSG, stamped=False, out=self.out)
        self.assertEqual(tag + DEFAULT_MSG, self.out.getvalue().strip())

    def test_display_event_no_stamp(self):
        tag = '[EVENT]: '

        p_utils.display_event(DEFAULT_MSG, stamped=False, out=self.out)
        self.assertEqual(tag + DEFAULT_MSG, self.out.getvalue().strip())

    def test_display_error_no_stamp(self):
        tag = '[ERROR]: '

        p_utils.display_error(DEFAULT_MSG, stamped=False, out=self.out)
        self.assertEqual(tag + DEFAULT_MSG, self.out.getvalue().strip())

    def test_display_success_no_stamp(self):
        tag = '[SUCCESS]: '
        post = ''

        p_utils.display_success(DEFAULT_MSG, post=post, stamped=False, out=self.out)
        self.assertEqual(tag + DEFAULT_MSG + post, self.out.getvalue().strip())

