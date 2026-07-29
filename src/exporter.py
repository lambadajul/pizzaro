import json

def export(data):

    with open(
        "data/exports/schedule.json",
        "w",
        encoding="utf8"
    ) as f:

        json.dump(data, f, indent=4)
