import wx


class MakeAccFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="계좌개설")
        self.SetSize(300, 260)
        self.mainPanel = wx.Panel(self)        

        self.fgridSizer = wx.FlexGridSizer(rows=4, cols=2, hgap=5, vgap=5)

        self.sectStatic  = wx.StaticText(self.mainPanel, label="계좌구분")
        self.idStatic  = wx.StaticText(self.mainPanel, label="계좌번호 ")
        self.nameStatic = wx.StaticText(self.mainPanel, label="이름 ")
        self.moneyStatic = wx.StaticText(self.mainPanel, label="입금액 ")

        accsect=['일반계좌', '특수게좌']
        self.sectCombo = wx.ComboBox(self.mainPanel, choices=accsect, style=wx.CB_READONLY)
        self.sectCombo.SetSelection(0)  #일반계좌 선택
        self.Bind(wx.EVT_COMBOBOX, self.onComboChange, self.sectCombo)
        
        self.idText  = wx.TextCtrl(self.mainPanel)
        self.nameText = wx.TextCtrl(self.mainPanel)
        self.moneyText = wx.TextCtrl(self.mainPanel)

        self.fgridSizer.Add(self.sectStatic)
        self.fgridSizer.Add(self.sectCombo, 0, wx.EXPAND)
        self.fgridSizer.Add(self.idStatic)
        self.fgridSizer.Add(self.idText, 0, wx.EXPAND)
        self.fgridSizer.Add(self.nameStatic)
        self.fgridSizer.Add(self.nameText, 0, wx.EXPAND)
        self.fgridSizer.Add(self.moneyStatic)
        self.fgridSizer.Add(self.moneyText, 0, wx.EXPAND)

        # 윈도우 크기 변경시 두 번째 컬럼의 너비도 따라 변경되도록 지정함.
        self.fgridSizer.AddGrowableCol(1) 

        # 윈도우 크기 변경시 두 번째 컬럼의 너비도 따라 변경되도록 지정함.
        self.fgridSizer.AddGrowableRow(3)
        
        self.vtBoxSizer = wx.BoxSizer(wx.VERTICAL)
        self.vtBoxSizer.Add(self.fgridSizer, 1, wx.EXPAND | wx.ALL, 5)
        
        gradeList = ['VIP', 'Gold', 'Silver', 'Normal'] 
          
        self.rbox = wx.RadioBox(self.mainPanel, label='등급', pos=(80, 10), choices=gradeList,
                                majorDimension=1, style=wx.RA_SPECIFY_ROWS) #가로정렬
        self.rbox.Disable()
        self.vtBoxSizer.Add(self.rbox, 1, wx.EXPAND | wx.ALL, 5)

        self.btn = wx.Button(self.mainPanel, label='계좌개설')
        self.btn.Bind(wx.EVT_BUTTON,self.onBtnClick)
        self.vtBoxSizer.Add(self.btn, 1, wx.EXPAND | wx.ALL, 5)
        
        self.mainPanel.SetSizer(self.vtBoxSizer)
        
    def onComboChange(self, event):
        idx = self.sectCombo.GetCurrentSelection()
        if idx==1:
            self.rbox.Enable(enable=True)
        else:
            self.rbox.Disable()
    
    def onBtnClick(self, event):
        pass
        
        
if __name__ == "__main__":
    app = wx.App()
    frame = MakeAccFrame()
    frame.Show()

    app.MainLoop()        
