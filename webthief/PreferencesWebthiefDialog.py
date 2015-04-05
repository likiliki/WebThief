# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
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

from gi.repository import Gio # pylint: disable=E0611

from locale import gettext as _

import logging
logger = logging.getLogger('webthief')

from webthief_lib.PreferencesDialog import PreferencesDialog

class PreferencesWebthiefDialog(PreferencesDialog):
    __gtype_name__ = "PreferencesWebthiefDialog"

    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the preferences dialog"""
        super(PreferencesWebthiefDialog, self).finish_initializing(builder)

        # Bind each preference widget to gsettings
        settings = Gio.Settings("net.launchpad.webthief")
        widget = self.builder.get_object('example_entry')
        settings.bind("example", widget, "text", Gio.SettingsBindFlags.DEFAULT)

        # Code for other initialization actions should be added here.
