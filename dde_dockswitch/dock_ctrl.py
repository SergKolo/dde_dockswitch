# functions responsible for Deepin dock control
import dbus_ctrl

dock_obj = [ "session", "com.deepin.dde.daemon.Dock", 
                "/com/deepin/dde/daemon/Dock", "com.deepin.dde.daemon.Dock"]

def get_desk_files(onlydocked=True):
    """ Obtains .desktop files of entries currently on the dock.
        Defaults to returning only those that are pinned to dock.
        If onlydocked=False, all entries on the dock (including 
        running but not pinned entries) get returned"""
    desk_files = []
    global dock_obj    
    for i in dbus_ctrl.get_dbus_property(*dock_obj,"Entries"):
        entry_obj = [ "session","com.deepin.dde.daemon.Dock", i, 
                      "com.deepin.dde.daemon.Dock.Entry", "DesktopFile"]
        desktop_file = dbus_ctrl.get_dbus_property(*entry_obj)
        if onlydocked and not dbus_ctrl.call_dbus_method(*dock_obj,"IsDocked",[desktop_file]):
            continue
        desktop_file = dbus_ctrl.get_dbus_property(*entry_obj)
        desk_files.append(str(desktop_file))
    return desk_files

def clear_dock():
    """  Undocks all entries. Running appications will still 
         appear but won't be pinned"""
    global dock_obj
    for desk_file in get_docked_desk_files():
        dbus_ctrl.call_dbus_method(*dock_obj,"RequestUndock",[desk_file])

def fill_dock(desk_files):
    """ Fills the dock with Entries as provided by desk_files list,
        in the order they appear on the list"""
    global dock_obj
    for index,desk_file in enumerate(desk_files):
        dbus_ctrl.call_dbus_method(*dock_obj,"RequestDock",[desk_file,index])
