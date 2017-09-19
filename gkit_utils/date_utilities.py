"""Date Utilities.

Module provides methods to fetch datestamps and convert their formats.
"""

from __future__ import absolute_import
import datetime

from dateutil import parser


def get_datestamp(ts_to_format=None, format_string="%Y%m%d"):
    """Datestamp formatter.

    Method formats a datetime object using the provided format
    string, and returns the formatted object as a string.

    Keyword Arguments:
        ts_to_format {datetime} -- original timestamp
                                    (default: {None})
        format_string {str}     -- desired timestamp format
                                    (default: {"%Y%m%d-%H%M%S"})

    Returns:
        {str} -- converted timestamp
    """
    if ts_to_format is None:
        ts_to_format = datetime.datetime.now()
    else:
        if is_date(ts_to_format):
            ts_to_format = parser.parse(ts_to_format)
    return ts_to_format.strftime(format_string)


def is_date(string):
    """Validate date strings.

    Method checks if a string can be parsed to a date.

    Arguments:
        string {str} -- string to validate
    """
    try:
        parser.parse(string)
        return True
    except ValueError:
        return False
