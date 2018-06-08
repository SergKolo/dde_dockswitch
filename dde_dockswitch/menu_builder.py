from gi.repository import Gtk
from collections import OrderedDict
import os,json
import dbus_ctrl
import dialogs

def add_menu_item(menu_obj, type=Gtk.MenuItem,
                  icon=None, label="HelloWorld", action=None, args=[]):
    """ dynamic function that can add menu items depending on
        the item type and other arguments"""

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

def add_submenu(top_menu, label="HelloWorld",**kwargs):
    """ utility function for adding submenus"""
    menuitem = Gtk.MenuItem(label)
    if kwargs and 'icon' in kwargs.keys():
        menuitem = Gtk.ImageMenuItem.new_with_label(label)
        menuitem.set_always_show_image(True)
        if '/' in kwargs['icon']:
            icon = Gtk.Image.new_from_file(kwargs['icon'])
        else:
            icon = Gtk.Image.new_from_icon_name(kwargs['icon'], 48)
        menuitem.set_image(icon)
    submenu = Gtk.Menu()
    menuitem.set_submenu(submenu)
    top_menu.append(menuitem)
    menuitem.show()
    return submenu

def build_base_menu(menu_obj):
    controls = add_submenu(menu_obj,label="Indicator Controls")
    base_menu=OrderedDict([
        ("About", {
            "icon": "info",
            "type": Gtk.ImageMenuItem,
            "action": dialogs.show_about
        }),
        ("Exit",{
            "icon": "exit",
            "type": Gtk.ImageMenuItem,
            "action": Gtk.main_quit
        })
    ])

    for key,val in base_menu.items():
        add_menu_item(controls,label=key,**val,args=[])
