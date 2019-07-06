from tkinter import *
#Entry
def printkey(event):
    print('press:' + event.char)
    print('keysym: '+ event.keysym)
#
root = Tk()

entry = Entry(root)
cb_dashboard =Checkbutton(root, name='salu' ,text='D', command=lamdda: self.fr)
cb_dashboard.grid(row=0,column=0)
cb_estad =Checkbutton(root,name='pres',text='E ', command=cbclickp)
cb_estad.grid(row=1, column=0, sticky=(W + E))

def cbclickp(sender):
        if sender==cb_estad : print('estad')
        if cb_busqofer['selected'] :   sel.frlist.pack

#
entry.bind('<Key>', printkey)
#
entry.pack()
root.mainloop()