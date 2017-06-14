from __future__ import absolute_import, division, print_function

import os
from datetime import datetime
from dateutil import parser


def get_datestamp(ts_to_format=None, format_string="%Y%m%d"):
    if ts_to_format is None:
        ts_to_format = datetime.now()
    return ts_to_format.strftime(format_string)


def is_date(string):
    try:
        parser.parse(string)
        return True
    except ValueError:
        return False


def get_latest_path_and_date(basedir, file_pattern='', delim=''):
    latest_date = datetime.strptime("19900101", "%Y%m%d")
    latest_path = None
    if os.path.isdir(basedir):

        # Get latest file path and date
        for file_name in os.listdir(basedir):
            file_parts = os.path.splitext(file_name)[0].split(delim)
            if ((not file_pattern or
                 (file_pattern and file_pattern.upper() in file_name.upper()))
                    and is_date(file_parts[-1])):
                test_date = datetime.strptime(file_parts[-1], "%Y%m%d")
                if test_date > latest_date:
                    latest_date = test_date
                    latest_path = os.path.join(basedir, file_name)
    return [latest_path, latest_date]
