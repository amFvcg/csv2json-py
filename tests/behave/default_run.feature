Feature: Default conversion to string values
    Scenario: Conversion without parameters
        Given csv file test.csv with input
        """
        Field1,Field2,Field3
        1,value,
        """
        When we run csv2json test.csv
        Then we expect to have file test.csv.json with content
        """
        [{"Field1": "1", "Field2": "value", "Field3": ""}]
        """
