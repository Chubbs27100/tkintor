from tkinter import*
root = Tk()
root.geometry("400x500")
w = Label(root,text="chocos and icecream",font=62,bg="cyan")
w.pack()
#creating 2 frames

#frist frame:
frame1=Frame(root)
frame1.pack(pady=20)
#adding 3 buttons in frame 1
b1 = Button(frame1,text="chocolate",fg="orange",bg="yellow")
b1.pack(side = RIGHT)
b2 = Button(frame1,text="crunchynut",fg="white",bg="black")
b2.pack(side = LEFT)
b3 = Button(frame1,text="white chocolate",fg="red",bg="blue")
b3.pack(side = LEFT)

#second frame
frame2=Frame(root)
frame2.pack(side = BOTTOM)
#adding 3 buttons in frame 2
b4 = Button(frame2,text="ice cream",fg="red",bg="blue")
b4.pack(side = BOTTOM)
b5 = Button(frame2,text="magnus",fg="green",bg="yellow")
b5.pack(side = BOTTOM)
b6 = Button(frame2,text="cone",fg="purple",bg="pink")
b6.pack(side = BOTTOM)

mainloop()
