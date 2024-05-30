import time
import board
import alarm

last_activity_time = None

def init(button_pins, timeout_hours=1):
    global last_activity_time
    last_activity_time = time.monotonic()

    if not button_pins:
        raise RuntimeError("No button pins provided for wakeup")

    return button_pins

def deepsleep(button_pins):
    # Create PinAlarm objects for each button pin
    pin_alarms = [alarm.pin.PinAlarm(pin=pin, value=False, pull=True) for pin in button_pins]

    # Go to deep sleep until one of the alarms is triggered
    alarm.exit_and_deep_sleep_until_alarms(*pin_alarms)

def keep_awake():
    global last_activity_time
    last_activity_time = time.monotonic()

def check_sleep(button_pins, timeout_hours=1):
    global last_activity_time
    if last_activity_time is None:
        raise RuntimeError("Sleep module not initialized. Call init() first.")
    
    current_time = time.monotonic()
    timeout_seconds = timeout_hours * 3600

    if current_time - last_activity_time >= timeout_seconds:
        deepsleep(button_pins)
