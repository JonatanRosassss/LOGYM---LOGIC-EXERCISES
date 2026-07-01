import wx

class CrearEjercicio(wx.Frame):
    def __init__(self, parent, panel_orquestador_principal):
        super().__init__(parent, title="Formulario: Alta de Ejercicios", size=(480, 680),
        style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))

        self.panel_orquestador_principal = panel_orquestador_principal
        self.SetBackgroundColour(wx.Colour(60, 60, 60))

        self.construir_interfaz_del_formulario()

    def construir_interfaz_del_formulario(self):
        sizer_vertical_de_la_ventana = wx.BoxSizer(wx.VERTICAL)


        def agregar_etiqueta_blanca(texto):
            etiqueta = wx.StaticText(self, label=texto)
            etiqueta.SetForegroundColour(wx.WHITE)
            sizer_vertical_de_la_ventana.Add(etiqueta, 0, wx.LEFT | wx.TOP, 10)

        agregar_etiqueta_blanca("Nombre de la actividad / ejercicio:")
        self.caja_texto_nombre = wx.TextCtrl(self)
        sizer_vertical_de_la_ventana.Add(self.caja_texto_nombre, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 15)

        agregar_etiqueta_blanca("Categoría temática:")
        self.caja_texto_categoria = wx.TextCtrl(self)
        sizer_vertical_de_la_ventana.Add(self.caja_texto_categoria, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 15)

        agregar_etiqueta_blanca("Dificultad (Escribir: Fácil, Media o Difícil):")
        self.caja_texto_dificultad = wx.TextCtrl(self, value="Fácil")
        sizer_vertical_de_la_ventana.Add(self.caja_texto_dificultad, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 15)

        agregar_etiqueta_blanca("Tiempo límite asignado (en segundos):")
        self.caja_texto_tiempo_segundos = wx.TextCtrl(self, value="120")
        sizer_vertical_de_la_ventana.Add(self.caja_texto_tiempo_segundos, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 15)

        agregar_etiqueta_blanca("Enunciado de; problema:")
        self.caja_texto_enunciado = wx.TextCtrl(self, style=wx.TE_MULTILINE, size=(-1, 80))
        sizer_vertical_de_la_ventana.Add(self.caja_texto_enunciado, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 15)

        # Secciones simplificadas para casos de prueba sin splitters complejos
        agregar_etiqueta_blanca("Caso de EJEMPLO - Input:")
        self.caja_texto_input_ejemplo = wx.TextCtrl(self, style=wx.TE_MULTILINE, size=(-1, 40))
        sizer_vertical_de_la_ventana.Add(self.caja_texto_input_ejemplo, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 15)

        agregar_etiqueta_blanca("Caso de EJEMPLO - Output:")
        self.caja_texto_output_ejemplo = wx.TextCtrl(self, style=wx.TE_MULTILINE, size=(-1, 40))
        sizer_vertical_de_la_ventana.Add(self.caja_texto_output_ejemplo, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 15)

        agregar_etiqueta_blanca("Caso de ENTREGA - Entrada (Input Entrega):")
        self.caja_texto_input_entrega = wx.TextCtrl(self, style=wx.TE_MULTILINE, size=(-1, 40))
        sizer_vertical_de_la_ventana.Add(self.caja_texto_input_entrega, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 15)

        agregar_etiqueta_blanca("Caso de ENTREGA - Salida Esperada (Output Entrega):")
        self.caja_texto_output_entrega = wx.TextCtrl(self, style=wx.TE_MULTILINE, size=(-1, 40))
        sizer_vertical_de_la_ventana.Add(self.caja_texto_output_entrega, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 15)

        self.boton_finalizar_guardado = wx.Button(self, label="Registrar Ejercicio")
        self.boton_finalizar_guardado.SetBackgroundColour(wx.Colour(140, 230, 140))
        self.boton_finalizar_guardado.Bind(wx.EVT_BUTTON, self.cuando_presionan_registrar_ejercicio)

        sizer_vertical_de_la_ventana.Add(self.boton_finalizar_guardado, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 20)

        self.SetSizer(sizer_vertical_de_la_ventana)
        self.Layout()

    def cuando_presionan_registrar_ejercicio(self, event):
        if self.caja_texto_nombre.GetValue().strip() == "" or self.caja_texto_enunciado.GetValue().strip() == "":
            wx.MessageBox("Faltan completar campos", "Termina", wx.OK | wx.ICON_WARNING)
            return

        try:
            conversion_tiempo = int(self.caja_texto_tiempo_segundos.GetValue())
        except:
            wx.MessageBox("El tiempo debe ser un número entero.", "Error de entrada", wx.OK | wx.ICON_ERROR)
            return


        ejercicio_formateado = {
            "nombre": self.caja_texto_nombre.GetValue().strip(),
            "configuracion": {
                "dificultad": self.caja_texto_dificultad.GetValue().strip(),
                "categoria": self.caja_texto_categoria.GetValue().strip(),
                "tiempo_limite_seg": conversion_tiempo
            },
            "enunciado": self.caja_texto_enunciado.GetValue().strip(),
            "complejidad": "O(N)",
            "casos_prueba": {
                "ejemplo": {
                    "input": self.caja_texto_input_ejemplo.GetValue().strip(),
                    "output": self.caja_texto_output_ejemplo.GetValue().strip()
                },
                "entrega": {
                    "input": self.caja_texto_input_entrega.GetValue().strip(),
                    "output": self.caja_texto_output_entrega.GetValue().strip()
                }
            }
        }

        # aprovecho que ya tengo un procesar ejec
        self.panel_orquestador_principal.procesar_pack_ejercicios([ejercicio_formateado])

        wx.MessageBox("El ejercicio se guardó y se actualizó la interfaz.", "Completado", wx.OK | wx.ICON_INFORMATION)
        self.Close()
