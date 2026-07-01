import wx
from Menu import CustomMenuBar
from Panel import MainPanel

import Splitter
import json

class MainFrame(wx.Frame):
    def __init__(self, parent=None, title="LoGym"):
        super().__init__(parent, title=title, size=(1920, 1080))

        #busca la clase de menu bar y la setea
        self.menubar = CustomMenuBar()
        self.SetMenuBar(self.menubar)

        self.CreateStatusBar()
        #self.SetStatusText("Listo")
        self.pnl_principal = MainPanel(self)
        self.pnl_principal.Layout()
        #mapea los eventos del menubar
        self.vincular_eventos()

    def vincular_eventos(self):
        self.Bind(wx.EVT_MENU, self.click_salir, id=wx.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.click_about, id=wx.ID_ABOUT)

        # self.Bind(wx.EVT_MENU, self._on_click_planeta, id=101)
        # self.Bind(wx.EVT_MENU, self._on_click_planeta, id=102)
        self.Bind(wx.EVT_MENU, self.click_importar_json, id=wx.ID_OPEN)
        self.Bind(wx.EVT_MENU, self.click_crear_ejercicio, id=wx.ID_NEW)
        self.Bind(wx.EVT_MENU, self.click_guia, id=201)
        self.Bind(wx.EVT_MENU, self.click_desactivar_timer, id=103)

    def click_salir(self, event):
        self.Close(True)

    def click_desactivar_timer(self, event):
        self.pnl_principal.apagar_temporizador()

    def click_importar_json(self, event):
        self.pnl_principal
        with wx.FileDialog(self, message="Seleccionar Pack de Ejercicios (JSON)", wildcard="Archivos JSON (*.json)|*.json", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as dlg_archivo:

            if dlg_archivo.ShowModal() == wx.ID_CANCEL:
                return

            ruta_archivo = dlg_archivo.GetPath()

            try:
                with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                    datos_json = json.load(archivo)

                if isinstance(datos_json, list) and len(datos_json) > 0:
                    self.pnl_principal.procesar_pack_ejercicios(datos_json)
                    self.SetStatusText(f"Pack importado con éxito. {len(datos_json)} ejercicios disponibles.")
                elif isinstance(datos_json, dict):
                    self.pnl_principal.procesar_pack_ejercicios(datos_json)
                    self.SetStatusText("Ejercicio individual importado con éxito.")
                else:
                    raise ValueError("ERROR json.")

            except Exception as error_json:
                wx.MessageBox(f"Error al procesar el archivo JSON:\n{str(error_json)}", "Error de Importación", wx.OK | wx.ICON_ERROR)

    #tira la ventanita emergente de la info
    def click_about(self, event):
        from VentanaAbout import VentanaAbout
        frm_creditos = VentanaAbout(self)
        frm_creditos.Show(True)

    def click_crear_ejercicio(self, event):
        id_item = event.GetId()
        self.SetStatusText(f"Seleccionaste el ítem con ID: {id_item}")
        from VentanaEjercicio import CrearEjercicio

        frm_formulario = CrearEjercicio(self, self.pnl_principal)
        frm_formulario.Show(True)

    def click_guia(self, event):
        from VentanaGuia import VentanaGuia
        # Pasamos 'self' como parent para que quede vinculada correctamente a la app principal
        frm_guia = VentanaGuia(self)
        frm_guia.Show(True)
