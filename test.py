import unittest
from jsonutils.merJson import MerJson
from unittest.mock import MagicMock
import json


class MerJson_MergeTest(unittest.TestCase):
    def setUp(self):
        self.merJson = MerJson

    def test_merge_2_json_with_same_key(self):
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
        json_merged_string = json.dumps(json.loads(json_merged_string))  # removing whitespaces
        assert json_merged_string == result_string

    def test_merge_2_json_with_multiple_keys(self):
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
        json_merged_string = json.dumps(json.loads(json_merged_string))  # removing whitespaces
        assert json_merged_string == result_string

    def test_merge_with_empty_json(self):
        json1 = json.loads("""{"strikers": [
                { "name": "Alexis Sanchez", "club": "Manchester United" },
                { "name": "Robin van Persie", "club": "Feyenoord" }
                ] }""")

        json2 = json.loads("""{}""")

        json_merged_string = json.dumps(json1)

        result_string = json.dumps(self.merJson.merge(self.merJson, json2, json1))
        json_merged_string = json.dumps(json.loads(json_merged_string))  # removing whitespaces
        assert json_merged_string == result_string

    def test_merge___non_english_chars(self):
        json1 = json.loads("""{"strikers": [
                { "name": "頁 - 設 - 是 - 煵 - 엌 - 嫠 - 쯦 - 案 - 煪 - ㍱ - 從 ", "club": "Manchester United" },
                { "name": "浤 - 搰 - ㍭ - 煤 - 洳", "club": "Feyenoord" }
                ] }""")

        json2 = json.loads("""
                {"strikers": [
                { "name": "頁Nicolas Pepe", "club": "Arsenal" }
                ] }""")

        json_merged_string = """
        {"strikers": [
                { "name": "頁 - 設 - 是 - 煵 - 엌 - 嫠 - 쯦 - 案 - 煪 - ㍱ - 從 ", "club": "Manchester United" },
                { "name": "浤 - 搰 - ㍭ - 煤 - 洳", "club": "Feyenoord" },
                { "name": "頁Nicolas Pepe", "club": "Arsenal" }
                ] }
        """

        result_string = json.dumps(self.merJson.merge(self.merJson, json2, json1))
        json_merged_string = json.dumps(json.loads(json_merged_string))  # removing whitespaces
        assert json_merged_string == result_string


# class MerJson_SizeLimitsTest(unittest.TestCase):
#     def setUp(self):
#         self.merJson = MerJson
#
#     def test_max_size_limit_is_not_exceeded(self):
#
#         self.merJson.read_json_to_dic = MagicMock(return_value=3)


if __name__ == '__main__':
    unittest.main()
