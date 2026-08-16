

def analyze_incident(incident):
    severity = incident["severity"]

    if severity == "High":
        return "This incident requires immediate investigation."

    elif severity == "Medium":
        return "This incident should be investigated soon."

    else:
        return "This incident is low priority."