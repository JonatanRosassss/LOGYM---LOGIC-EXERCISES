import wx
import Frame
class LoGymApp(wx.App):
    def __init__(self, redirect=False, filename=None, useBestVisual=False, clearSigInt=True):
        super().__init__(redirect, filename, useBestVisual, clearSigInt)
        self.frame = Frame.MainFrame()
        self.frame.Show(True)

if __name__ == '__main__':
    app = LoGymApp(False)
    app.MainLoop()
AttributeError



