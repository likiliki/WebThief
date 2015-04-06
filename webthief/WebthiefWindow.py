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

from locale import gettext as _

from gi.repository import Gtk, WebKit # pylint: disable=E0611
import os
import logging
logger = logging.getLogger('webthief')

from webthief_lib import Window
from webthief.AboutWebthiefDialog import AboutWebthiefDialog
from webthief.AyudaDialog import AyudaDialog

# Variables
URL = "http://google.es"
URLfija = "http://google.es"

# See webthief_lib.Window.py for more details about how this class works
class WebthiefWindow(Window):
    __gtype_name__ = "WebthiefWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(WebthiefWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutWebthiefDialog

        # inicio de objetos utilizados en la aplicacion-----------------------
        self.entryUrl = self.builder.get_object('entryUrl')
        self.botonInicio = self.builder.get_object('botonInicio')
        self.botonRecarga = self.builder.get_object('botonRecarga')
        self.scrolledwindow = self.builder.get_object('scrolledwindow')
        self.toolImg = self.builder.get_object('toolImg')
        self.toolbar1 = self.builder.get_object('toolbar1')            
        
        # Configuracion inicial de objetos------------------------------------
        # Web View in ScrollerWindow
        self.webview = WebKit.WebView()
        self.scrolledwindow.add(self.webview)
        self.webview.show()
        self.webview.open(URL)

        # establecer tema
        context = self.toolbar1.get_style_context()
        context.add_class(Gtk.STYLE_CLASS_PRIMARY_TOOLBAR)

    # funciones propias------------------------------------------
    # Signal - BotonInicioClicked
    def on_botonInicio_clicked(self, widget):
    	# print "boton Home"        
    	self.webview.open(URLfija)        

    # Signal - BotonRecargaClicked
    def on_botonRecarga_clicked(self, widget):
    	# print "boton Recargar"
    	self.webview.reload()

    # Signal - Sacar Imagenes
    def on_toolImg_activate(self, widget):
    	print "Boton Saca Imagenes" 
    
    # signal - Navegar Hacia URL
    def on_entryUrl_activate(self, widget):        
        URL = "http://" + widget.get_text()
        # print URL
        self.webview.open(URL)

    # signal - Mostrar ayuda
    def on_helpapp_activate(self, widget):
        ayuda = AyudaDialog()
        ayuda.show()