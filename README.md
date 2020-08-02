[![Build Status](https://travis-ci.org/centic9/headset-charge-indicator.svg)](https://travis-ci.org/centic9/headset-charge-indicator)
[![Tag](https://img.shields.io/github/tag/centic9/headset-charge-indicator.svg)](https://github.com/centic9/headset-charge-indicator/tags)

A simple app-indicator for GNOME desktops to provide support for controlling some features of
a number of wireless headsets.

![Screenshot](headset-charge-indicator.png)

It supports displaying the battery charge, turning on/off LEDs and adjusting the sidetone level of the microphone. 

It additionally supports displaying the 'chat-mix' level of Steelseries Arctis headphones.

It uses the tool from https://github.com/Sapd/HeadsetControl/ for connecting to a number of
popular headsets and fetches information to display it in the app-indicator bar
on the desktop.

If an additional external script is provided, it also allows to switch between sending sound to the soundcard or to
the Headset and record from the correct microphone.

## Installation

On Ubuntu/Debian based distributions, install the following packages

    sudo apt-get install python3-gi libappindicator3-1 gnome-icon-theme gir1.2-appindicator3-0.1

On other distributions, you might need to install `pygobject`, but this is untested, PRs with 
more information welcome!

### Building HeadsetControl

Follow the instructions at https://github.com/Sapd/HeadsetControl/ for building the binary and
note down the path to it.

You can test the helper application manually via `headsetcontrol -b -c`, this should print the current
battery level to the console.

## Usage

Build/install the required executable `headseatcontrol` according to the instructions 
above then start it via 

    python3 headset-charge-indicator.py <location of headsetcontrol-executable>

A Headset-icon should appear in the area for app-indicators together with a percentage number.

If you provide a second commandline argument, an additional "Switch" menu will be added with 
options to switch between Soundcard and Headset. The provided application or script will be
invoked with "1" for soundcard and "2" for headset.

A script can for example use pactl and/or pacmd to send audio output to the correct endpoint
as well as setting audio input to the correct microphone.

## Supported Headsets

Look at the description of https://github.com/Sapd/HeadsetControl/, headset which support 
at least fetching battery information are supported here as well, other functionality will work 
if the headset supports it.

## Supported Desktop Envrionemnts

The tool uses Python Bindings for the GNOME appindicator functionality. So it is mainly supported on this desktop environment. 

However some other Desktop environments have some support for appindicators, so it might be possible to run this tool on other desktop environments as well.

Currently known behavior/support:

* GNOME: Works fully
* Cinnamon: Seems to work, but percentage is not displayed as part of the indicator-icon
* KDE/Plasma: Seems to work, but percentage is not displayed as part of the indicator-icon
* MATE: Runs, but does not display an icon
* LXDE: Runs, but does not display an icon
* Budgie: Runs, but does not display an icon
* XFCE: Runs, but indicator-icon only appears for a very short time and then disappears again
* OpenBox: ??

Please let me know via an issue if you successfully run it on another desktop environment or know of
a way to make it run better on any of those desktop environments!

## Debugging

The python application will print out some information to standard-output which may give some
more information if things go wrong.

## Licensing

* headset-charge-indicator is licensed under the [BSD 2-Clause License].

[BSD 2-Clause License]: https://opensource.org/licenses/bsd-license.php

## Like it?

If you like my software please star the repository.

If you find this application useful and would like to support it, you can [Sponsor the author](https://github.com/sponsors/centic9)

