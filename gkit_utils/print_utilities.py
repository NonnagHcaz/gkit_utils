from __future__ import absolute_import, print_function

import time

try:
    import arcpy
except ImportError:
    arcpy = None

try:
    from . import time_utilities as t_utils
    from . import message_generator as msg_gen
except ValueError:
    import time_utilities as t_utils
    import message_generator as msg_gen


def timeit(func=None, *args):
    print('\n')
    display_message('PROGRAM STARTED...', post='\n')
    display_divider()
    start_time = time.time()
    if func is not None:
        func(*args)
    end_time = time.time()
    display_divider()
    display_message('PROGRAM ENDED.', post='\n')
    print(
        'Elapsed:\n\t{} s\n\n\n'.format(
            t_utils.elapsed(start_time, end_time)
        )
    )


def _display(msg, tag='', cli=True):
    if arcpy and 'ERROR' in tag.upper():
        arcpy.AddError(msg)
    elif arcpy:
        arcpy.AddMessage(msg)
    elif cli:
        print(msg)


def display_divider(token='*', count=72, pre='\n', post='\n', cli=True):
    p_msg = msg_gen.generate_divider(token, count, pre, post)
    _display(p_msg, '', cli)


def display_message(msg, tag='', pre='', post='', cli=True, stamped=True):
    p_msg = msg_gen.generate_message(msg, tag, pre, post, stamped)
    _display(p_msg, tag, cli)


def display_error(msg, tag='ERROR', pre='', post='', cli=True, stamped=True):
    p_msg = msg_gen.generate_error(msg, tag, pre, post, stamped)
    _display(p_msg, tag, cli)


def display_event(msg, tag='EVENT', pre='', post='', cli=True, stamped=True):
    p_msg = msg_gen.generate_event(msg, tag, pre, post, stamped)
    _display(p_msg, tag, cli)


def display_success(
    msg, tag='SUCCESS', pre='', post='\n', cli=True, stamped=True
):
    p_msg = msg_gen.generate_success(msg, tag, pre, post, stamped)
    _display(p_msg, tag, cli)
