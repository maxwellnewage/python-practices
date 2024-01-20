"""
JSON Writer
"""

import json

if __name__ == '__main__':
    # save data
    with open("resources/generated/data.json", "w") as file:
        data = {
            "Person 1": {
                "first_name": "Maxwell",
                "last_name": "Smart",
                "year": 2024,
                "money": 230.5
            }
        }

        json.dump(data, file, indent=4)

    # read data
    with open("resources/generated/data.json", "r") as file:
        data = json.load(file)
        print(data["Person 1"]["first_name"])

    # update data
    with open("resources/generated/data.json", "r") as file:
        data = json.load(file)
        data.update({
            "Person 2": {
                "first_name": "Tomas",
                "last_name": "Volt",
                "year": 2023,
                "money": 250.5
            }
        })

    # commit updated data
    with open("resources/generated/data.json", "w") as file:
        json.dump(data, file, indent=4)
