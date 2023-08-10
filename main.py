import json


def extract_names(data, filename):
    seen = set()
    if isinstance(data, dict):
        if "data" in data and isinstance(data["data"], dict) and "name" in data["data"]:
            if data["data"]["name"] not in seen:
                seen.add(data["data"]["name"])
                filename.write(data["data"]["name"] + "\n")
        for key, value in data.items():
            extract_names(value, filename)
    elif isinstance(data, list):
        for item in data:
            extract_names(item, filename)


if __name__ == "__main__":
    # load file.json into json_data
    json_data = json.load(open("file.json"))

    extract_names(json_data, open("genes.txt", "w"))





