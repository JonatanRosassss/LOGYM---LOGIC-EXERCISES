import wx

class VentanaGuia(wx.Frame):
    def __init__(self, parent):
        super().__init__(parent, title="Guía de LoGym", size=(520, 640),
                         style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))

        # Color de fondo claro idéntico al gris/azul suave de la imagen
        self.SetBackgroundColour(wx.Colour(235, 240, 245))

        self.construir_contenido_de_la_guia_explicativa()

    def construir_contenido_de_la_guia_explicativa(self):
        sizer_principal_vertical_de_la_guia = wx.BoxSizer(wx.VERTICAL)

        texto_titulo_principal_que_es_logym = wx.StaticText(self, label="¿Que es LoGym?", style=wx.ALIGN_CENTER_HORIZONTAL)
        texto_titulo_principal_que_es_logym.SetFont(wx.Font(22, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        sizer_principal_vertical_de_la_guia.Add(texto_titulo_principal_que_es_logym, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, 20)

        panel_recuadro_del_logo_simulado = wx.Panel(self, style=wx.BORDER_SIMPLE, size=(160, 75))
        panel_recuadro_del_logo_simulado.SetBackgroundColour(wx.WHITE)

        # texto_interno_del_logo_logym = wx.StaticText(panel_recuadro_del_logo_simulado, label="LOGYM")
        # texto_interno_del_logo_logym.SetFont(wx.Font(14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        # texto_interno_del_logo_logym.SetForegroundColour(wx.Colour(0, 90, 180))
        imagen_cruda = wx.Image("logym.png", wx.BITMAP_TYPE_PNG)
        imagen_escalada = imagen_cruda.Scale(160, 65, wx.IMAGE_QUALITY_HIGH)
        bitmap_del_logo = wx.Bitmap(imagen_escalada)

        logo_visual_imagen = wx.StaticBitmap(panel_recuadro_del_logo_simulado, -1, bitmap_del_logo)

        sizer_interno_del_panel_del_logo = wx.BoxSizer(wx.VERTICAL)
        sizer_interno_del_panel_del_logo.Add(logo_visual_imagen, 0, wx.ALIGN_CENTER | wx.TOP, 8)
        panel_recuadro_del_logo_simulado.SetSizer(sizer_interno_del_panel_del_logo)

        sizer_principal_vertical_de_la_guia.Add(panel_recuadro_del_logo_simulado, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP | wx.BOTTOM, 15)
        texto_parrafo_introduccion_de_la_app = wx.StaticText(self, label=(
            "LoGym es una aplicacion hecha para practicar la logica.\n"
            "No es un Compilador o IDE, tu editor o ide sera tu zona.\n"
            "LoGym unicamente validara tus resultados"
        ))
        texto_parrafo_introduccion_de_la_app.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        sizer_principal_vertical_de_la_guia.Add(texto_parrafo_introduccion_de_la_app, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM, 20)

        texto_subtitulo_ruta_de_un_ejercicio = wx.StaticText(self, label="Ruta de un Ejercicio:")
        texto_subtitulo_ruta_de_un_ejercicio.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        sizer_principal_vertical_de_la_guia.Add(texto_subtitulo_ruta_de_un_ejercicio, 0, wx.LEFT | wx.BOTTOM, 15)

        def reglon_pasos(titulo, explicacion):
            texto_armado_completo = wx.StaticText(self, label=f"{titulo} {explicacion}")
            texto_armado_completo.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
            sizer_principal_vertical_de_la_guia.Add(texto_armado_completo, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM, 10)

        reglon_pasos("Seleccioná el Reto:", "Elegí una categoría técnica (ej: Operadores, Índices de Arrays) y un nivel de dificultad.")
        reglon_pasos("Analizá el Problema:", "Leé detenidamente el enunciado.")
        reglon_pasos("Copiá el Input:", "Tomá el caso de prueba asignado y llevalo a tu propio código.")
        reglon_pasos("Procesá:", "Escribí tu algoritmo en tu lenguaje de preferencia.\nHacé que tu programa(VS Code, etc) procese el Input y genere un resultado.")
        reglon_pasos("Comproba:", "Pegá el Output que tiro tu consola en el cuadro de texto de LoGym y presioná Comprobar.")

        texto_aclaracion_estadisticas_final = wx.StaticText(self, label="Si la respuesta es correcta, se tomara en cuenta cuanto tardaste y se sumara a tus estadisticas")
        texto_aclaracion_estadisticas_final.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        sizer_principal_vertical_de_la_guia.Add(texto_aclaracion_estadisticas_final, 0, wx.LEFT | wx.RIGHT | wx.TOP, 10)

        self.SetSizer(sizer_principal_vertical_de_la_guia)
        self.Layout()
