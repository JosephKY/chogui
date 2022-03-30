import tkintergui as gui
gui.resizable(True,True)

e = gui.Box()

def re(element):
    print("click")
    gui.windowsize(400,400)
    gui.applyConfig()

e.size(0,25,0,10)
e.pos(0,10,0,10)
e.onclick(re)
e.render()

b = gui.Box()

b.size(0,25,0,10)
b.pos(0,35,0,10)
b.color("00ff00")
b.render()

gui.finish()