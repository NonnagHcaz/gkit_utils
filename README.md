Gannon Toolkit Library - Utilities (gkit_utils)
=================================

[![Travis - Linux](https://img.shields.io/travis/NonnagHcaz/gkit_utils.svg?label=Linux%20Status)](https://travis-ci.org/NonnagHcaz/gkit_utils) [![AppVeyor - Windows](https://img.shields.io/appveyor/ci/NonnagHcaz/gkit-utils.svg?label=Windows%20Status)](https://ci.appveyor.com/project/NonnagHcaz/gkit-utils)  
[![Codecov](https://img.shields.io/codecov/c/github/NonnagHcaz/gkit_utils.svg?label=Coverage)](https://codecov.io/github/NonnagHcaz/gkit_utils?branch=master) [![Code Health](https://landscape.io/github/NonnagHcaz/gkit_utils/master/landscape.svg?style=flat&label=Health)](https://landscape.io/github/NonnagHcaz/gkit_utils/master)  

Written by Zachary Gannon.   

---

DESCRIPTION:
------------

This repository is a collection of utility methods to improve or simplify common tasks like printing with timestamps and tags, reading and writing files, and emulating bash functions.   

---

MODULES:
--------

The `gkit_utils` package includes the following utilities modules:  

  - `gkit_utils.date_utilities`  
    - Provides methods to fetch datestamps and convert their formats.  
  - `gkit_utils.file_utilities`  
    - Provides wrapper methods to standard read/write methods for CSV, JSON, INI (config), and TXT files.  
  - `gkit_utils.print_utilities`  
    - Provides methods to display messages with timestamps, message type tags, and dividers.  
    - Also provides a method to time (theoretically) any method.  
  - `gkit_utils.time_utilities`  
    - Provides methods to fetch timestamps and convert their formats.  
    - Also provides a method to fetch the elapsed time between two timestamps.   

Additionally, the `gkit_utils` package contains the following helper modules:  

  - `gkit_utils.message_generator`  
    - Essentially the backbone of the `print_utilities` module.  
    - This module creates the tagged messages, whereas `print_utilities` displays them.  

---

KNOWN BUGS:
-----------

  - `gkit_utils.file_utilities.prepend_headings()`:
    - Breaks integrity of order of columns per row in Python < 3.6.

  - `gkit_utils.file_utilities.convert_file()`:
    - Does not work. Not sure if salvageable in current state.

---

TODO:
-----

  - Write docs

