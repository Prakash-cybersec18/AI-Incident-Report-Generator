MITRE_MAPPING = {
    "Phishing Attack": {
        "technique": "T1566",
        "name": "Phishing"
    },

    "Malware": {
        "technique": "T1204",
        "name": "User Execution"
    },

    "Ransomware": {
        "technique": "T1486",
        "name": "Data Encrypted for Impact"
    }
}


def get_mitre(incident_type):
    return MITRE_MAPPING.get(
        incident_type,
        {
            "technique": "Unknown",
            "name": "Unknown"
        }
    )