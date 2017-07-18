"""
    Author: Zachary Gannon
    Module: config_reader.py
"""

from __future__ import absolute_import, division, print_function

import warnings

try:
    # Python 2
    from ConfigParser import ConfigParser
except ImportError:
    # Python 3
    from configparser import ConfigParser


class ConfigReader():
    """Summary
        Wrapper for Python's ConfigParser module.

        See link for ini file configuration:
            https://wiki.python.org/moin/ConfigParserExamples
    """

    def __init__(self, *args, **kwargs):
        self.read_config = read_config
        self.read_section_map = read_section_map


def read_config(filepath, headings=None, section=0):
    """Summary
        Method returns dictionary of contents under the specified
        section heading.
    Args:
        section (Stirng): name of section to read contents of

    Returns:
        Dictionary: mapping of keys and values for the specified section
                    for the specified file
    """

    return_dict = {}
    cparser = ConfigParser()

    # Initialize ConfigReader object
    cparser.read(filepath)

    # Get sections in config file
    sections = cparser.sections()

    # Get mapping of specific section
    section_map = read_section_map(cparser, sections[section])

    # Get only the values we need
    if not headings:
        headings = section_map.keys()
    for key in headings:
        try:
            return_dict[key] = section_map[key.lower()]
        except KeyError as ke:
            warnings.warn(str(ke))
            return_dict[key] = None
    return return_dict


def read_section_map(cparser, section):
    """Summary
        Method returns dictionary of contents under the specified
        section heading.
    Args:
        cparser (ConfigParser): parser object
        section (Stirng): name of section to read contents of

    Returns:
        Dictionary: mapping of keys and values for the specified section
    """

    return_dict = {}
    options = cparser.options(section)
    for option in options:
        try:
            return_dict[option] = cparser.get(section, option)
        except Exception as e:
            return_dict[option] = None
    return return_dict
