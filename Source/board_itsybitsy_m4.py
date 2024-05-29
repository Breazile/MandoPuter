import board
import busio
import digitalio
import displayio
from analogio import AnalogIn
from adafruit_st7789 import ST7789
from adafruit_bitmap_font import bitmap_font
import adafruit_dotstar as dotstar

SPI_SPEED = 48000000

def init():
    displayio.release_displays()
    spi = board.SPI()
    while not spi.try_lock():
        pass
    spi.configure(baudrate=SPI_SPEED)
    spi.unlock()

    tft_cs    = board.D2
    tft_dc    = board.D3
    lcd_rst   = board.D4
    lcd_light = board.D10

    display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, baudrate=SPI_SPEED, reset=lcd_rst, polarity=0, phase=0)

    return display_bus, lcd_light

def configure_led(enable_leds):
    led = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
    if enable_leds > 0:
       led.brightness = 0
    return led

def configure_battery_monitor():
    vbat_voltage_pin = AnalogIn(board.A1)
    return vbat_voltage_pin
