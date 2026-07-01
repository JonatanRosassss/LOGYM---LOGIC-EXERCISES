import wx

class CustomMenuBar(wx.MenuBar):
    def __init__(self):
        super().__init__()
        self._inicializar_menus()
#esto va inicalizar el menu bar, codigo que se tomo de la demo
    def _inicializar_menus(self):
        menu_archivo = wx.Menu()
        menu_archivo.Append(wx.ID_NEW, "&Crear Ejercicio", "Información sobre Mercurio")
        menu_archivo.Append(wx.ID_OPEN, "&Importar pack de Ejercicios(JSON)", "Información sobre Venus")
        #menu_archivo.Append(103, "&Rendimiento(PDF)", "Información sobre la Tierra")
        menu_archivo.Append(104, "&Salir", "Información sobre la Tierra")
        # menu_archivo.AppendSeparator()
        # menu_archivo.Append(104, "&Mars", "Información sobre Marte")

        menu_herramientas = wx.Menu()
        #menu_herramientas.Append(101, "&Cambiar Tema", "Información sobre Mercurio")
        #menu_herramientas.Append(102, "&Borrar Historial", "Información sobre Venus")
        menu_herramientas.Append(103, "&Desactivar Temporizador", "Información sobre la Tierra")
        # menu_editar.Append(wx.ID_UNDO, "&Deshacer\tCtrl+Z", "Deshacer última acción")
        # menu_editar.Append(wx.ID_REDO, "&Rehacer\tCtrl+Y", "Rehacer última acción")
        # menu_editar.AppendSeparator()
        # menu_editar.Append(wx.ID_COPY, "&Copiar\tCtrl+C", "Copiar selección")
        # menu_editar.Append(wx.ID_PASTE, "&Pegar\tCtrl+V", "Pegar desde el portapapeles")

        menu_ayuda = wx.Menu()
        menu_ayuda.Append(wx.ID_ABOUT, "&Acerca de LoGym", "Información sobre el software")
        menu_ayuda.Append(201, "&Guía de LoGym", "Muestra el manual de usuario")

        self.Append(menu_archivo, "&Archivo")
        self.Append(menu_herramientas, "&Herramientas")
        self.Append(menu_ayuda, "&Ayuda")
