import wx

class PanelNavegacionFiltros(wx.Panel):




    def __init__(self, parent):
        super().__init__(parent)
        self.SetBackgroundColour(wx.Colour(50, 50, 50))

        #porque los diccionarios? porque es lo que mas facil es para manejar los json
        #si hiciera una clase despues lo tendria que parsear
        nuevo_ejercicio = {
          "nombre": "Bit++",
          "configuracion": {
            "categoria": "Operadores",
            "dificultad": "Facil"
          }
        }
        nuevo_ejercicio2 = {
          "nombre": "Bit--",
          "configuracion": {
            "categoria": "Operadores",
            "dificultad": "Facilss"
          }
        }
        self.sizer_vertical_donde_se_van_acumulando_los_botones_de_ejercicios = None
        self.funcion_callback_que_se_ejecuta_al_elegir_un_ejercicio = None
        self.inicializar_todos_los_componentes_del_panel_de_filtros()
        self.agregar_ejercicio_en_la_lista_visual(nuevo_ejercicio)
        self.agregar_ejercicio_en_la_lista_visual(nuevo_ejercicio2)

    def set_callback(self, funcion):
        self.funcion_callback_que_se_ejecuta_al_elegir_un_ejercicio = funcion
    def inicializar_todos_los_componentes_del_panel_de_filtros(self):
        sizer_contenedor_de_toda_la_columna_izquierda = wx.BoxSizer(wx.VERTICAL)

        texto_titulo_principal_que_dice_selecciona_lo_que_hoy_quieres_practicar = wx.StaticText(self, label="Selecciona lo que hoy\nquieres practicar", style=wx.ALIGN_CENTER_HORIZONTAL)
        texto_titulo_principal_que_dice_selecciona_lo_que_hoy_quieres_practicar.SetForegroundColour(wx.WHITE)
        texto_titulo_principal_que_dice_selecciona_lo_que_hoy_quieres_practicar.SetFont(wx.Font(14, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        sizer_contenedor_de_toda_la_columna_izquierda.Add(texto_titulo_principal_que_dice_selecciona_lo_que_hoy_quieres_practicar, 0, wx.ALL | wx.EXPAND, 15)

        texto_secundario_que_dice_filtrar = wx.StaticText(self, label="FILTRAR", style=wx.ALIGN_CENTER_HORIZONTAL)
        texto_secundario_que_dice_filtrar.SetForegroundColour(wx.WHITE)
        texto_secundario_que_dice_filtrar.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        sizer_contenedor_de_toda_la_columna_izquierda.Add(texto_secundario_que_dice_filtrar, 0, wx.BOTTOM | wx.ALIGN_CENTER, 5)

        grilla_flex_para_acomodar_los_combobox_de_filtros = wx.FlexGridSizer(rows=2, cols=2, vgap=10, hgap=10)
        texto_label_que_dice_categoria = wx.StaticText(self, label="Categoria:")
        texto_label_que_dice_categoria.SetForegroundColour(wx.WHITE)
        self.combo_desplegable_para_elegir_la_categoria = wx.ComboBox(self, style=wx.CB_READONLY)

        texto_label_que_dice_dificultad = wx.StaticText(self, label="Dificultad:")
        texto_label_que_dice_dificultad.SetForegroundColour(wx.WHITE)
        self.combo_desplegable_para_elegir_la_dificultad = wx.ComboBox(self, style=wx.CB_READONLY)

        grilla_flex_para_acomodar_los_combobox_de_filtros.AddMany([(texto_label_que_dice_categoria, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 20), (self.combo_desplegable_para_elegir_la_categoria, 1, wx.EXPAND | wx.RIGHT, 20), (texto_label_que_dice_dificultad, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 20), (self.combo_desplegable_para_elegir_la_dificultad, 1, wx.EXPAND | wx.RIGHT, 20)])
        #esto es para que ocupe el tamanio del espacio segun el estiramiento del splitter, el primer 1 significa la columna y el segundo es la proporcion
        grilla_flex_para_acomodar_los_combobox_de_filtros.AddGrowableCol(1, 1)
        sizer_contenedor_de_toda_la_columna_izquierda.Add(grilla_flex_para_acomodar_los_combobox_de_filtros, 0, wx.EXPAND | wx.BOTTOM, 20)
        #esto es para el caso de que haya monton de ejrciciios, prevenir eso y habilitar un scroll
        self.ventana_con_scroll_para_los_ejercicios_disponibles = wx.ScrolledWindow(self, style=wx.VSCROLL | wx.BORDER_SIMPLE)
        self.ventana_con_scroll_para_los_ejercicios_disponibles.SetBackgroundColour(wx.Colour(220, 220, 220))
        #en vez de que se scrollie pixel por pixel ira de 20 en 20, el primer 0 quiere decir que va a ir vertical
        self.ventana_con_scroll_para_los_ejercicios_disponibles.SetScrollRate(0, 20)

        self.sizer_vertical_donde_se_van_acumulando_los_botones_de_ejercicios = wx.BoxSizer(wx.VERTICAL)
        self.ventana_con_scroll_para_los_ejercicios_disponibles.SetSizer(self.sizer_vertical_donde_se_van_acumulando_los_botones_de_ejercicios)

        sizer_contenedor_de_toda_la_columna_izquierda.Add(self.ventana_con_scroll_para_los_ejercicios_disponibles, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 20)

        texto_label_que_dice_temario = wx.StaticText(self, label="T E M A R I O", style=wx.ALIGN_CENTER_HORIZONTAL)
        texto_label_que_dice_temario.SetForegroundColour(wx.WHITE)
        texto_label_que_dice_temario.SetFont(wx.Font(12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        sizer_contenedor_de_toda_la_columna_izquierda.Add(texto_label_que_dice_temario, 0, wx.BOTTOM | wx.ALIGN_CENTER, 5)
        #el arbol, esto es para dividir los , oculta la raiz, dice que no hay botones y dibuja un borde fino
        self.controlador_del_arbol_para_el_temario = wx.TreeCtrl(self, style=wx.TR_HIDE_ROOT | wx.TR_NO_BUTTONS | wx.BORDER_SIMPLE)
        self.controlador_del_arbol_para_el_temario.SetBackgroundColour(wx.Colour(220, 220, 220))
        self.nodo_raiz_oculto_del_arbol_de_temas = self.controlador_del_arbol_para_el_temario.AddRoot("Root")

        sizer_contenedor_de_toda_la_columna_izquierda.Add(self.controlador_del_arbol_para_el_temario, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 20)
        self.SetSizer(sizer_contenedor_de_toda_la_columna_izquierda)

#cada vez que se detecta un ejercicio nuevo, pum, los inyecta
    def agregar_ejercicio_en_la_lista_visual(self, datos_en_un_diccionario_del_ejercicio: dict):
        #lo mismo de los parametros en caso de fallo
        nombre_del_ejercicio_recuperado = datos_en_un_diccionario_del_ejercicio.get("nombre", "Sin título")
        categoria_del_ejercicio_recuperada = datos_en_un_diccionario_del_ejercicio.get("configuracion", {}).get("categoria", "General")
        dificultad_del_ejercicio_recuperada = datos_en_un_diccionario_del_ejercicio.get("configuracion", {}).get("dificultad", "Facil")
        #se crean sobre el panel de ejercicios que es el que tiene el scrollwindow
        boton_creado_para_seleccionar_este_ejercicio = wx.Button(self.ventana_con_scroll_para_los_ejercicios_disponibles, label=nombre_del_ejercicio_recuperado, size=(120, -1))
        texto_con_la_descripcion_de_categoria_y_dificultad = wx.StaticText(self.ventana_con_scroll_para_los_ejercicios_disponibles, label=f"{categoria_del_ejercicio_recuperada}, {dificultad_del_ejercicio_recuperada}")
        texto_con_la_descripcion_de_categoria_y_dificultad.SetForegroundColour(wx.BLACK)

        boton_creado_para_seleccionar_este_ejercicio.Bind(wx.EVT_BUTTON, lambda evt, d=datos_en_un_diccionario_del_ejercicio: self.cuando_el_usuario_hace_click_en_un_ejercicio(d))

        self.sizer_vertical_donde_se_van_acumulando_los_botones_de_ejercicios.Add(boton_creado_para_seleccionar_este_ejercicio, 0, wx.TOP | wx.LEFT, 10)
        self.sizer_vertical_donde_se_van_acumulando_los_botones_de_ejercicios.Add(texto_con_la_descripcion_de_categoria_y_dificultad, 0, wx.BOTTOM | wx.LEFT, 5)

        self.ventana_con_scroll_para_los_ejercicios_disponibles.Layout()
        #le dice a la ventanita de scroll que se crecio el contenido
        self.ventana_con_scroll_para_los_ejercicios_disponibles.FitInside()

    def actualizar_toda_la_lista_del_temario_visual(self, lista_con_las_categorias_a_cargar: list):
#antes de inyectar algo, elimina lo anterior
        self.controlador_del_arbol_para_el_temario.DeleteChildren(self.nodo_raiz_oculto_del_arbol_de_temas)
        for cada_categoria_de_la_lista in lista_con_las_categorias_a_cargar:
            self.controlador_del_arbol_para_el_temario.AppendItem(self.nodo_raiz_oculto_del_arbol_de_temas, cada_categoria_de_la_lista)
        self.controlador_del_arbol_para_el_temario.ExpandAll()

    def cuando_el_usuario_hace_click_en_un_ejercicio(self, datos):
        if self.funcion_callback_que_se_ejecuta_al_elegir_un_ejercicio:
            self.funcion_callback_que_se_ejecuta_al_elegir_un_ejercicio(datos)
