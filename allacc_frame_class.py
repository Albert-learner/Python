import wx.grid
#https://wxpython.org/Phoenix/docs/html/wx.grid.Grid.html 참조
class AllAccFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="전체계좌조회")
        self.SetSize(350, 315)
        self.mainPanel = wx.Panel(self)        
        
        self.grid = wx.grid.Grid(self.mainPanel)
        self.grid.CreateGrid(0,4) 
        self.grid.SetColLabelValue(0, "계좌번호")
        self.grid.SetColLabelValue(1, "이름")
        self.grid.SetColLabelValue(2, "잔액")
        self.grid.SetColLabelValue(3, "등급")
        self.grid.SetRowLabelSize(1)
        
        self.grid.AppendRows(numRows=3, updateLabels=True) #동적 행수 증가
        
        self.__readOnlyGridCell()
        
        self.vtBoxSizer = wx.BoxSizer(wx.VERTICAL)

        self.btn = wx.Button(self.mainPanel, label='전체계좌조회')
        self.btn.Bind(wx.EVT_BUTTON,self.onBtnClick)
        self.vtBoxSizer.Add(self.btn, 0, wx.EXPAND | wx.ALL, 5)
        self.vtBoxSizer.Add(self.grid, 1, wx.EXPAND | wx.ALL, 5)
        
        self.mainPanel.SetSizer(self.vtBoxSizer)
    
    #각 셀 입력 불가
    def __readOnlyGridCell(self):
        rows = self.grid.GetNumberRows()
        cols = self.grid.GetNumberCols()
        for r in range(rows):
            for c in range(cols):
                self.grid.SetReadOnly(r, c, True)    
        
    def onBtnClick(self, event):
        pass
        #self.grid.DeleteRows(pos=0, numRows=self.grid.GetNumberRows(), updateLabels=True)
        #self.grid.AppendRows(numRows=10, updateLabels=True)
        #self.grid.SetCellValue(0, 0,str(1))  #각 셀 데이터 입력
        #self.__readOnlyGridCell()
        
        
if __name__ == "__main__":
    app = wx.App()
    frame = AllAccFrame()
    frame.Show()

    app.MainLoop()        
