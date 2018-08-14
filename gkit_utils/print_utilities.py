"""Print Utilities.

Module provides methods to display messages with timestamps,
message type tagss, and dividers.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import time

# try:
#     import arcpy
# except ImportError:
#     arcpy = None

from . import message_generator as msg_gen
from . import time_utilities as t_utils


# def timeit(func=None, *args, **kwargs):
#     """Time a function.

#     Method provides ability to time (theoretically) any method.
#     """
#     out = sys.stdout
#     if 'out' in kwargs:
#         out = kwargs['out']

#     out.write('\n')
#     print_startup('PROGRAM STARTED...', **kwargs)
#     print_divider(**kwargs)
#     start_time = time.time()
#     if func is not None:
#         func(*args, **kwargs)
#     end_time = time.time()
#     print_divider(**kwargs)
#     print_message('PROGRAM ENDED.', post='\n', **kwargs)
#     elapsed = t_utils.get_elapsed(start_time, end_time)

#     secs = float(elapsed)

#     hours = secs // 3600
#     secs -= 3600 * hours

#     mins = secs // 60
#     secs -= 60 * mins

#     out.write('Elapsed:\n\t%02d:%02d:%02d\n\n\n' % (hours, mins, secs))


#######################################################################
# Print methods
#######################################################################

def _print(msg, **kwargs):
    out = sys.stdout
    if 'out' in kwargs and kwargs['out']:
        out = kwargs['out']

    msg = msg + '\n'

    # if arcpy and 'ERROR' in tag.upper():
    #     arcpy.AddError(msg)
    # elif arcpy:
    #     arcpy.AddMessage(msg)
    # else:
    out.write(msg)


def print_divider(token='*', count=72, pre='\n', post='\n', **kwargs):
    r"""print a divider.

    Method prints a divider.

    Keyword Arguments:
        token {str}     -- token used to print
                            (default: {'*'})
        count {number}  -- divider length
                            (default: {72})
        pre {str}       -- token to print before message
                            (default: {'\n'})
        post {str}      -- token to print after message
                            (default: {'\n'})
    """
    p_msg = msg_gen.generate_divider(token, count, pre, post)
    _print(p_msg, **kwargs)


def print_message(msg, tags=[''], pre='', post='', **kwargs):
    r"""print a generic message.

    Method prints a generic message.

    Arguments:
        msg {str} -- message to print

    Keyword Arguments:
        tags {str}       -- tags to denote type of message
                            (default: {''})
        pre {str}       -- token to print before message
                            (default: {'\n'})
        post {str}      -- token to print after message
                            (default: {'\n'})
    """
    p_msg = msg_gen.generate_message(msg, tags, pre, post, **kwargs)
    _print(p_msg, **kwargs)


def print_error(msg, tags=['ERROR'], pre='', post='', **kwargs):
    r"""print an error message.

    Method prints an error message.

    Arguments:
        msg {str} -- message to print

    Keyword Arguments:
        tags {str}       -- tags to denote type of message
                            (default: {'ERROR'})
        pre {str}       -- token to print before message
                            (default: {'\n'})
        post {str}      -- token to print after message
                            (default: {'\n'})
    """
    p_msg = msg_gen.generate_error(msg, tags, pre, post, **kwargs)
    _print(p_msg, **kwargs)


def print_event(msg, tags=['EVENT'], pre='', post='', **kwargs):
    r"""print an event message.

    Method prints an event message.

    Arguments:
        msg {str} -- message to print

    Keyword Arguments:
        tags {str}       -- tags to denote type of message
                            (default: {'EVENT'})
        pre {str}       -- token to print before message
                            (default: {'\n'})
        post {str}      -- token to print after message
                            (default: {'\n'})
    """
    p_msg = msg_gen.generate_event(msg, tags, pre, post, **kwargs)
    _print(p_msg, **kwargs)


def print_success(msg, tags=['SUCCESS'], pre='', post='', **kwargs):
    r"""print a success message.

    Method prints a success message.

    Arguments:
        msg {str} -- message to print

    Keyword Arguments:
        tags {str}       -- tags to denote type of message
                            (default: {'SUCCESS'})
        pre {str}       -- token to print before message
                            (default: {'\n'})
        post {str}      -- token to print after message
                            (default: {'\n'})
    """
    p_msg = msg_gen.generate_success(msg, tags, pre, post, **kwargs)
    _print(p_msg, **kwargs)


def print_startup(msg, tags=['STARTUP'], pre='', post='', **kwargs):
    r"""print a startup message.

    Method prints a startup message.

    Arguments:
        msg {str} -- message to print

    Keyword Arguments:
        tags {str}       -- tags to denote type of message
                            (default: {'SUCCESS'})
        pre {str}       -- token to print before message
                            (default: {'\n'})
        post {str}      -- token to print after message
                            (default: {'\n'})
    """
    p_msg = msg_gen.generate_startup(msg, tags, pre, post, **kwargs)
    _print(p_msg, **kwargs)
