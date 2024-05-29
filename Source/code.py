import gc
import time
import displayio
import battery_monitor
import display_images
from adafruit_display_text import label
import adafruit_imageload

# -----------------------------------------------------------------------------
# Board Configuration
# -----------------------------------------------------------------------------

# Board setup imports (uncomment the one corresponding to your board)
import board_lilygo as board_setup            # LilyGo RP2040 w/ 1.14" LCD    https://amzn.to/4aBkma1
# import board_esp32_s3 as board_setup          # Adafruit ESP32-S3 Feather     https://www.adafruit.com/product/5477
# import board_feather_m4 as board_setup        # Adafruit Feather M4 Express   https://www.adafruit.com/product/3857
# import board_itsybitsy_m4 as board_setup      # Adafruit ItsyBitsy M4 Express https://www.adafruit.com/product/3800
# import board_itsybitsy_rp2040 as board_setup  # Adafruit ItsyBitsy RP2040     https://www.adafruit.com/product/4888
# import board_pipico_rp2040 as board_setup     # Raspberry Pi Pico RP2040      https://www.adafruit.com/product/4864

# -----------------------------------------------------------------------------
# Display Configuration
# -----------------------------------------------------------------------------

# Display type
# Choose the type of display you are using. Only one should be uncommented.
DISPLAY = "1.14" #Pre-Beskar   # Adafruit 1.14" LCD display  https://www.adafruit.com/product/4383
# DISPLAY = "1.30" #"Beskar"     # Adafruit 1.3" LCD display   https://www.adafruit.com/product/4313
# DISPLAY = "1.44"               # Adafruit 1.44" LCD display  https://www.adafruit.com/product/2088
# DISPLAY = "0.96"               # Adafruit 0.96" LCD display  https://www.adafruit.com/product/3533

# Backlight brightness (0% to 100%)
DISP_BRIGHT = 80

# Owner name settings
SHOW_NAME = 1                     # Set to 1 to display the name, or 0 to not display a name
OWNER_NAME = "Your Name Here"     # Name of the owner to be shown
NAME_COLOR = 0x00FF00             # Green on black (choose colors here - https://www.color-hex.com/)
NAME_HOLD = 3.0                   # How many seconds to display the name

# Battery monitoring settings
BATTERY_SZ = 500  # Size of battery in mAh (only for the ESP32-S3 board)
BATTERY_MON = 1  # Set to 1 to enable the battery monitor, 0 to disable it
LOW_BATT_LEVEL = 10  # Show the low battery icon when the battery goes below this percentage

# Other settings for debugging
ENABLE_LEDS = 1  # Set to 1 to turn on LEDs for debugging, set to 0 to save battery
DEBUG_SERIAL = 1  # If your board has a debug port, you can read the system messages.

# -----------------------------------------------------------------------------
# Banner graphics settings
# -----------------------------------------------------------------------------

# Setting screen resolution based on display type, do not change these
if DISPLAY == "1.30":
    RESOLUTION = 240
elif DISPLAY == "1.14":
    RESOLUTION = 135
elif DISPLAY == "1.44":
    RESOLUTION = 128
elif DISPLAY == "0.96":
    RESOLUTION = 80

# Banner graphic(s) shown after the owner's name and before the sequence starts
SHOW_IMG = 2  # How many images to show. 0 = no images, 1 = 1 image, 2 = 2 images

IMG1 = f"TheMandalorian{RESOLUTION}.bmp"  # File name of the first 8-bit BMP graphic to be shown after each text sequence
IMG1_HOLD = 5.00  # How long the first image is displayed in seconds

IMG2 = f"BabyYoda{RESOLUTION}.bmp"  # File name of the second 8-bit BMP graphic to be shown after the first image
IMG2_HOLD = 5.00  # How long the second image is displayed in seconds

# -----------------------------------------------------------------------------
# Mandalorian character sequence
# -----------------------------------------------------------------------------

messages = ["MLM", "JBM", "SAS", "JAS", "JBM", "MLM", "SAS", "AJS", "SAS"]
# Time that each character group is shown 0.50 is 500 milliseconds, or 1/2 of a second
delays = [0.75, 0.75, 0.65, 0.75, 0.50, 0.84, 1.00, 0.35, 0.84]
TEXT_COLOR = 0xFF0000  # Red on black (choose colors here - https://www.color-hex.com/)

# -----------------------------------------------------------------------------
# DO NOT EDIT BELOW THIS LINE. THESE ARE THE MAIN FUNCTIONS
# -----------------------------------------------------------------------------

def debug_print(text):
    if DEBUG_SERIAL:
        print(text)

debug_print(f"Starting MandoPuter in {DISPLAY} mode.")

# Setup
display_bus, lcd_light = board_setup.init()

debug_print("Display bus initialized")

# Initialize display
display, font, offset = display_images.init(DISPLAY, display_bus, lcd_light)
debug_print("Display initialized")

led = board_setup.configure_led(ENABLE_LEDS)
debug_print("LED configured")

if BATTERY_MON:
    battery_monitoring = board_setup.configure_battery_monitor()
    debug_print("Battery monitor configured")

# Turn on the Backlight
display.brightness = DISP_BRIGHT / 100
debug_print("Backlight turned on")

# Show the owner's name at startup
if SHOW_NAME:
    display_images.display_name(display, font, OWNER_NAME, NAME_HOLD, NAME_COLOR)
    debug_print(f"Displayed owner name: {OWNER_NAME}")

# Show the banner graphic(s)
if SHOW_IMG:
    display_images.display_image(display, IMG1, IMG1_HOLD)
    debug_print(f"Displayed image: {IMG1}")
    if SHOW_IMG > 1:
        display_images.display_image(display, IMG2, IMG2_HOLD)
        debug_print(f"Displayed image: {IMG2}")

# Main loop
gc.collect()
debug_print("Starting main loop")

stage = displayio.Group()
display.show(stage)
text = label.Label(font, text=messages[0], color=TEXT_COLOR)
stage.append(text)

maxwidth = max(text.bounding_box[2] for msg in messages)
text.x = int((display.width - maxwidth) / 2) - 1
text.y = int(display.height / 2) + offset

if BATTERY_MON:
    lowbattImg, lowbattPal = adafruit_imageload.load("LowBatt.bmp", bitmap=displayio.Bitmap, palette=displayio.Palette)
    lowbattX = int(display.width - lowbattImg.width)
    lowbattY = int(display.height - lowbattImg.height)
    batt_tile = displayio.TileGrid(lowbattImg, pixel_shader=lowbattPal, x=lowbattX, y=lowbattY)

low_batt_icon = 0

while True:
    for index, msg in enumerate(messages):
        text.text = msg
        display.refresh()
        time.sleep(delays[index])
        
    if BATTERY_MON:
        batt_percent = battery_monitor.get_batt_percent(battery_monitoring)
        debug_print(f"Battery percentage: {batt_percent}%")
        
        if batt_percent < LOW_BATT_LEVEL:
            if low_batt_icon == 0:
                stage.append(batt_tile)
                low_batt_icon = 1
                debug_print("Low battery icon displayed")
        else:
            if low_batt_icon > 0:
                stage.pop()
                low_batt_icon = 0
                debug_print("Low battery icon removed")
