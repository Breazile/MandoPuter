import gc
import time
import displayio
import adafruit_imageload
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font

def display_name(display, font, name, hold, color, resolution):
    if resolution == 128 or resolution == 80:
        ownerfont = bitmap_font.load_font("Alef-Bold-12.bdf")  # 12 point bitmap font
    else :
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
