Overview
========
It's a simple application (or set of applications written in different
languages) that:

1. reads a csv file and mapping;

2. maps data from csv to JSON based on mapping file;

3. does a validation of csv data supplied:

- validates if csv lines are mappable;

- validates if column count is correct;


Requirements
============
See 'test' directory.

* *test_data* - input data;

* *test_mapping* - examplary mapping;

* *test_output* - output for 'normal' mode; first line contains exit code;
next lines is a JSON with parsed input;

* *test_validation_output* - output for 'validation' mode; first line contains
exit code; next lines (if present) list lines that failed;
