import tkinter as tk
import time
import psutil


class App():

    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text="")
        self.label.pack()
        self.update()
        self.root.overrideredirect(True)
        self._offsetx = 0
        self._offsety = 0
        self.root.bind('<Button-1>', self.clickwin)
        self.root.bind('<B1-Motion>', self.dragwin)
        self.root.lift()
        self.root.call('wm', 'attributes', '.', '-topmost', True)
        self.root.after_idle(self.root.call, 'wm',
                             'attributes', '.', '-topmost', True)
        self.root.mainloop()

    def update(self):
        battery = psutil.sensors_battery()
        plug = ""
        if battery.power_plugged:
            plug = "•"

        now = '{}   {}% {}'.format(time.strftime(
            "%H:%M   %d %b"), battery.percent, plug)
        self.label.configure(text=now, font='-family roboto -size 8', fg = 'white', background = 'black')
        self.root.after(1000, self.update)

    def dragwin(self, event):
        x = self.root.winfo_pointerx() - self._offsetx
        y = self.root.winfo_pointery() - self._offsety
        self.root.geometry('+{x}+{y}'.format(x=x, y=y))

    def clickwin(self, event):
        self._offsetx = event.x
        self._offsety = event.y


app = App()
