import tkinter as tk
import START
import fare_calculator


''' 主頁：顯示各功能按鈕 '''

class homepage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text = '南方小幫手', font=('Arial',40,'bold'))\
            .pack(side = 'top', fill = 'x', pady = 50)
<<<<<<< HEAD
        tk.Button(self, text='捐款名冊'\
            ).pack()
        tk.Button(self, text='志工名冊'\
            ).pack()
        tk.Button(self, text='出席設定'\
            , command = lambda:master.switch_frame(fare_calculator.fare)).pack()
        tk.Button(self, text='學期統計'\
            ).pack()
=======
        tk.Button(self, text='填寫出席'\
            , command = lambda:master.switch_frame(fare_calculator.fare)).pack()
>>>>>>> a489096dc70bdfbe91aef8e36f06ee31e191e86c
        


        
