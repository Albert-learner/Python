import wx

from makeacc_frame_class import MakeAccFrame

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="숭실 은행")
        self.accs = {}
        self.menubar = wx.MenuBar()
        accMenu = wx.Menu()  # wx.Menu 인스턴스 생성
        makeaccMenu = accMenu.Append(wx.ID_ANY, "계좌개설") # wx.MenuItem 인스턴스 생성
        depositMenu = accMenu.Append(wx.ID_ANY, "입금")
        withdrawMenu = accMenu.Append(wx.ID_ANY, "출금")
        accInfoMenu = accMenu.Append(wx.ID_ANY, "계좌조회")     
        allaccInfoMenu = accMenu.Append(wx.ID_ANY, "전체계좌조회")                   
        accMenu.AppendSeparator()
        exitMenu = accMenu.Append(wx.ID_ANY, "끝내기")

        self.menubar.Append(accMenu, "&계좌")
        self.SetMenuBar(self.menubar)

        self.Bind(wx.EVT_MENU, self.onMakeAcc, makeaccMenu)


    def onMakeAcc(self, event):
        frame = MakeAccFrame()
        frame.Show();

if __name__ == "__main__":
    app = wx.App()
    frame = MainFrame()
    frame.Show()

    app.MainLoop()        
