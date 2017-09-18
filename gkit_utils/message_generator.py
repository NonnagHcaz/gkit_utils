from __future__ import absolute_import

from . import time_utilities as t_utils


def generate_divider(token='*', count=72, pre='\n', post='\n'):
    msg = token * count
    return generate_message(msg, 'DIVIDER', pre, post, False)


def generate_error(msg, tag='ERROR', pre='', post='', stamped=True):
    return generate_message(msg, tag, pre, post, stamped)


def generate_event(msg, tag='EVENT', pre='', post='', stamped=True):
    return generate_message(msg, tag, pre, post, stamped)


def generate_message(msg, tag='', pre='', post='', stamped=True):
    if tag:
        if tag.upper() in 'DIVIDER':
            ftag = ''
        else:
            ftag = get_tag_head(tag)
    else:
        ftag = ' '
    p_msg = str(ftag) + str(pre) + str(msg) + str(post)
    if stamped and t_utils:
        timestamp = t_utils.get_timestamp()
        p_msg = get_tag_string(timestamp) + p_msg
    return p_msg


def generate_success(msg, tag='SUCCESS', pre='', post='\n', stamped=True):
    return generate_message(msg, tag, pre, post, stamped)


def get_tag_head(msg, sep=':', pre='[', post=']'):
    return get_tag_string(msg, pre, post) + str(sep) + ' '


def get_tag_string(msg, pre='[', post=']'):
    return str(pre) + str(msg) + str(post)
