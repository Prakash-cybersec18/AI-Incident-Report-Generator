import csv
import os


def save_csv_summary(incidents):

    os.makedirs("reports", exist_ok=True)

    filename = "reports/incident_summary.csv"

    with open(filename, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Incident ID",
            "Incident Type",
            "Severity",
            "MITRE ATT&CK",
            "Status",
            "IOC Risk",
            "Confidence",
            "Threat Intel Source",
            "Country",
            "ASN",
            "Malicious",
            "Suspicious",
            "Harmless",
            "Undetected"
        ])

        for incident in incidents:

            threat_info = incident.get("threat_intelligence", {})

            reputation = threat_info.get("reputation", {})

            ioc_reputation = incident.get("ioc_reputation", {})

            writer.writerow([
                incident.get("incident_id"),
                incident.get("incident_type"),
                incident.get("severity"),
                incident.get("mitre_attack"),
                incident.get("status"),

                ioc_reputation.get("risk", "UNKNOWN"),
                ioc_reputation.get("confidence", "UNKNOWN"),

                threat_info.get("source", "Unknown"),
                threat_info.get("country", "Unknown"),
                threat_info.get("asn", "Unknown"),

                reputation.get("malicious", 0),
                reputation.get("suspicious", 0),
                reputation.get("harmless", 0),
                reputation.get("undetected", 0)
            ])

    print(f"\nCSV Summary saved: {filename}")