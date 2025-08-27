
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

def vitals_ok(temperature, pulseRate, spo2, alert_fn=display_warning):
    vitals = {
        "temperature": temperature,
        "pulse": pulseRate,
        "spo2": spo2
    }

    all_ok = True
    for name, value in vitals.items():
        ok, message = check_vital(name, value)
        if not ok:
            all_ok = False
            if alert_fn:  # decoupled → can be mocked in tests
                alert_fn(message)
    return all_ok

