from tkinter import *

def onKeyDown(e):
    # The obvious information
    c = e.keysym
    s = e.state

    # Manual way to get the modifiers
    ctrl  = (s & 0x4) != 0
    alt   = (s & 0x8) != 0 or (s & 0x80) != 0
    shift = (s & 0x1) != 0

    # Merge it into an output
    # if alt:
    #     c = 'alt+' + c
    if shift:
        c = 'shift+' + c
    if ctrl:
        c = 'ctrl+' + c
    print(c)

# Run the tk window
root = Tk()
root.bind('<Alt-Control-KeyPress>', onKeyDown)
root.bind('<Alt-Shift-KeyPress>', onKeyDown)
root.mainloop()