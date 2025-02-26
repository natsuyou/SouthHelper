import tkinter as tk
import homepage
import fare_calculator

''' 主視窗與切換功能 '''

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('800x600+100+100')
        self._frame = None
        #self.switch_frame(fare_calculator.fare)
        self.switch_frame(homepage.homepage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()