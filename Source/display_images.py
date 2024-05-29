import gc
import time
import displayio
import adafruit_imageload
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font
from adafruit_st7789 import ST7789
from adafruit_st7735r import ST7735R

def init(DISPLAY, display_bus, lcd_light):
  
    if DISPLAY   == "1.44":
        display = ST7735R(display_bus, rotation=90, width=128, height=128, colstart=2, rowstart=3, auto_refresh=False, backlight_pin=lcd_light, brightness=0)
        font = bitmap_font.load_font("mandalor82.bdf")
        offset = 8
        
    elif DISPLAY == "1.30":
        display = ST7789(display_bus, rotation=0, width=240, height=240, rowstart=80, auto_refresh=False, backlight_pin=lcd_light, brightness=0)
        font = bitmap_font.load_font("mandalor165.bdf")
        offset = 14
        
    elif DISPLAY == "1.14":
        display = ST7789(display_bus, rotation=270, width=240, height=135, rowstart=40, colstart=53, auto_refresh=False, backlight_pin=lcd_light, brightness=0)
        font = bitmap_font.load_font("mandalor135.bdf")
        offset = 12
        
    elif DISPLAY == "0.96":
        display = ST7735R(display_bus, rotation=270, width=160, height=80, colstart=24, bgr=True, auto_refresh=False, backlight_pin=lcd_light, brightness=0)
        font = bitmap_font.load_font("mandalor76.bdf")
        offset = 8
        
    return display, font, offset

def display_name(display, font, name, hold, color):
    if display.width <= 128:
        ownerfont = bitmap_font.load_font("Alef-Bold-12.bdf")  # 12 point bitmap font
    else:
        ownerfont = bitmap_font.load_font("Alef-Bold-18.bdf")  # 18 point bitmap font
    banner_text = label.Label(ownerfont, text=name, color=color)
    banner_text.x = int(((display.width - banner_text.bounding_box[2]) / 2) - 1)
    banner_text.y = int(((display.height - banner_text.bounding_box[3]) / 2) + 1)
    display.show(banner_text)
    display.refresh()
    time.sleep(hold)
    del ownerfont
    del banner_text
    gc.collect()

def display_image(display, img, hold):
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
    img_group = displayio.Group()
    img_group.append(tile_grid)
    display.show(img_group)
    display.refresh()
    time.sleep(hold)
    img_group.pop()
    del bitmap
    del img_group
    del tile_grid
    gc.collect()
