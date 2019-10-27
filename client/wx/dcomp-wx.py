import json
import urllib.request
import wx

from wx.lib.pubsub import setuparg1
from wx.lib.pubsub import pub

from task_enc import TaskEncryption

class TaskPanel(wx.Panel):  
    def __init__(self, parent):
        super().__init__(parent)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)

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
        task_button.SetDefault()
        task_button.Bind(wx.EVT_BUTTON, self.on_load_tasks_click)
        main_sizer.Add(task_button, 0, wx.BOTTOM | wx.CENTER, 5)
        button_sizer.Add(task_button, 0, wx.CENTER|wx.ALL, 5)

        stop_button = wx.Button(self, label='Stop Tasks')
        stop_button.Disable()
        button_sizer.Add(stop_button, 0, wx.CENTER|wx.ALL, 5)
        main_sizer.Add(button_sizer, 0, wx.CENTER)

        self.SetSizer(main_sizer)

    def start_task(self, task):
        print("start_task called with", task, flush=True)
        task_encryption.run(task)

    def on_task_item_click(self, event):
        index = self.list_ctrl.GetFocusedItem()

        if index >= 0:
            print("selected {}".format(str(self.row_obj_dict[index])), flush=True)

            task = str(self.row_obj_dict[index])
            self.start_task(task)


    def on_load_tasks_click(self, event):
        try:
            with urllib.request.urlopen("http://localhost:5000/tasks") as url:
                data = json.loads(url.read().decode())

                index = 0
                for name, desc in data.items():
                    self.list_ctrl.InsertItem(index, name)
                    self.list_ctrl.SetItem(index, 1, desc)
                    self.row_obj_dict[index] = name
                    index = index + 1
            pub.sendMessage(('change_statusbar_main'), "Connected")
        except urllib.error.HTTPError as e:
            wx.MessageBox(str(e.code), 'Error', wx.OK | wx.ICON_ERROR)
        except urllib.error.URLError as e:
            wx.MessageBox(str(e.reason), 'Error', wx.OK | wx.ICON_ERROR)

class DCompFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None,
                         title='dcomp')
        self.panel = TaskPanel(self)
        self.statusbar = self.CreateStatusBar(2)
        pub.subscribe(self.change_statusbar_main, 'change_statusbar_main')
        pub.subscribe(self.change_statusbar_task_count, 'change_statusbar_task_count')
        pub.sendMessage(('change_statusbar_main'), "Not Connected")
        pub.sendMessage(('change_statusbar_task_count'), "0")

        self.SetMinSize((500,250))
        self.Center()
        self.Show()

    def change_statusbar_main(self, msg):
        self.SetStatusText(msg.data)

    def change_statusbar_task_count(self, msg):
        self.SetStatusText(msg.data, 1)

if __name__ == '__main__':

    app = wx.App(False)
    frame = DCompFrame()
    #icon from http://icons8.com/
    frame.SetIcon(wx.Icon("Sirubico-Black-Metal-PC.ico"))

    task_encryption = TaskEncryption()

    print(str(task_encryption), flush=True)
    app.MainLoop()
