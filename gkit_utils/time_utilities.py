"""Module provides methods to fetch timestamps and convert their formats.
"""

from __future__ import absolute_import
import datetime


def get_timestamp(ts_to_format=None, format_string="%Y%m%d-%H%M%S"):
    """Method formats a datetime.datetime object using the provided format
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
    return ts_to_format.strftime(format_string)


def get_elapsed(start, end, pre='0', post='4'):
    """Method computes the difference between two datetime.datetime objects,
    and returns the difference as a string.

    Arguments:
        start {datetime}    -- start time
        end {datetime}      -- end time

    Keyword Arguments:
        pre {str}   -- leading 0's
                        (default: {'0'})
        post {str}  -- precision
                        (default: {'4'})

    Returns:
        {str} -- elapsed time
    """
    f_str = ''.join(['{', str(pre), ':.', str(post), 'f}'])
    e_str = round((end - start), int(post))
    return f_str.format(e_str)


def elapsed(start, end, pre='0', post='4'):
    # !DEPRECATED! Use get_elapsed() with same params.
    return get_elapsed(start, end, pre, post)
