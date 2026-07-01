import wx

class VentanaAbout(wx.Frame):
    def __init__(self, parent):
        super().__init__(parent, title="Sobre Mi", size=(380, 420),
        style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))

        self.SetBackgroundColour(wx.Colour(240, 240, 240))

        self.construir_interfaz_creditos()

    def construir_interfaz_creditos(self):
        sizer_principal_vertical = wx.BoxSizer(wx.VERTICAL)

        panel_logo_recuadro = wx.Panel(self, style=wx.BORDER_SIMPLE, size=(180, 85))
        panel_logo_recuadro.SetBackgroundColour(wx.WHITE)

        imagen_cruda_sm = wx.Image("logym.png", wx.BITMAP_TYPE_PNG)
        imagen_escalada_sm = imagen_cruda_sm.Scale(160, 65, wx.IMAGE_QUALITY_HIGH)
        bitmap_del_logo_sm = wx.Bitmap(imagen_escalada_sm)

        logo_visual_imagen_sm = wx.StaticBitmap(panel_logo_recuadro, -1, bitmap_del_logo_sm)

        sizer_interno_logo = wx.BoxSizer(wx.VERTICAL)
        sizer_interno_logo.Add(logo_visual_imagen_sm, 0, wx.ALIGN_CENTER | wx.TOP, 8)
        panel_logo_recuadro.SetSizer(sizer_interno_logo)

        sizer_principal_vertical.Add(panel_logo_recuadro, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP | wx.BOTTOM, 20)
        texto_seccion_sobre_mi = wx.StaticText(self, label="SOBRE MI")
        texto_seccion_sobre_mi.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        sizer_principal_vertical.Add(texto_seccion_sobre_mi, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM, 15)

        texto_producido_por = wx.StaticText(self, label="Producido por:")
        texto_producido_por.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        sizer_principal_vertical.Add(texto_producido_por, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM, 10)

        texto_datos_alumno = wx.StaticText(self, label="Jonatan Rosas\nDesarrollador de Software", style=wx.ALIGN_CENTER_HORIZONTAL)
        texto_datos_alumno.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        sizer_principal_vertical.Add(texto_datos_alumno, 0, wx.ALIGN_CENTER_HORIZONTAL)

        sizer_principal_vertical.AddStretchSpacer(1)

        texto_version_borrador = wx.StaticText(self, label="Version Final")
        texto_version_borrador.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        sizer_principal_vertical.Add(texto_version_borrador, 0, wx.LEFT | wx.BOTTOM, 12)

        self.SetSizer(sizer_principal_vertical)
        self.Layout()
