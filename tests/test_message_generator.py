from __future__ import absolute_import, division, print_function

import unittest

from .context import message_generator as mg

DEFAULT_MSG = 'TEST'


class MessageGeneratorTests(unittest.TestCase):
    def test_generate_divider(self):
        token = '*'
        count = 72
        pre = '\n'
        post = '\n'
        tag = pre + token * count + post

        msg = mg.generate_divider(token=token, count=count, pre=pre, post=post)
        self.assertEqual(tag, msg)

    def test_generate_message_no_stamp_no_tag(self):
        tag = ' '

        msg = mg.generate_message(DEFAULT_MSG, stamped=False)
        self.assertEqual(tag + DEFAULT_MSG, msg)

    def test_generate_message_no_stamp(self):
        pre = '['
        post = ']'
        sep = ':'
        tag = pre + DEFAULT_MSG + post + sep + ' '

        msg = mg.generate_message(DEFAULT_MSG, tag=DEFAULT_MSG, stamped=False)
        self.assertEqual(tag + DEFAULT_MSG, msg)

    def test_generate_event_no_stamp(self):
        tag = '[EVENT]: '

        msg = mg.generate_event(DEFAULT_MSG, stamped=False)
        self.assertEqual(tag + DEFAULT_MSG, msg)

    def test_generate_error_no_stamp(self):
        tag = '[ERROR]: '

        msg = mg.generate_error(DEFAULT_MSG, stamped=False)
        self.assertEqual(tag + DEFAULT_MSG, msg)

    def test_generate_success_no_stamp(self):
        tag = '[SUCCESS]: '

        msg = mg.generate_success(DEFAULT_MSG, stamped=False)
        self.assertEqual(tag + DEFAULT_MSG + '\n', msg)

    def test_generate_startup_no_stamp(self):
        tag = '[STARTUP]: '

        msg = mg.generate_startup(DEFAULT_MSG, stamped=False)
        self.assertEqual(tag + DEFAULT_MSG + '\n', msg)

    def test_generate_tag_string(self):
        pre = '['
        post = ']'
        tag = pre + DEFAULT_MSG + post

        msg = mg.generate_tag_string(DEFAULT_MSG, pre=pre, post=post)
        self.assertEqual(tag, msg)

    def test_generate_tag_head(self):
        pre = '['
        post = ']'
        sep = ':'
        tag = pre + DEFAULT_MSG + post + sep + ' '

        msg = mg.generate_tag_head(DEFAULT_MSG, pre=pre, post=post, sep=sep)
        self.assertEqual(tag, msg)
