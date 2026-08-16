from app.threat_intel import enrich_iocs

iocs = {
    "ip_address": "8.8.8.8"
}

print(enrich_iocs(iocs))