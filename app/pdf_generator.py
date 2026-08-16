from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os


def generate_pdf_report(incident, ai_report, threat_info, reputation):

    os.makedirs("reports", exist_ok=True)

    filename = f"reports/incident_{incident['incident_id']}.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    # Title
    story.append(
        Paragraph(
            "<b>AI Incident Response Report</b>",
            styles["Title"]
        )
    )

    story.append(Spacer(1, 15))

    # Incident Details
    story.append(
        Paragraph(
            "<b>Incident Details</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            f"Incident ID: {incident['incident_id']}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Type: {incident['incident_type']}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Severity: {incident['severity']}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Date: {incident['date']}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Affected User: {incident['affected_user']}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Status: {incident['status']}",
            styles["Normal"]
        )
    )

    story.append(Spacer(1, 15))

    # AI Report
    story.append(
        Paragraph(
            "<b>AI Analysis</b>",
            styles["Heading2"]
        )
    )

    for line in ai_report.split("\n"):

        if line.strip():
            story.append(
                Paragraph(
                    line,
                    styles["Normal"]
                )
            )

    # ==================================================
    # THREAT INTELLIGENCE
    # ==================================================

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "<b>Threat Intelligence</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            f"Source: {threat_info.get('source', 'Unknown')}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Country: {threat_info.get('country', 'Unknown')}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"ASN: {threat_info.get('asn', 'Unknown')}",
            styles["Normal"]
        )
    )

    # Reputation
    story.append(Spacer(1, 10))

    story.append(
        Paragraph(
            "<b>Reputation</b>",
            styles["Heading3"]
        )
    )

    reputation_data = threat_info.get("reputation", {})

    story.append(
        Paragraph(
            f"Malicious: {reputation_data.get('malicious', 0)}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Suspicious: {reputation_data.get('suspicious', 0)}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Harmless: {reputation_data.get('harmless', 0)}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Undetected: {reputation_data.get('undetected', 0)}",
            styles["Normal"]
        )
    )

    # IOC Risk
    story.append(Spacer(1, 10))

    story.append(
        Paragraph(
            f"<b>IOC Risk:</b> {reputation.get('risk', 'UNKNOWN')}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Confidence:</b> {reputation.get('confidence', 'UNKNOWN')}",
            styles["Normal"]
        )
    )

    # Build PDF
    doc.build(story)

    print(f"PDF report saved: {filename}")