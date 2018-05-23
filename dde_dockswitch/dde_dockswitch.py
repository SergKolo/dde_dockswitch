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


class DeepinDockSwitch(object):

    def __init__(self):
        self.app = AppIndicator3.Indicator.new(
            'dde_dock_list', "",
            AppIndicator3.IndicatorCategory.OTHER
        )
        self.app.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.make_menu()
        self.app.set_icon("drive-harddisk-symbolik")

#    def quit(self,*args):
#        """ closes indicator """
#        Gtk.main_quit()

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


    def make_menu(self, *args):
        """ generates entries in the indicator"""
        if hasattr(self, 'app_menu'):
            for item in self.app_menu.get_children():
                self.app_menu.remove(item)
        self.app_menu = Gtk.Menu()


        with open(os.path.join(os.path.dirname(__file__),'base_menu.json') ) as menu_file:
             base_menu = json.load(menu_file)
             for key,val in base_menu.items():
                 val["type"] = eval(val["type"])
                 val["action"] = eval(val["action"])
                 self.add_menu_item(self.app_menu,label=key,**val,args=[None])
             # Add dymic eval of type and action
        self.app.set_menu(self.app_menu)
        self.app_menu.show_all()

# TODO: edit. alot
    def add_menu_item(self, menu_obj, type=Gtk.MenuItem,
                      icon=None, label="HelloWorld", action=None, args=[]):
        """ dynamic function that can add menu items depending on
            the item type and other arguments"""
        #print(label,type,action)

        menu_item = None
        if type is Gtk.ImageMenuItem and label:
            menu_item = Gtk.ImageMenuItem.new_with_label(label)
            menu_item.set_always_show_image(True)
            if '/' in icon:
                icon = Gtk.Image.new_from_file(icon)
            else:
                icon = Gtk.Image.new_from_icon_name(icon, 48)
            menu_item.set_image(icon)
        elif type is Gtk.ImageMenuItem and not label:
            menu_item = Gtk.ImageMenuItem()
            menu_item.set_always_show_image(True)
            if '/' in icon:
                icon = Gtk.Image.new_from_file(icon)
            else:
                icon = Gtk.Image.new_from_icon_name(icon, 16)
            menu_item.set_image(icon)
        elif type is Gtk.MenuItem:
            menu_item = Gtk.MenuItem(label)
        elif type is Gtk.SeparatorMenuItem:
            menu_item = Gtk.SeparatorMenuItem()
        if action:
            menu_item.connect('activate', action, *args)
        menu_obj.append(menu_item)
        menu_obj.show()



if __name__ == '__main__':
    switch = DeepinDockSwitch()
    switch.run()
