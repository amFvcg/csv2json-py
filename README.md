# csv2json

[![Build Status](https://travis-ci.org/amFvcg/csv_parser.svg?branch=master)](https://travis-ci.org/amFvcg/csv_parser)

## Requirements

1. Default run should result in all the fields being of type string or null

>    Given csv file test.csv with input
>    """
>        Field1,Field2,Field3
>        1,value,
>    """
>    When we run csv2json test.csv
>    Then we expect to have file test.csv.json with content
>    """
>       [{"Field1": "1", "Field2": "value", "Field3": null}]
>    """
