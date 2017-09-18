"""Message Generator.

Module provides helper methods for the print_utilities module.
"""

from __future__ import absolute_import

from . import time_utilities as t_utils


def generate_divider(token='*', count=72, pre='\n', post='\n', **kwargs):
    """Generates divider string.

    Method generates a divider string.

    Keyword Arguments:
        token {str}     -- token used to generate
                            (default: {'*'})
        count {number}  -- divider length
                            (default: {72})
        pre {str}       -- token to generate before message
                            (default: {r'\n'})
        post {str}      -- token to generate after message
                            (default: {r'\n'})
    """
    msg = token * count
    kwargs['stamped'] = False
    return _generate(msg=msg, tag='DIVIDER', pre=pre, post=post, **kwargs)


def generate_error(msg, tag='ERROR', pre='', post='', **kwargs):
    """Generate an error message.

    Method generates an error message.

    Arguments:
        msg {str}       -- message to generate

    Keyword Arguments:
        tag {str}       -- tag to denote type of message
                            (default: {'ERROR'})
        pre {str}       -- token to generate before message
                            (default: {r'\n'})
        post {str}      -- token to generate after message
                            (default: {r'\n'})
    """
    return _generate(msg=msg, tag=tag, pre=pre, post=post, **kwargs)


def generate_event(msg, tag='EVENT', pre='', post='', **kwargs):
    """Generate an event message.

    Method generates an event message.

    Arguments:
        msg {str}       -- message to generate

    Keyword Arguments:
        tag {str}       -- tag to denote type of message
                            (default: {'EVENT'})
        pre {str}       -- token to generate before message
                            (default: {r'\n'})
        post {str}      -- token to generate after message
                            (default: {r'\n'})
    """
    return _generate(msg=msg, tag=tag, pre=pre, post=post, **kwargs)


def generate_success(msg, tag='SUCCESS', pre='', post='\n', **kwargs):
    """Generate a success message.

    Method generates a success message.

    Arguments:
        msg {str}       -- message to generate

    Keyword Arguments:
        tag {str}       -- tag to denote type of message
                            (default: {'SUCCESS'})
        pre {str}       -- token to generate before message
                            (default: {r'\n'})
        post {str}      -- token to generate after message
                            (default: {r'\n'})
    """
    return _generate(msg=msg, tag=tag, pre=pre, post=post, **kwargs)


def generate_message(msg, tag='', pre='', post='', **kwargs):
    """Generate a generic message.

    Method generates a generic message.

    Arguments:
        msg {str}       -- message to generate

    Keyword Arguments:
        tag {str}       -- tag to denote type of message
                            (default: {''})
        pre {str}       -- token to generate before message
                            (default: {r'\n'})
        post {str}      -- token to generate after message
                            (default: {r'\n'})
    """
    return _generate(msg=msg, tag=tag, pre=pre, post=post, **kwargs)


def _generate(msg, tag='', pre='', post='', **kwargs):
    div = False
    if tag:
        if tag.upper() in 'DIVIDER':
            ftag = ''
            div = True
        else:
            ftag = generate_tag_head(tag)
    else:
        ftag = ' '

    if not div and 'stamped' in kwargs and kwargs['stamped'] and t_utils:
        timestamp = generate_tag_string(t_utils.get_timestamp())
    else:
        timestamp = ''

    p_msg = timestamp + str(ftag) + str(pre) + str(msg) + str(post)
    return p_msg


def generate_tag_head(msg, sep=':', pre='[', post=']'):
    """Generate a tag head string.

    Method formats a tag string as a header.

    Arguments:
        msg {str}   -- tag to format

    Keyword Arguments:
        sep {str}   -- separator token for tag and rest of message
                        (default: {':'})
        pre {str}   -- left bounding token for tag item
                        (default: {'['})
        post {str}  -- right bounding token for tag item
                        (default: {']'})
    """
    return generate_tag_string(msg, pre, post) + str(sep) + ' '


def generate_tag_string(msg, pre='[', post=']'):
    """Generate a tag string.

    Method formats a tag string.

    Arguments:
        msg {str}   -- tag to format

    Keyword Arguments:
        pre {str}   -- left bounding token for tag item
                        (default: {'['})
        post {str}  -- right bounding token for tag item
                        (default: {']'})
    """
    return str(pre) + str(msg) + str(post)
