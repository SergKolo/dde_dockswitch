#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright © 2018 Sergiy Kolodyazhnyy <1047481448@qq.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import gi,os,json
gi.require_version('AppIndicator3', '0.1')
from gi.repository import GLib as glib
from gi.repository import AppIndicator3 
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import Gio
from gi.repository.Gdk import ScrollDirection
from collections import OrderedDict

import menu_builder


class DeepinDockSwitch(object):

    def __init__(self):
        self.app = AppIndicator3.Indicator.new(
            'dde_dock_list', "",
            AppIndicator3.IndicatorCategory.OTHER
        )
        self.app.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.make_menu()
        self.app.set_icon("drive-harddisk-symbolik")

    def run(self):
        """ Launches the indicator """
        try:
            Gtk.main()
        except KeyboardInterrupt:
            pass

    def update():
        pass

    def callback():
        pass

    def no_on(self):
        pass


    def make_menu(self, *args):
        """ generates entries in the indicator"""
        if hasattr(self, 'app_menu'):
            for item in self.app_menu.get_children():
                self.app_menu.remove(item)
        self.app_menu = Gtk.Menu()

        menu_builder.build_base_menu(self.app_menu)
        self.app_menu.show_all()
        self.app.set_menu(self.app_menu)



if __name__ == '__main__':
    switch = DeepinDockSwitch()
    switch.run()
