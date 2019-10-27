import json
import urllib.request
import wx

from wx.lib.pubsub import setuparg1
from wx.lib.pubsub import pub

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
        self.list_ctrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_task_item_click)

        main_sizer.Add(self.list_ctrl, 1, wx.ALL | wx.EXPAND, 5)        
        task_button = wx.Button(self, label='Load Tasks')
        task_button.Bind(wx.EVT_BUTTON, self.on_load_tasks_click)
        main_sizer.Add(task_button, 0, wx.BOTTOM | wx.CENTER, 5)

        self.SetSizer(main_sizer)

    def on_task_item_click(self, event):
        print(event)

    def on_load_tasks_click(self, event):
        print(event)
        self.list_ctrl.DeleteAllItems()

        try:
            with urllib.request.urlopen("http://localhost:5000/tasks") as url:
                data = json.loads(url.read().decode())
                print(data)

                index = 0
                for name, desc in data.items():
                	self.list_ctrl.InsertItem(index, name)
                	self.list_ctrl.SetItem(index, 1, desc)
                	index = index + 1
            pub.sendMessage(('change_statusbar'), "Connected")
        except urllib.error.HTTPError as e:
            wx.MessageBox(str(e.code), 'Error', wx.OK | wx.ICON_ERROR)
        except urllib.error.URLError as e:
            wx.MessageBox(str(e.reason), 'Error', wx.OK | wx.ICON_ERROR)

class DCompFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None,
                         title='dcomp')
        self.panel = TaskPanel(self)
        self.statusbar = self.CreateStatusBar(1)
        pub.subscribe(self.change_statusbar, 'change_statusbar')
        pub.sendMessage(('change_statusbar'), "Not Connected")
        self.SetMinSize((500,250))
        self.Center()
        self.Show()

    def change_statusbar(self, msg):
        print(str(msg))
        self.SetStatusText(msg.data)

if __name__ == '__main__':
    app = wx.App(False)
    frame = DCompFrame()
    #icon from http://icons8.com/
    frame.SetIcon(wx.Icon("Sirubico-Black-Metal-PC.ico"))
    app.MainLoop()
