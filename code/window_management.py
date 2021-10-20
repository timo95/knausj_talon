from talon import Module

mod = Module()


@mod.action_class
class Actions:
    def window_maximize():
        """Maximize window to windowed fullscreen"""
    def window_restore():
        """Restore window to original size"""
    def window_menu():
        """Open menu to manage window"""
    def window_overview():
        """Open window overview"""
