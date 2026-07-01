import wx
import PanelNavegacion

class PanelEjercicio(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.SetBackgroundColour(wx.Colour(60, 60, 60))
        self.callback_empezar = None
        self.sizer_principal = wx.BoxSizer(wx.VERTICAL)

        self.crear_parte_de_arriba_titulos()
        self.crear_caja_texto_para_el_enunciado()
        self.crear_cuadro_con_ejemplos_de_input_y_output()
        self.crear_boton_de_abajo_para_empezar()

        self.SetSizer(self.sizer_principal)
        self.Layout()

    def set_callback_empezar(self, funcion_callback):
        self.callback_empezar = funcion_callback

    #  logo de la app y los datos cargados del ejercicio
    def crear_parte_de_arriba_titulos(self):
        lbl_titulo_logym = wx.StaticText(self, label="L O G Y M\nEJERCICIOS", style=wx.ALIGN_CENTER_HORIZONTAL)
        lbl_titulo_logym.SetForegroundColour(wx.Colour(200, 200, 200))
        lbl_titulo_logym.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        self.lbl_nombre_ejercicio = wx.StaticText(self, label='"Seleccione un ejercicio"', style=wx.ALIGN_CENTER_HORIZONTAL)
        self.lbl_nombre_ejercicio.SetForegroundColour(wx.WHITE)
        self.lbl_nombre_ejercicio.SetFont(wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        self.lbl_nivel_tema = wx.StaticText(self, label='Nivel "-" Tema "-"', style=wx.ALIGN_CENTER_HORIZONTAL)
        self.lbl_nivel_tema.SetForegroundColour(wx.WHITE)
        self.lbl_nivel_tema.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        self.lbl_complejidad = wx.StaticText(self, label='Complejidad esperada: "-"', style=wx.ALIGN_CENTER_HORIZONTAL)
        self.lbl_complejidad.SetForegroundColour(wx.Colour(180, 180, 180))
        self.lbl_complejidad.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        self.sizer_principal.Add(lbl_titulo_logym, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 15)
        self.sizer_principal.Add(self.lbl_nombre_ejercicio, 0, wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.sizer_principal.Add(self.lbl_nivel_tema, 0, wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 20)
        self.sizer_principal.Add(self.lbl_complejidad, 0, wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 20) # Nuevo elemento asume el margen principal

    # El cuadrado gris del medio donde va el texto largo del problema
    def crear_caja_texto_para_el_enunciado(self):
        # multiline para saltos de linea, readonly para que no me editen el tp y rich por si pintan estilos dsp
        self.txt_enunciado = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER)
        self.txt_enunciado.SetBackgroundColour(wx.Colour(100, 100, 100))
        self.txt_enunciado.SetForegroundColour(wx.Colour(200,200,200))
        self.txt_enunciado.SetFont(wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))

        self.sizer_principal.Add(self.txt_enunciado, 1, wx.EXPAND | wx.LEFT | wx.RIGHT, 40)

    #  zona de abajo que te muestra q entra y qué sale de ejemplo
    def crear_cuadro_con_ejemplos_de_input_y_output(self):
        lbl_ejemplos = wx.StaticText(self, label="Ejemplos:")
        lbl_ejemplos.SetForegroundColour(wx.WHITE)
        lbl_ejemplos.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        self.sizer_principal.Add(lbl_ejemplos, 0, wx.TOP | wx.LEFT, 20)

        panel_ejemplos = wx.Panel(self)
        panel_ejemplos.SetBackgroundColour(wx.Colour(230, 230, 230))

        #  para que todo el tamaño se ajuste solo según el texto que venga adentro
        sizer_grilla = wx.FlexGridSizer(rows=2, cols=2, vgap=15, hgap=20)

        lbl_input_titulo = wx.StaticText(panel_ejemplos, label="Input:")
        lbl_input_titulo.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        self.lbl_input_valor = wx.StaticText(panel_ejemplos, label="")
        self.lbl_input_valor.SetForegroundColour(wx.Colour(200, 100, 0))
        self.lbl_input_valor.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        lbl_output_titulo = wx.StaticText(panel_ejemplos, label="Output:")
        lbl_output_titulo.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        self.lbl_output_valor = wx.StaticText(panel_ejemplos, label="")
        self.lbl_output_valor.SetForegroundColour(wx.Colour(200, 100, 0))
        self.lbl_output_valor.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        sizer_grilla.AddMany([(lbl_input_titulo, 0, wx.ALL, 15),
                                                         (self.lbl_input_valor, 1, wx.TOP | wx.EXPAND, 15), (lbl_output_titulo, 0, wx.ALL, 15), (self.lbl_output_valor, 1, wx.BOTTOM | wx.EXPAND, 15)])

        panel_ejemplos.SetSizer(sizer_grilla)
        self.sizer_principal.Add(panel_ejemplos, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 40)

    # Buttonn de arrancar y el cartelito con los minutos de duración
    def crear_boton_de_abajo_para_empezar(self):
        self.btn_empezar = wx.Button(self, label="Empezar", size=(-1, 50))
        self.btn_empezar.SetBackgroundColour(wx.Colour(180, 255, 180))
        self.btn_empezar.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        self.btn_empezar.Disable()

        self.btn_empezar.Bind(wx.EVT_BUTTON, self.click_empezar)

        self.lbl_tiempo = wx.StaticText(self, label="Contará con un tiempo de - minutos", style=wx.ALIGN_CENTER_HORIZONTAL)
        self.lbl_tiempo.SetForegroundColour(wx.WHITE)
        self.lbl_tiempo.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        self.sizer_principal.Add(self.btn_empezar, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 40)
        self.sizer_principal.Add(self.lbl_tiempo, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 20)

    def click_empezar(self, event):
        if self.callback_empezar:
            self.callback_empezar()

    # se agarra el dic que viene y se recibe con get por las dudas
    def cargar_ejercicio(self, datos_ejercicio: dict):
        nombre = datos_ejercicio.get("nombre", "Error de lectura")
        dificultad = datos_ejercicio.get("configuracion", {}).get("dificultad", "N/A")
        categoria = datos_ejercicio.get("configuracion", {}).get("categoria", "N/A")
        enunciado = datos_ejercicio.get("enunciado", "Sin contenido.")
        tiempo_segundos = datos_ejercicio.get("configuracion", {}).get("tiempo_limite_seg", 0)
        input_ej = datos_ejercicio.get("casos_prueba", {}).get("ejemplo", {}).get("input", "")
        output_ej = datos_ejercicio.get("casos_prueba", {}).get("ejemplo", {}).get("output", "")
        complejidad = datos_ejercicio.get("complejidad", "233223")
        input_entrega = datos_ejercicio.get("casos_prueba", {}).get("entrega", {}).get("input", "")
       # output_entrega = datos_ejercicio.get("casos_prueba", {}).get("entrega", {}).get("output", "")

        # se setea todo
        self.lbl_nombre_ejercicio.SetLabel(f'"{nombre}"')
        self.lbl_nivel_tema.SetLabel(f'Nivel "{dificultad}" "{categoria}"')
        self.txt_enunciado.SetValue(enunciado)
        self.lbl_input_valor.SetLabel(input_ej)
        self.lbl_output_valor.SetLabel(output_ej)
        self.lbl_complejidad.SetLabel(f'Complejidad esperada: "{complejidad}"')
        # doble barra clave
        minutos_totales = tiempo_segundos // 60
        self.lbl_tiempo.SetLabel(f"Contará con un tiempo de {minutos_totales} minutos")

        self.btn_empezar.Enable()
        self.Layout()
