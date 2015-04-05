# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from locale import gettext as _

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('webthief')

from webthief_lib import Window
from webthief.AboutWebthiefDialog import AboutWebthiefDialog
from webthief.PreferencesWebthiefDialog import PreferencesWebthiefDialog

# See webthief_lib.Window.py for more details about how this class works
class WebthiefWindow(Window):
    __gtype_name__ = "WebthiefWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(WebthiefWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutWebthiefDialog
        self.PreferencesDialog = PreferencesWebthiefDialog

        # Code for other initialization actions should be added here.

