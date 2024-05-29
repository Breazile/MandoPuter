import board
import busio
import digitalio
import displayio
from analogio import AnalogIn

SPI_SPEED = 48000000

def init():
    displayio.release_displays()
    spi = busio.SPI(clock=board.GP10, MOSI=board.GP11, MISO=board.GP12)
    while not spi.try_lock():
        pass
    spi.configure(baudrate=SPI_SPEED)
    spi.unlock()

    tft_cs    = board.GP28
    tft_dc    = board.GP14
    lcd_rst   = board.GP27
    lcd_light = board.GP15

    display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, baudrate=SPI_SPEED, reset=lcd_rst, polarity=0, phase=0)

    return display_bus, lcd_light

def configure_led(enable_leds):
    led = digitalio.DigitalInOut(board.LED)
    led.direction = digitalio.Direction.OUTPUT
    if enable_leds > 0:
       led.value = True
    else:
       led.value = False
    return led

def configure_battery_monitor():
    vbat_voltage_pin = AnalogIn(board.GP26)
    return vbat_voltage_pin
