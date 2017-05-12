from __future__ import absolute_import, division, print_function

import sys
import os

########################################################################
# System methods
########################################################################


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS or sys._MEIPASS2
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
