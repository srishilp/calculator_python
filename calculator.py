from tkinter import *
from tkinter import font

def click(event):
    global scvalue
    text = event.widget.cget("text")

    if text == "=":

        if scvalue.get().isdigit():
            value=int(scvalue.get())

        else:
            try:
                value = eval(display.get())
            except Exception as e:
                print(e)
                value="Error"

        scvalue.set(value)
        display.update()

    elif text == "AC":
        scvalue.set("")
        display.update()

    else:
        scvalue.set(scvalue.get() + text)
        display.update()

def equalerror():
    try:
        click

    except:
        scvalue.set("Error")
        scvalue=""



window = Tk()
window.geometry("415x550")
window.configure(bg="grey")
window.title("Calculator")


scvalue = StringVar()
scvalue.set("")

display = Entry(window,textvar=scvalue,font="lucida 30 bold",justify="right")
display.pack(fill=X, ipadx=8,pady=10,padx=10)
#display.grid(row=0, columnspan=10)


f=Frame(window, width = 412, height = 80,bg="grey")

b9=Button(f, text="9" ,padx=14,pady=11, font="lucida 25 bold" )
b9.grid(row=1,column=0,padx=9,pady=6)
b9.bind("<Button-1>",click)

b8=Button(f, text="8" ,padx=14,pady=11, font="lucida 25 bold" )
b8.grid(row=1,column=1,padx=9,pady=6)
b8.bind("<Button-1>",click)

b7=Button(f, text="7" ,padx=14,pady=11, font="lucida 25 bold" )
b7.grid(row=1,column=2,padx=9,pady=6)
b7.bind("<Button-1>",click)
f.pack()

b6=Button(f, text="6" ,padx=14,pady=11, font="lucida 25 bold" )
b6.grid(row=2,column=0,padx=9,pady=6)
b6.bind("<Button-1>",click)

b5=Button(f, text="5" ,padx=14,pady=11, font="lucida 25 bold" )
b5.grid(row=2,column=1,padx=9,pady=6)
b5.bind("<Button-1>",click)

b4=Button(f, text="4" ,padx=14,pady=11, font="lucida 25 bold" )
b4.grid(row=2,column=2,padx=9,pady=6)
b4.bind("<Button-1>",click)
f.pack()

b3=Button(f, text="3" ,padx=14,pady=11, font="lucida 25 bold" )
b3.grid(row=3,column=0,padx=9,pady=6)
b3.bind("<Button-1>",click)

b2=Button(f, text="2" ,padx=14,pady=11, font="lucida 25 bold" )
b2.grid(row=3,column=1,padx=9,pady=6)
b2.bind("<Button-1>",click)

b1=Button(f, text="1" ,padx=14,pady=11, font="lucida 25 bold" )
b1.grid(row=3,column=2,padx=9,pady=6)
b1.bind("<Button-1>",click)
f.pack()

b=Button(f, text="AC" ,padx=16,pady=11,height = 1,bg="#ae393d",width = 1,font="lucida 20 bold" )
b.grid(row=0,column=3,padx=9,pady=6)
b.bind("<Button-1>",click)
scvalue.set("")

b=Button(f, text="/" ,padx=14,pady=11,height = 1,width = 1, font="lucida 25 bold" )
b.grid(row=1,column=3,padx=9,pady=6)
b.bind("<Button-1>",click)

b=Button(f, text="*" ,padx=14,pady=11,height = 1,width = 1, font="lucida 25 bold" )
b.grid(row=2,column=3,padx=9,pady=6)
b.bind("<Button-1>",click)

b=Button(f, text="-" ,padx=14,pady=11,height = 1,width = 1, font="lucida 25 bold" )
b.grid(row=3,column=3,padx=9,pady=6)
b.bind("<Button-1>",click)

f.pack()

b0=Button(f, text="0" ,padx=14,pady=11, font="lucida 25 bold" )
b0.grid(row=4,column=0,padx=9,pady=6)
b0.bind("<Button-1>",click)


b=Button(f, text="." ,padx=14,pady=11,height = 1,width = 1, font="lucida 25 bold" )
b.grid(row=4,column=1,padx=9,pady=6)
b.bind("<Button-1>",click)

b=Button(f,  bg="#338dff",text="=" ,padx=14,pady=11, font="lucida 25 bold")
b.grid(row=4,column=2,padx=9,pady=6)
b.bind("<Button-1>",click)

b=Button(f, text="+" ,padx=14,pady=11,height = 1,width = 1, font="lucida 25 bold" )
b.grid(row=4,column=3,padx=9,pady=6)
b.bind("<Button-1>",click)

f.pack()


def hello():
    print("button clicked")

window.mainloop()



                     

