# Decoding the Gauntlet Display

This page focuses on decoding the character sequence used in the TV series [The Mandalorian](https://www.starwars.com/series/the-mandalorian) so it can be used to configure an accurate display for cosplay using a [MandoPuter](https://github.com/Breazile/MandoPuter)

<div align="center">
  <img src="GauntletLcd.JPG" height="300px" align="center"/>
  <img src="DisplayZoom.png" height="300px" align="center"/>
</div>

## A New Font

<div align="center">
  <img src="MandoAF-charset.png" height="450px" align="center"/>
</div>


If you look closely you will notice that the font used in the gauntlet is different from what was seen in the original Star Wars Series. At this point we lack a complete reference for the font, but we do know 14 characters from the [challenge coin](https://www.bobafettfanclub.com/multimedia/daily/1866/). 

In addition, we have seen one new character on the gauntlet display <img src="Glyphs/NewChar.JPG" height="35px" align="center"/>, but are not 100% sure which character this maps to, but I'm assuming it is a J until we have a better reference.

There are a couple of alternate fonts being made that closely match the new type style. They are over on [AurekFonts](https://aurekfonts.github.io/):

[MandoAF](https://aurekfonts.github.io/?font=MandoAF) (the L glyph is not consistent with the challenge coin L)
[Mando Alban's Bane BETA](https://aurekfonts.github.io/?font=AlbansBane) (the L glyph is not consistent with the challenge coin L)

The MandoAF font is based on the [Star Wars: The Mandalorian: The Ultimate Visual Guide](https://starwars.fandom.com/wiki/Star_Wars:_The_Mandalorian:_The_Ultimate_Visual_Guide), and has better typeface spacing compared to Mando Alban's Bane (at least for MandoPuter Use). 

I have a modified version of the MandoAF font with the corrected L glyph (upside down V glyph which is consistent with the 2004 font). I call it the [MandoPuter Font](https://github.com/Breazile/MandoPuter/blob/master/MandoPuter.otf). In addition, I have updated the J glyph to an upside down version of the 8 glyph (same as the current L glyph). The glyph was seen on a gauntlet, but we do not know which character this is assigned to. J is my best guess looking at the 2004 font, and was a duplicate of the I glyph in the MandoAF font anyway.

## Original Series Font

<div align="center">
  <img src="2004Font.JPG" height="450px" align="center"/>
</div>


You can see the font decoded from the original Star Wars series over on the [Erikstormtrooper website](http://www.erikstormtrooper.com/mandalorian.htm). It was decoded from the 2004 Star Wars trilogy DVD set.

This font is useful in trying to decode new characters, or at least making an educated guess of which letter a new font character should be assigned to.

## Font References

![Image](ChallengeCoin.jpg)


The [challenge coin](https://www.bobafettfanclub.com/multimedia/daily/1866/) was a big help in the creation of the new font. It has 14 characters listed and spells out "THE MANDALORIAN" and "THIS IS THE WAY"

## Font Glyph Details

The MandoPuter column shows the gliphs that I am using in the MandoPuter distribution and is the most accurate font that I am aware of.

ABC | Coin | MandoPuter | 2004 | Notes
--- | ---- | --- | --- | -----
A | <img src="Glyphs/CC-A.png" height="76px" align="center"/> | <img src="Glyphs/N-A.png" height="76px" align="center"/> | <img src="Glyphs/O-A.png" height="76px" align="center"/> |
A | ![Image](Glyphs/CC-A.png) | ![Image](Glyphs/N-A.png) | ![Image](Glyphs/O-A.png) |
B | | ![Image](Glyphs/N-B.png) | ![Image](Glyphs/O-B.png) |
C | | ![Image](Glyphs/N-C.png) | ![Image](Glyphs/O-C.png) |
D | ![Image](Glyphs/CC-D.png) | ![Image](Glyphs/N-D.png) | ![Image](Glyphs/O-D.png) |
E | ![Image](Glyphs/CC-E.png) | ![Image](Glyphs/N-E.png) | ![Image](Glyphs/O-E.png) |
F | | ![Image](Glyphs/N-F.png) | ![Image](Glyphs/O-F.png) |
G | | ![Image](Glyphs/N-G.png) | ![Image](Glyphs/O-G.png) |
H | ![Image](Glyphs/CC-H.png) | ![Image](Glyphs/N-H.png) | ![Image](Glyphs/O-H.png) |
I | ![Image](Glyphs/CC-I.png) | ![Image](Glyphs/N-I.png) | ![Image](Glyphs/O-I.png) |
J | | ![Image](Glyphs/N-J.png) | ![Image](Glyphs/O-J.png) | My best guess based on the 2004 font. MandoAF and Mando Alban's Bane BETA uses a duplication of the I glyph
K | | ![Image](Glyphs/N-K.png) | ![Image](Glyphs/O-K.png) |
L | ![Image](Glyphs/CC-L.png) | ![Image](Glyphs/N-L.png) | ![Image](Glyphs/O-L.png) | Glyph is incorrect in MandoAF and Mando Alban's Bane BETA
M | ![Image](Glyphs/CC-M.png) | ![Image](Glyphs/N-M.png) | ![Image](Glyphs/O-M.png) |
N | ![Image](Glyphs/CC-N.png) | ![Image](Glyphs/N-N.png) | ![Image](Glyphs/O-N.png) |
O | ![Image](Glyphs/CC-O.png) | ![Image](Glyphs/N-O.png) | ![Image](Glyphs/O-O.png) |
P | | ![Image](Glyphs/N-P.png) | ![Image](Glyphs/O-P.png) |
Q | | ![Image](Glyphs/N-Q.png) | ![Image](Glyphs/O-Q.png) |
R | ![Image](Glyphs/CC-R.png) | ![Image](Glyphs/N-R.png) | ![Image](Glyphs/O-R.png) |
S | ![Image](Glyphs/CC-S.png) | ![Image](Glyphs/N-S.png) | ![Image](Glyphs/O-S.png) |
T | ![Image](Glyphs/CC-T.png) | ![Image](Glyphs/N-T.png) | ![Image](Glyphs/O-T.png) |
U | | ![Image](Glyphs/N-U.png) | ![Image](Glyphs/O-U.png) |
V | | ![Image](Glyphs/N-V.png) | ![Image](Glyphs/O-V.png) |
W | ![Image](Glyphs/CC-W.png) | ![Image](Glyphs/N-W.png) | ![Image](Glyphs/O-W.png) |
X | | ![Image](Glyphs/N-X.png) | ![Image](Glyphs/O-X.png) | A duplication of the W glyph in MandoAF and Mando Alban's Bane BETA
Y | ![Image](Glyphs/CC-Y.png) | ![Image](Glyphs/N-Y.png) | ![Image](Glyphs/O-Y.png) |
Z | | ![Image](Glyphs/N-Z.png) | ![Image](Glyphs/O-Z.png) |
0 | | ![Image](Glyphs/N-0.png) | ![Image](Glyphs/O-0.png) |
1 | | ![Image](Glyphs/N-1.png) | ![Image](Glyphs/O-1.png) |
2 | | ![Image](Glyphs/N-2.png) | ![Image](Glyphs/O-2.png) |
3 | | ![Image](Glyphs/N-3.png) | ![Image](Glyphs/O-3.png) |
4 | | ![Image](Glyphs/N-4.png) | ![Image](Glyphs/O-4.png) |
5 | | ![Image](Glyphs/N-5.png) | ![Image](Glyphs/O-5.png) |
6 | | ![Image](Glyphs/N-6.png) | ![Image](Glyphs/O-6.png) |
7 | | ![Image](Glyphs/N-7.png) | ![Image](Glyphs/O-7.png) |
8 | | ![Image](Glyphs/N-8.png) | ![Image](Glyphs/O-8.png) |
9 | | ![Image](Glyphs/N-9.png) | ![Image](Glyphs/O-9.png) |

## Screen References

### The Mandalorian Season 1

Sequences from The Mandalorian episodes - work in progress coming soon

Episode | From | To | Sequence | Notes
--- | ---- | --- | --- | -----
Episode #1 - The Mandalorian | 02:11 | 02:16 | ??? | Blury and a lot of motion. Display refresh vs camera frame rate artifacts
Episode #1 - The Mandalorian | 02:22 | 02:29 | ??? | Blury and a lot of motion. Display refresh vs camera frame rate artifacts
Episode #1 - The Mandalorian | 02:46 | 03:22 | ??? | Out of focus, but you can get some timing information on sequence changes
Episode #1 - The Mandalorian | 07:05 | 07:06 | ??? | Out of focus
Episode #1 - The Mandalorian | 10:55 | 10:58 | ??? | Out of focus
Episode #1 - The Mandalorian | 11:39 | 11:43 | ??? | Out of focus, but you can get some timing information on sequence changes
Episode #1 - The Mandalorian | 12:06 | 12:07 | ??? | Out of focus
Episode #1 - The Mandalorian | 12:16 | 12:20 | ??? | Out of focus, but you can get some timing information on sequence changes
Episode #1 - The Mandalorian | 13:02 | 13:04 | ??? | Out of focus
Episode #1 - The Mandalorian | 18:20 | 18:40 | ??? | Out of focus
Episode #1 - The Mandalorian | 19:24 | 19:35 | ??? | Out of focus
Episode #1 - The Mandalorian | 24:09 | 24:38 | ??? | Out of focus, but you can get some timing information on sequence changes
Episode #1 - The Mandalorian | 24:48 | 24:55 | ??? | Out of focus, but you can get some timing information on sequence changes
Episode #1 - The Mandalorian | 35:13 | 35:19 | ??? | Out of focus

### Disney Gallery Star Wars: The Mandalorian

Gauntlet sequences from behind the scenes footage in [Disney Gallery Star Wars: The Mandalorian](https://disneyplusoriginals.disney.com/show/disney-gallery-the-mandalorian). Timestamps are close, and should get you close to when the sequence starts. ??? charaters mean I do not know what they are. Many shots are blurry or too far away to make out clearly.

Episode | From | To | Sequence | Notes
--- | ---- | --- | --- | -----
Episode #3 - Cast | 03:59 | 04:01 | MLM JBM SAS JAS | Assuming the J glyph is correct. Video cuts away after the last sequence and might still be in transition
Episode #3 - Cast | 04:09 | 04:13 | ??? ??? ??? ??? TRH ??? | Small text with some detail missing. Might yield some sequences
Episode #3 - Cast | 04:29 | 04:33 | SAS JBM JRS SAS | Assuming the J glyph is correct. Very clear sequence
Episode #3 - Cast | 04:40 | 04:41 | ??? | Hard to make out, display refresh vs camera frame rate artifacts
Episode #3 - Cast | 09:27 | 09:29 | ??? TRH | Small and slightly out of focus
Episode #3 - Cast | 09:51 | 09:55 | ??? | Small and out of focus

## Current MandoPuter Sequence

Work in progress, coming soon

## Contributions

Thanks to **Luke Dailey** for starting the conversation and sparking renewed interest in finding the sequence. Also thanks to Luke for pointing me to the AurekFont fonts.

Thanks to **Aldo Andrei** for pouring through video clips and putting together the most accurate sequence for the MandoPuter.

Thanks to the many folks in the Mandalorian Facebook groups who are always willing to pitch in and help: 

- [The Mandalorian (costume and prop builders)](https://www.facebook.com/groups/495779494260405)
- [The MANDALORIAN- Din Djarin Costumers Guild](https://www.facebook.com/groups/594812984625855)
- [The Mandalorian - Costuming Group](https://www.facebook.com/groups/1175965535908616)
- [Mandalorian Costuming](https://www.facebook.com/groups/mandaloriancostuming)
