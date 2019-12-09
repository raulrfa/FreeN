from tkinter import *

screen_width=1920
screen_height=1080
value=4

root = Tk()

common_product_frame = Frame(root, width=1000, height=800,highlightbackground='grey', highlightcolor='grey', highlightthickness=5)
common_product_frame.pack()
common_product_frame.propagate(0)    

def btnclick():
    text2_button.pack_forget()


text1_button = Button(common_product_frame, width=15, height=value, text="Text1", font="Tahoma 14 bold",command=btnclick)
text1_button.pack(side=TOP)
text2_button = Button(common_product_frame, width=15, height=value, text="Text2", font="Tahoma 14 bold")
text2_button.pack(side=TOP,fill=X)




root.mainloop()