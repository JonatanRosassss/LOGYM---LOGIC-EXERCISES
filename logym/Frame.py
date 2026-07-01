import wx
from Menu import CustomMenuBar
from Panel import MainPanel

import Splitter
import json
class MainFrame(wx.Frame):
    def __init__(self, parent=None, title="LoGym"):
        super().__init__(parent, title=title, size=(1920, 1080))

        #busca la clase de menu bar y la setea
        self.barra_de_menu_personalizada_de_la_parte_superior = CustomMenuBar()
        self.SetMenuBar(self.barra_de_menu_personalizada_de_la_parte_superior)

        self.CreateStatusBar()
        #self.SetStatusText("Listo")
        self.panel_contenedor_principal_de_toda_la_interfaz = MainPanel(self)
        self.panel_contenedor_principal_de_toda_la_interfaz.Layout()
        #mapea los eventos del menubar
        self.vincular_eventos()

    def vincular_eventos(self):
        self.Bind(wx.EVT_MENU, self.cuando_salir, id=wx.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.cuando_about_me, id=wx.ID_ABOUT)

        # self.Bind(wx.EVT_MENU, self._on_click_planeta, id=101)
        # self.Bind(wx.EVT_MENU, self._on_click_planeta, id=102)
        self.Bind(wx.EVT_MENU, self.click_importar_json, id=wx.ID_OPEN)
        self.Bind(wx.EVT_MENU, self.cuando_el_usuario_toca_el_item_del_menu_planeta, id=wx.ID_NEW)
    def cuando_salir(self, event):
        self.Close(True)

    def click_importar_json(self, event):
        self.panel_contenedor_principal_de_toda_la_interfaz
        with wx.FileDialog(self, message="Seleccionar Pack de Ejercicios (JSON)", wildcard="Archivos JSON (*.json)|*.json", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as ventana_emergente_para_elegir_el_archivo_json:

            if ventana_emergente_para_elegir_el_archivo_json.ShowModal() == wx.ID_CANCEL:
                return

            ruta_completa_del_archivo_json_seleccionado = ventana_emergente_para_elegir_el_archivo_json.GetPath()

            try:
                with open(ruta_completa_del_archivo_json_seleccionado, "r", encoding="utf-8") as arc_abierto:
                    datos_desde_archivo_json = json.load(arc_abierto)

                if isinstance(datos_desde_archivo_json, list) and len(datos_desde_archivo_json) > 0:
                    self.panel_contenedor_principal_de_toda_la_interfaz.procesar_pack_ejercicios(datos_desde_archivo_json)
                    self.SetStatusText(f"Pack importado con éxito. {len(datos_desde_archivo_json)} ejercicios disponibles.")
                elif isinstance(datos_desde_archivo_json, dict):
                    self.panel_contenedor_principal_de_toda_la_interfaz.procesar_pack_ejercicios(datos_desde_archivo_json)
                    self.SetStatusText("Ejercicio individual importado con éxito.")
                else:
                    raise ValueError("ERROR json.")

            except Exception as error_capturado_durante_la_lectura_del_json:
                wx.MessageBox(f"Error al procesar el archivo JSON:\n{str(error_capturado_durante_la_lectura_del_json)}", "Error de Importación", wx.OK | wx.ICON_ERROR)

    #tira la ventanita emergente de la info
    def cuando_about_me(self, event):
        wx.MessageBox("LoGym v1.0\nSistema tatatat.", "Acerca de", wx.OK | wx.ICON_INFORMATION)

    def cuando_el_usuario_toca_el_item_del_menu_planeta(self, event):
        identificador_unico_del_item_que_se_toco = event.GetId()
        self.SetStatusText(f"Seleccionaste el ítem con ID: {identificador_unico_del_item_que_se_toco}")
