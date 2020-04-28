A simple app-indicator for GNOME desktops to display the battery charge of some wirless headsets.

It uses the tool from https://github.com/Sapd/HeadsetControl/ for connecting to a number of
popular headsets and fetches battery charge information to display it in the app-indicator bar
on the desktop.

## Installation

On Ubuntu/Debian based distributions, install the following packages

    sudo apt-get install python3-gi libappindicator3-dev gnome-icon-theme

On others, you might need to install `pygobject`, but this is untested, PRs with more information welcome!

### Building HeadsetControl

Follow the instructions at https://github.com/Sapd/HeadsetControl/ for building the binary and
note down the path to it.

You can check the helper application manually via `headsetcontrol -b -c`

## Usage

Build/install according to the instructions above then start it via 

    `python3 headset-charge-indicator.py` <location of headsetcontrol>

A Headset-icon should appear in the area for app-indicators together with a percentage numbers.

## Supported Headsets

Look at the description of https://github.com/Sapd/HeadsetControl/, any headset which supports 
fetching battery is supported here as well.

## Notice

This application is distributed in the hope that it will be useful,\
but WITHOUT ANY WARRANTY; without even the implied warranty of\
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\
GNU General Public License for more details.

## License

Released under GPL v3.

## Like it?

If you like my software please star the repository.
