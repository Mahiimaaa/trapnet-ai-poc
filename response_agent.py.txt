# response_agent.py

def autonomous_response(device, risk_level):
    actions = []

    if risk_level == "HIGH":
        actions.append("Rate limiting applied")
        actions.append("Redirected to honeypot")
        actions.append("Device isolated")
        actions.append("Firewall rules updated")
        actions.append("User notified")

    return actions


if __name__ == "__main__":
    from device_discovery import discover_devices
    from risk_scoring import calculate_risk

    for device in discover_devices():
        risk = calculate_risk(device)
        actions = autonomous_response(device, risk)
        if actions:
            print(f"\nActions for {device['name']}:")
            for action in actions:
                print("-", action)
