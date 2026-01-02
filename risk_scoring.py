# risk_scoring.py

def calculate_risk(device):
    """
    Simple risk scoring based on device type and firmware
    """
    risk_score = 0

    if device["firmware"] == "outdated":
        risk_score += 50

    if device["type"] in ["Camera", "Router"]:
        risk_score += 30

    if risk_score >= 70:
        return "HIGH"
    elif risk_score >= 40:
        return "MEDIUM"
    else:
        return "LOW"


if __name__ == "__main__":
    from device_discovery import discover_devices

    devices = discover_devices()
    for d in devices:
        print(d["name"], "Risk:", calculate_risk(d))
