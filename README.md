# Changes from Jon Breazile's https://github.com/Breazile/MandoPuter/

* Repository cleanup. Still supporting all the same boards, but with less release work for the maintainers. 
* Added debugging prints for boards with serial ports.
* Additional board support. Compatibility for boards with a built in LCD screens.
* Fixed broken links


![Image](Images/MandoChannel.jpg)
# What is a MandoPuter?

A basic electronics system that will display Mandalorian characters on a small display (I'm paying homage to Lego Batman with the name "Puter"). Use this as a starting point for adding displays to your costume (like a gauntlet). Feel free to copy the design, modify it, or make feature requests. 

## Contents
* [Features](README.md#Features)
* [Wish List](README.md#Wish-List)
* [Parts list](README.md#Parts-list)
* [Which board should I use?](README.md#Which-board-should-I-use)
* [Suggested Tools](README.md#Suggested-Tools)
* [Installation Steps](README.md#Installation-Steps)
    1. [Install the software and files on the board](README.md#Install-the-software-and-files-on-the-board)
    2. [Customize options](README.md#Customize-options)
    3. [Solder the LCD](README.md#Solder-the-LCD)
    4. [Power the board](README.md#Power-the-board)
* [Latest Mandalorian Font](README.md#Latest-Mandalorian-Font)
* [Where can I get help?](README.md#Where-can-I-get-help)
* [Troubleshooting](README.md#Troubleshooting)
* [Want to know more?](README.md#Want-to-know-more)

## Features:

* Many supported boards (including a Raspberry Pi).
* Configurable startup text and images
* Mandalorian font
* Configurable low battery icon
* Configurable LCD backlight brightness
* Disable the onboard LED to save power
* RAM efficient and easy to understand implementation

## Wish List:

* Code refactor, for easier configuration and maintenance.
* Wifi configuration page for changing the splash screen
* Compatibility with latest circuitpython 9
* Deep sleep - command the board to sleep for a certain amount of time (or until an external button is pressed)
* Bluetooth - I'm looking into Bluetooth features once Adafruit has completed development
* Audio - playback of audio files (WAV)

## Parts list

Some links are amazon affiliate links.  We are a participant in the Amazon Services LLC Associates Program, an affiliate advertising program designed to provide a means for us to earn fees by linking to Amazon.com and affiliated sites.

1) Display and Microcontroller Selections
    1) Combined Devices
    - [LilyGo RP2040 w/ 1.14" LCD](https://amzn.to/4aBkma1)
    2) LCD and Microcontroller Seperate
        1) One supported display
        - [1.14" LCD](https://www.adafruit.com/product/4383)  **<--- preferred display for the GreatApeStudioArt [pre-Beskar](https://greatapestudio.com/products/the-mandalorian-bracers-digital-3d-models-download) gauntlet**
        - [1.30" LCD](https://www.adafruit.com/product/4313)  **<--- preferred display for the GreatApeStudioArt [Beskar](https://greatapestudio.com/products/the-mandalorian-beskar-bracers-digital-3d-model-download) gauntlet**
        2) One microcontroller board that supports CircuitPython (see [Which board should I use?](README.md#Which-board-should-I-use) below)
            * [Adafruit ESP32-S3 Feather](https://www.adafruit.com/product/5477) (get the 2MB PSRAM version)
            * [Adafruit Feather M4 Express](https://amzn.to/3V1B3pp)
            * [Adafruit ItsyBitsy M4 Express](https://www.adafruit.com/product/3800)
            * [Adafruit ItsyBitsy RP2040](https://www.adafruit.com/product/4888)
            * [Raspberry Pi Pico RP2040](https://amzn.to/3x1Jedi)
2) 3.7V LiPoly Battery, [500 mAh](https://amzn.to/3wVGzlu) or [1200 mAh](https://amzn.to/3R0ZJxi) are good choices. You can also use a [USB battery bank](https://amzn.to/4bDhKtN) and power the board via the USB port (battery level monitoring not supported through USB power).
3) Optional [Backpack Add-On](https://amzn.to/454OwBG) if you are using an ItsyBitsy or a Raspberry Pi and you want to connect a LiPoly battery to them. This will also charge the battery when the USB port has power. This is not needed if you plan to power the board from a USB power pack.
4) Small Gauge wire. [26awg 4 conductor wire](https://amzn.to/3WWl26Q) - Optional if using the lcd+microcontroller single board.
5) Optional [Switch](https://amzn.to/3V0uFyL) for a LiPoly battery.

If you have any trouble finding the parts above, check [OctoPart](https://www.octopart.com) for other sellers.

## Which board should I use?

Board | LCD | CPU & RAM | Flash storage | Battery Connector | Battery Charger | Fuel Gauge | WiFi & Bluetooth*
------------ | ------------- | ------------ | ------- | ------ | -------- | ---
[Adafruit ESP32-S3 Feather](https://www.adafruit.com/product/5477) |  | Dual Core Tensilica processor @ 240MHz, 2 MB RAM | 4 MB | Yes | Built-in | Yes | Yes / Yes
[Adafruit Feather M4 Express](https://www.adafruit.com/product/3857) | | Cortex M4 core @ 120 MHz, 192 KB RAM | 512 KB | Yes | Built-in | No | No
[Adafruit ItsyBitsy M4 Express](https://www.adafruit.com/product/3800) | | Cortex M4 core @ 120 MHz, 192 KB RAM | 512 KB | No | No | No | No
[Adafruit ItsyBitsy RP2040](https://www.adafruit.com/product/4888) |  | Cortex M0+ dual core @ 125 MHz, 264 KB RAM | 8 MB | No | No | No | No
[Raspberry Pi Pico RP2040](https://www.adafruit.com/product/4864) | | Dual ARM Cortex-M0+ @ 133MHz, 264 KB RAM | 2 MB | No | No | No | No
[LilyGo RP2040 w/ 1.14" LCD](https://amzn.to/4aBkma1) | 1.14" LCD | Dual ARM Cortex-M0+ @ 133MHz, 264 KB RAM | 4 MB | Yes | Yes | Yes | Yes / No

\* WiFi & Bluetooth are currently not used, but considering in the future.

Bigger RAM and flash storage space means you can add bigger graphics to the startup sequence. When loading those images it will attempt to load in RAM. If there is not enough RAM then it will load directly from flash to the screen which is slower (looks like a wipe effect).

Some boards have a built-in LiPoly battery fuel gauge which monitors the battery and can give an accurate level of charge.  The ESP32-S3 Feather board currently has a [bug](https://github.com/adafruit/circuitpython/issues/6311). The LiPoly battery voltage is only a rough approximation of battery level because LiPoly batteries are relatively flat when discharging.

## Suggested Tools

1) [Solder Station](http://amzn.to/2wbvd9h)
1) [0.3mm Solder](http://amzn.to/2w4WP1v)
1) [Flush Wire Cutters (ebay $2)](http://www.ebay.com/sch/i.html?_nkw=side+cutters+flush&_udhi=2)
1) [Wire Strippers (ebay $5)](http://www.ebay.com/sch/i.html?_nkw=multifunction%20wire%20strippers&_udhi=5)
1) Isopropyl Alcohol for cleaning solder flux. No link, buy this local from any grocery / drug store / hardware store.

The linked solder iron is a good temperature controlled beginner model.  If you want an upgrade, the [Pine64 Pinecil](https://amzn.to/3X0fkRg) is the envy of my peers.  You will need at least a 60W USB-C PD power supply or you can make one from an old drill battery. No instructions here, [search hackaday](https://hackaday.com/2023/06/22/portable-soldering-station-runs-on-drill-batteries/).

## Installation Steps

You'll follow 4 main steps to get things setup:

1) Install the software and files on the board (drag and drop)
2) Select your board configuration
3) Solder the LCD
4) Power the board

No need to write any code or use any other fancy tools. All of the code is in the file code.py, so you can install CircuitPython and modify the code to suit your needs. Jon has an [older video](https://www.youtube.com/watch?v=ql2s0-QgcFI) that walks through the steps of updating CircuitPython and copying the MandoPuter files.

### 1. Install the software and files on the board

You will likely need to update the [CircuitPython](https://circuitpython.org/) that is on your board to the version 8 (not the latest). Once you receive the board you will need to hold the **BOOT** button while connecting it to your computer via USB, and update CircuitPython via drag and drop to the usb drive.

CircuitPython versions 8.0.0-Beta6 to 8.2.7 have been tested with this code (your board may need to be updated/downgraded). See [CircuitPython](https://circuitpython.org/) for updating your specific board. Select "Previous Versions of CircuitPython" and find the correct .uf2 file version.

Once your device reboots and you see a usb drive named "CIRCUITPY", return here and click the green download button at the top of this page.  Unzip the copy of the repo and find the Source folder, the files inside are what needs to be copied to your device (drag and drop).

Make sure you let the copy finish before you remove the USB cable or reset the board, or your system could be corrupted. It could take up to 90 seconds or more on some systems. If that happens, please read the [troubleshooting page](https://learn.adafruit.com/adafruit-esp32-s3-feather/troubleshooting)

If you did it right, you will have overwritten the code.py file located in the root directory of your board.

### 2. Select your board configuration in `code.py`

You can make selections for:

- Display type (Beskar - 1.3", or Pre-Beskar 1.14") - should already be set for you in the ZIP file
- Board type (boards have different capabilities) - should already be set for you in the ZIP file
- Your name (if you want to display your name on boot)
- Banner graphic (If you want 1 or 2 images displayed after your name before the sequence starts)
- Customize the Mandalorian character sequence (if you want something different)
- Customize the LCD backlight level (if you have the pink LIT wire connected to the LCD)
- Turn on the low battery icon if you want that feature. You must have the battery monitor wire soldered (not needed on Feather M4 and ESP32-S3). The ESP32-S3 library currently has a [bug](https://github.com/adafruit/circuitpython/issues/6311) where communications to the battery monitor chip fails occasionally. I would disable battery monitoring until that bug is fixed. Monitoring of a USB battery pack is not supported.

#### Examples of Basic Configuration:

1. **Choose the Display Type**:
   - In the `code.py` file, find the section labeled `# Set the display type`.
   - Uncomment the line corresponding to the display you are using by removing the `#` at the beginning of the line.
   - Ensure only one display type is uncommented at a time.
   - Example:
     ```python
     DISPLAY        = "Pre-Beskar"           # Adafruit 1.14" LCD display  https://www.adafruit.com/product/4383
     #DISPLAY       = "Beskar"               # Adafruit 1.3" LCD display   https://www.adafruit.com/product/4313
     #DISPLAY       = "1.44"                 # Adafruit 1.44" LCD display  https://www.adafruit.com/product/2088
     #DISPLAY       = "0.96"                 # Adafruit 0.96" LCD display  https://www.adafruit.com/product/3533
     ```

2. **Set the Display Brightness**:
   - Adjust the display brightness by modifying the `DISP_BRIGHT` variable.
   - The value should be between 0 and 100 (representing the percentage of brightness).
   - Example:
     ```python
     DISP_BRIGHT    = 80                     # How bright to make the display - 0% to 100%
     ```

3. **Select the Board Type**:
   - In the `code.py` file, find the section labeled `# Board being used`.
   - Uncomment the line corresponding to the board you are using by removing the `#` at the beginning of the line.
   - Ensure only one board type is uncommented at a time.
   - Example:
     ```python
     #BOARD_TYPE    = "ESP32-S3"             # ESP32-S3                  https://www.adafruit.com/product/5477
     #BOARD_TYPE    = "FeatherM4"            # Feather M4 Express        https://www.adafruit.com/product/3857
     #BOARD_TYPE    = "ItsyBitsyM4"          # ItsyBitsy M4 Express      https://www.adafruit.com/product/3800
     #BOARD_TYPE    = "ItsyBitsyRP2040"      # ItsyBitsy RP2040          https://www.adafruit.com/product/4888
     #BOARD_TYPE    = "PiPicoRP2040"         # Raspberry Pi Pico RP2040  https://www.adafruit.com/product/4864
     BOARD_TYPE     = "RS2040LILYGO"         # New RS2040LILYGO board
     ```

4. **Customize Owner Information**:
   - Set the `SHOW_NAME` variable to `1` to display the owner's name on startup, or `0` to not display it.
   - Modify the `OWNER_NAME` variable to the desired name.
   - Adjust the `NAME_COLOR` variable to change the color of the name display (use the [color-hex.com](https://www.color-hex.com/) website for color codes).
   - Set the `NAME_HOLD` variable to define how many seconds the name should be displayed.
   - Example:
     ```python
     SHOW_NAME      = 1                      # Set to 1 to display the name, or 0 to not display a name
     OWNER_NAME     = "Your Name Here"       # Name of the owner to be shown
     NAME_COLOR     = 0x00FF00               # Green on black (you can chose colors here - https://www.color-hex.com/)
     NAME_HOLD      = 3.0                    # How many seconds to display the name
     ```

Please follow this [guide](https://learn.adafruit.com/custom-fonts-for-pyportal-circuitpython-display/overview) if you would like to create a custom font.

4. **Save**:

After making changes, save the `code.py` file.  At this point your program should be running (circuitpython auto runs your pgram after saving the file).

### 3. Solder the LCD

Do not skip to this step! Update your board and install the Mandoputer files **before** you start soldering anything. Make sure the basics work just in case you damage the board during soldering. Plugging the Feather into USB will power the board, you don't need a battery yet. If you have the battery connected when powered via USB it will charge (if your board has a charger). Do not use alkaline or NiMH batteries and connect to the battery port - this will destroy the LiPoly charger and there's no way to disable the charger. Do not use 7.4V RC batteries on the battery port - this will destroy the board. If you do not have a LiPoly battery then consider using a USB power bank.

You will need to solder 8 wires to the LCD, and both LCDs have the same pinout. This is low power, so 26 gauge wire will do just fine. Adafruit has a great [soldering guide](https://learn.adafruit.com/adafruit-guide-excellent-soldering) if you are new to soldering. Use a good [solder with flux](https://amzn.to/4aE3gZm) in it. That makes it much easier to make a good solder joint, and you only need to touch the parts for a second or two.

The pink wire to the LIT pin on the display is optional, and only needed if you want to control the backlight level. It will be required in the future deep sleep feature which will need to turn off the display (only supported on the ESP32-S3 Feather).

#### 3a. Pre-Beskar LCD Wiring

##### Wiring the 1.14" Display to the Adafruit ESP32-S3 Feather
<div align="center">
  <img src="Images/FeatherESP32-S3Pre-BeskarWiring.jpg" height="200px" align="center"/>
</div>

##### Wiring the 1.14" Display to the Adafruit Feather M4 Express
<div align="center">
  <img src="Images/FeatherM4ExpressPre-BeskarWiring.jpg" height="200px" align="center"/>
</div>

##### Wiring the 1.14" Display to the Adafruit ItsyBitsy M4 Express
<div align="center">
  <img src="Images/ItsyBitsyM4Pre-BeskarWiring.jpg" height="200px" align="center"/>
</div>

##### Wiring the 1.14" Display to the Adafruit ItsyBitsy RP2040
<div align="center">
  <img src="Images/ItsyBitsyRP2040Pre-BeskarWiring.jpg" height="200px" align="center"/>
</div>

##### Wiring the 1.14" Display to the Raspberry Pi Pico RP2040
<div align="center">
  <img src="Images/RaspberryPiPicoRP2040Pre-BeskarWiring.jpg" height="200px" align="center"/>
</div>

#### 3b. Beskar LCD Wiring

##### Wiring the 1.3" Display to the Adafruit ESP32-S3 Feather
<div align="center">
  <img src="Images/FeatherESP32-S3BeskarWiring.jpg" height="200px" align="center"/>
</div>

##### Wiring the 1.3" Display to the Adafruit Feather M4 Express
<div align="center">
  <img src="Images/FeatherM4ExpressBeskarWiring.jpg" height="200px" align="center"/>
</div>

##### Wiring the 1.3" Display to the Adafruit ItsyBitsy M4 Express
<div align="center">
  <img src="Images/ItsyBitsyM4BeskarWiring.jpg" height="200px" align="center"/>
</div>

##### Wiring the 1.3" Display to the Adafruit ItsyBitsy RP2040
<div align="center">
  <img src="Images/ItsyBitsyRP2040BeskarWiring.jpg" height="200px" align="center"/>
</div>

##### Wiring the 1.3" Display to the Raspberry Pi Pico RP2040
<div align="center">
  <img src="Images/RaspberryPiPicoRP2040BeskarWiring.jpg" height="200px" align="center"/>
</div>

For the Beskar display you will need to cut off the mounting tabs with a pair of side cutters. Be careful that you do not cut the main board in the process.

<div align="center">
  <img src="Images/CutLCD1.jpg" height="300px" align="center"/>  <img src="Images/CutLCD2.jpg" height="300px" align="center"/>
</div>

### 4. Power the board

You have a couple of different options to power the board:

* Connect a USB power source to the USB port on the board. Boards with an onboard charger will not charge anything connected to USB. Battery monitoring will not work when powered via USB.
* Connect a LiPoly battery to the board

If you choose a board that does not have an on-board battery charger you will have to buy a separate [charger](https://www.adafruit.com/product/1904) to charge the battery (unless you use the backpack board in the next paragraph). With an on-board charger it will charge when you have power to USB. 

For boards that do not have a battery connector you can solder on a battery [backpack board](https://www.adafruit.com/product/2124) which will also charge the battery. If you don't want an onboard charger simply solder a [battery pigtail](https://www.adafruit.com/product/3814) to the board (match the red and black wires in the diagram below). Another option is power the board via any USB battery or power device if you prefer that (connected to the USB port).

Here's a wiring diagram for the ItsyBitsy (all versions are the same wiring) or the Raspberry Pi with the Backpack Add-on.
<div align="center">
  <img src="Images/ItsyBitsyM4Power.jpg" height="200px" align="center"/><img src="Images/RaspberryPiPower.jpg" height="200px" align="center"/>
</div>

If you are not using an Adafruit battery then you need to check the polarity of the battery wiring. The black wire should be closest to the USB connector, see the picture below for the correct polarity on boards that have a LiPoly connector.

<div align="center">
  <img src="Images/BatteryPolarity.jpg" height="200px" align="center"/>
</div>

##### Jumper for monitoring battery voltage

The ItsyBitsy and Raspberry Pi boards need an extra jumper wire to read the LiPoly battery voltage. Change the `BATTERY_MON` setting to 1 to enable reading the battery voltage and display the low battery icon.

Here are the jumper wire locations for the ItsyBitsy M4 Express, ItsyBitsy RP2040, and Raspberry Pi Pico boards

<div align="center">
  <img src="Images/ItsyBitsyM4BatteryMon.jpg" height="100px" align="center"/>
  <img src="Images/ItsyBitsyRP2040BatteryMon.jpg" height="100px" align="center"/>
  <img src="Images/RaspberryBatteryMon.jpg" height="100px" align="center"/>
</div>

## Latest Mandalorian Font

Jon has an in depth page on the fonts and sequence [here](https://github.com/Breazile/MandoPuter/blob/master/MandoaDecode.md).

The font used on the show is different from the font in the original Star Wars movies. The best match for the font is the [Mando AF](https://aurekfonts.github.io/?font=MandoAF) font. The L characters is not correct (should look like the inverted V character), and the J and X characters are duplicates of characters before them. Jon modified this font and fixed the characters - [MandoPuter.sfd](https://github.com/Breazile/MandoPuter/blob/master/MandoPuter.sfd). Bitmap fonts source are now correct with non-proportional spacing as of 1/17/2023.

Adafruit has a guide on how to convert TTF or OTF fonts to BDF (bitmap) fonts that MandoPuter uses. [Custom Fonts for CircuitPython Displays](https://learn.adafruit.com/custom-fonts-for-pyportal-circuitpython-display/conversion)

Maybe we will find hidden meaning in the sequence. Mandalorian language reference here : https://www.mandoa.org/

## Troubleshooting

If you do not see anything on the display, check the onboard LED to see if the code is running properly. If you see a blue or red flashing LED then there is an error in the code. If that happens try updating CircuitPython, and be sure you copied **ALL** the files from the ZIP Source folder to the CIRCUITPY drive. You might also have an error in the code (code.py) if you have made a mistake, so try using the unmodified one from the ZIP file. 

You may power the board from the USB port, so try running it with the battery removed to isolate a battery related problem.

Other brands of LCDs may require different polarity in the SPI communication signaling. Please stick to the linked parts for best results.

## Want to know more?

Check out this [getting started guide](https://learn.adafruit.com/welcome-to-circuitpython/overview) on CircuitPython. There's also a [CircuitPython essentials guide](https://learn.adafruit.com/circuitpython-essentials/circuitpython-essentials) that good to read through.

- [CircuitPython Downloads](https://circuitpython.org/downloads)
- [Adafruit CircuitPython Library Bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/tree/master/libraries)
- [CircuitPython GitHub](https://github.com/adafruit/circuitpython)
- [CircuitPython internal libraries](https://github.com/adafruit/circuitpython/tree/master/shared-bindings)

You should be ready to go. The system should run once the file is saved, and you should see the font look like this:
