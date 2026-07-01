import wx

class CrearEjercicio(wx.Frame):
    def __init__(self, parent, panel_orquestador_principal):
        super().__init__(parent, title="Formulario: Alta de Ejercicios", size=(480, 680),
        style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))

        self.orquestador_principal = panel_orquestador_principal
        self.SetBackgroundColour(wx.Colour(60, 60, 60))

        self.construir_interfaz()

    def construir_interfaz(self):
        sizer_principal = wx.BoxSizer(wx.VERTICAL)

        def agregar_etiqueta_blanca(texto):
            lbl_etiqueta = wx.StaticText(self, label=texto)
            lbl_etiqueta.SetForegroundColour(wx.WHITE)
            sizer_principal.Add(lbl_etiqueta, 0, wx.LEFT | wx.TOP, 10)

        agregar_etiqueta_blanca("Nombre de la actividad / ejercicio:")
        self.txt_nombre = wx.TextCtrl(self)
        sizer_principal.Add(self.txt_nombre, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 15)

        agregar_etiqueta_blanca("Categoría temática:")
        self.txt_categoria = wx.TextCtrl(self)
        sizer_principal.Add(self.txt_categoria, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 15)

        agregar_etiqueta_blanca("Dificultad (Escribir: Fácil, Media o Difícil):")
        self.txt_dificultad = wx.TextCtrl(self, value="Fácil")
        sizer_principal.Add(self.txt_dificultad, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 15)

        agregar_etiqueta_blanca("Tiempo límite asignado (en segundos):")
        self.txt_tiempo = wx.TextCtrl(self, value="120")
        sizer_principal.Add(self.txt_tiempo, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 15)

        agregar_etiqueta_blanca("Enunciado de; problema:")
        self.txt_enunciado = wx.TextCtrl(self, style=wx.TE_MULTILINE, size=(-1, 80))
        sizer_principal.Add(self.txt_enunciado, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 15)

        # Secciones simplificadas para casos de prueba sin splitters complejos
        agregar_etiqueta_blanca("Caso de EJEMPLO - Input:")
        self.txt_input_ejemplo = wx.TextCtrl(self, style=wx.TE_MULTILINE, size=(-1, 40))
        sizer_principal.Add(self.txt_input_ejemplo, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 15)

        agregar_etiqueta_blanca("Caso de EJEMPLO - Output:")
        self.txt_output_ejemplo = wx.TextCtrl(self, style=wx.TE_MULTILINE, size=(-1, 40))
        sizer_principal.Add(self.txt_output_ejemplo, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 15)

        agregar_etiqueta_blanca("Caso de ENTREGA - Entrada (Input Entrega):")
        self.txt_input_entrega = wx.TextCtrl(self, style=wx.TE_MULTILINE, size=(-1, 40))
        sizer_principal.Add(self.txt_input_entrega, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 15)

        agregar_etiqueta_blanca("Caso de ENTREGA - Salida Esperada (Output Entrega):")
        self.txt_output_entrega = wx.TextCtrl(self, style=wx.TE_MULTILINE, size=(-1, 40))
        sizer_principal.Add(self.txt_output_entrega, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 15)

        self.btn_registrar = wx.Button(self, label="Registrar Ejercicio")
        self.btn_registrar.SetBackgroundColour(wx.Colour(140, 230, 140))
        self.btn_registrar.Bind(wx.EVT_BUTTON, self.click_registrar)

        sizer_principal.Add(self.btn_registrar, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 20)

        self.SetSizer(sizer_principal)
        self.Layout()

    def click_registrar(self, event):
        if self.txt_nombre.GetValue().strip() == "" or self.txt_enunciado.GetValue().strip() == "":
            wx.MessageBox("Faltan completar campos", "Termina", wx.OK | wx.ICON_WARNING)
            return

        try:
            conversion_tiempo = int(self.txt_tiempo.GetValue())
        except:
            wx.MessageBox("El tiempo debe ser un número entero.", "Error de entrada", wx.OK | wx.ICON_ERROR)
            return


        ejercicio_formateado = {
            "nombre": self.txt_nombre.GetValue().strip(),
            "configuracion": {
                "dificultad": self.txt_dificultad.GetValue().strip(),
                "categoria": self.txt_categoria.GetValue().strip(),
                "tiempo_limite_seg": conversion_tiempo
            },
            "enunciado": self.txt_enunciado.GetValue().strip(),
            "complejidad": "O(N)",
            "casos_prueba": {
                "ejemplo": {
                    "input": self.txt_input_ejemplo.GetValue().strip(),
                    "output": self.txt_output_ejemplo.GetValue().strip()
                },
                "entrega": {
                    "input": self.txt_input_entrega.GetValue().strip(),
                    "output": self.txt_output_entrega.GetValue().strip()
                }
            }
        }

        # aprovecho que ya tengo un procesar ejec
        self.orquestador_principal.procesar_pack_ejercicios([ejercicio_formateado])

        wx.MessageBox("El ejercicio se guardó y se actualizó la interfaz.", "Completado", wx.OK | wx.ICON_INFORMATION)
        self.Close()
