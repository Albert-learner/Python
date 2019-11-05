import wx


class AccInfoFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="계좌조회")
        self.SetSize(300, 225)
        self.mainPanel = wx.Panel(self)        

        self.fgridSizer = wx.FlexGridSizer(rows=5, cols=2, hgap=5, vgap=5)

        self.idStatic  = wx.StaticText(self.mainPanel, label="계좌번호 ")
        self.nameStatic = wx.StaticText(self.mainPanel, label="이름 ")
        self.moneyStatic = wx.StaticText(self.mainPanel, label="입금액 ")
        self.sectStatic  = wx.StaticText(self.mainPanel, label="계좌구분")
        self.gradeStatic  = wx.StaticText(self.mainPanel, label="등급")
                        
        self.idText  = wx.TextCtrl(self.mainPanel)
        self.nameText = wx.TextCtrl(self.mainPanel)
        self.moneyText = wx.TextCtrl(self.mainPanel)
        self.sectText = wx.TextCtrl(self.mainPanel)
        self.gradeText = wx.TextCtrl(self.mainPanel)
        
        self.nameText.Disable()
        self.moneyText.Disable()
        self.sectText.Disable()
        self.gradeText.Disable()

        self.fgridSizer.Add(self.idStatic)
        self.fgridSizer.Add(self.idText, 0, wx.EXPAND)
        self.fgridSizer.Add(self.nameStatic)
        self.fgridSizer.Add(self.nameText, 0, wx.EXPAND)
        self.fgridSizer.Add(self.moneyStatic)
        self.fgridSizer.Add(self.moneyText, 0, wx.EXPAND)
        self.fgridSizer.Add(self.sectStatic)
        self.fgridSizer.Add(self.sectText, 0, wx.EXPAND)
        self.fgridSizer.Add(self.gradeStatic)
        self.fgridSizer.Add(self.gradeText, 0, wx.EXPAND)

        # 윈도우 크기 변경시 두 번째 컬럼의 너비도 따라 변경되도록 지정함.
        self.fgridSizer.AddGrowableCol(1) 

        # 윈도우 크기 변경시 두 번째 컬럼의 너비도 따라 변경되도록 지정함.
        self.fgridSizer.AddGrowableRow(3)
        
        self.vtBoxSizer = wx.BoxSizer(wx.VERTICAL)
        self.vtBoxSizer.Add(self.fgridSizer, 1, wx.EXPAND | wx.ALL, 5)

        self.btn = wx.Button(self.mainPanel, label='계좌조회')
        self.btn.Bind(wx.EVT_BUTTON,self.onBtnClick)
        self.vtBoxSizer.Add(self.btn, 1, wx.EXPAND | wx.ALL, 5)
        
        self.mainPanel.SetSizer(self.vtBoxSizer)
    
    def onBtnClick(self, event):
        pass
        
        
if __name__ == "__main__":
    app = wx.App()
    frame = AccInfoFrame()
    frame.Show()

    app.MainLoop()        
