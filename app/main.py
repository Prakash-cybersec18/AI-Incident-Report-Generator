from app.parser import read_incident
from app.analyzer import analyze_incident
from app.ioc import extract_iocs
from app.ai_engine import generate_text
from app.report_generator import generate_html_report
from app.pdf_generator import generate_pdf_report
from app.file_loader import get_incident_files
from app.mitre_mapper import get_mitre
from app.threat_intel import enrich_iocs
from app.logger import logger
from app.csv_report import save_csv_summary
from app.reputation import get_reputation_score
from app.progress import show_progress, show_overall_progress

incident_summary = []
files = get_incident_files()
total_stages = 9

total_incidents = len(files)
completed_incidents = 0

for file in files:
    completed_stages = 0
    try:

     print("=" * 60)
     print(f"Processing: {file}")

     logger.info(f"Processing incident file: {file}")
     print("=" * 60)

     incident = read_incident(file)

     show_progress("Parsing incident", 100)

     completed_stages += 1
     show_overall_progress(completed_stages, total_stages, incident["incident_id"])

     analysis = analyze_incident(incident)

     show_progress("Analyzing incident", 100)

     completed_stages += 1
     show_overall_progress(completed_stages, total_stages, incident["incident_id"])

     iocs = extract_iocs(incident)

     show_progress("Extracting IOCs", 100)

     completed_stages += 1
     show_overall_progress(completed_stages, total_stages, incident["incident_id"])

     threat_info = enrich_iocs(iocs)

     show_progress("Threat Intelligence", 100)

     completed_stages += 1
     show_overall_progress(completed_stages, total_stages, incident["incident_id"])

     reputation = get_reputation_score(threat_info)

     show_progress("IOC Reputation", 100)

     completed_stages += 1
     show_overall_progress(completed_stages, total_stages, incident["incident_id"])

     print("\n===== IOC REPUTATION =====")
     print(reputation)

     print("\n===== THREAT INTELLIGENCE =====")
     print(threat_info)

     mitre = get_mitre(incident["incident_type"])

     show_progress("MITRE ATT&CK Mapping", 100)

     completed_stages += 1
     show_overall_progress(completed_stages, total_stages, incident["incident_id"])

     incident_summary.append({
    "incident_id": incident["incident_id"],
    "incident_type": incident["incident_type"],
    "severity": incident["severity"],
    "mitre_attack": mitre,
    "status": incident["status"],
    "ioc_reputation": reputation,
    "threat_intelligence": threat_info
     })

     logger.info("Completed successfully")
    except Exception as e:

        print(f"Error processing {file}: {e}")

        logger.error(f"Error processing {file}: {e}")

        continue
    incident_for_ai = {
        "incident_id": incident["incident_id"],
        "incident_type": incident["incident_type"],
        "severity": incident["severity"],
        "analysis": analysis,
        "iocs": iocs,
        "mitre_attack": mitre,
        "description": incident["description"],
        "threat_intelligence": threat_info
     }
    prompt = f"""
    You are an experienced SOC Level-2 Incident Response Analyst.

    Generate a professional cybersecurity incident report.

    Incident Data:
    {incident_for_ai}

    The report MUST contain the following sections:

    1. Executive Summary
    2. Incident Impact
    3. Indicators of Compromise (IOCs)
    4. Threat Intelligence
    5. MITRE ATT&CK Mapping
    6. Containment Recommendations
    7. Remediation Recommendations
    8. Risk Assessment

    Threat Intelligence:
    Use ONLY the supplied VirusTotal information.

    Include:
    - Source
    - Country
    - ASN
    - Malicious count
    - Suspicious count
    - Harmless count
    - Undetected count

    Do NOT invent threat intelligence.

    MITRE:
    Use ONLY the supplied MITRE ATT&CK technique.

    Do NOT invent another MITRE technique.

    Use professional SOC terminology.

    Keep the report between 300 and 400 words.
    """

    response = generate_text(prompt)
    show_progress("AI Analysis", 100)
    completed_stages += 1
    show_overall_progress(
    completed_stages,
    total_stages,
    incident["incident_id"]
 )
    generate_html_report(
    incident,
    response,
    threat_info,
    reputation
     )

    show_progress("HTML Report", 100)
    completed_stages += 1
    show_overall_progress(completed_stages, total_stages, incident["incident_id"])

    logger.info(f"HTML report generated for {incident['incident_id']}")

    generate_pdf_report(
    incident,
    response,
    threat_info,
    reputation
     )

    show_progress("PDF Report", 100)
    completed_stages += 1
    show_overall_progress(completed_stages, total_stages, incident["incident_id"])

    logger.info(f"PDF report generated for {incident['incident_id']}")

    print(f"Completed: {incident['incident_id']}")
    logger.info(f"Completed processing {incident['incident_id']}")

    completed_incidents += 1

    batch_percent = int(
            (completed_incidents / total_incidents) * 100
        )

    print("\n===== BATCH PROGRESS =====")
    show_progress("Overall Batch", batch_percent)

    print(
            f"{completed_incidents} / {total_incidents} incidents completed"
        )

save_csv_summary(incident_summary)