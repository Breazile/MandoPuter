import board
import busio
import digitalio
import displayio
from analogio import AnalogIn
from adafruit_st7735r import ST7735R
from adafruit_bitmap_font import bitmap_font

SPI_SPEED = 48000000

def initialize_display():
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
    display = ST7735R(display_bus, rotation=270, width=160, height=80, colstart=24, bgr=True, auto_refresh=False, backlight_pin=lcd_light, brightness=0)
    font = bitmap_font.load_font("mandalor76.bdf")
    offset = 8

    return display, font, offset

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
