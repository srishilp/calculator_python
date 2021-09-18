from tkinter import *
window = Tk()
window.geometry("500x500")
window.configure(bg="grey")
window.title("Calculator")

entry = Entry()
entry.grid(row=0, columnspan=10, sticky=W + E)

button7 = Button( text="7")
button7.grid(row=1, column=0)

button8 = Button( text="8")
button8.grid(row=1, column=1)

button9 = Button( text="9")
button9.grid(row=1, column=2)


def hello():
    print("button clicked")

"""button1=Button(window,text="1",command=hello,height=5,width=5)
button1.place( x=10, y = 100)

button2=Button(window,text="2",command=hello,height=5,width=5)
button2.place( x=50, y = 100)
"""

                                             


window.mainloop()
