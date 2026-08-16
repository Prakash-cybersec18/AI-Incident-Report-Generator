MITRE_MAPPING = {
    "Phishing Attack": {
        "id": "T1566",
        "name": "Phishing"
    },
    "Malware Infection": {
        "id": "T1204",
        "name": "User Execution"
    },
    "Brute Force Attack": {
        "id": "T1110",
        "name": "Brute Force"
    },
    "Ransomware": {
        "id": "T1486",
        "name": "Data Encrypted for Impact"
    },
    "Privilege Escalation": {
        "id": "T1068",
        "name": "Exploitation for Privilege Escalation"
    }
}


def get_mitre(incident_type):
    return MITRE_MAPPING.get(
        incident_type,
        {
            "id": "Unknown",
            "name": "Unknown Technique"
        }
    )