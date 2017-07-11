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

    # def test_display_event_prints_correctly(self):
    #     p_utils.display_event(DEFAULT_MSG)
