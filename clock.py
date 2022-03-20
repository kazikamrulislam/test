# Clock Python

from tkinter import Label, Tk
import time

app_clock = Tk()
app_clock.title("GUI Digital Clock")
app_clock.geometry('422x150')
app_clock.resizable(1,1)
font_size = ("Boulder", 72, "bold")
background = '#f2e750'
forground = '#363529'
border = 20
label = Label(app_clock,font = font_size, bg = background, fg = forground, bd = border)
label.grid(row=0, column=0)

def digi_clock():
  curr_time = time.localtime()
  curr_clock = time.strftime("%H:%M:%S", curr_time)
  label.config(text = curr_clock)
  label.after(200, digi_clock)
digi_clock()
app_clock.mainloop()