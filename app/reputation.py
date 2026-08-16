def get_reputation_score(threat_info):

    reputation = threat_info.get("reputation", {})

    malicious = reputation.get("malicious", 0)
    suspicious = reputation.get("suspicious", 0)

    if malicious > 10:
        risk = "CRITICAL"
    elif malicious > 5:
        risk = "HIGH"
    elif malicious > 0:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    if malicious > 0 or suspicious > 0:
        confidence = "HIGH"
    else:
        confidence = "MEDIUM"

    return {
        "risk": risk,
        "confidence": confidence
    }