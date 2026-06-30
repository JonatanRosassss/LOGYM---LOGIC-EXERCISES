import wx
import Splitter
from PanelNavegacion import PanelNavegacionFiltros
from PanelEjercicio import PanelEjercicio
from PanelEntrega import PanelEntrega

class MainPanel(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent)
        self.SetBackgroundColour(wx.Colour(240, 240, 240))

        self.sizer_contenedor_principal = None
        self.panel_donde_esta_el_ejercicio = None
        self.menu_izquierdo_de_filtros = None

        self.crear_pantalla_principal()

    def crear_pantalla_principal(self):
        self.sizer_contenedor_principal = wx.BoxSizer(wx.VERTICAL)

        # después vemos si se usa
        # txt_bienvenida = wx.StaticText(self, label="Bienvenido a LoGym\n(Menú cargado exitosamente)", style=wx.ALIGN_CENTER_HORIZONTAL)
        # txt_bienvenida.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        # self.sizer_contenedor_principal.Add(txt_bienvenida, 1, wx.TOP | wx.ALIGN_CENTER, 20)

        self.partir_pantalla_en_pedazos()
        self.SetSizer(self.sizer_contenedor_principal)

    # ARMAr separadores. Izquierda y derecha (el derecho se vuelve a partir en dos pq sino explota todoKKKK
    def partir_pantalla_en_pedazos(self):
        panel_style = wx.BORDER_SUNKEN # por si llega a hacer falta después

        separador_grande_principal = Splitter.MySplitter(self, -1)
        separador_grande_principal.SetMinimumPaneSize(150)

        self.menu_izquierdo_de_filtros = PanelNavegacionFiltros(separador_grande_principal)
        self.menu_izquierdo_de_filtros.set_callback(self.meter_datos_del_ejercicio_en_pantalla)

        separador_de_la_derecha = Splitter.MySplitter(separador_grande_principal, -1)
        separador_de_la_derecha.SetMinimumPaneSize(150)

        self.panel_donde_esta_el_ejercicio = PanelEjercicio(separador_de_la_derecha)
        panel_abajo_zona_entrega = PanelEntrega(separador_de_la_derecha)

        # metido en una sola línea  para que no ocupe media pantalla
        separador_de_la_derecha.SplitVertically(self.panel_donde_esta_el_ejercicio, panel_abajo_zona_entrega, 900)
        separador_grande_principal.SplitVertically(self.menu_izquierdo_de_filtros, separador_de_la_derecha, 400)

        self.sizer_contenedor_principal.Add(separador_grande_principal, 1, wx.EXPAND | wx.ALL, 5)

    def procesar_pack_ejercicios(self, lista_ejercicios: list):
        # Chequeo rápido para que no rompa si los paneles están vacíos
        if not self.menu_izquierdo_de_filtros or not self.panel_donde_esta_el_ejercicio:
            print("pmumm.")
            return

        for cada_ejercicio in lista_ejercicios:
            self.menu_izquierdo_de_filtros.agregar_ejercicio_en_la_lista_visual(cada_ejercicio)

        if len(lista_ejercicios) > 0:
            self.panel_donde_esta_el_ejercicio.cargar_ejercicio(lista_ejercicios[0])

    def meter_datos_del_ejercicio_en_pantalla(self, datos_en_diccionario: dict):
        if self.panel_donde_esta_el_ejercicio:
            self.panel_donde_esta_el_ejercicio.cargar_ejercicio(datos_en_diccionario)
