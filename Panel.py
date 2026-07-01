import wx
import Splitter
from PanelNavegacion import PanelNavegacionFiltros
from PanelEjercicio import PanelEjercicio
from PanelEntrega import PanelEntrega

class MainPanel(wx.Panel):
#aprender las callbacks me mato, tuve que pedir guia a la ia de como usarlo pq sino ni idea.
    def __init__(self, parent):
        super().__init__(parent)
        self.SetBackgroundColour(wx.Colour(240, 240, 240))

        self.sizer_principal = None
        self.pnl_ejercicio = None
        self.pnl_filtros = None
        self.pnl_entrega = None

        self.ejercicio_actual = None
        self.segundos_restantes = 0
        self.timer_ejercicio = wx.Timer(self)

        self.Bind(wx.EVT_TIMER, self.on_timer_tick, self.timer_ejercicio)

        self.inicializar_ui()
        self.cargar_datos_iniciales()

    def inicializar_ui(self):
        self.sizer_principal = wx.BoxSizer(wx.VERTICAL)

        # después vemos si se usa
        # txt_bienvenida = wx.StaticText(self, label="Bienvenido a LoGym\n(Menú cargado exitosamente)", style=wx.ALIGN_CENTER_HORIZONTAL)
        # txt_bienvenida.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        # self.sizer_principal.Add(txt_bienvenida, 1, wx.TOP | wx.ALIGN_CENTER, 20)

        self.configurar_splitters()
        self.SetSizer(self.sizer_principal)

    def cargar_datos_iniciales(self):
        import Utilidades as u
        datos = u.leer_ejercicios()

        if not datos: return

        categoria_unique= set()
        dificultad_unique = set()
        for d in datos:
            categoria_unique.add(d.get("configuracion", {}).get("categoria", ""))
            dificultad_unique.add(d.get("configuracion", {}).get("dificultad", ""))

        self.pnl_filtros.actualizar_opciones_filtros(list(categoria_unique), list(dificultad_unique))
        self.pnl_filtros.actualizar_temario(list(categoria_unique))
        self.pnl_filtros.filtrado_archivo()

        if len(datos) > 0:
            self.mostrar_ejercicio(datos[0])

    # ARMAr separadores. Izquierda y derecha (el derecho se vuelve a partir en dos pq sino explota todoKKKK
    def configurar_splitters(self):
        panel_style = wx.BORDER_SUNKEN # por si llega a hacer falta después

        splitter_principal = Splitter.MySplitter(self, -1)
        splitter_principal.SetMinimumPaneSize(150)

        self.pnl_filtros = PanelNavegacionFiltros(splitter_principal)
        self.pnl_filtros.set_callback(self.mostrar_ejercicio)

        splitter_derecho = Splitter.MySplitter(splitter_principal, -1)
        splitter_derecho.SetMinimumPaneSize(150)

        self.pnl_ejercicio = PanelEjercicio(splitter_derecho)
        self.pnl_entrega = PanelEntrega(splitter_derecho)

        self.pnl_ejercicio.set_callback_empezar(self.iniciar_timer)
        self.pnl_entrega.set_callback_comprobar(self.validar_solucion)

        # metido en una sola línea  para que no ocupe media pantalla
        splitter_derecho.SplitVertically(self.pnl_ejercicio, self.pnl_entrega, 900)
        splitter_principal.SplitVertically(self.pnl_filtros, splitter_derecho, 400)

        self.sizer_principal.Add(splitter_principal, 1, wx.EXPAND | wx.ALL, 5)

    def procesar_ejercicios(self, lista_ejercicios: list):
        import Utilidades as U
        # Chequeo rápido para que no rompa si los paneles están vacíos
        if not self.pnl_filtros or not self.pnl_ejercicio:
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
        self.pnl_filtros.actualizar_opciones_filtros(list(categoria_unique), list(dificultad_unique))
        # for cada_ejercicio in lista_ejercicios:
        #     self.pnl_filtros.agregar_ejercicio_en_la_lista_visual(cada_ejercicio)

        self.pnl_filtros.actualizar_temario(list(categoria_unique))

        self.pnl_filtros.filtrado_archivo()

        if len(lista_ejercicios) > 0 and len(datos):
            #self.pnl_ejercicio.cargar_ejercicio(lista_ejercicios[0])
            #self.pnl_ejercicio.cargar_ejercicio(datos[0])
            self.mostrar_ejercicio(datos[0])

    def mostrar_ejercicio(self, datos_ejercicio: dict):
        if self.pnl_ejercicio:
            self.pnl_ejercicio.cargar_ejercicio(datos_ejercicio)
        self.ejercicio_actual = datos_ejercicio
        self.pnl_entrega.limpiar_panel()

        if self.pnl_ejercicio:
            self.pnl_ejercicio.cargar_ejercicio(datos_ejercicio)

    def iniciar_timer(self):
        if not self.ejercicio_actual:
            return
        config = self.ejercicio_actual.get("configuracion", {})
        self.segundos_restantes = config.get("tiempo_limite_seg", 0)

        casos = self.ejercicio_actual.get("casos_prueba", {})
        input_entrega = casos.get("entrega", {}).get("input", "No hay input de entrega definido.")
        self.pnl_entrega.cargar_input_evaluacion(input_entrega)

        minutos = self.segundos_restantes // 60
        segundos = self.segundos_restantes % 60
        self.pnl_entrega.actualizar_display_tiempo(minutos, segundos)
        self.timer_ejercicio.Start(1000)

    def on_timer_tick(self, event):
        if self.segundos_restantes > 0:
            self.segundos_restantes -= 1
            minutos = self.segundos_restantes // 60
            segundos = self.segundos_restantes % 60
            self.pnl_entrega.actualizar_display_tiempo(minutos, segundos)
        else:
            self.timer_ejercicio.Stop()
            wx.MessageBox("El tiempo límite expiro! Tu entrega ya no será válida.", "Tiempo Expirado", wx.OK | wx.ICON_WARNING)

    def validar_solucion(self, output_usuario: str):
        if not self.ejercicio_actual:
            return

        if not self.timer_ejercicio.IsRunning() and self.segundos_restantes == 0:
            wx.MessageBox("No podes enviar soluciones sin iniciar el temporizador o con el tiempo agotado.", "Error de Envío", wx.OK | wx.ICON_ERROR)
            return

        casos = self.ejercicio_actual.get("casos_prueba", {})
        output_esperado = casos.get("entrega", {}).get("output", "").strip()

        if output_usuario == output_esperado:
            self.timer_ejercicio.Stop()
            wx.MessageBox("¡RESPUESTA CORRECTA !\n Resolviste el problema con éxito.", "Evaluación Exitosa", wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox("RESPUESTA INCORRECTA .\nRevisa tu lógica e intenta de nuevo.", "Evaluación Fallida", wx.OK | wx.ICON_EXCLAMATION)

    def detener_timer(self):
        self.timer_ejercicio.Stop()

        self.pnl_entrega.texto_desactivado()

        wx.MessageBox("Temporizador desactivado.")
