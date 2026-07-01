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
        self.panel_abajo_zona_entrega = None

        self.ejercicio_seleccionado_actual = None
        self.segundos_restantes = 0
        self.temporizador_ejercicio = wx.Timer(self)

        self.Bind(wx.EVT_TIMER, self.on_tick_temporizador, self.temporizador_ejercicio)

        self.crear_pantalla_principal()
        self.cargar_datos_iniciales_archivo()

    def crear_pantalla_principal(self):
        self.sizer_contenedor_principal = wx.BoxSizer(wx.VERTICAL)

        # después vemos si se usa
        # txt_bienvenida = wx.StaticText(self, label="Bienvenido a LoGym\n(Menú cargado exitosamente)", style=wx.ALIGN_CENTER_HORIZONTAL)
        # txt_bienvenida.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        # self.sizer_contenedor_principal.Add(txt_bienvenida, 1, wx.TOP | wx.ALIGN_CENTER, 20)

        self.partir_pantalla_en_pedazos()
        self.SetSizer(self.sizer_contenedor_principal)

    def cargar_datos_iniciales_archivo(self):
        import Utilidades as u
        datos = u.leer_ejercicios()

        if not datos: return

        categoria_unique= set()
        dificultad_unique = set()
        for d in datos:
            categoria_unique.add(d.get("configuracion", {}).get("categoria", ""))
            dificultad_unique.add(d.get("configuracion", {}).get("dificultad", ""))

        self.menu_izquierdo_de_filtros.actualizar_opciones_filtros(list(categoria_unique), list(dificultad_unique))
        self.menu_izquierdo_de_filtros.filtrado_archivo()

        if len(datos) > 0:
            self.meter_datos_del_ejercicio_en_pantalla(datos[0])

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
        self.panel_abajo_zona_entrega = PanelEntrega(separador_de_la_derecha)

        self.panel_donde_esta_el_ejercicio.set_callback_empezar(self.iniciar_cuenta_regresiva)
        self.panel_abajo_zona_entrega.set_callback_comprobar(self.validar_solucion_del_usuario)

        # metido en una sola línea  para que no ocupe media pantalla
        separador_de_la_derecha.SplitVertically(self.panel_donde_esta_el_ejercicio, self.panel_abajo_zona_entrega, 900)
        separador_grande_principal.SplitVertically(self.menu_izquierdo_de_filtros, separador_de_la_derecha, 400)

        self.sizer_contenedor_principal.Add(separador_grande_principal, 1, wx.EXPAND | wx.ALL, 5)



    def procesar_pack_ejercicios(self, lista_ejercicios: list):
        import Utilidades as U
        # Chequeo rápido para que no rompa si los paneles están vacíos
        if not self.menu_izquierdo_de_filtros or not self.panel_donde_esta_el_ejercicio:
            print("pmumm.")
            return
        print("llegue a procesar algo?")
        nuevos = U.guardar_ejercicios(lista_ejercicios)
        if (not nuevos): print("No hay nuevos")

        print("no llegue a leer los ejs")
        datos = U.leer_ejercicios()

        #esto lo busque y es para que sea mucho mas optimo en terminos de memoria y demas
        categoria_unique = set()
        dificultad_unique = set()

        for e in datos:
            categoria_unique.add(e.get("configuracion", {}).get("categoria", ""))
            dificultad_unique.add(e.get("configuracion", {}).get("dificultad", ""))
        self.menu_izquierdo_de_filtros.actualizar_opciones_filtros(list(categoria_unique), list(dificultad_unique))
        # for cada_ejercicio in lista_ejercicios:
        #     self.menu_izquierdo_de_filtros.agregar_ejercicio_en_la_lista_visual(cada_ejercicio)
        self.menu_izquierdo_de_filtros.filtrado_archivo()


        if len(lista_ejercicios) > 0 and len(datos):
            #self.panel_donde_esta_el_ejercicio.cargar_ejercicio(lista_ejercicios[0])
            #self.panel_donde_esta_el_ejercicio.cargar_ejercicio(datos[0])
            self.meter_datos_del_ejercicio_en_pantalla(datos[0])

    def meter_datos_del_ejercicio_en_pantalla(self, datos_en_diccionario: dict):
        if self.panel_donde_esta_el_ejercicio:
            self.panel_donde_esta_el_ejercicio.cargar_ejercicio(datos_en_diccionario)
        self.ejercicio_seleccionado_actual = datos_en_diccionario
        self.panel_abajo_zona_entrega.limpiar_panel()

        if self.panel_donde_esta_el_ejercicio:
            self.panel_donde_esta_el_ejercicio.cargar_ejercicio(datos_en_diccionario)

    def iniciar_cuenta_regresiva(self):
        if not self.ejercicio_seleccionado_actual:
            return
        config = self.ejercicio_seleccionado_actual.get("configuracion", {})
        self.segundos_restantes = config.get("tiempo_limite_seg", 0)

        casos = self.ejercicio_seleccionado_actual.get("casos_prueba", {})
        input_entrega = casos.get("entrega", {}).get("input", "No hay input de entrega definido.")
        self.panel_abajo_zona_entrega.cargar_input_evaluacion(input_entrega)

        minutos = self.segundos_restantes // 60
        segundos = self.segundos_restantes % 60
        self.panel_abajo_zona_entrega.actualizar_display_tiempo(minutos, segundos)
        self.temporizador_ejercicio.Start(1000)

    def on_tick_temporizador(self, event):
        if self.segundos_restantes > 0:
            self.segundos_restantes -= 1
            minutos = self.segundos_restantes // 60
            segundos = self.segundos_restantes % 60
            self.panel_abajo_zona_entrega.actualizar_display_tiempo(minutos, segundos)
        else:
            self.temporizador_ejercicio.Stop()
            wx.MessageBox("El tiempo límite expiro! Tu entrega ya no será válida.", "Tiempo Expirado", wx.OK | wx.ICON_WARNING)

    def validar_solucion_del_usuario(self, output_usuario: str):
        if not self.ejercicio_seleccionado_actual:
            return

        if not self.temporizador_ejercicio.IsRunning() and self.segundos_restantes == 0:
            wx.MessageBox("No podes enviar soluciones sin iniciar el temporizador o con el tiempo agotado.", "Error de Envío", wx.OK | wx.ICON_ERROR)
            return

        casos = self.ejercicio_seleccionado_actual.get("casos_prueba", {})
        output_esperado = casos.get("entrega", {}).get("output", "").strip()

        if output_usuario == output_esperado:
            self.temporizador_ejercicio.Stop()
            wx.MessageBox("¡RESPUESTA CORRECTA !\n Resolviste el problema con éxito.", "Evaluación Exitosa", wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox("RESPUESTA INCORRECTA .\nRevisa tu lógica e intenta de nuevo.", "Evaluación Fallida", wx.OK | wx.ICON_EXCLAMATION)
