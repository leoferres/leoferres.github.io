---
layout: post
comments: true
title:  "Brief History Of Character Sets"
date:   2016-10-23 11:41:10 -0300
tags: [history, charsets]
---

The following is a short note I wrote on the history of character
sets. Here you can find
[the pdf](/assets/main.pdf).

<!--more-->

This document has been typeset with ```XeLaTeX```, using the
Emacs23-snapshot (gtk) and Ubuntu Hardy Heron. The pdf uses many
fonts, the best I could find for every script, together with the
website where I found it.


### Fonts

First install the fonts, I used:

~~~bash
sudo apt install fonts-linuxlibertine fonts-mph-2b-damase fonts-ancient-scripts
~~~

and in your ```tex``` file:

~~~tex
\newfontinstance{\greek}{Linux Libertine O} % Greek
\newfontinstance{\phoenician}{MPH 2B Damase} % Phoenician
\newfontinstance{\hieroglyph}{Aegyptus} % Egyptian
~~~

```XeLaTeX``` has changed since I first wrote this document, so I had
to do the following hack:

~~~tex
\let\newfontinstance=\newfontfamily
~~~

### Emacs and Unicode:

Emacs23 deals with Unicode nicely. In order to change the input
method; that is, in order to change the script, use ```ucs-insert```,
and the Unicode hexadecimal number. For example, for the G1 vulture in
the hyeroglyphs, use ```ucs-insert``` and the type ```F3B7A```.
