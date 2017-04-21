# csv2json [![Build Status](https://travis-ci.org/amFvcg/csv2json-py.svg?branch=master)](https://travis-ci.org/amFvcg/csv_parser)


Application that converts given csv files into JSON arrays of objects.

In simplest form it reads a CSV header and creates a list of objects with string-typed values.

There's also an option to provide a mapping of columns to proper types.


## Features 

1. [Default run should result in all the fields being of type string or null](tests/behave/default_run.feature)

2. [Support for mapping file, describing field types used in conversion](tests/behave/mapping_file.feature)

3. [Autodeduction of mappings for list of files](tests.behave/autodeduction.feature)
