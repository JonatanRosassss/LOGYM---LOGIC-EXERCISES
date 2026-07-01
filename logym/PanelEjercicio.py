import wx
import PanelNavegacion

class PanelEjercicio(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.SetBackgroundColour(wx.Colour(60, 60, 60))
        self.callback_al_empezar = None
        self.sizer_que_va_para_abajo_todo_junto = wx.BoxSizer(wx.VERTICAL)

        self.crear_parte_de_arriba_titulos()
        self.crear_caja_texto_para_el_enunciado()
        self.crear_cuadro_con_ejemplos_de_input_y_output()
        self.crear_boton_de_abajo_para_empezar()

        self.SetSizer(self.sizer_que_va_para_abajo_todo_junto)
        self.Layout()
    def set_callback_empezar(self, funcion_callback):
        self.callback_al_empezar = funcion_callback


    #  logo de la app y los datos cargados del ejercicio
    def crear_parte_de_arriba_titulos(self):
        texto_logym_bien_grande = wx.StaticText(self, label="L O G Y M\nEJERCICIOS", style=wx.ALIGN_CENTER_HORIZONTAL)
        texto_logym_bien_grande.SetForegroundColour(wx.Colour(200, 200, 200))
        texto_logym_bien_grande.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        self.texto_nombre_del_ejercicio_seleccionado = wx.StaticText(self, label='"Seleccione un ejercicio"', style=wx.ALIGN_CENTER_HORIZONTAL)
        self.texto_nombre_del_ejercicio_seleccionado.SetForegroundColour(wx.WHITE)
        self.texto_nombre_del_ejercicio_seleccionado.SetFont(wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        self.texto_nivel_y_tema_del_ejercicio = wx.StaticText(self, label='Nivel "-" Tema "-"', style=wx.ALIGN_CENTER_HORIZONTAL)
        self.texto_nivel_y_tema_del_ejercicio.SetForegroundColour(wx.WHITE)
        self.texto_nivel_y_tema_del_ejercicio.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        self.texto_complejidad_esperada = wx.StaticText(self, label='Complejidad esperada: "-"', style=wx.ALIGN_CENTER_HORIZONTAL)
        self.texto_complejidad_esperada.SetForegroundColour(wx.Colour(180, 180, 180))
        self.texto_complejidad_esperada.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        self.sizer_que_va_para_abajo_todo_junto.Add(texto_logym_bien_grande, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 15)
        self.sizer_que_va_para_abajo_todo_junto.Add(self.texto_nombre_del_ejercicio_seleccionado, 0, wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.sizer_que_va_para_abajo_todo_junto.Add(self.texto_nivel_y_tema_del_ejercicio, 0, wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 20)
        self.sizer_que_va_para_abajo_todo_junto.Add(self.texto_complejidad_esperada, 0, wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 20) # Nuevo elemento asume el margen principal
    # El cuadrado gris del medio donde va el texto largo del problema
    def crear_caja_texto_para_el_enunciado(self):
        # multiline para saltos de linea, readonly para que no me editen el tp y rich por si pintan estilos dsp
        self.caja_grande_texto_enunciado = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER)
        self.caja_grande_texto_enunciado.SetBackgroundColour(wx.Colour(100, 100, 100))
        self.caja_grande_texto_enunciado.SetForegroundColour(wx.Colour(200,200,200))
        self.caja_grande_texto_enunciado.SetFont(wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))

        self.sizer_que_va_para_abajo_todo_junto.Add(self.caja_grande_texto_enunciado, 1, wx.EXPAND | wx.LEFT | wx.RIGHT, 40)

    #  zona de abajo que te muestra q entra y qué sale de ejemplo
    def crear_cuadro_con_ejemplos_de_input_y_output(self):
        texto_que_dice_ejemplos = wx.StaticText(self, label="Ejemplos:")
        texto_que_dice_ejemplos.SetForegroundColour(wx.WHITE)
        texto_que_dice_ejemplos.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        self.sizer_que_va_para_abajo_todo_junto.Add(texto_que_dice_ejemplos, 0, wx.TOP | wx.LEFT, 20)

        panel_chico_para_los_ejemplos = wx.Panel(self)
        panel_chico_para_los_ejemplos.SetBackgroundColour(wx.Colour(230, 230, 230))

        #  para que todo el tamaño se ajuste solo según el texto que venga adentro
        grilla_flex_para_acomodar_los_ejemplos = wx.FlexGridSizer(rows=2, cols=2, vgap=15, hgap=20)

        texto_entrada_input = wx.StaticText(panel_chico_para_los_ejemplos, label="Input:")
        texto_entrada_input.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        self.texto_valor_que_entra = wx.StaticText(panel_chico_para_los_ejemplos, label="")
        self.texto_valor_que_entra.SetForegroundColour(wx.Colour(200, 100, 0))
        self.texto_valor_que_entra.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        texto_salida_output = wx.StaticText(panel_chico_para_los_ejemplos, label="Output:")
        texto_salida_output.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        self.texto_valor_que_sale = wx.StaticText(panel_chico_para_los_ejemplos, label="")
        self.texto_valor_que_sale.SetForegroundColour(wx.Colour(200, 100, 0))
        self.texto_valor_que_sale.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        grilla_flex_para_acomodar_los_ejemplos.AddMany([(texto_entrada_input, 0, wx.ALL, 15),
                                                         (self.texto_valor_que_entra, 1, wx.TOP | wx.EXPAND, 15), (texto_salida_output, 0, wx.ALL, 15), (self.texto_valor_que_sale, 1, wx.BOTTOM | wx.EXPAND, 15)])

        panel_chico_para_los_ejemplos.SetSizer(grilla_flex_para_acomodar_los_ejemplos)
        self.sizer_que_va_para_abajo_todo_junto.Add(panel_chico_para_los_ejemplos, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 40)

    # Buttonn de arrancar y el cartelito con los minutos de duración
    def crear_boton_de_abajo_para_empezar(self):
        self.boton_verde_para_empezar = wx.Button(self, label="Empezar", size=(-1, 50))
        self.boton_verde_para_empezar.SetBackgroundColour(wx.Colour(180, 255, 180))
        self.boton_verde_para_empezar.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        self.boton_verde_para_empezar.Disable()

        self.boton_verde_para_empezar.Bind(wx.EVT_BUTTON, self.click_empezar)

        self.texto_que_muestra_los_minutos = wx.StaticText(self, label="Contará con un tiempo de - minutos", style=wx.ALIGN_CENTER_HORIZONTAL)
        self.texto_que_muestra_los_minutos.SetForegroundColour(wx.WHITE)
        self.texto_que_muestra_los_minutos.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        self.sizer_que_va_para_abajo_todo_junto.Add(self.boton_verde_para_empezar, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 40)
        self.sizer_que_va_para_abajo_todo_junto.Add(self.texto_que_muestra_los_minutos, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 20)

    def click_empezar(self, event):
        if self.callback_al_empezar:
            self.callback_al_empezar()

    # se agarra el dic que viene y se recibe con get por las dudas
    def cargar_ejercicio(self, datos_en_un_diccionario: dict):
        nombre_ejercicio = datos_en_un_diccionario.get("nombre", "Error de lectura")
        dificultad_ejercicio = datos_en_un_diccionario.get("configuracion", {}).get("dificultad", "N/A")
        categoria_ejercicio = datos_en_un_diccionario.get("configuracion", {}).get("categoria", "N/A")
        enunciado_ejercicio = datos_en_un_diccionario.get("enunciado", "Sin contenido.")
        tiempo_en_segundos = datos_en_un_diccionario.get("configuracion", {}).get("tiempo_limite_seg", 0)
        ejemplo_de_entrada = datos_en_un_diccionario.get("casos_prueba", {}).get("ejemplo", {}).get("input", "")
        ejemplo_de_salida = datos_en_un_diccionario.get("casos_prueba", {}).get("ejemplo", {}).get("output", "")
        complejidad_ejercicio = datos_en_un_diccionario.get("complejidad", "233223")
        input_entrega = datos_en_un_diccionario.get("casos_prueba", {}).get("entrega", {}).get("input", "")
       # output_entrega = datos_en_un_diccionario.get("casos_prueba", {}).get("entrega", {}).get("output", "")

        # se setea todo
        self.texto_nombre_del_ejercicio_seleccionado.SetLabel(f'"{nombre_ejercicio}"')
        self.texto_nivel_y_tema_del_ejercicio.SetLabel(f'Nivel "{dificultad_ejercicio}" "{categoria_ejercicio}"')
        self.caja_grande_texto_enunciado.SetValue(enunciado_ejercicio)
        self.texto_valor_que_entra.SetLabel(ejemplo_de_entrada)
        self.texto_valor_que_sale.SetLabel(ejemplo_de_salida)
        self.texto_complejidad_esperada.SetLabel(f'Complejidad esperada: "{complejidad_ejercicio}"')
        # doble barra clave
        minutos_totales_calculados = tiempo_en_segundos // 60
        self.texto_que_muestra_los_minutos.SetLabel(f"Contará con un tiempo de {minutos_totales_calculados} minutos")

        self.boton_verde_para_empezar.Enable()
        self.Layout()
