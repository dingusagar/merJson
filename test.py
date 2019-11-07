import unittest
from jsonutils.merJson import MerJson
import json

class MerJsonTest(unittest.TestCase):
    def setUp(self):
        self.merJson = MerJson


    def test_merge_2(self):

        json1 = json.loads("""{"strikers": [
                { "name": "Alexis Sanchez", "club": "Manchester United" },
                { "name": "Robin van Persie", "club": "Feyenoord" }
                ] }""")

        json2 = json.loads("""
                {"strikers": [
                { "name": "Nicolas Pepe", "club": "Arsenal" }
                ] }""")

        json_merged_string = """
        {"strikers": [
                { "name": "Alexis Sanchez", "club": "Manchester United" },
                { "name": "Robin van Persie", "club": "Feyenoord" },
                { "name": "Nicolas Pepe", "club": "Arsenal" }
                ] }
        """

        result_string = json.dumps(self.merJson.merge(self.merJson, json2, json1))
        json_merged_string = json.dumps(json.loads(json_merged_string)) # removing whitespaces
        assert json_merged_string == result_string



    def test_merge_2_multiple_keys(self):

        json1 = json.loads("""{"strikers": [
                { "name": "Alexis Sanchez", "club": "Manchester United" },
                { "name": "Robin van Persie", "club": "Feyenoord" }
                ] }""")

        json2 = json.loads("""
                {"employees": [
                { "name": "Nicolas Pepe", "age": "22" }
                ] }""")

        json_merged_string = """
        {"strikers": [
                { "name": "Alexis Sanchez", "club": "Manchester United" },
                { "name": "Robin van Persie", "club": "Feyenoord" }
                ],"employees": [
                { "name": "Nicolas Pepe", "age": "22" }
                ]  }
        """

        result_string = json.dumps(self.merJson.merge(self.merJson, json2, json1))
        json_merged_string = json.dumps(json.loads(json_merged_string)) # removing whitespaces
        assert json_merged_string == result_string






if __name__ == '__main__':
    unittest.main()