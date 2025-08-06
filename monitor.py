
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

def check_temperature_range(temperature):
    if temperature > 102 or temperature < 95:
        display_warning('Temperature critical!')
        return False
    return True

def check_pulse_rate_range(pulseRate):
    if pulseRate < 60 or pulseRate > 100:
        display_warning('Pulse Rate is out of range!')
        return False
    return True

def check_spo2_range(spo2):
    if spo2 < 90:
        display_warning('Oxygen Saturation out of range!')
        return False
    return True

def vitals_ok(temperature, pulseRate, spo2):
    checks = [check_temperature_range(temperature),check_pulse_rate_range(pulseRate),check_spo2_range(spo2)]
    return all(checks)
