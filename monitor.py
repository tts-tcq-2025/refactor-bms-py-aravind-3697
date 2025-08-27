from time import sleep
import sys

def display_warning(message):
    print(message)
    for _ in range(6):
        print('\r* ', end='')
        sys.stdout.flush()
        sleep(1)
        print('\r *', end='')
        sys.stdout.flush()
        sleep(1)

def is_within_range(value, low, high):
    return low <= value <= high

VITAL_LIMITS = {
    "temperature": {"low": 95, "high": 102, "message": "Temperature critical!"},
    "pulse": {"low": 60, "high": 100, "message": "Pulse Rate is out of range!"},
    "spo2": {"low": 90, "high": 100, "message": "Oxygen Saturation out of range!"}
}

def check_vital(name, value):
    limits = VITAL_LIMITS[name]
    if not is_within_range(value, limits["low"], limits["high"]):
        return False, limits["message"]
    return True, None

def evaluate_vitals(vitals):
    """Return list of failed messages (empty if all good)."""
    messages = []
    for name, value in vitals.items():
        ok, message = check_vital(name, value)
        if not ok:
            messages.append(message)
    return messages

def process_alerts(messages, alert_fn):
    if alert_fn:
        for msg in messages:
            alert_fn(msg)

def vitals_ok(temperature, pulseRate, spo2, alert_fn=display_warning):
    vitals = {
        "temperature": temperature,
        "pulse": pulseRate,
        "spo2": spo2
    }
    failed_messages = evaluate_vitals(vitals)
    process_alerts(failed_messages, alert_fn)
    return len(failed_messages) == 0

