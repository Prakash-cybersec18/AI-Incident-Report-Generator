

import json

def read_incident(file_path):

    with open(file_path, "r") as file:
        incident = json.load(file)

    return incident