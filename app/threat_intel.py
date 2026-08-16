import requests

from app.config import VIRUSTOTAL_API_KEY


headers = {
    "x-apikey": VIRUSTOTAL_API_KEY
}


def enrich_iocs(iocs):

    ip = iocs["ip_address"]

    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"

    try:

        response = requests.get(url, headers=headers, timeout=20)

        if response.status_code == 200:

            data = response.json()["data"]["attributes"]

            stats = data["last_analysis_stats"]

            return {
                "source": "VirusTotal",
                "reputation": stats,
                "country": data.get("country", "Unknown"),
                "asn": data.get("asn", "Unknown")
            }

        return {
            "source": "VirusTotal",
            "error": f"HTTP {response.status_code}"
        }

    except Exception as e:

        return {
            "source": "VirusTotal",
            "error": str(e)
        }