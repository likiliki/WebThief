# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from locale import gettext as _

import logging
logger = logging.getLogger('webthief')

from webthief_lib.AboutDialog import AboutDialog

# See webthief_lib.AboutDialog.py for more details about how this class works.
class AboutWebthiefDialog(AboutDialog):
    __gtype_name__ = "AboutWebthiefDialog"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the about dialog"""
        super(AboutWebthiefDialog, self).finish_initializing(builder)

        # Code for other initialization actions should be added here.

