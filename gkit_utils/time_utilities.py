from __future__ import absolute_import, print_function

import datetime


def get_timestamp(ts_to_format=None, format_string="%Y%m%d-%H%M%S"):
    if ts_to_format is None:
        ts_to_format = datetime.datetime.now()
    return ts_to_format.strftime(format_string)


def elapsed(start, end, pre='0', post='4'):
    f_str = ''.join(['{', str(pre), ':.', str(post), 'f}'])
    e_str = round((end - start), int(post))
    return f_str.format(e_str)
