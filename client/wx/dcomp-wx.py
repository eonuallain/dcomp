import wx

class TaskPanel(wx.Panel):    
    def __init__(self, parent):
        super().__init__(parent)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.row_obj_dict = {}

        self.list_ctrl = wx.ListCtrl(
            self, size=(-1, 100), 
            style=wx.LC_REPORT | wx.BORDER_SUNKEN
        )
        self.list_ctrl.InsertColumn(0, 'Task', width=140)
        self.list_ctrl.InsertColumn(1, 'Description', width=300)
        main_sizer.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 5)        
        edit_button = wx.Button(self, label='Load Tasks')
        edit_button.Bind(wx.EVT_BUTTON, self.on_click)
        main_sizer.Add(edit_button, 0, wx.ALL | wx.CENTER, 5)        
        self.SetSizer(main_sizer)

    def on_click(self, event):
        print(event)

class DCompFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None,
                         title='dcomp')
        self.panel = TaskPanel(self)
        self.Show()

if __name__ == '__main__':
    app = wx.App(False)
    frame = DCompFrame()
    app.MainLoop()
