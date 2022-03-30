import tkintergui as gui
gui.resizable(True,True)

e = gui.Box()

def re(element):
    gui.windowsize(1000,90)
    gui.windowsizemethod(1)

e.size(0,25,0,10)
e.__borderwidth = 0
e.pos(0,10,0,10)
e.onclick(re)
e.content("Hello World!")
e.fontsize(10)
e.render()

b = gui.Box()

b.size(0,25,0,10)
b.pos(0,35,0,10)
b.color("00ff00")
b.render()

gui.finish()