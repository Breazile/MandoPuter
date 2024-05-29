def get_batt_percent(batt_pin):
    batt_volts = (batt_pin.value * 3.3) / 65536 * 2
    batt_volts += 0.05
    if batt_volts > 3.80:
        return 86
    elif batt_volts > 3.65:
        return 50
    elif batt_volts > 3.40:
        return 25
    else:
        return 5
