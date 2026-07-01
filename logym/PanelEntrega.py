import wx

class PanelEntrega(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.SetBackgroundColour(wx.Colour(40, 40, 40))

        self.sizer_contenedor_de_la_derecha_para_entrega = wx.BoxSizer(wx.VERTICAL)
        # lo mismo de inicializar todo o crear la interfaz del panel derecho de todo
        self.crear_titulo_de_la_entrega()
        self.crear_seccion_input_colocar()
        self.crear_seccion_pegar_output()
        self.crear_reloj_temporizador_de_abajo()

        self.SetSizer(self.sizer_contenedor_de_la_derecha_para_entrega)
        self.Layout()

    def set_callback_comprobar(self, funcion_callback):
        self.callback_comprobar = funcion_callback

    def crear_titulo_de_la_entrega(self):
        texto_titulo_entrega = wx.StaticText(self, label="Entrega")
        texto_titulo_entrega.SetForegroundColour(wx.WHITE)
        texto_titulo_entrega.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        self.sizer_contenedor_de_la_derecha_para_entrega.Add(texto_titulo_entrega, 0, wx.TOP | wx.LEFT | wx.BOTTOM, 20)

    def crear_seccion_input_colocar(self):
        texto_label_input_a_colocar = wx.StaticText(self, label="Input a Colocar:")
        texto_label_input_a_colocar.SetForegroundColour(wx.WHITE)
        texto_label_input_a_colocar.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        self.sizer_contenedor_de_la_derecha_para_entrega.Add(texto_label_input_a_colocar, 0, wx.LEFT | wx.BOTTOM, 10)

        self.caja_texto_input_real_generado = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER)
        self.caja_texto_input_real_generado.SetBackgroundColour(wx.Colour(220, 220, 220))
        self.caja_texto_input_real_generado.SetForegroundColour(wx.Colour(255, 140, 0))
        self.caja_texto_input_real_generado.SetFont(wx.Font(11, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        self.caja_texto_input_real_generado.SetMinSize((-1, 100))
        self.sizer_contenedor_de_la_derecha_para_entrega.Add(self.caja_texto_input_real_generado, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 20)

        self.boton_para_copiar_el_input = wx.Button(self, label="Copiar", size=(100, 35))
        self.boton_para_copiar_el_input.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))

        self.boton_para_copiar_el_input.Bind(wx.EVT_BUTTON, self.click_copiar)
        self.sizer_contenedor_de_la_derecha_para_entrega.Add(self.boton_para_copiar_el_input, 0, wx.LEFT | wx.BOTTOM, 20)

    def crear_seccion_pegar_output(self):
        texto_label_colocar_output = wx.StaticText(self, label="Colocar Output:")
        texto_label_colocar_output.SetForegroundColour(wx.WHITE)
        texto_label_colocar_output.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        self.sizer_contenedor_de_la_derecha_para_entrega.Add(texto_label_colocar_output, 0, wx.LEFT | wx.BOTTOM, 10)

        self.caja_texto_donde_el_usuario_escribe_su_output = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.NO_BORDER)
        self.caja_texto_donde_el_usuario_escribe_su_output.SetMinSize((-1, 50))
        self.sizer_contenedor_de_la_derecha_para_entrega.Add(self.caja_texto_donde_el_usuario_escribe_su_output, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 20)

        self.boton_para_comprobar_si_esta_bien_el_ejercicio = wx.Button(self, label="Comprobar", size=(120, 40))
        self.boton_para_comprobar_si_esta_bien_el_ejercicio.SetBackgroundColour(wx.Colour(180, 255, 180))
        self.boton_para_comprobar_si_esta_bien_el_ejercicio.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))

        self.boton_para_comprobar_si_esta_bien_el_ejercicio.Bind(wx.EVT_BUTTON, self.click_comprobar)
        self.sizer_contenedor_de_la_derecha_para_entrega.Add(self.boton_para_comprobar_si_esta_bien_el_ejercicio, 0, wx.LEFT | wx.BOTTOM, 20)



    def crear_reloj_temporizador_de_abajo(self):
        # esto era para empujar hacia abajo
        self.sizer_contenedor_de_la_derecha_para_entrega.AddStretchSpacer(1)

        self.texto_label_del_tiempo_restante = wx.StaticText(self, label="TIEMPO RESTANTE: --:--", style=wx.ALIGN_CENTER_HORIZONTAL)
        self.texto_label_del_tiempo_restante.SetForegroundColour(wx.WHITE)
        self.texto_label_del_tiempo_restante.SetFont(wx.Font(14, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        self.sizer_contenedor_de_la_derecha_para_entrega.Add(self.texto_label_del_tiempo_restante, 0, wx.EXPAND | wx.BOTTOM, 30)

    def cargar_input_evaluacion(self, texto_input: str):
        self.caja_texto_input_real_generado.SetValue(texto_input)

    def obtener_output_usuario(self) -> str:
        return self.caja_texto_donde_el_usuario_escribe_su_output.GetValue().strip()

    def actualizar_display_tiempo(self, minutos: int, segundos: int):
        #  números menores a 10 tengan un 0 a la izquierda
        self.texto_label_del_tiempo_restante.SetLabel(f"TIEMPO RESTANTE: {minutos}:{segundos:02d}")

    def limpiar_panel(self):
        self.caja_texto_input_real_generado.Clear()
        self.caja_texto_donde_el_usuario_escribe_su_output.Clear()
        self.texto_label_del_tiempo_restante.SetLabel("TIEMPO RESTANTE: --:--")

    def click_copiar(self, event):
        content = self.caja_texto_input_real_generado.GetValue()
        if not content: return

        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(wx.TextDataObject(content))
            wx.TheClipboard.Close()

    def click_comprobar(self, event):
        if hasattr(self, 'callback_comprobar') and self.callback_comprobar:
            self.callback_comprobar(self.obtener_output_usuario())
