concerton-controller
====================

A project that transforms a old [Concerton V5076](http://www.radiomuseum.org/r/conserton_wien_v5076.html) to a music server.

This repository contains a python script that starts listening to the GPIO of a Raspberry Pi and translates that input to MPD-commands. Those commands (play, pause, etc.) are sent to Mopidy, which is running on the Raspberry Pi. The GPIO ports are connected to a [Concerton V5076](http://www.radiomuseum.org/r/conserton_wien_v5076.html).

The Concerton V5076:

<img src="https://dl.dropboxusercontent.com/u/15951523/Bilder/20140213_153244.jpg" alt="Concerton V5076" style="max-width: 300px">

wired to a Raspberry Pi:

<img src="https://dl.dropboxusercontent.com/u/15951523/Bilder/20140305_192929.jpg" alt="Raspberry Pi" style="max-width: 300px">

The inside of the Concerton V5076:

<img src="https://dl.dropboxusercontent.com/u/15951523/Bilder/20140305_192945.jpg" alt="Inside of the Concerton" style="max-width: 300px">
