#!/usr/bin/env python
#
# Simple AppIndicator which uses the HeadsetControl application from 
# https://github.com/Sapd/HeadsetControl/ for retrieving charge information
# for wireless headsets and displays it as app-indicator
#
#
# Simple start this application as background process, i.e. during
# startup of the graphical desktop


from gi.repository import Gtk, GLib
from gi.repository import AppIndicator3 as appindicator
from subprocess import check_output

APPINDICATOR_ID = 'headphonecharge'

def change_label(ind):
    output=check_output(["/home/dstadler/HeadsetControl/build/headsetcontrol","-b","-c"] )
    print(output)
    ind.set_label(output + '%', '           ')
    if int(output) < 30:
        ind.set_status (appindicator.IndicatorStatus.ATTENTION)
    else:
        ind.set_status (appindicator.IndicatorStatus.ACTIVE)

    return True

def quit(source):
    Gtk.main_quit()

if __name__ == "__main__":
  ind = appindicator.Indicator.new (
                        "headphonecharge",
                        "audio-headset",
                        appindicator.IndicatorCategory.HARDWARE )
  ind.set_status (appindicator.IndicatorStatus.ACTIVE)
  # no icon found yet: ind.set_attention_icon ("indicator-messages-new")
  ind.set_label("-1%", '           ')
  
  # refresh value right away
  change_label(ind)

  # create a menu with an Exit-item
  menu = Gtk.Menu()
  menu_items = Gtk.MenuItem("Exit")
  menu.append(menu_items)
  menu_items.connect("activate", quit)
  menu_items.show_all()
  ind.set_menu(menu)

  # update printed charge every 60 seconds
  GLib.timeout_add(60000, change_label, ind)

  Gtk.main()
