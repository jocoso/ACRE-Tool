import wx

class Displayer(wx.App):
    def __init__(self, image):
        self.image = image 
        super().__init__(useBestVisual=True, clearSigInt=True)

    def OnInit(self):
        self.frame = wx.Frame(parent=None, title="Displayer")
        self.draw(self.image)
        self.frame.Show()
        return True


