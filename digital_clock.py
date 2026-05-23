from tkinter import *
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title("Clock")
root.resizable(False, False) # lock the window size
def update_time():
    current_time = strftime("%I:%M:%S %p")
    label.config(text=current_time)
    label.after(1000, update_time) # call again after 1 second
label = Label(
    root,
    font=("ds-digital", 80),
    background="black",
    foreground="cyan"
)
label.pack(anchor="center", padx=20, pady=20)
update_time()
root.mainloop()