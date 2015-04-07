# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
# This file is part of WEBTHIEF.
#    WEBTHIEF is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    WEBTHIEF is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with WEBTHIEF.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk, WebKit # pylint: disable=E0611
import os

from webthief_lib.helpers import get_builder

import gettext
from gettext import gettext as _
gettext.textdomain('webthief')

URL = "file://" + os.path.dirname(__file__) + "/help.html"

class AyudaDialog(Gtk.Dialog):
    __gtype_name__ = "AyudaDialog"

    def __new__(cls):
        """Special static method that's automatically called by Python when 
        constructing a new instance of this class.
        
        Returns a fully instantiated AyudaDialog object.
        """
        builder = get_builder('AyudaDialog')
        new_object = builder.get_object('ayuda_dialog')
        new_object.finish_initializing(builder)
        return new_object

    def finish_initializing(self, builder):
        """Called when we're finished initializing.
        """
        # Get a reference to the builder and set up the signals.
        self.builder = builder
        self.ui = builder.get_ui(self)
        # new options
        self.scrolledwindowhelp = self.builder.get_object('scrolledwindowhelp')

        # Web View in ScrollerWindow
        self.webview2 = WebKit.WebView()
        self.scrolledwindowhelp.add(self.webview2)
        self.webview2.show()
        self.webview2.open(URL)
        

    def on_btn_ok_clicked(self, widget, data=None):
        """The user has elected to save the changes.

        Called before the dialog returns Gtk.ResponseType.OK from run().
        """
        self.destroy()
        pass

    def on_btn_cancel_clicked(self, widget, data=None):
        """The user has elected cancel changes.

        Called before the dialog returns Gtk.ResponseType.CANCEL for run()
        """
        self.destroy()
        pass


if __name__ == "__main__":
    dialog = AyudaDialog()
    dialog.show()
    Gtk.main()
