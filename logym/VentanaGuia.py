import wx

class VentanaGuia(wx.Frame):
    def __init__(self, parent):
        super().__init__(parent, title="Guía de LoGym", size=(520, 640),
        style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))

        self.SetBackgroundColour(wx.Colour(235, 240, 245))

        self.construir_contenido()

    def construir_contenido(self):
        sizer_principal = wx.BoxSizer(wx.VERTICAL)

        lbl_titulo = wx.StaticText(self, label="¿Que es LoGym?", style=wx.ALIGN_CENTER_HORIZONTAL)
        lbl_titulo.SetFont(wx.Font(22, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        sizer_principal.Add(lbl_titulo, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, 20)

        pnl_logo = wx.Panel(self, style=wx.BORDER_SIMPLE, size=(160, 75))
        pnl_logo.SetBackgroundColour(wx.WHITE)

        # lbl_logo = wx.StaticText(pnl_logo, label="LOGYM")
        # lbl_logo.SetFont(wx.Font(14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        # lbl_logo.SetForegroundColour(wx.Colour(0, 90, 180))

        img_logo = wx.Image("logym.png", wx.BITMAP_TYPE_PNG)
        img_escalada = img_logo.Scale(160, 65, wx.IMAGE_QUALITY_HIGH)
        bmp_logo = wx.Bitmap(img_escalada)

        bmp_ctrl_logo = wx.StaticBitmap(pnl_logo, -1, bmp_logo)

        sizer_logo = wx.BoxSizer(wx.VERTICAL)
        sizer_logo.Add(bmp_ctrl_logo, 0, wx.ALIGN_CENTER | wx.TOP, 8)
        pnl_logo.SetSizer(sizer_logo)

        sizer_principal.Add(pnl_logo, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP | wx.BOTTOM, 15)

        lbl_introduccion = wx.StaticText(self, label=(
            "LoGym es una aplicacion hecha para practicar la logica.\n"
            "No es un Compilador o IDE, tu editor o ide sera tu zona.\n"
            "LoGym unicamente validara tus resultados"
        ))
        lbl_introduccion.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        sizer_principal.Add(lbl_introduccion, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM, 20)

        lbl_subtitulo_ruta = wx.StaticText(self, label="Ruta de un Ejercicio:")
        lbl_subtitulo_ruta.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        sizer_principal.Add(lbl_subtitulo_ruta, 0, wx.LEFT | wx.BOTTOM, 15)

        def agregar_renglon_paso(titulo, explicacion):
            lbl_paso = wx.StaticText(self, label=f"{titulo} {explicacion}")
            lbl_paso.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
            sizer_principal.Add(lbl_paso, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM, 10)

        agregar_renglon_paso("Seleccioná el Reto:", "Elegí una categoría técnica (ej: Operadores, Índices de Arrays) y un nivel de dificultad.")
        agregar_renglon_paso("Analizá el Problema:", "Leé detenidamente el enunciado.")
        agregar_renglon_paso("Copiá el Input:", "Tomá el caso de prueba asignado y llevalo a tu propio código.")
        agregar_renglon_paso("Procesá:", "Escribí tu algoritmo en tu lenguaje de preferencia.\nHacé que tu programa(VS Code, etc) procese el Input y genere un resultado.")
        agregar_renglon_paso("Comproba:", "Pegá el Output que tiro tu consola en el cuadro de texto de LoGym y presioná Comprobar.")

        lbl_aclaracion = wx.StaticText(self, label="Si la respuesta es correcta, se tomara en cuenta cuanto tardaste y se sumara a tus estadisticas")
        lbl_aclaracion.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        sizer_principal.Add(lbl_aclaracion, 0, wx.LEFT | wx.RIGHT | wx.TOP, 10)

        self.SetSizer(sizer_principal)
        self.Layout()
