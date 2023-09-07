import tkinter as tk
from tkinter import messagebox
def love_warning():
    text = messagebox.askyesno("warning","accept my love baby!!")
    if text:
        messagebox.showinfo("congratulation", "love you too baby")
    else:
        love_warning()

win=tk.Tk()

warning_button = tk.Button(win, text="Show Warning (Yes/No)", command=love_warning())
warning_button.pack()

win.mainloop()