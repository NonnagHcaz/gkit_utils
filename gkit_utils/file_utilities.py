"""File Utilities.

Module provides wrapper methods to standard read/write methods for CSV,
JSON, INI (config), and TXT files.
"""

from __future__ import absolute_import
from __future__ import print_function
import csv
import errno
import fileinput
import json
import os
import warnings
from collections import OrderedDict

from six.moves.configparser import ConfigParser


########################################################################
# Public general file util methods
########################################################################


def mkdir_p(path):
    """Recursively make directories.

    Method emulates the Unix mkdir -p.

    Arguments:
        path {str} -- Path to make directory(ies) to.
    """
    try:
        os.makedirs(path)
    except OSError as err_msg:  # Python >2.5
        if err_msg.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


########################################################################
# Read methods
########################################################################


def read(file_path, **kwargs):
    """Read a file.

    Wraps read_file() to provide a standard method signature.

    Arguments:
        file_path {str} -- path of file to read
    """
    return read_file(file_path, **kwargs)


def read_file(file_path, **kwargs):
    """Read a file.

    Wraps read_json() and read_csv() to read files and provides file type
    auto-detect.

    Arguments:
        file_path {str} -- path of file to read
    """
    file_ext = os.path.splitext(file_path.upper())[1]

    if 'JSON' in file_ext:
        return read_json(file_path)
    elif 'CSV' in file_ext:
        return read_csv(file_path, **kwargs)
    else:
        with open(file_path) as file_pointer:
            return file_pointer.read()


def read_json(file_path, encoding='UTF-8', ordered=True):
    """Read a JSON file.

    Wraps the json.load() method.

    Arguments:
        file_path {str} -- path of file to read

    Keyword Arguments:
        encoding {str}  -- encoding to read the file with
                            (default: {'UTF-8'})
        ordered {bool}  -- flag to return the file contents in an OrderedDict
                            (default: {True})
    """
    kwargs = {}
    return_dict = {}
    try:
        kwargs['encoding'] = encoding
        if ordered:
            kwargs['object_pairs_hook'] = OrderedDict
        with open(file_path, 'r') as file_pointer:
            return_dict = json.load(file_pointer, **kwargs)
    except (IOError, ValueError) as err_msg:
        warnings.warn(str(err_msg))
    return return_dict


def read_csv(file_path, delimiter=',', headings=False, **kwargs):
    """Read a CSV file.

    Emulates csv.DictReader().read() functionality.
    Probably better to use DictReader/DictWriter than these CSV methods.

    Arguments:
        file_path {[type]} -- [description]

    Keyword Arguments:
        delimiter {str} -- [description] (default: {','})
        headings {bool} -- [description] (default: {False})
    """
    # [{'r0c1': 'r1c1', 'r0c2': 'r1c2', ... , 'r0cn': 'r1cn'}]

    return_list = []
    try:
        with open(file_path, 'r') as file_pointer:

            row = 0
            heads = []
            if 'heads_list' in kwargs:
                heads = kwargs['heads_list']

            for line_in in file_pointer:
                entry_dict = {}
                line = line_in.strip().split(delimiter)
                if len(line) > 0:
                    if row <= 0 and headings and not heads:
                        heads = line
                    else:
                        col = 0
                        for entry in line:
                            if heads:
                                head = heads[col]
                            else:
                                head = col
                            entry_dict[head] = entry
                            col += 1
                        return_list.append(entry_dict)
                    row += 1
    except IOError as err_msg:
        warnings.warn(str(err_msg))
    return return_list


def read_config(file_path, section):
    """Read an INI file.

    [description]

    Arguments:
        file_path {[type]} -- [description]

    Keyword Arguments:
        headings {[type]} -- [description] (default: {None})
        section {number} -- [description] (default: {0})
    """
    return_dict = {}
    cparser = ConfigParser()

    # Initialize ConfigReader object
    cparser.read(file_path)

    # Get mapping of specific section
    section_map = read_section_map(cparser, section)

    # Get only the values we need
    headings = list(section_map.keys())

    for key in headings:
        try:
            return_dict[key] = section_map[key.lower()]
        except KeyError as err_msg:
            warnings.warn(str(err_msg))
            return_dict[key] = None
    return return_dict


def read_section_map(cparser, section):
    """Read a section of a ConfigReader object.

    [description]

    Arguments:
        cparser {[type]} -- [description]
        section {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    return_dict = {}
    options = cparser.options(section)
    for option in options:
        try:
            return_dict[option] = cparser.get(section, option)
        except ConfigParser.NoSectionError:
            return_dict[option] = None
    return return_dict


########################################################################
# Write methods
########################################################################


def write(file_path, data, mode='w', **kwargs):
    """Write to a file.

    [description]

    Arguments:
        file_path {[type]} -- [description]
        data {[type]} -- [description]
        **kwargs {[type]} -- [description]

    Keyword Arguments:
        mode {str} -- [description] (default: {'w'})
    """
    write_file(file_path, data, mode, **kwargs)


def write_file(file_path, data, mode='w', **kwargs):
    """Write to a file.

    [description]

    Arguments:
        file_path {[type]} -- [description]
        data {[type]} -- [description]
        **kwargs {[type]} -- [description]

    Keyword Arguments:
        mode {str} -- [description] (default: {'w'})
    """
    file_ext = os.path.splitext(file_path.upper())[1]
    if 'JSON' in file_ext:
        write_json(file_path, data, mode=mode, **kwargs)
    elif 'CSV' in file_ext:
        write_csv(file_path, data, mode=mode, **kwargs)
    else:
        with open(file_path, mode=mode) as file_pointer:
            file_pointer.write(data)


def write_json(file_path, data, mode='w', **kwargs):
    """Write to a JSON file.

    [description]

    Arguments:
        file_path {[type]} -- [description]
        data {[type]} -- [description]
        **kwargs {[type]} -- [description]

    Keyword Arguments:
        mode {str} -- [description] (default: {'w'})
    """
    with open(file_path, mode) as file_pointer:
        json.dump(data, file_pointer, **kwargs)


def write_csv(file_path, data, delimiter=',', mode='w'):
    """Write to a CSV file.

    [description]

    Arguments:
        file_path {[type]} -- [description]
        data {[type]} -- [description]

    Keyword Arguments:
        delimiter {str} -- [description] (default: {','})
        mode {str} -- [description] (default: {'w'})
    """
    try:
        file_pointer = open(file_path, mode, newline='')
    except TypeError:
        if 'b' not in mode:
            mode += 'b'
        file_pointer = open(file_path, mode)

    writer = csv.DictWriter(
        file_pointer, fieldnames=list(data[0].keys()), delimiter=delimiter)

    writer.writeheader()
    writer.writerows(data)
    del writer
    file_pointer.close()


########################################################################
# Data format methods
########################################################################

# def format_list_of_dicts_from_file(in_dict_list, base_path):
#     base_dict = read_json(base_path)
#     return format_list_of_dicts(in_dict_list, base_dict)

# def format_dictionary_from_file(in_dict, base_path):
#     base_dict = read_json(base_path)
#     return format_dictionary(in_dict, base_dict)

# def format_dictionary(in_dict, base_dict):
#     return_dict = {}

#     for key, val in base_dict.items():
#         if '$' in key:
#             key = key[1:]
#             new_key = in_dict[key]
#         else:
#             new_key = key

#         if isinstance(val, dict):
#             new_val = format_dictionary(in_dict[key], val)
#         return_dict[new_key] = new_val
#     return return_dict

# def format_list_of_dicts(in_dict_list, base_dict):
#     return_list = []

#     for in_dict in in_dict_list:
#         return_list.append(format_dictionary(in_dict, base_dict))
#     return return_list

# def batch_prepend_headings(basedir, head_list, delimiter=','):
#     for base_file in os.listdir(basedir):
#         prepend_headings(
#             os.path.join(basedir, base_file), head_list, delimiter)

# def prepend_headings(base_file, head_list=None, delimiter=','):
#     if head_list:
#         headers = delimiter.join([str(head) for head in head_list]).strip()
#     else:
#         headers = ''
#     if os.path.exists(base_file):
#         for line in fileinput.input(files=[base_file], inplace=True):
#             if fileinput.isfirstline() and headers not in line:
#                 print(headers)
#             print(line[:-1])


def convert_delimiter_inline(file_path, old_delimiter=',', new_delimiter='|'):
    """Convert file delimiter.

    Method converts all delimiter tokens in a file and makes changes to the
    file itself.

    Arguments:
        file_path {str}     -- path of file to convert delimiters

    Keyword Arguments:
        old_delimiter {str} -- original delimiter
                                (default: {','})
        new_delimiter {str} -- desired delimiter
                                (default: {'|'})
    """
    if os.path.exists(file_path):
        for line in fileinput.input(files=[file_path], inplace=True):
            print((line[:-1].replace(old_delimiter, new_delimiter)))


########################################################################
# Conversion methods
########################################################################

# DOES NOT WORK

# def convert_file(in_path, out_path, out_write=True, **kwargs):
#     in_ext = os.path.splitext(in_path)[1].upper()
#     # out_ext = os.path.splitext(out_path)[1].upper()

#     if 'in_delimiter' in kwargs:
#         in_delim = kwargs['in_delimiter']
#     else:
#         in_delim = ','

#     # if 'out_delimiter' in kwargs:
#     #     out_delim = kwargs['out_delimiter']
#     # else:
#     #     out_delim = ','

#     if 'in_heads_list' in kwargs:
#         in_heads_list = kwargs['in_heads_list']
#         in_has_heads = True
#     else:
#         in_heads_list = None
#         in_has_heads = False

#     in_data = None
#     out_data = None

#     if 'CSV' in in_ext or 'TXT' in in_ext:
#         in_data = read_csv(in_path, in_delim, in_has_heads, **{
#             'heads_list': in_heads_list,
#         })
#     elif 'JSON' in in_ext:
#         in_data = read_json(in_path)
#     else:
#         kwargs['heads_list'] = in_heads_list
#         in_data = read_file(in_path, **kwargs)

#     if out_write and out_data:
#         write_file(out_path, out_data)
#     return out_data
