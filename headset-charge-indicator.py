#!/usr/bin/env python3
#
# Simple AppIndicator which uses the HeadsetControl application from 
# https://github.com/Sapd/HeadsetControl/ for retrieving charge information
# for wireless headsets and displays it as app-indicator
#
#
# Simple start this application as background process, i.e. during
# startup of the graphical desktop

from sys import argv
from gi.repository import Gtk, GLib
from gi.repository import AppIndicator3 as appindicator
from subprocess import check_output, CalledProcessError

APPINDICATOR_ID = 'headset-charge-indicator'

global HEADSETCONTROL_BINARY
HEADSETCONTROL_BINARY = None

OPTION_BATTERY = '-b'
OPTION_SILENT = '-c'
OPTION_CHATMIX = '-m'
OPTION_SIDETONE = '-s'
OPTION_LED = '-l'

global ind
ind = None
global chatmix
chatmix = None

def change_label(dummy):
    try:
        output=check_output([HEADSETCONTROL_BINARY,OPTION_BATTERY,OPTION_SILENT] )
        print('Bat: ' + str(output, 'utf-8'))
        ind.set_label(str(output, 'utf-8') + '%', '999%')
        if int(output) < 30:
            ind.set_status (appindicator.IndicatorStatus.ATTENTION)
        else:
            ind.set_status (appindicator.IndicatorStatus.ACTIVE)
    except CalledProcessError as e:
        print(e)
        ind.set_label('N/A', '999%')

    return True

def change_chatmix(dummy):
    try:
        output=check_output([HEADSETCONTROL_BINARY,OPTION_CHATMIX,OPTION_SILENT] )
        print("ChatMix: " + str(output, 'utf-8'))
        chatmix.get_child().set_text('ChatMix: ' + str(output, 'utf-8'))
    except CalledProcessError as e:
        print(e)
        menu.get_child().set_text('N/A')

    return True

def set_sidetone(dummy, level):
    print("Set sidetone to: " + str(level))
    try:
        output=check_output([HEADSETCONTROL_BINARY,OPTION_SIDETONE,str(level),OPTION_SILENT] )
        print("Result: " + str(output, 'utf-8'))
    except CalledProcessError as e:
        print(e)

    return True

def set_led(dummy, level):
    print("Set LED to: " + str(level))
    try:
        output=check_output([HEADSETCONTROL_BINARY,OPTION_LED,str(level),OPTION_SILENT] )
        print("Result: " + str(output, 'utf-8'))
    except CalledProcessError as e:
        print(e)

    return True

def sidetone_menu():
    # we map 5 levels to the range of [0-128]
    # The Steelseries Arctis internally supports 0-0x12, i.e. 0-18
#    OFF -> 0
#    LOW -> 32
#    MEDIUM -> 64
#    HIGH -> 96
#    MAX -> 128

    sidemenu = Gtk.Menu()

    off = Gtk.MenuItem("off")
    off.connect("activate", set_sidetone, 0)
    sidemenu.append(off)
    off.show_all()

    low = Gtk.MenuItem("low")
    low.connect("activate", set_sidetone, 32)
    sidemenu.append(low)
    low.show_all()

    medium = Gtk.MenuItem("medium")
    medium.connect("activate", set_sidetone, 64)
    sidemenu.append(medium)
    medium.show_all()

    high = Gtk.MenuItem("high")
    high.connect("activate", set_sidetone, 96)
    sidemenu.append(high)
    high.show_all()

    maximum = Gtk.MenuItem("max")
    maximum.connect("activate", set_sidetone, 128)
    sidemenu.append(maximum)
    maximum.show_all()

    return sidemenu

def led_menu():
    ledmenu = Gtk.Menu()

    off = Gtk.MenuItem("off")
    off.connect("activate", set_led, 0)
    ledmenu.append(off)
    off.show_all()

    on = Gtk.MenuItem("on")
    on.connect("activate", set_led, 1)
    ledmenu.append(on)
    on.show_all()

    return ledmenu

def refresh(dummy):
    change_label(None)
    change_chatmix(None)

def quit(source):
    Gtk.main_quit()

if __name__ == "__main__":
  if len(argv) != 2:
    print("Need one commandline argumetn for the location of the HeadsetControl binary")
    exit(1)

  HEADSETCONTROL_BINARY = argv[1]

  ind = appindicator.Indicator.new (
                        APPINDICATOR_ID,
                        "audio-headset",
                        appindicator.IndicatorCategory.HARDWARE )
  ind.set_status (appindicator.IndicatorStatus.ACTIVE)
  # no icon found yet: ind.set_attention_icon ("indicator-messages-new")
  ind.set_label("-1%", '999%')

  # create a menu with an Exit-item
  menu = Gtk.Menu()
  
  menu_items = Gtk.MenuItem("Refresh")
  menu.append(menu_items)
  menu_items.connect("activate", refresh)
  menu_items.show_all()
  
  menu_items = Gtk.MenuItem("Chat: -1")
  menu.append(menu_items)
  menu_items.show_all()
  chatmix = menu_items

  menu_items = Gtk.MenuItem("Sidetone")
  menu.append(menu_items)
  menu_items.show_all()
  menu_items.set_submenu(sidetone_menu())

  menu_items = Gtk.MenuItem("LED")
  menu.append(menu_items)
  menu_items.show_all()
  menu_items.set_submenu(led_menu())
  
  menu_items = Gtk.MenuItem("Exit")
  menu.append(menu_items)
  menu_items.connect("activate", quit)
  menu_items.show_all()
  
  ind.set_menu(menu)

  # update printed charge every 60 seconds
  GLib.timeout_add(60000, change_label, None)
  GLib.timeout_add(60000, change_chatmix, None)

  # refresh values right away
  change_label(None)
  change_chatmix(None)

  Gtk.main()
