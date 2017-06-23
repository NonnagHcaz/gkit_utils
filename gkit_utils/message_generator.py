from __future__ import absolute_import, print_function

try:
    from . import time_utilities as t_utils
except ValueError:
    import time_utilities as t_utils


def generate_divider(token='*', count=72, pre='\n', post='\n'):
    msg = token * count
    return generate_message(msg, '', pre, post, False)


def generate_message(msg, tag='', pre='', post='', stamped=True):
    if tag and ':' not in tag:
        tag += ': '
    p_msg = str(tag) + str(pre) + str(msg) + str(post)
    if stamped and t_utils:
        ts = t_utils.get_timestamp()
        p_msg = get_tag_head(ts) + p_msg
    return p_msg


def generate_error(msg, tag='ERROR', pre='', post='', stamped=True):
    return generate_message(msg, tag, pre, post, stamped)


def generate_event(msg, tag='EVENT', pre='', post='', stamped=True):
    return generate_message(msg, tag, pre, post, stamped)


def generate_success(msg, tag='SUCCESS', pre='', post='\n', stamped=True):
    return generate_message(msg, tag, pre, post, stamped)


def get_tag_string(tag_str, tag_open='[', tag_close=']'):
    return str(tag_open) + str(tag_str) + str(tag_close)


def get_tag_head(tag_str, tag_sep=':', tag_open='[', tag_close=']'):
    return get_tag_string(tag_str, tag_open, tag_close) + str(tag_sep) + ' '
