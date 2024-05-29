import board
import busio
import displayio
import digitalio
from analogio import AnalogIn

SPI_SPEED = 48000000

def init():
    displayio.release_displays()
    spi = busio.SPI(clock=board.GP2, MOSI=board.GP3)
    while not spi.try_lock():
        pass
    spi.configure(baudrate=SPI_SPEED)
    spi.unlock()

    tft_cs    = board.GP5
    tft_dc    = board.GP1
    lcd_rst   = board.GP0
    lcd_light = board.GP4

    display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, baudrate=SPI_SPEED, reset=lcd_rst, polarity=0, phase=0)

    return display_bus, lcd_light

def configure_led(enable_leds):
    led = digitalio.DigitalInOut(board.GP25)
    led.direction = digitalio.Direction.OUTPUT
    if enable_leds > 0:
       led.value = True
    else:
       led.value = False
    return led

def configure_battery_monitor():
    vbat_voltage_pin = AnalogIn(board.GP26)
    return vbat_voltage_pin
