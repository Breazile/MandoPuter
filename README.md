# What is a MandoPuter?

A basic electronics system that will display Mandalorian characters on a small display (I'm paying homage to Lego Batman with the name). Use this as a starting point for adding displays to your costume (like a gauntlet). Feel free to copy the design, modify it, or make feature requests. This is the way!

## Parts list:

You will need the following parts:

1) Small LCD [Display](https://www.adafruit.com/product/4383)
2) [Microcontroller Board](https://www.adafruit.com/product/3857)
3) 4.2/3.7V [Battery](https://www.adafruit.com/category/917) (my 500 mAh battery in the picture below ran for over 12 hours)
4) Small Gauge (22-30) [Wire](https://www.amazon.com/Stranded-Nano-Flexible-Insulated-Electrical/dp/B07DCV7BDD/ref=sr_1_1_sspa?keywords=24+gauge+wire&qid=1577768346&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzR1IxUzhXVlJRMFoxJmVuY3J5cHRlZElkPUEwMjE2ODM0MTRRSVkyQlBIRTZJSiZlbmNyeXB0ZWRBZElkPUEwNzE2MTQ1UURZTURJT0VDUEMzJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==) 

## Recommended Tools:

1) Fine tip [Soldering Iron](https://www.amazon.com/Hakko-FX888D29BY-ESD-Safe-Digital-Soldering/dp/B00OSM27T8?ref_=ast_bbp_dp) (I use a Hakko FX-100, but any fine tip will work)
2) Solder ([what I'm using](https://www.amazon.com/gp/product/B00FGHTZFI/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1))
3) Solder flux ([what I'm using](https://www.amazon.com/gp/product/B01N8ZX7ZQ/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1))
4) [Micro Cutters](https://www.amazon.com/gp/product/B0765NMV68/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
5) [Wire Strippers](https://www.amazon.com/dp/B000XEUPMQ/ref=twister_B07JCDW6X6?_encoding=UTF8&psc=1)
6) [Tweezers](https://www.amazon.com/gp/product/B01MA5CCDO/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
7) [Isopropyl Alcohol](https://www.amazon.com/gp/product/B005DNQX3C/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) for cleaning solder flux
8) A computer with a USB port
9) Micro USB [Cable](https://www.amazon.com/AmazonBasics-Male-Micro-Cable-Black/dp/B0711PVX6Z/ref=sxin_2_ac_d_rm?ac_md=0-0-bWljcm8gdXNiIGNhYmxl-ac_d_rm&keywords=micro+USB+cable&pd_rd_i=B0711PVX6Z&pd_rd_r=0c98cacf-0fa0-4c33-a20e-4d50696b8c55&pd_rd_w=EvHyD&pd_rd_wg=74RAP&pf_rd_p=e2f20af2-9651-42af-9a45-89425d5bae34&pf_rd_r=DBF2336PKCKSAH0KHNCG&psc=1&qid=1577768200)

## I have the parts, now what do I do?

You'll follow 3 main steps to get things setup:

1) Setup the Feather M4 board with CircuitPython, and make sure it enumerates on your PC
2) Solder the display to the board
3) Copy the files

That's it, no need to write any code or use any other fancy tools. I have the source code here, so you can install CircuitPython and modify the code to suit your needs. More on that in another guide.

### Feather Setup

Setup the Feather M4 first before you start soldering anything. Make sure the basics work just in case you damage the board during soldering. The primary guide to the Feather is [here](https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51), but you can skip ahead to the [CircuitPython setup](https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/circuitpython). Plugging the Feather into USB will power the board, you don't need a battery yet. If you have the battery connected when powered via USB it will charge. Power management details are [here](https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/power-management). When you plug the Feather into your computer, it should show up just like a USB key and you copy file to it in the same way. No need to download anything.

### Solder the LCD

Solder the LCD to the Feather M4, so they can talk to each other. Adafruit has a great [soldering guide](https://learn.adafruit.com/adafruit-guide-excellent-soldering) if you are new to soldering. The only thing they did not mention is adding flux to the solder joint first. That makes it much easier to make a good solder joint, and you only need to touch the parts for a second or two.

Feather Pin | LCD Pin
------------ | -------------
3V | Vin
GND | GND
CLK | SCK
MO | MOSI
5 | RST
6 | TFTCS
9 | DC 

![Image](https://github.com/Breazile/MandoPuter/blob/master/Feather.jpg)

### Copy the files to the Feather

![Image](https://github.com/Breazile/MandoPuter/blob/master/MandoPuter.jpg)



Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/Breazile/MandoPuter/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
