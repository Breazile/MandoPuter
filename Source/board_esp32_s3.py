import board
import busio
import digitalio
import displayio
import neopixel
from adafruit_st7789 import ST7789
from adafruit_bitmap_font import bitmap_font
from adafruit_lc709203f import LC709203F

SPI_SPEED = 48000000

def init():
    displayio.release_displays()
    spi = board.SPI()
    while not spi.try_lock():
        pass
    spi.configure(baudrate=SPI_SPEED)
    spi.unlock()

    tft_cs    = board.D6
    tft_dc    = board.D9
    lcd_rst   = board.D5
    lcd_light = board.D10

    display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, baudrate=SPI_SPEED, reset=lcd_rst, polarity=0, phase=0)

    return display_bus, lcd_light

def configure_led(enable_leds):
    led_pwr = digitalio.DigitalInOut(board.NEOPIXEL_POWER)
    led_pwr.direction = digitalio.Direction.OUTPUT
    led = neopixel.NeoPixel(board.NEOPIXEL, 1)
    if enable_leds > 0:
       led_pwr.value = True
    else:
       led_pwr.value = False
    return led

def configure_battery_monitor():
    i2c = board.I2C()
    sensor = LC709203F(i2c)
    sensor.PackSize = 500
    return sensor
