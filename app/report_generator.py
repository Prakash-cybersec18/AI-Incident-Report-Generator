import os


def generate_html_report(incident, ai_report, threat_info, reputation):

    filename = f"reports/incident_{incident['incident_id']}.html"

    os.makedirs("reports", exist_ok=True)

    html = f"""
<!DOCTYPE html>

<html>
<head>

<meta charset="UTF-8">

<title>Incident Report</title>

<style>

body {{
    font-family: Arial, Helvetica, sans-serif;
    background:#f4f6f9;
    margin:40px;
}}

.container {{
    background:white;
    padding:30px;
    border-radius:10px;
    box-shadow:0 0 10px rgba(0,0,0,.15);
}}

h1 {{
    color:#003366;
}}

table {{
    width:100%;
    border-collapse:collapse;
    margin-bottom:30px;
}}

th {{
    background:#003366;
    color:white;
    padding:10px;
}}

td {{
    border:1px solid #ddd;
    padding:10px;
}}

.section {{
    margin-top:30px;
}}

.ai {{
    background:#f8f8f8;
    border-left:5px solid #003366;
    padding:20px;
    white-space:pre-wrap;
}}

.footer {{
    margin-top:40px;
    text-align:center;
    color:gray;
    font-size:13px;
}}

.high {{
    color:red;
    font-weight:bold;
}}

.medium {{
    color:orange;
    font-weight:bold;
}}

.low {{
    color:green;
    font-weight:bold;
}}

</style>

</head>

<body>

<div class="container">

<h1>AI Incident Response Report</h1>

<div class="section">

<h2>Incident Details</h2>

<table>

<tr>
<th>Field</th>
<th>Value</th>
</tr>

<tr>
<td>Incident ID</td>
<td>{incident["incident_id"]}</td>
</tr>

<tr>
<td>Incident Type</td>
<td>{incident["incident_type"]}</td>
</tr>

<tr>
<td>Severity</td>
<td class="{incident["severity"].lower()}">{incident["severity"]}</td>
</tr>

<tr>
<td>Date</td>
<td>{incident["date"]}</td>
</tr>

<tr>
<td>Affected User</td>
<td>{incident["affected_user"]}</td>
</tr>

<tr>
<td>Status</td>
<td>{incident["status"]}</td>
</tr>

</table>

</div>

<div class="section">

<h2>AI Analysis</h2>

<div class="section">

<h2>Threat Intelligence</h2>

<table>

<tr>
<td><strong>Source</strong></td>
<td>{threat_info.get("source", "Unknown")}</td>
</tr>

<tr>
<td><strong>Country</strong></td>
<td>{threat_info.get("country", "Unknown")}</td>
</tr>

<tr>
<td><strong>ASN</strong></td>
<td>{threat_info.get("asn", "Unknown")}</td>
</tr>

</table>

<h3>Reputation</h3>

<table>

<tr>
<td>Malicious</td>
<td>{threat_info.get("reputation", {}).get("malicious", 0)}</td>
</tr>

<tr>
<td>Suspicious</td>
<td>{threat_info.get("reputation", {}).get("suspicious", 0)}</td>
</tr>

<tr>
<td>Harmless</td>
<td>{threat_info.get("reputation", {}).get("harmless", 0)}</td>
</tr>

<tr>
<td>Undetected</td>
<td>{threat_info.get("reputation", {}).get("undetected", 0)}</td>
</tr>

</table>

<h3>IOC Risk Assessment</h3>

<p>
<strong>Risk:</strong> {reputation.get("risk", "UNKNOWN")}
</p>

<p>
<strong>Confidence:</strong> {reputation.get("confidence", "UNKNOWN")}
</p>

</div>

<div class="ai">

{ai_report}

</div>

</div>

<div class="footer">

Generated automatically by AI Incident Report Generator

</div>

</div>

</body>

</html>

"""

    with open(filename, "w", encoding="utf-8") as file:
        file.write(html)

    print(f"\nHTML report saved: {filename}")