from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500,height=250)
window.config(padx=20,pady=20)

entry = Entry(width=10)
entry.insert(END,string="0")
entry.grid(row=0,column=1,padx=5,pady=10)

miles = Label(text="Miles")
miles.grid(row=0,column=2,padx=5,pady=10)

label3 = Label(text="is equal to")
label3.grid(row=1,column=0,padx=10,pady=10)

label4 = Label(text="Km")
label4.grid(row=1,column=3,padx=5,pady=10)

result = Label(text="0")
result.grid(row=1,column=1,padx=5,pady=10)

def Mi_Km():
    num = entry.get()
    if num.isdigit():
        total = (int(num) * 8) / 5
        result.config(text=total)
    else:
        result.config(text="please Enter a number")

button = Button(text="Calculate",command=Mi_Km)
button.grid(row=2,column=1)


window.mainloop()