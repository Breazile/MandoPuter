"""
MandoPuter will display text in a Mandalorian font on a tiny LCD display

File   - code.py
Author - Jon Breazile

https://github.com/Breazile/MandoPuter

Font credits to ErikStormtrooper, the bitmap fonts were created from his TrueType font
http://www.erikstormtrooper.com/mandalorian.htm
"""
import gc
import time
import alarm
import board
import busio
import pwmio
import neopixel
import digitalio
import displayio
import adafruit_dotstar as dotstar
import adafruit_imageload
from analogio import AnalogIn
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font
from adafruit_st7789 import ST7789
from adafruit_st7735r import ST7735R
from adafruit_lc709203f import LC709203F

"""
  ----------- User configurable items -----------

  This is where you can customize your display and hardware setup.
  Select either the Pre-Beskar (1.14" LCD) or Beskar (1.3" LCD) display.
  Some lines are commented out which means the line is not active.
  A commented line starts with a #


"""
# Set the display type
DISPLAY        = "Pre-Beskar"           # Adafruit 1.14" LCD display  https://www.adafruit.com/product/4383
#DISPLAY       = "Beskar"               # Adafruit 1.3" LCD display   https://www.adafruit.com/product/4313
#DISPLAY       = "1.44"                 # Adafruit 1.44" LCD display  https://www.adafruit.com/product/2088
#DISPLAY        = "0.96"                 # Adafruit 0.96" LCD display  https://www.adafruit.com/product/3533
DISP_BRIGHT    = 80                     # How bright to make the display - 0% to 100%

# Board being used
#BOARD_TYPE    = "ESP32-S3"             # ESP32-S3                  https://www.adafruit.com/product/5477
#BOARD_TYPE    = "FeatherM4"            # Feather M4 Express        https://www.adafruit.com/product/3857
#BOARD_TYPE    = "ItsyBitsyM4"          # ItsyBitsy M4 Express      https://www.adafruit.com/product/3800
#BOARD_TYPE    = "ItsyBitsyRP2040"      # ItsyBitsy RP2040          https://www.adafruit.com/product/4888
#BOARD_TYPE    = "PiPicoRP2040"         # Raspberry Pi Pico RP2040  https://www.adafruit.com/product/4864
BOARD_TYPE     = "RS2040LILYGO"         # New RS2040LILYGO board

# Name of the owner shown after startup and before the sequence starts
SHOW_NAME      = 1                      # Set to 1 to display the name, or 0 to not display a name
OWNER_NAME     = "Your Name Here"       # Name of the owner to be shown
NAME_COLOR     = 0x00FF00               # Green on black (you can chose colors here - https://www.color-hex.com/)
NAME_HOLD      = 3.0                    # How many seconds to display the name

#########################################

# Mandalorian charater sequence that is shown on the display
messages       = [ "MLM", "JBM", "SAS", "JAS", "JBM", "MLM", "SAS", "AJS", "SAS"]
# Time that each character group is shown 0.50 is 500 milliseconds, or 1/2 of a second
delays         = [  0.75,  0.75,  0.650,  0.75, 0.50,  0.84,  1.00,  0.35,  0.84]
TEXT_COLOR     = 0xFF0000               # Red on black (you can chose colors here - https://www.color-hex.com/)

#########################################

# Setting screen resolution, do not change these
if DISPLAY == "Beskar":
    RESOLUTION = 240
elif DISPLAY == "Pre-Beskar":
    RESOLUTION = 135
elif DISPLAY == "1.44":
    RESOLUTION = 128
elif DISPLAY == "0.96":
    RESOLUTION = 80
    
# Banner graphic(s) shown after the owner's name and before the sequence starts
SHOW_IMG       = 2                      # How many images to show. 0 = no images, 1 = 1 image, 2 = 2 images
IMG1           = "TheMandalorian" + str(RESOLUTION) + ".bmp"   # File name of the first 8 bit BMP graphic to be shown after each text sequence
IMG1_HOLD      = 5.00                   # How long the first image is displayed in seconds
IMG2           = "BabyYoda" + str(RESOLUTION) + ".bmp"         # File name of the second 8 bit BMP graphic to be shown after the first image
IMG2_HOLD      = 5.00                   # How long the second image is displayed in seconds

# Other settings for debugging and battery monitoring
BATTERY_SZ     = 500                    # Size of battery in mAh (only for the ESP32-S3 board)
BATTERY_MON    = 1                      # Set to 1 to enable the battery monitor, 0 to disable it
LOW_BATT_LEVEL = 10                     # Show the low battery icon when the battery goes below this percentage
ENABLE_LEDS    = 1                      # Set to 1 to turn on LEDs for debugging, set to 0 to save battery
SPI_SPEED      = 48000000               # How fast the SPI bus to the LCD operates
DEBUG_SERIAL   = 1                      # If your board has a debug port, you can read the system messages.
"""
# ---------------------------------------------------------------------------------
"""

def debug_print(text):
    if DEBUG_SERIAL:
        print(text)

def DisplayName(name, hold, color, init_tm):
    debug_print(f"Displaying name: {name}")
    if RESOLUTION == 128 or RESOLUTION == 80:
        ownerfont = bitmap_font.load_font("Alef-Bold-12.bdf")  # 18 point bitmap font
    else :
        ownerfont = bitmap_font.load_font("Alef-Bold-18.bdf")  # 18 point bitmap font
    banner_text = label.Label(ownerfont, text=name, color=color)
    banner_text.x = int(((display.width - banner_text.bounding_box[2])/2)-1)
    banner_text.y = int(((display.height - banner_text.bounding_box[3])/2)+1)
    display.show(banner_text)
    display.refresh()
    if SHOW_IMG > 0:
        time.sleep(hold)              # Display the name before the graphics
    else:
        if hold > init_tm:
            time.sleep(hold - init_tm)  # minus the initialization time if there are images
    # release memory
    del ownerfont
    del banner_text
    gc.collect()

def DisplayImage(img, hold, images, init_tm):
    debug_print(f"Displaying image: {img}")
    # Create the first image centered on the display
    try:
        bitmap, palette = adafruit_imageload.load(img, bitmap=displayio.Bitmap, palette=displayio.Palette)
    except:
        bitmap = displayio.OnDiskBitmap(img)
        palette = bitmap.pixel_shader
    x = int((display.width - bitmap.width) / 2)
    y = int((display.height - bitmap.height) / 2)
    if x < 0: x = 0
    if y < 0: y = 0
    tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette, x=x, y=y)
    img = displayio.Group()
    img.append(tile_grid)
    display.show(img)
    display.refresh()
    if hold > init_tm:
        if images > 1:
            time.sleep(hold)              # hold the first image before showing the second
        else:
            if hold > init_tm:
                time.sleep(hold - init_tm)  # minus the initialization time if there is 1 image
    img.pop()
    del bitmap
    del img
    del tile_grid
    gc.collect()

def GetBattPercent(batt_pin):
    debug_print("Reading battery percentage")
    percent = 0
    # read the battery voltage (approximation, not exact levels with no fuel gauge to read)
    batt_volts = (batt_pin.value * 3.3) / 65536 * 2
    
    if BOARD_TYPE == "RS2040LILYGO":
        batt_volts += 0.05
    
    debug_print(f"Battery voltage: {batt_volts}")

    if batt_volts > 3.80:
        percent = 86                    # 100% to 81% capacity
    elif batt_volts > 3.65:
        percent = 50                    # 80%  to 31% capacity
    elif batt_volts > 3.40:
        percent = 25                    # 30%  to 16% capacity
    else:
        percent = 5                     # 15%  to  0% capacity
    return percent

debug_print(f"Starting MandoPuter in {DISPLAY} mode for the {BOARD_TYPE} hardware.")

# Turn off the LCD Backlight
displayio.release_displays()

# Setup the bus, display object, and font for the display
if BOARD_TYPE == "RS2040LILYGO":
    spi = busio.SPI(clock=board.GP2, MOSI=board.GP3)
elif BOARD_TYPE == "PiPicoRP2040":
    spi = busio.SPI(clock=board.GP10, MOSI=board.GP11, MISO=board.GP12)
else:
    spi = board.SPI()

while not spi.try_lock():
    pass

spi.configure(baudrate=SPI_SPEED)  # Configure SPI with the specified speed
spi.unlock()

if BOARD_TYPE == "RS2040LILYGO":
    tft_cs    = board.GP5
    tft_dc    = board.GP1
    lcd_rst   = board.GP0
    lcd_light = board.GP4
elif BOARD_TYPE == "FeatherM4" or BOARD_TYPE == "ESP32-S3":
    tft_cs  = board.D6
    tft_dc  = board.D9
    lcd_rst = board.D5
    lcd_light = board.D10
elif BOARD_TYPE == "PiPicoRP2040":
    tft_cs    = board.GP28
    tft_dc    = board.GP14
    lcd_rst   = board.GP27
    lcd_light = board.GP15
else:
    lcd_light = board.D10
    tft_cs = board.D2
    tft_dc  = board.D3
    lcd_rst = board.D4

debug_print("Display bus and pins configured.")

display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, baudrate=SPI_SPEED, reset=lcd_rst, polarity=0, phase=0)
if DISPLAY == "Pre-Beskar":
    display     = ST7789(display_bus, rotation=270, width=240, height=135, rowstart=40, colstart=53, auto_refresh=False, backlight_pin=lcd_light, brightness=0)
    font        = bitmap_font.load_font("mandalor135.bdf")  # 135 pixel tall bitmap font
    offset      = 12
elif DISPLAY == "Beskar":
    display     = ST7789(display_bus, rotation=0, width=240, height=240, rowstart=80, auto_refresh=False, backlight_pin=lcd_light, brightness=0)
    font        = bitmap_font.load_font("mandalor165.bdf")  # 165 pixel tall bitmap font
    offset      = 14
elif DISPLAY == "1.44":
    display     = ST7735R(display_bus, rotation=90, width=128, height=128, colstart=2, rowstart=3, auto_refresh=False, backlight_pin=lcd_light, brightness=0)
    font        = bitmap_font.load_font("mandalor82.bdf")  # 82 pixel tall bitmap font
    offset      = 8
elif DISPLAY == "0.96":
    display = ST7735R(display_bus, rotation=270, width=160, height=80, colstart=24, bgr=True, auto_refresh=False, backlight_pin=lcd_light, brightness=0)
    font        = bitmap_font.load_font("mandalor76.bdf")  # 70 pixel tall bitmap font
    offset      = 8
stage = displayio.Group()
display.show(stage)

debug_print("Display initialized and font loaded.")

# Disable WiFi power
if BOARD_TYPE == "ESP32-S3":
    import wifi
    wifi.radio.enabled = 0

# Configure LEDs
if BOARD_TYPE == "ESP32-S3":
    # setup the onboard neopixel LED power control
    led_pwr = digitalio.DigitalInOut(board.NEOPIXEL_POWER)
    led_pwr.direction = digitalio.Direction.OUTPUT

if BOARD_TYPE == "FeatherM4" or BOARD_TYPE == "ESP32-S3" or BOARD_TYPE == "ItsyBitsyRP2040":
    led = neopixel.NeoPixel(board.NEOPIXEL, 1)
elif BOARD_TYPE == "ItsyBitsyM4":
    led = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1) # onboard dotstar
elif BOARD_TYPE == "PiPicoRP2040":
    led = digitalio.DigitalInOut(board.LED)
    led.direction = digitalio.Direction.OUTPUT
elif BOARD_TYPE == "RS2040LILYGO":
    led = digitalio.DigitalInOut(board.GP25)
    led.direction = digitalio.Direction.OUTPUT

# Blink LED to indicate the script is running

if ENABLE_LEDS > 0:
    debug_print("Enabling LEDs")
    if BOARD_TYPE == "RS2040LILYGO":
        led.value = True
    elif BOARD_TYPE != "PiPicoRP2040":
        led.brightness = 0.05  # dim the LED to 5%
        led[0] = (255, 0, 255) # purple
    if BOARD_TYPE == "ESP32-S3":
        led_pwr.value = True
else:
    debug_print("Disabling LEDs")
    if BOARD_TYPE != "PiPicoRP2040":
        led.brightness = 0  # dim the LED to 0%
    if BOARD_TYPE == "ESP32-S3":
        led_pwr.value = False

debug_print("LEDs configured.")

# Setup battery monitoring
if BATTERY_MON > 0:
    lowbattX = 0
    lowbattY = 0
    vbat_voltage_pin = 0
    if BOARD_TYPE == "ESP32-S3":
        i2c = board.I2C()  # uses board.SCL and board.SDA
        sensor = LC709203F(i2c)
        sensor.PackSize = BATTERY_SZ
    elif BOARD_TYPE == "FeatherM4":
        vbat_voltage_pin = AnalogIn(board.VOLTAGE_MONITOR) # for measuring battery voltage
    elif BOARD_TYPE == "PiPicoRP2040":
        # battery voltage measurements need a jumper from VSYS to ADC0 (pin 39 - 31)
        vbat_voltage_pin = AnalogIn(board.GP26) # for measuring battery voltage
    elif BOARD_TYPE == "ItsyBitsyM4" or BOARD_TYPE == "ItsyBitsyRP2040":
        # battery voltage measurements need a jumper from batt to A1
        vbat_voltage_pin = AnalogIn(board.A1)
    elif BOARD_TYPE == "RS2040LILYGO":
        vbat_voltage_pin = AnalogIn(board.GP26)

    # Create the second image centered on the display
    lowbattImg, lowbattPal = adafruit_imageload.load("LowBatt.bmp", bitmap=displayio.Bitmap, palette=displayio.Palette)
    x = int(display.width - lowbattImg.width)
    y = int(display.height - lowbattImg.height)
    if x < 0: x = 0
    if y < 0: y = 0
    lowbattX = x
    lowbattY = y
else:
    # Disable I2C port power
    if BOARD_TYPE == "ESP32-S3":
        i2c_pwr = digitalio.DigitalInOut(board.I2C_POWER)
        i2c_pwr.direction = digitalio.Direction.OUTPUT
        i2c_pwr.value = False

debug_print("Battery monitoring configured.")

# Turn on the Backlight
display.brightness = DISP_BRIGHT / 100
init_time = 4.5   # how long it takes to initialize the sequence

# Show the owner's name at startup
if SHOW_NAME > 0:
    DisplayName(OWNER_NAME, NAME_HOLD, NAME_COLOR, init_time)

# Show the banner graphic(s)
if SHOW_IMG > 0:
    DisplayImage(IMG1, IMG1_HOLD, SHOW_IMG, init_time)
    DisplayImage(IMG2, IMG2_HOLD, SHOW_IMG, init_time)

gc.collect()
low_batt_icon = 0
batt_percent  = 0

# Prepare the Mandalorian characters
maxwidth = 0
text   = label.Label(font, text=messages[0], color=TEXT_COLOR)
for msg in messages:
    text.text = msg
    if maxwidth < text.width:
        maxwidth = text.width
text.text = messages[0]
text.x = int(((display.width - maxwidth)/2)-1)
text.y = int((display.height / 2)+offset)
if text.x < 0:
    text.x = 0
if text.y < 0:
    text.y = 0
stage.append(text)

# Initialize the low battery icon
if BATTERY_MON > 0:
    batt_tile = displayio.TileGrid(lowbattImg, pixel_shader=lowbattPal, x=lowbattX, y=lowbattY)

display.show(stage)

debug_print("Entering main loop.")

while True:
    index = 0
    for msg in messages:
        text.text = msg
        display.refresh()
        if BOARD_TYPE == "PiPicoRP2040":
            time.sleep(delays[index]* 0.75)
        else:
            time.sleep(delays[index])
        index = index + 1

    if BATTERY_MON > 0:
        if BOARD_TYPE == "ESP32-S3":
            sensor = LC709203F(i2c)
            batt_percent = sensor.cell_percent
        elif BOARD_TYPE == "FeatherM4" or BOARD_TYPE == "ItsyBitsyM4" or BOARD_TYPE == "ItsyBitsyRP2040" or BOARD_TYPE == "PiPicoRP2040":
            batt_percent = GetBattPercent(vbat_voltage_pin)
        
        debug_print(f"Batt Percent: {batt_percent} %")
        if batt_percent < LOW_BATT_LEVEL:
            # Add low battery icon
            if low_batt_icon == 0:
                stage.append(batt_tile)
                low_batt_icon = 1
        else:
            if low_batt_icon > 0:
                # Remove low battery icon
                stage.pop()
                low_batt_icon = 0
