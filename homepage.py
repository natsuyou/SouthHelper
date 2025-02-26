import tkinter as tk
import START
import fare_calculator


''' 主頁：顯示各功能按鈕 '''

class homepage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text = '南方小幫手', font=('Arial',40,'bold'))\
            .pack(side = 'top', fill = 'x', pady = 50)
        tk.Button(self, text='填寫出席'\
            , command = lambda:master.switch_frame(fare_calculator.fare)).pack()
        


        
