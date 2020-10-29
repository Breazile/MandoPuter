# Decoding the Gauntlet Display

This page focuses on decoding the character sequence used in the TV series [The Mandalorian](https://www.starwars.com/series/the-mandalorian) so it can be used to configure an accurate display for cosplay using a [MandoPuter](https://github.com/Breazile/MandoPuter)

<div align="center">
  <img src="GauntletLcd.JPG" height="300px" align="center"/>
  <img src="DisplayZoom.png" height="300px" align="center"/>
</div>

## A New Font

<div align="center">
  <img src="MandoAF-charset.png" height="450px" align="center"/>
</div><br>

If you look closely you will notice that the font used in the gauntlet is different from what was seen in the original Star Wars Series. At this point we lack a complete reference for the font, but we do know 14 characters from the [challenge coin](https://www.bobafettfanclub.com/multimedia/daily/1866/). 

In addition, we have seen one new character on the gauntlet display <img src="Glyphs/NewChar.JPG" height="35px" align="center"/>, but are not 100% sure which character this maps to. I'm assuming it is a J until we have a better reference.

There are a couple of alternate fonts being made that closely match the new type style. They are over on [AurekFonts](https://aurekfonts.github.io/):

[MandoAF](https://aurekfonts.github.io/?font=MandoAF) (the L glyph is not consistent with the challenge coin L)
[Mando Alban's Bane BETA](https://aurekfonts.github.io/?font=AlbansBane) (the L glyph is not consistent with the challenge coin L)

The MandoAF font is based on the [Star Wars: The Mandalorian: The Ultimate Visual Guide](https://starwars.fandom.com/wiki/Star_Wars:_The_Mandalorian:_The_Ultimate_Visual_Guide), and has better typeface spacing compared to Mando Alban's Bane (at least for MandoPuter Use). 

I have a modified version of the MandoAF font with the corrected L glyph (upside down V glyph which is consistent with the 2004 font). I call it the [MandoPuter Font](https://github.com/Breazile/MandoPuter/blob/master/MandoPuter.otf). In addition, I have updated the J glyph to an upside down version of the 8 glyph (same as the current L glyph). The glyph was seen on a gauntlet, but we do not know which character this is assigned to. J is my best guess looking at the 2004 font, and was a duplicate of the I glyph in the MandoAF font anyway.

## Original Series Font

<div align="center">
  <img src="2004Font.JPG" height="250px" align="center"/>
</div><br>

You can see the font decoded from the original Star Wars series over on the [Erikstormtrooper website](http://www.erikstormtrooper.com/mandalorian.htm). It was decoded from the 2004 Star Wars trilogy DVD set.

This font is useful in trying to decode new characters, or at least making an educated guess of which letter a new font character should be assigned to.

## Font References

<div align="center">
  <img src="ChallengeCoin.jpg" height="200px" align="center"/>
</div><br>

The [challenge coin](https://www.bobafettfanclub.com/multimedia/daily/1866/) was a big help in the creation of the new font. It has 14 characters listed and spells out "THE MANDALORIAN" and "THIS IS THE WAY"

## Font Glyph Details
This is the modified font sheet for the characters used in the [MandoPuter Font](https://github.com/Breazile/MandoPuter/blob/master/MandoPuter.otf). The graphic is a modified version of [Mando Alban's Bane [BETA]](https://aurekfonts.github.io/?font=AlbansBane) font sheet with a couple of characters changed according to the table below.

<div align="center">
  <a href="https://aurekfonts.github.io/?font=AlbansBane">
    <img src="https://github.com/Breazile/MandoPuter/blob/master/Glyphs/MandoPuterFont.png" height="450px" align="center"/>
  </a>
</div><br>

ABC | Coin | MandoPuter | MandoAF | 2004 | Notes
:---: | :----: | :---: | :-------: | :---: | :-----
A | <img src="Glyphs/CC-A.png" height="50px" align="center"/> | <img src="Glyphs/N-A.png" height="50px" align="center"/> | <img src="Glyphs/N-A.png" height="50px" align="center"/> | <img src="Glyphs/O-A.png" height="50px" align="center"/> |
B | | <img src="Glyphs/N-B.png" height="50px" align="center"/> | <img src="Glyphs/N-B.png" height="50px" align="center"/> | <img src="Glyphs/O-B.png" height="50px" align="center"/> | |
C | | <img src="Glyphs/N-C.png" height="50px" align="center"/> | <img src="Glyphs/N-C.png" height="50px" align="center"/> | <img src="Glyphs/O-C.png" height="50px" align="center"/> | |
D | <img src="Glyphs/CC-D.png" height="50px" align="center"/> | <img src="Glyphs/N-D.png" height="50px" align="center"/> | <img src="Glyphs/N-D.png" height="50px" align="center"/> | <img src="Glyphs/O-D.png" height="50px" align="center"/> |
E | <img src="Glyphs/CC-E.png" height="50px" align="center"/> | <img src="Glyphs/N-E.png" height="50px" align="center"/> | <img src="Glyphs/N-E.png" height="50px" align="center"/> | <img src="Glyphs/O-E.png" height="50px" align="center"/> |
F | | <img src="Glyphs/N-F.png" height="50px" align="center"/> | <img src="Glyphs/N-F.png" height="50px" align="center"/> | <img src="Glyphs/O-F.png" height="50px" align="center"/> | |
G | | <img src="Glyphs/N-G.png" height="50px" align="center"/> | <img src="Glyphs/N-G.png" height="50px" align="center"/> | <img src="Glyphs/O-G.png" height="50px" align="center"/> | |
H | <img src="Glyphs/CC-H.png" height="50px" align="center"/> | <img src="Glyphs/N-H.png" height="50px" align="center"/> | <img src="Glyphs/N-H.png" height="50px" align="center"/> | <img src="Glyphs/O-H.png" height="50px" align="center"/> |
I | <img src="Glyphs/CC-I.png" height="50px" align="center"/> | <img src="Glyphs/N-I.png" height="50px" align="center"/> | <img src="Glyphs/N-I.png" height="50px" align="center"/> | <img src="Glyphs/O-I.png" height="50px" align="center"/> |
J | | <img src="Glyphs/N-J.png" height="50px" align="center"/> | <img src="Glyphs/N-I.png" height="50px" align="center"/> | <img src="Glyphs/O-J.png" height="50px" align="center"/> | My best guess based on the 2004 font. MandoAF and Mando Alban's Bane BETA uses a duplication of the I glyph
K | | <img src="Glyphs/N-K.png" height="50px" align="center"/> | <img src="Glyphs/N-K.png" height="50px" align="center"/> | <img src="Glyphs/O-K.png" height="50px" align="center"/> | |
L | <img src="Glyphs/CC-L.png" height="50px" align="center"/> | <img src="Glyphs/N-L.png" height="50px" align="center"/> | <img src="Glyphs/N-J.png" height="50px" align="center"/> | <img src="Glyphs/O-L.png" height="50px" align="center"/> | Glyph does not match the challenge coin in MandoAF and Mando Alban's Bane BETA
M | <img src="Glyphs/CC-M.png" height="50px" align="center"/> | <img src="Glyphs/N-M.png" height="50px" align="center"/> | <img src="Glyphs/N-M.png" height="50px" align="center"/> | <img src="Glyphs/O-M.png" height="50px" align="center"/> |
N | <img src="Glyphs/CC-N.png" height="50px" align="center"/> | <img src="Glyphs/N-N.png" height="50px" align="center"/> | <img src="Glyphs/N-N.png" height="50px" align="center"/> | <img src="Glyphs/O-N.png" height="50px" align="center"/> |
O | <img src="Glyphs/CC-O.png" height="50px" align="center"/> | <img src="Glyphs/N-O.png" height="50px" align="center"/> | <img src="Glyphs/N-O.png" height="50px" align="center"/> | <img src="Glyphs/O-O.png" height="50px" align="center"/> |
P | | <img src="Glyphs/N-P.png" height="50px" align="center"/> | <img src="Glyphs/N-P.png" height="50px" align="center"/> | <img src="Glyphs/O-P.png" height="50px" align="center"/> | |
Q | | <img src="Glyphs/N-Q.png" height="50px" align="center"/> | <img src="Glyphs/N-Q.png" height="50px" align="center"/> | <img src="Glyphs/O-Q.png" height="50px" align="center"/> | |
R | <img src="Glyphs/CC-R.png" height="50px" align="center"/> | <img src="Glyphs/N-R.png" height="50px" align="center"/> | <img src="Glyphs/N-R.png" height="50px" align="center"/> | <img src="Glyphs/O-R.png" height="50px" align="center"/> |
S | <img src="Glyphs/CC-S.png" height="50px" align="center"/> | <img src="Glyphs/N-S.png" height="50px" align="center"/> | <img src="Glyphs/N-S.png" height="50px" align="center"/> | <img src="Glyphs/O-S.png" height="50px" align="center"/> |
T | <img src="Glyphs/CC-T.png" height="50px" align="center"/> | <img src="Glyphs/N-T.png" height="50px" align="center"/> | <img src="Glyphs/N-T.png" height="50px" align="center"/> | <img src="Glyphs/O-T.png" height="50px" align="center"/> |
U | | <img src="Glyphs/N-U.png" height="50px" align="center"/> | <img src="Glyphs/N-U.png" height="50px" align="center"/> | <img src="Glyphs/O-U.png" height="50px" align="center"/> | |
V | | <img src="Glyphs/N-V.png" height="50px" align="center"/> | <img src="Glyphs/N-V.png" height="50px" align="center"/> | <img src="Glyphs/O-V.png" height="50px" align="center"/> | |
W | <img src="Glyphs/CC-W.png" height="50px" align="center"/> | <img src="Glyphs/N-W.png" height="50px" align="center"/> | <img src="Glyphs/N-W.png" height="50px" align="center"/> | <img src="Glyphs/O-W.png" height="50px" align="center"/> |
X | | <img src="Glyphs/N-X.png" height="50px" align="center"/> | <img src="Glyphs/N-X.png" height="50px" align="center"/> | <img src="Glyphs/O-X.png" height="50px" align="center"/> | A duplication of the W glyph in MandoAF and Mando Alban's Bane BETA
Y | <img src="Glyphs/CC-Y.png" height="50px" align="center"/> | <img src="Glyphs/N-Y.png" height="50px" align="center"/> | <img src="Glyphs/N-Y.png" height="50px" align="center"/> | <img src="Glyphs/O-Y.png" height="50px" align="center"/> |
Z | | <img src="Glyphs/N-Z.png" height="50px" align="center"/> | <img src="Glyphs/N-Z.png" height="50px" align="center"/> | <img src="Glyphs/O-Z.png" height="50px" align="center"/> | |
0 | | <img src="Glyphs/N-0.png" height="50px" align="center"/> | <img src="Glyphs/N-0.png" height="50px" align="center"/> | <img src="Glyphs/O-0.png" height="50px" align="center"/> | |
1 | | <img src="Glyphs/N-1.png" height="50px" align="center"/> | <img src="Glyphs/N-1.png" height="50px" align="center"/> | <img src="Glyphs/O-1.png" height="50px" align="center"/> | |
2 | | <img src="Glyphs/N-2.png" height="50px" align="center"/> | <img src="Glyphs/N-2.png" height="50px" align="center"/> | <img src="Glyphs/O-2.png" height="50px" align="center"/> | |
3 | | <img src="Glyphs/N-3.png" height="50px" align="center"/> | <img src="Glyphs/N-3.png" height="50px" align="center"/> | <img src="Glyphs/O-3.png" height="50px" align="center"/> | |
4 | | <img src="Glyphs/N-4.png" height="50px" align="center"/> | <img src="Glyphs/N-4.png" height="50px" align="center"/> | <img src="Glyphs/O-4.png" height="50px" align="center"/> | |
5 | | <img src="Glyphs/N-5.png" height="50px" align="center"/> | <img src="Glyphs/N-5.png" height="50px" align="center"/> | <img src="Glyphs/O-5.png" height="50px" align="center"/> | |
6 | | <img src="Glyphs/N-6.png" height="50px" align="center"/> | <img src="Glyphs/N-6.png" height="50px" align="center"/> | <img src="Glyphs/O-6.png" height="50px" align="center"/> | |
7 | | <img src="Glyphs/N-7.png" height="50px" align="center"/> | <img src="Glyphs/N-7.png" height="50px" align="center"/> | <img src="Glyphs/O-7.png" height="50px" align="center"/> | |
8 | | <img src="Glyphs/N-8.png" height="50px" align="center"/> | <img src="Glyphs/N-8.png" height="50px" align="center"/> | <img src="Glyphs/O-8.png" height="50px" align="center"/> | |
9 | | <img src="Glyphs/N-9.png" height="50px" align="center"/> | <img src="Glyphs/N-9.png" height="50px" align="center"/> | <img src="Glyphs/O-9.png" height="50px" align="center"/> | |

## Screen References

Sequences from [The Mandalorian](https://disneyplusoriginals.disney.com/show/the-mandalorian-season-two) episodes - work in progress coming soon. ??? characters means the glyphs have not been identified for the clip.

### The Mandalorian Season 1

#### Episode 1: The Mandalorian
From | To | Sequence | Notes
:----: | :--: | :-------- | :-----
02:11 | 02:16 | ??? | Blury and a lot of motion. Display refresh vs camera frame rate artifacts
02:22 | 02:29 | ??? | Blury and a lot of motion. Display refresh vs camera frame rate artifacts
02:46 | 03:22 | ??? | Out of focus, but you can get some timing information on sequence changes
07:05 | 07:06 | ??? | Out of focus
10:55 | 10:58 | ??? | Out of focus
11:39 | 11:43 | ??? | Out of focus, but you can get some timing information on sequence changes
12:06 | 12:07 | ??? | Out of focus
12:16 | 12:20 | ??? | Out of focus, but you can get some timing information on sequence changes
13:02 | 13:04 | ??? | Out of focus
18:20 | 18:40 | ??? | Out of focus
19:24 | 19:35 | ??? | Out of focus
24:09 | 24:38 | ??? | Out of focus, but you can get some timing information on sequence changes
24:48 | 24:55 | ??? | Out of focus, but you can get some timing information on sequence changes
35:13 | 35:19 | ??? | Out of focus

#### Episode 2: The Child
From | To | Sequence | Notes
:----: | :--: | :-------- | :-----
02:44 | 02:48 | ?ET SAS TRH | Out of focus, best guess
04:42 | 04:46 | ??? | Out of focus
09:55 | 09:66 | ??? ??? | Out of focus, two sequences
10:11 | 10:15 | ??? ??? | Out of focus, at least two sequences
10:21 | 10:24 | ??? ??? | Out of focus, at least two sequences
13:29 | 13:37 | ??? ??? | Out of focus, at least two sequences
17:04 | 17:05 | ??? | Out of focus
17:27 | 17:30 | ??? ??? | Out of focus, at least two sequences
21:32 | 21:37 | ??? ??? | Out of focus, at least two or three sequences
24:27 | 24:39 | TRH A?S | Out of focus
24:48 | 24:53 | JBM MLM SAS AJS SAS | Scene is mirrored, out of focus, compare with Gallery episode #3

#### Episode 3: The Sin
From | To | Sequence | Notes
:----: | :--: | :-------- | :-----
06:29 | 06:35 | SAS TRH SAS ??? | Last sequence not clear
08:21 | 08:26 | ??? | Out of focus
08:46 | 08:55 | ??? | Out of focus
09:19 | 09:23 | ??? | Out of focus, but you can get some timing information on sequence changes
10:19 | 10:24 | ??? | Out of focus, but you can get some timing information on sequence changes
11:22 | 11:30 | ??? | Out of focus, but you can get some timing information on sequence changes
14:47 | 14:50 | ??? ??? ??? | The first time we see the Beskar gauntlet
14:58 | 15:03 | ??? | Out of focus
15:30 | 15:34 | ??? | Has some timing information
15:51 | 16:02 | TRH ??? | Good sequence to decode on a large TV
16:11 | 16:26 | ??? ??? | Has some timing information
20:09 | 20:12 | ??? | 
20:26 | 20:30 | JBM | 
21:21 | 21:23 | ??? TRH | 
21:47 | 21:50 | ??? ??? | Various other short views in the rescue scene up to the whistling birds
23:55 | 24:01 | ??? | 
28:34 | 28:35 | ??? | 
29:59 | 30:01 | TRH | 
30:16 | 30:12 | TRH SAS MLM | SAS is shown for only 2 frames
30:16 | 30:18 | DSC JAS ??? | Could be SAS instead of JAS
30:43 | 30:49 | ??? ??? | 
30:55 | 30:57 | ??? TRH ??? | 
31:06 | 30:13 | ??? TRH ??? | Out of focus

#### Episode 4: Sanctuary
From | To | Sequence | Notes
:----: | :--: | :-------- | :-----
05:59 | 06:00 | ??? | 
07:04 | 07:07 | ??? | 
07:33 | 07:33 | ??? | 
07:35 | 07:37 | ??? | 
07:49 | 07:50 | ??? | Has some timing information
07:55 | 07:58 | ??? | Has some timing information
08:10 | 08:12 | ??? | 
10:05 | 10:08 | ??? |  Good reference for sequence timing/cycling
10:14 | 10:16 | ??? |  Good reference for sequence timing/cycling
10:27 | 10:28 | ??? |  Hard to make out, 2 strings
10:44 | 10:45 | ??? |  Angle hard to make out
12:49 | 12:51 | ??? |  Blurry and angled when clear shot
13:17 | 13:19 | ??? |  Angle makes it hard to decipher. Cant tell if "twitch" cycling is video glitch or new sequence
13:26 | 13:27 | ??? |  
14:47 | 14:47 | ??? |  Blurry until he stops his turn for about ~4 frames
14:55 | 15:05 | ??? |  This would of been perfect had it not been for focus blur. You can make out the timing for what I believe might be the full sequence
16:28 | 16:29 | ??? | 
16:33 | 16:34 | ??? |  Few frames fisible with swing of hand
17:08 | 17:10 | (JQS/SQS/JQJ?) DS(T/C?) SAS TRH MLM  | Quick cycle of 5 or 6 Ehns

### Disney Gallery Star Wars: The Mandalorian

Gauntlet sequences from behind the scenes footage in [Disney Gallery Star Wars: The Mandalorian](https://disneyplusoriginals.disney.com/show/disney-gallery-the-mandalorian). Timestamps are close, and should get you close to when the sequence starts. ??? charaters mean I do not know what they are. Many shots are blurry or too far away to make out clearly.

Episode | From | To | Sequence | Notes
:-------: | :----: | :--: | :---------------- | :-----
#3 | 03:59 | 04:01 | MLM JBM SAS JAS | Assuming the J glyph is correct. Video cuts away after the last sequence and might still be in transition (Beskar)
#3 | 04:09 | 04:13 | ??? TRH ??? | Small text with some detail missing. Might yield some sequences  (Beskar)
#3 | 04:29 | 04:33 | SAS JBM JRS SAS | Assuming the J glyph is correct. Very clear sequence  (no Beskar)
#3 | 04:40 | 04:41 | ??? | Hard to make out, display refresh vs camera frame rate artifacts  (Beskar)
#3 | 09:27 | 09:29 | ??? TRH | Small and slightly out of focus  (Beskar)
#3 | 09:51 | 09:55 | ??? | Small and out of focus  (Beskar)

## Current MandoPuter Sequences that have been decoded

**Episode 2: The Child - 24:48**
```
messages = [ "JBM", "MLM", "SAS", "AJS", "SAS"]
delays =   [  0.50,  0.84,  1.00,  0.35,  0.84]
```

**Episode 3: The Sin - 06:29**
```
messages = [ "SAS", "TRH", "SAS"]
delays =   [  1.00,  0.67,  1.00]
```

**Disney Gallery Star Wars: The Mandalorian episode #3 - 03:59**
```
messages = [ "MLM", "JBM", "SAS", "JAS"]
delays =   [  0.75,  0.75,  0.65, 0.75 ]
```

## Contributions

Thanks to **Luke Dailey** for starting the conversation and sparking renewed interest in finding the sequence. Also thanks to Luke for pointing me to the AurekFont fonts.

Thanks to **Aldo Andrei** for pouring through video clips and putting together the most accurate sequence for the MandoPuter.

Thanks to the many folks in the Mandalorian Facebook groups who are always willing to pitch in and help: 

- [The Mandalorian (costume and prop builders)](https://www.facebook.com/groups/495779494260405)
- [The MANDALORIAN- Din Djarin Costumers Guild](https://www.facebook.com/groups/594812984625855)
- [The Mandalorian - Costuming Group](https://www.facebook.com/groups/1175965535908616)
- [Mandalorian Costuming](https://www.facebook.com/groups/mandaloriancostuming)
