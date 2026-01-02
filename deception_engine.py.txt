# deception_engine.py

def deploy_deception(device, risk_level):
    if risk_level == "HIGH":
        return f"{device['name']} traffic redirected to honeypot"
    return f"{device['name']} operating normally"


if __name__ == "__main__":
    from device_discovery import discover_devices
    from risk_scoring import calculate_risk

    for device in discover_devices():
        risk = calculate_risk(device)
        print(deploy_deception(device, risk))
