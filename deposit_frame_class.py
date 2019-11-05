import wx


class DepositFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="입금")
        self.SetSize(300, 140)
        self.mainPanel = wx.Panel(self)        

        self.fgridSizer = wx.FlexGridSizer(rows=2, cols=2, hgap=5, vgap=5)

        self.idStatic  = wx.StaticText(self.mainPanel, label="계좌번호 ")
        self.moneyStatic = wx.StaticText(self.mainPanel, label="입금액 ")
        
        self.idText  = wx.TextCtrl(self.mainPanel)
        self.moneyText = wx.TextCtrl(self.mainPanel)

        self.fgridSizer.Add(self.idStatic)
        self.fgridSizer.Add(self.idText, 0, wx.EXPAND)
        self.fgridSizer.Add(self.moneyStatic)
        self.fgridSizer.Add(self.moneyText, 0, wx.EXPAND)

        # 윈도우 크기 변경시 두 번째 컬럼의 너비도 따라 변경되도록 지정함.
        self.fgridSizer.AddGrowableCol(1) 

        # 윈도우 크기 변경시 두 번째 컬럼의 너비도 따라 변경되도록 지정함.
        self.fgridSizer.AddGrowableRow(1)
        
        self.vtBoxSizer = wx.BoxSizer(wx.VERTICAL)
        self.vtBoxSizer.Add(self.fgridSizer, 1, wx.EXPAND | wx.ALL, 5)

        self.btn = wx.Button(self.mainPanel, label='입금')
        self.btn.Bind(wx.EVT_BUTTON,self.onBtnClick)
        self.vtBoxSizer.Add(self.btn, 1, wx.EXPAND | wx.ALL, 5)
        
        self.mainPanel.SetSizer(self.vtBoxSizer)

    
    def onBtnClick(self, event):
        pass
        
        
if __name__ == "__main__":
    app = wx.App()
    frame = DepositFrame()
    frame.Show()

    app.MainLoop()        
