import json


def read_test_data_from_json():
    with open("test_data.json", "r", encoding='utf-8') as all_data:
        data = json.load(all_data)
    return data
