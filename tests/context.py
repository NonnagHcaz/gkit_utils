# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0,
                os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gkit_utils import date_utilities
from gkit_utils import file_utilities
from gkit_utils import message_generator
from gkit_utils import print_utilities
from gkit_utils import time_utilities

BASEDIR = './tests'
DATA_DIR = os.path.join(BASEDIR, 'dat')
