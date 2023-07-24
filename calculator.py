import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation +=str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,"error")


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0,"end")


win = tk.Tk()
win.geometry("300x275")

text_result = tk.Text(win,height=2,width=16,font=("Arial",24))
text_result.grid(columnspan=5)

btn1=tk.Button(win,text="1",command=lambda: add_to_calculation(1),width=5,font=("Arial",14))
btn1.grid(row=2,column=0)
btn2=tk.Button(win,text="2",command=lambda: add_to_calculation(2),width=5,font=("Arial",14))
btn2.grid(row=2,column=1)
btn3=tk.Button(win,text="3",command=lambda: add_to_calculation(3),width=5,font=("Arial",14))
btn3.grid(row=2,column=2)
btn4=tk.Button(win,text="4",command=lambda: add_to_calculation(4),width=5,font=("Arial",14))
btn4.grid(row=3,column=0)
btn5=tk.Button(win,text="5",command=lambda: add_to_calculation(5),width=5,font=("Arial",14))
btn5.grid(row=3,column=1)
btn6=tk.Button(win,text="6",command=lambda: add_to_calculation(6),width=5,font=("Arial",14))
btn6.grid(row=3,column=2)
btn7=tk.Button(win,text="7",command=lambda: add_to_calculation(7),width=5,font=("Arial",14))
btn7.grid(row=4,column=0)
btn8=tk.Button(win,text="8",command=lambda: add_to_calculation(8),width=5,font=("Arial",14))
btn8.grid(row=4,column=1)
btn9=tk.Button(win,text="9",command=lambda: add_to_calculation(9),width=5,font=("Arial",14))
btn9.grid(row=4,column=2)
btn0=tk.Button(win,text="0",command=lambda: add_to_calculation(0),width=5,font=("Arial",14))
btn0.grid(row=5,column=1)
btn_plus=tk.Button(win,text="+",command=lambda: add_to_calculation("+"),width=5,font=("Arial",14))
btn_plus.grid(row=2,column=3)
btn_minus=tk.Button(win,text="-",command=lambda: add_to_calculation("-"),width=5,font=("Arial",14))
btn_minus.grid(row=3,column=3)
btn_mult=tk.Button(win,text="*",command=lambda: add_to_calculation("*"),width=5,font=("Arial",14))
btn_mult.grid(row=4,column=3)
btn_div=tk.Button(win,text="/",command=lambda: add_to_calculation("/"),width=5,font=("Arial",14))
btn_div.grid(row=5,column=3)
btn_open=tk.Button(win,text="(",command=lambda: add_to_calculation("("),width=5,font=("Arial",14))
btn_open.grid(row=5,column=0)
btn_clo=tk.Button(win,text=")",command=lambda: add_to_calculation(")"),width=5,font=("Arial",14))
btn_clo.grid(row=5,column=2)
btn_equ=tk.Button(win,text="=",command=evaluate_calculation,width=12,font=("Arial",14))
btn_equ.grid(row=6,column=2, columnspan=2)
btn_clr=tk.Button(win,text="C",command=clear_field,width=12,font=("Arial",14))
btn_clr.grid(row=6,column=0, columnspan=2)

win.mainloop()

