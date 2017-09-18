from __future__ import absolute_import
import datetime

from dateutil import parser


def get_datestamp(ts_to_format=None, format_string="%Y%m%d"):
    if ts_to_format is None:
        ts_to_format = datetime.datetime.now()
    else:
        if is_date(ts_to_format):
            ts_to_format = parser.parse(ts_to_format)
    return ts_to_format.strftime(format_string)


def is_date(string):
    try:
        parser.parse(string)
        return True
    except ValueError:
        return False
