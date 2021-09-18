from tkinter import *
window = Tk()
window.geometry("500x500")
window.configure(bg="grey")
window.title("Calculator")

entry = Entry()
entry.grid(row=0, columnspan=10, sticky=W + E)

button1 = Button( text="1")
button1.grid(row=1, column=0)

button2 = Button( text="2")
button2.grid(row=1, column=1)

button3 = Button( text="3")
button3.grid(row=1, column=2)

def hello():
    print("button clicked")

"""button1=Button(window,text="1",command=hello,height=5,width=5)
button1.place( x=10, y = 100)

button2=Button(window,text="2",command=hello,height=5,width=5)
button2.place( x=50, y = 100)
"""

                                             


window.mainloop()
