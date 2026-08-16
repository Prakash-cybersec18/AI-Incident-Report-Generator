import os


def get_incident_files(folder="data"):
    files = []

    for file in os.listdir(folder):
        if file.endswith(".json"):
            files.append(os.path.join(folder, file))

    return files