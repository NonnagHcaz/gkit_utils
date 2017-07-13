"""
    Author: Zachary Gannon
    Module: db2_wrapper.py
"""

from __future__ import absolute_import, division, print_function

import ibm_db

# Class expects the following dictionary keys when passing connection args
DB_HEADS = ['DB_NAME', 'DB_HOST', 'DB_PORT', 'DB_PROT', 'DB_UID', 'DB_PWD']

# Class expects the following when using the simplified connection method.
DB_HEADS_MIN = ['DB_NAME', 'DB_UID', 'DB_PWD']


class DB2Wrapper():
    """Summary
        Class provides wrapper methods for Python's ibm_db module.

    Attributes:
        connection (ibm_db.connection): class scoped connection object
    """

    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        self.connection = None

    def setup_connection(self, db_dict):
        """Summary
            Method allows easy retrieval of a persistent (class scoped)
            connection object. Method expects dictionary with minimum keys
            defined by DB_HEADS_MIN.

        Args:
            db_dict (Dictionary): mapping of expected keys and connection
            values

        Returns:
            ibm_db.connection: connection object
        """

        # Check validity of dictionary. We could use try/except, but that won't
        # catch specific malformed keys.
        key_diffs = get_list_diff(DB_HEADS_MIN, db_dict.keys())

        if len(key_diffs) <= 0:
            # Dictionary is valid
            self.connection = ibm_db.connect("dsn=" + db_dict['DB_NAME'],
                                             db_dict['DB_UID'],
                                             db_dict['DB_PWD'])
        else:
            # Dictionary is invalid, so print missing expected keys
            print('ERROR: The following fields must be set:')
            for head in ['DB_NAME', 'DB_UID', 'DB_PWD']:
                if head not in db_dict.keys():
                    print('\t{}'.format(head))
            self.connection = None
        return self.connection

    def setup_connection_with_host(self, db_dict):
        """Summary
            Method allows easy retrieval of a persistent (class scoped)
            connection object. Method expects dictionary with keys
            defined by DB_HEADS list.
        Args:
            db_dict (Dictionary): mapping of expected keys and
            connection values

        Returns:
            ibm_db.connection: connection object
        """

        key_diffs = get_list_diff(DB_HEADS, db_dict.keys())
        if len(key_diffs) <= 0:
            # Dictionary is valid, so build connection string.
            # NOTE: The connection string is a semicolon (;) separated
            # list of the connection parameters, concatenated together
            # and passed as the first parameter to the ibm_db.connect
            # method.
            connection_string = ' '.join([
                'DATABASE={};'.format(db_dict['DB_NAME']),
                'HOSTNAME={};'.format(db_dict['DB_HOST']),
                'PORT={};'.format(db_dict['DB_PORT']),
                'PROTOCOL={};'.format(db_dict['DB_PROT']),
                'UID={};'.format(db_dict['DB_UID']),
                'PWD={};'.format(db_dict['DB_PWD'])
            ])
            self.connection = ibm_db.connect(connection_string, '', '')
        else:
            # Dictionary is invalid, fall back to simple connection
            self.connection = self.setup_connection(db_dict)
        return self.connection

    def fetch_results(self, command, connection=None):
        """Summary
            Method executes SQL queries and returns list of dictionaries
            with results

        Args:
            command (String): SQL raw string
            connection (ibm_db.connection): allows specific connection

        Returns:
            List: List of dictionaries containing {heading: record value}
        """
        return_list = []
        if connection is None:
            connection = self.connection
        stmt = ibm_db.exec_immediate(connection, command)
        result = ibm_db.fetch_assoc(stmt)
        while result:
            return_list.append(result)
            result = ibm_db.fetch_assoc(stmt)
        return return_list

    def close_connection(self, connection=None):
        """Summary
            Method closes a specific connection or the class scoped
            connection if none specified.
        Args:
            connection (ibm_db.connection, optional): connection to close

        Returns:
            boolean: Success or fail of connection closing
        """
        if connection is None:
            connection = self.connection
        return ibm_db.close(connection)

    def get_connection(self):
        """Summary
            Method returns instance of the class scoped connection object
        Returns:
            ibm_db.connection: class scoped connection object
        """
        return self.connection


def get_expected_keys():
    """Summary
        Method returns expected dictionary connection keys.
    Returns:
        Dictionary: Expected connection headings
    """
    return DB_HEADS


def get_list_diff(list1, list2):
    return list(set(list1) - set(list2))
