from __future__ import absolute_import, print_function

import os
import errno
import csv
import fileinput
import json

from collections import OrderedDict

########################################################################
# Public general file util methods
########################################################################


def mkdir_p(path):
    # Function performs cli command: mkdir -p
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


########################################################################
# Read methods
########################################################################


def read(file_path, **kwargs):
    return read_file(file_path, **kwargs)


def read_file(file_path, **kwargs):
    file_ext = os.path.splitext(file_path.upper())[1]

    if 'delimiter' in kwargs:
        delimiter = kwargs['delimiter']
    else:
        delimiter = ','

    if 'headings' in kwargs:
        headings = kwargs['headings']
    else:
        headings = False

    if 'JSON' in file_ext:
        return read_json(file_path)
    elif 'CSV' in file_ext:
        return read_csv(file_path, delimiter, headings, **kwargs)
    else:
        with open(file_path) as fp:
            return fp.read()


def read_json(file_path, encoding='UTF-8', ordered=True):
    kwargs = {}
    return_dict = {}
    if os.path.exists(file_path):
        kwargs['encoding'] = encoding
        if ordered:
            kwargs['object_pairs_hook'] = OrderedDict
        with open(file_path, 'r') as fp:
            return_dict = json.load(fp, **kwargs)
    return return_dict


def read_csv(file_path, delimiter=',', headings=False, **kwargs):
    # [{'r0c1': 'r1c1', 'r0c2': 'r1c2', ... , 'r0cn': 'r1cn'}]

    return_list = []
    with open(file_path, 'r') as fp:
        row = 0
        if 'heads_list' in kwargs:
            heads = kwargs['heads_list']
        else:
            heads = []
        # lines = fp.readlines()
        for line_in in fp:
            entry_dict = {}
            line = line_in.rstrip('\n').split(delimiter)
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
    return return_list


########################################################################
# Write methods
########################################################################


def write_file(file_path, data, mode='w'):
    with open(file_path, mode) as fp:
        file_ext = os.path.splitext(file_path.upper())[1]
        if 'JSON' in file_ext:
            json.dump(data, fp, indent=4, sort_keys=True)
        elif 'CSV' in file_ext:
            contents = ''
            if isinstance(data, dict):
                for key, vals in data.items():
                    new_line = key + ',' + ','.join(vals)
                    contents = '\n'.join([contents, new_line])
            elif isinstance(data, list):
                contents = '\n'.join(data)
            fp.write(contents)
        else:
            fp.write(data)


def write_csv(file_path, rows):
    with open(file_path, 'w') as fp:
        writer = csv.DictWriter(fp, fieldnames=rows[0].keys())
        writer.writeheader()
        for row in rows:
            stripped_row = {
                k: (v.strip() if isinstance(v, str) else v)
                for k, v in row.items()
            }
            writer.writerow(stripped_row)


########################################################################
# Data format methods
########################################################################


def get_dict_value(*key_list, **key_dict):
    for key in key_list:
        if key in key_dict:
            return key_dict[key]


def format_list_of_dicts_from_file(in_dict_list, base_path):
    base_dict = read_json(base_path)
    return format_list_of_dicts(in_dict_list, base_dict)


def format_dictionary_from_file(in_dict, base_path):
    base_dict = read_json(base_path)
    return format_dictionary(in_dict, base_dict)


def format_dictionary(in_dict, base_dict):
    return_dict = {}

    for key, val in base_dict.items():
        if '$' in key:
            key = key[1:]
            new_key = in_dict[key]
        else:
            new_key = key

        if isinstance(val, dict):
            new_val = format_dictionary(in_dict[key], val)
        return_dict[new_key] = new_val
    return return_dict


def format_list_of_dicts(in_dict_list, base_dict):
    return_list = []

    for in_dict in in_dict_list:
        return_list.append(format_dictionary(in_dict, base_dict))
    return return_list


def batch_prepend_headings(basedir, head_list, delim=','):
    for base_file in os.listdir(basedir):
        prepend_headings(os.path.join(basedir, base_file), head_list, delim)


def prepend_headings(base_file, head_list, delim=','):
    headers = delim.join(head_list)
    if os.path.exists(base_file):
        for line in fileinput.input(files=[base_file], inplace=True):
            if fileinput.isfirstline() and headers not in line:
                print(headers)


def convert_delimiter_inline(base_file, old_delimiter=',', new_delimiter='|'):
    if os.path.exists(base_file):
        for line in fileinput.input(files=[base_file], inplace=True):
            print(line[:-1].replace(old_delimiter, new_delimiter))


########################################################################
# Conversion methods
########################################################################


def convert_file(in_path, out_path, out_write=True, **kwargs):
    in_ext = os.path.splitext(in_path)[1].upper()
    # out_ext = os.path.splitext(out_path)[1].upper()

    if 'template' in kwargs:
        template = kwargs['template']
    else:
        template = None

    # if 'out_format' in kwargs:
    #     out_format = kwargs['out_format']
    # else:
    #     out_format = False

    if 'in_delimiter' in kwargs:
        in_delim = kwargs['in_delimiter']
    else:
        in_delim = ','

    # if 'out_delimiter' in kwargs:
    #     out_delim = kwargs['out_delimiter']
    # else:
    #     out_delim = ','

    if 'in_heads_list' in kwargs:
        in_heads_list = kwargs['in_heads_list']
        in_has_heads = True
    else:
        in_heads_list = None
        in_has_heads = False

    # if 'out_heads_list' in kwargs:
    #     out_heads_list = kwargs['out_heads_list']
    #     out_has_heads = True
    # else:
    #     out_heads_list = None
    #     out_has_heads = False

    in_data = None
    out_data = None

    if 'CSV' in in_ext or 'TXT' in in_ext:
        in_data = read_csv(in_path, in_delim, in_has_heads, **{
            'heads_list': in_heads_list,
        })
    elif 'JSON' in in_ext:
        in_data = read_json(in_path)
    else:
        kwargs['heads_list'] = in_heads_list
        in_data = read_file(in_path, **kwargs)

    if template and in_data:
        out_data = format_dictionary(in_data, template)
    else:
        out_data = in_data

    # if out_format:
    #     out_data = format_csp(out_data)

    if out_write and out_data:
        write_file(out_path, out_data)
    return out_data
