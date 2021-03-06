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

import subprocess

import menu_builder, dialogs,config_ctrl,dbus_ctrl,dock_ctrl


class DeepinDockSwitch(object):

    all_lists = OrderedDict()

    def __init__(self):
        self.app = AppIndicator3.Indicator.new(
            'dde_dock_list', "",
            AppIndicator3.IndicatorCategory.OTHER
        )

        config_file = os.path.join(os.environ["HOME"],".config/dde_dockswitch/docklists.json")

        self.app.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.make_menu()

        icon = '/usr/share/pixmaps/dde_dockswitch_icon.png'
        if os.path.exists(icon):
            self.app.set_icon(icon)
        else:
            icon = os.path.join(os.path.dirname(__file__),'dde_dockswitch_icon.png')
            self.app.set_icon(icon)

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
        global all_lists
        if hasattr(self, 'app_menu'):
            for item in self.app_menu.get_children():
                self.app_menu.remove(item)
        self.app_menu = Gtk.Menu()

        # Wrappers for menu entries that call refresh on main menu

        def fill_dock_and_update(ignore,fill):
             dock_ctrl.fill_dock(None,fill)
             self.make_menu()

        def remove_entry_wrap(ignore):
            dialogs.remove_entry_diag()
            self.make_menu()

        all_lists = config_ctrl.read_config_file()
        for list_label,desk_files in all_lists.items():
            if desk_files == list(dock_ctrl.get_desk_files()):
                list_label = "\u2605 " + list_label 
            item_params={ "label": list_label, 
                          "action": fill_dock_and_update,
                          "args": [desk_files]
            }
            menu_builder.add_menu_item(self.app_menu,**item_params)

        menu_builder.add_menu_item(self.app_menu,type=Gtk.SeparatorMenuItem)

        dock_controls = [
            { "label": "Save", 
              "type": Gtk.ImageMenuItem,
              "icon": "gtk-save", 
              "action": self.record_currently_docked,
              "args":[] },

            { "label": "Rotate",
              "type": Gtk.ImageMenuItem,
              "icon": "object-flip-vertical",
              "action": dock_ctrl.rotate_dock,
              "args": []},

            { "label": "Remove",
              "type": Gtk.ImageMenuItem,
              "icon": "list-remove",
              "action": remove_entry_wrap,
              "args": []},

            { "label": "Clear",
              "type": Gtk.ImageMenuItem,
              "icon": "user-trash",
              "action": dock_ctrl.clear_dock,
              "args": []}
        ]

        dock_ctrl_submenu = menu_builder.add_submenu(self.app_menu,label="Dock Controls")
        for i in dock_controls:
            menu_builder.add_menu_item(dock_ctrl_submenu,**i)

        menu_builder.build_base_menu(self.app_menu)
        self.app_menu.show_all()
        self.app.set_menu(self.app_menu)

    def record_currently_docked(self,*args):
        global all_lists
        docked_desk_files = dock_ctrl.get_desk_files(onlydocked=True)
        name = self.run_cmd(['zenity','--entry', 
                      '--text',"Name this list",
                      '--entry-text',"Default entry"]).decode().rstrip()
        if name:
            # this probably will have to be global
            all_lists = {**all_lists,name: docked_desk_files}
            config_ctrl.write_config_file(all_lists)
            self.make_menu()
        


    def run_cmd(self, cmdlist):
        """ utility: reusable function for running external commands """
        try:
            stdout = subprocess.check_output(cmdlist)
        except subprocess.CalledProcessError:
            # TODO
            pass
        else:
            if stdout:
                return stdout


        

if __name__ == '__main__':
    switch = DeepinDockSwitch()
    switch.run()
