#!/usr/bin/env python3
#
# This will just test if app-indicator works for
# a given window manager

import argparse
from gi import require_version

require_version('Gtk', '3.0')
require_version('AppIndicator3', '0.1')

from gi.repository import Gtk, GLib
from gi.repository import AppIndicator3 as appindicator

APPINDICATOR_ID = 'headset-charge-indicator'

global ind
ind = None

def quit_app(source):
    Gtk.main_quit()


if __name__ == "__main__":
    ind = appindicator.Indicator.new(
        APPINDICATOR_ID,
        "edit-delete",
        appindicator.IndicatorCategory.HARDWARE)
    ind.set_status(appindicator.IndicatorStatus.ACTIVE)
    ind.set_label("-1%", '999%')

    # create a menu with an Exit-item
    menu = Gtk.Menu()

    menu_items = Gtk.MenuItem(label="Exit")
    menu.append(menu_items)
    menu_items.connect("activate", quit_app)
    menu_items.show_all()

    ind.set_menu(menu)

    Gtk.main()
