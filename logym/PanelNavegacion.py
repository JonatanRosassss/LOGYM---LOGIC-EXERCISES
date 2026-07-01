import wx

class PanelNavegacionFiltros(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent)
        self.SetBackgroundColour(wx.Colour(50, 50, 50))

        #porque los diccionarios? porque es lo que mas facil es para manejar los json
        #si hiciera una clase despues lo tendria que parsear
        # nuevo_ejercicio = { ... }
        self.sizer_ejercicios = None
        self.callback_seleccionar_ejercicio = None
        self.inicializar_componentes()

    def set_callback(self, funcion):
        self.callback_seleccionar_ejercicio = funcion

    def inicializar_componentes(self):
        sizer_principal = wx.BoxSizer(wx.VERTICAL)

        lbl_titulo_practicar = wx.StaticText(self, label="Selecciona lo que hoy\nquieres practicar", style=wx.ALIGN_CENTER_HORIZONTAL)
        lbl_titulo_practicar.SetForegroundColour(wx.WHITE)
        lbl_titulo_practicar.SetFont(wx.Font(14, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        sizer_principal.Add(lbl_titulo_practicar, 0, wx.ALL | wx.EXPAND, 15)

        lbl_filtrar = wx.StaticText(self, label="FILTRAR", style=wx.ALIGN_CENTER_HORIZONTAL)
        lbl_filtrar.SetForegroundColour(wx.WHITE)
        lbl_filtrar.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        sizer_principal.Add(lbl_filtrar, 0, wx.BOTTOM | wx.ALIGN_CENTER, 5)

        sizer_filtros = wx.FlexGridSizer(rows=2, cols=2, vgap=10, hgap=10)

        lbl_categoria = wx.StaticText(self, label="Categoria:")
        lbl_categoria.SetForegroundColour(wx.WHITE)
        self.cmb_categoria = wx.ComboBox(self, style=wx.CB_READONLY)

        lbl_dificultad = wx.StaticText(self, label="Dificultad:")
        lbl_dificultad.SetForegroundColour(wx.WHITE)
        self.cmb_dificultad = wx.ComboBox(self, style=wx.CB_READONLY)

        sizer_filtros.AddMany([
            (lbl_categoria, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 20),
            (self.cmb_categoria, 1, wx.EXPAND | wx.RIGHT, 20),
            (lbl_dificultad, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 20),
            (self.cmb_dificultad, 1, wx.EXPAND | wx.RIGHT, 20)
        ])

        #esto es para que ocupe el tamanio del espacio segun el estiramiento del splitter, el primer 1 significa la columna y el segundo es la proporcion
        sizer_filtros.AddGrowableCol(1, 1)
        sizer_principal.Add(sizer_filtros, 0, wx.EXPAND | wx.BOTTOM, 20)

        #esto es para el caso de que haya monton de ejrciciios, prevenir eso y habilitar un scroll
        self.scroll_ejercicios = wx.ScrolledWindow(self, style=wx.VSCROLL | wx.BORDER_SIMPLE)
        self.scroll_ejercicios.SetBackgroundColour(wx.Colour(220, 220, 220))
        #en vez de que se scrollie pixel por pixel ira de 20 en 20, el primer 0 quiere decir que va a ir vertical
        self.scroll_ejercicios.SetScrollRate(0, 20)

        self.cmb_categoria.Bind(wx.EVT_COMBOBOX, self.filtrado_archivo)
        self.cmb_dificultad.Bind(wx.EVT_COMBOBOX, self.filtrado_archivo)

        self.sizer_ejercicios = wx.BoxSizer(wx.VERTICAL)
        self.scroll_ejercicios.SetSizer(self.sizer_ejercicios)

        sizer_principal.Add(self.scroll_ejercicios, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 20)

        lbl_temario = wx.StaticText(self, label="T E M A R I O", style=wx.ALIGN_CENTER_HORIZONTAL)
        lbl_temario.SetForegroundColour(wx.WHITE)
        lbl_temario.SetFont(wx.Font(16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        sizer_principal.Add(lbl_temario, 0, wx.BOTTOM | wx.ALIGN_CENTER, 5)

        #el arbol, esto es para dividir los , oculta la raiz, dice que no hay botones y dibuja un borde fino
        self.tree_temario = wx.TreeCtrl(self, style=wx.TR_HIDE_ROOT | wx.TR_NO_BUTTONS | wx.BORDER_SIMPLE)
        self.tree_temario.SetBackgroundColour(wx.Colour(220, 220, 220))

        fuente_tree = wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.tree_temario.SetFont(fuente_tree)

        self.tree_root = self.tree_temario.AddRoot("Root")
        self.tree_temario.Bind(wx.EVT_TREE_SEL_CHANGED, self.click_tema_arbol)

        sizer_principal.Add(self.tree_temario, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 20)
        self.SetSizer(sizer_principal)

    def click_tema_arbol(self, event):
        item_seleccionado = event.GetItem()
        texto_nodo = self.tree_temario.GetItemText(item_seleccionado)
        self.cmb_categoria.SetStringSelection(texto_nodo)
        self.filtrado_archivo()

    #cada vez que se detecta un ejercicio nuevo, pum, los inyecta
    def agregar_ejercicio_en_la_lista_visual(self, datos_ejercicio: dict):
        #lo mismo de los parametros en caso de fallo
        nombre = datos_ejercicio.get("nombre", "Sin título")
        categoria = datos_ejercicio.get("configuracion", {}).get("categoria", "General")
        dificultad = datos_ejercicio.get("configuracion", {}).get("dificultad", "Facil")

        #se crean sobre el panel de ejercicios que es el que tiene el scrollwindow
        btn_ejercicio = wx.Button(self.scroll_ejercicios, label=nombre, size=(120, -1))
        lbl_detalles = wx.StaticText(self.scroll_ejercicios, label=f"{categoria}, {dificultad}")
        lbl_detalles.SetForegroundColour(wx.BLACK)

        btn_ejercicio.Bind(wx.EVT_BUTTON, lambda evt, d=datos_ejercicio: self.click_ejercicio(d))

        self.sizer_ejercicios.Add(btn_ejercicio, 0, wx.TOP | wx.LEFT, 10)
        self.sizer_ejercicios.Add(lbl_detalles, 0, wx.BOTTOM | wx.LEFT, 5)

        self.scroll_ejercicios.Layout()
        #le dice a la ventanita de scroll que se crecio el contenido
        self.scroll_ejercicios.FitInside()

    def actualizar_temario(self, categorias: list):
        #antes de inyectar algo, elimina lo anterior
        self.tree_temario.DeleteChildren(self.tree_root)
        for cat in categorias:
            self.tree_temario.AppendItem(self.tree_root, cat)
        self.tree_temario.ExpandAll()

    def click_ejercicio(self, datos):
        if self.callback_seleccionar_ejercicio:
            self.callback_seleccionar_ejercicio(datos)

    def actualizar_opciones_filtros(self, categorias:list, dificultades:list):
        self.cmb_categoria.Clear()
        self.cmb_categoria.Append("Todas")
        for c in categorias:
            self.cmb_categoria.Append(c)
        self.cmb_categoria.SetSelection(0)

        self.cmb_dificultad.Clear()
        self.cmb_dificultad.Append("Todas")
        for d in dificultades:
            self.cmb_dificultad.Append(d)
        self.cmb_dificultad.SetSelection(0)

    def filtrado_archivo(self, event = None):
        import Utilidades

        categ_selec = self.cmb_categoria.GetStringSelection()
        dific_selec = self.cmb_dificultad.GetStringSelection()
        ejercicios = Utilidades.leer_ejercicios()
        self.limpiar()
        for e in ejercicios:
            cat_ejercicio = e.get("configuracion", {}).get("categoria", "")
            dif_ejercicio = e.get("configuracion", {}).get("dificultad", "")

            cumple_categ = (categ_selec == "Todas" or categ_selec == cat_ejercicio)
            cumple_dif  = (dific_selec == "Todas" or dific_selec == dif_ejercicio)

            if cumple_categ and cumple_dif:
                self.agregar_ejercicio_en_la_lista_visual(e)

    def limpiar(self):
        self.sizer_ejercicios.Clear(True)
        self.scroll_ejercicios.Layout()
        self.scroll_ejercicios.FitInside()
