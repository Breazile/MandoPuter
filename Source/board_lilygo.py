import board
import busio
import displayio
import digitalio
from analogio import AnalogIn
from adafruit_st7789 import ST7789
from adafruit_bitmap_font import bitmap_font

SPI_SPEED = 48000000

def initialize_display():
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
    display = ST7789(display_bus, rotation=270, width=240, height=135, rowstart=40, colstart=53, auto_refresh=False, backlight_pin=lcd_light, brightness=0)
    font = bitmap_font.load_font("mandalor135.bdf")
    offset = 12

    return display, font, offset

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
