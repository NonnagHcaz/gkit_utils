"""print_utilities.py

Module provides methods to display messages with timestamps, message type tags,
and dividers.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import time

try:
    import arcpy
except ImportError:
    arcpy = None

from . import message_generator as msg_gen
from . import time_utilities as t_utils


def timeit(func=None, *args, **kwargs):
    out = sys.stdout
    if 'out' in kwargs:
        out = kwargs['out']

    out.write('\n')
    display_message('PROGRAM STARTED...', post='\n', out=out)
    display_divider(out=out)
    start_time = time.time()
    if func is not None:
        func(*args)
    end_time = time.time()
    display_divider(out=out)
    display_message('PROGRAM ENDED.', post='\n', out=out)
    elapsed = t_utils.elapsed(start_time, end_time)

    secs = float(elapsed)

    hours = secs // 3600
    secs -= 3600 * hours

    mins = secs // 60
    secs -= 60 * mins

    out.write('Elapsed:\n\t%02d:%02d:%02d\n\n\n' % (hours, mins, secs))


def _display(msg, tag='', cli=True, out=sys.stdout):
    if arcpy and 'ERROR' in tag.upper():
        arcpy.AddError(msg)
    elif arcpy:
        arcpy.AddMessage(msg)
    elif cli:
        out.write(msg)


def display_divider(token='*',
                    count=72,
                    pre='\n',
                    post='\n',
                    cli=True,
                    out=sys.stdout):
    p_msg = msg_gen.generate_divider(token, count, pre, post)
    _display(p_msg, '', cli, out)


def display_message(msg,
                    tag='',
                    pre='',
                    post='',
                    cli=True,
                    stamped=True,
                    out=sys.stdout):
    p_msg = msg_gen.generate_message(msg, tag, pre, post, stamped)
    _display(p_msg, tag, cli, out)


def display_error(msg,
                  tag='ERROR',
                  pre='',
                  post='',
                  cli=True,
                  stamped=True,
                  out=sys.stdout):
    p_msg = msg_gen.generate_error(msg, tag, pre, post, stamped)
    _display(p_msg, tag, cli, out)


def display_event(msg,
                  tag='EVENT',
                  pre='',
                  post='',
                  cli=True,
                  stamped=True,
                  out=sys.stdout):
    p_msg = msg_gen.generate_event(msg, tag, pre, post, stamped)
    _display(p_msg, tag, cli, out)


def display_success(msg,
                    tag='SUCCESS',
                    pre='',
                    post='\n',
                    cli=True,
                    stamped=True,
                    out=sys.stdout):
    p_msg = msg_gen.generate_success(msg, tag, pre, post, stamped)
    _display(p_msg, tag, cli, out)
