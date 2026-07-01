import wx

class PanelEntrega(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.SetBackgroundColour(wx.Colour(40, 40, 40))

        self.sizer_principal = wx.BoxSizer(wx.VERTICAL)
        # lo mismo de inicializar todo o crear la interfaz del panel derecho de todo
        self.crear_titulo_de_la_entrega()
        self.crear_seccion_input_colocar()
        self.crear_seccion_pegar_output()
        self.crear_reloj_temporizador_de_abajo()

        self.SetSizer(self.sizer_principal)
        self.Layout()

    def set_callback_comprobar(self, funcion_callback):
        self.callback_comprobar = funcion_callback

    def crear_titulo_de_la_entrega(self):
        lbl_titulo_entrega = wx.StaticText(self, label="Entrega")
        lbl_titulo_entrega.SetForegroundColour(wx.WHITE)
        lbl_titulo_entrega.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        self.sizer_principal.Add(lbl_titulo_entrega, 0, wx.TOP | wx.LEFT | wx.BOTTOM, 20)

    def crear_seccion_input_colocar(self):
        lbl_input_colocar = wx.StaticText(self, label="Input a Colocar:")
        lbl_input_colocar.SetForegroundColour(wx.WHITE)
        lbl_input_colocar.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        self.sizer_principal.Add(lbl_input_colocar, 0, wx.LEFT | wx.BOTTOM, 10)

        self.txt_input = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.NO_BORDER)
        self.txt_input.SetBackgroundColour(wx.Colour(220, 220, 220))
        self.txt_input.SetForegroundColour(wx.Colour(255, 140, 0))
        self.txt_input.SetFont(wx.Font(11, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        self.txt_input.SetMinSize((-1, 100))
        self.sizer_principal.Add(self.txt_input, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 20)

        self.btn_copiar = wx.Button(self, label="Copiar", size=(100, 35))
        self.btn_copiar.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))

        self.btn_copiar.Bind(wx.EVT_BUTTON, self.click_copiar)
        self.sizer_principal.Add(self.btn_copiar, 0, wx.LEFT | wx.BOTTOM, 20)

    def crear_seccion_pegar_output(self):
        lbl_colocar_output = wx.StaticText(self, label="Colocar Output:")
        lbl_colocar_output.SetForegroundColour(wx.WHITE)
        lbl_colocar_output.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        self.sizer_principal.Add(lbl_colocar_output, 0, wx.LEFT | wx.BOTTOM, 10)

        self.txt_output = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.NO_BORDER)
        self.txt_output.SetMinSize((-1, 50))
        self.sizer_principal.Add(self.txt_output, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 20)

        self.btn_comprobar = wx.Button(self, label="Comprobar", size=(120, 40))
        self.btn_comprobar.SetBackgroundColour(wx.Colour(180, 255, 180))
        self.btn_comprobar.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))

        self.btn_comprobar.Bind(wx.EVT_BUTTON, self.click_comprobar)
        self.sizer_principal.Add(self.btn_comprobar, 0, wx.LEFT | wx.BOTTOM, 20)

    def crear_reloj_temporizador_de_abajo(self):
        # esto era para empujar hacia abajo
        self.sizer_principal.AddStretchSpacer(1)

        self.lbl_tiempo_restante = wx.StaticText(self, label="TIEMPO RESTANTE: --:--", style=wx.ALIGN_CENTER_HORIZONTAL)
        self.lbl_tiempo_restante.SetForegroundColour(wx.WHITE)
        self.lbl_tiempo_restante.SetFont(wx.Font(14, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        self.sizer_principal.Add(self.lbl_tiempo_restante, 0, wx.EXPAND | wx.BOTTOM, 30)

    def cargar_input_evaluacion(self, texto_input: str):
        self.txt_input.SetValue(texto_input)

    def obtener_output_usuario(self) -> str:
        return self.txt_output.GetValue().strip()

    def actualizar_display_tiempo(self, minutos: int, segundos: int):
        #  números menores a 10 tengan un 0 a la izquierda
        self.lbl_tiempo_restante.SetLabel(f"TIEMPO RESTANTE: {minutos}:{segundos:02d}")

    def limpiar_panel(self):
        self.txt_input.Clear()
        self.txt_output.Clear()
        self.lbl_tiempo_restante.SetLabel("TIEMPO RESTANTE: --:--")

    def click_copiar(self, event):
        content = self.txt_input.GetValue()
        if not content: return

        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(wx.TextDataObject(content))
            wx.TheClipboard.Close()

    def click_comprobar(self, event):
        if hasattr(self, 'callback_comprobar') and self.callback_comprobar:
            self.callback_comprobar(self.obtener_output_usuario())

    def texto_desactivado(self):
        self.lbl_tiempo_restante.SetLabel("TIEMPO DESACTIVADO")
