Feature: Support for mapping file, describing field types used in conversion
    Scenario: Conversion with mapping
        Given csv file test.csv
        """
        0,value,0 
        1,,1
        """
        And mapping file test.mapping
        """
        Id=int
        Val=string
        Present=bool
        """
        When we run csv2json --mapping=test.mapping test.csv
        Then we expect to have file test.csv.json with content
        """
        [{"Id": 0, "Val": "value", "Present": false}, {"Id": 1, "Val": "", "Present": true}]
        """
