import os
from gi.repository import Gtk
import subprocess
import config_ctrl

def show_about(*args):
    print(args)
    builder = Gtk.Builder()
    builder.add_from_file(os.path.join( 
            os.path.dirname(__file__),
            'dde_dockswitch_about.glade'  ) )
    #print([ i.get_children() for i in builder.get_objects() ])

    # might be better to get children of the 
    # ButtonBox and actually connect Close button
    # to a signal handler
    
    w = builder.get_object("about_dialog")
    response = w.run()
    print("Response",response)
    w.destroy()


def remove_entry_diag(*args):

    dialog = [
        'zenity', '--list', '--checklist', '--title', 
        "Select lists to remove", '--column', "", '--column', "Lists",
    ] 
    lists = config_ctrl.read_config_file()
    
    for i in  lists.keys():
        dialog.append('FALSE')
        dialog.append(i)

    out = subprocess.check_output(dialog).decode().strip()

    for list_name in out.split('|'):
        lists.pop(list_name)

    config_ctrl.write_config_file(lists) 
