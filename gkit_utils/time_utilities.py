from __future__ import absolute_import
import datetime


def get_timestamp(ts_to_format=None, format_string="%Y%m%d-%H%M%S"):
    if ts_to_format is None:
        ts_to_format = datetime.datetime.now()
    return ts_to_format.strftime(format_string)


def get_elapsed(start, end, pre='0', post='4'):
    return elapsed(start, end, pre, post)


def elapsed(start, end, pre='0', post='4'):
    # !DEPRECATED! Use get_elapsed() with same params.
    f_str = ''.join(['{', str(pre), ':.', str(post), 'f}'])
    e_str = round((end - start), int(post))
    return f_str.format(e_str)
