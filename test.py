import tkintergui as gui
gui.blocklinux()
gui.resizable(False,True)
gui.title("Testing!")
gui.windowsizemethod(2)
gui.windowsize(50,50)
gui.fullscreen(False)
gui.borderless(False)

def test(element):
    print("Hello World!")
    print(element)

element = gui.Box()
element.size(0,25,0,10)
element.pos(0,0,0,0)
element.color("000000")
element.fontfamily("segoe")
element.fontsize(25)
element.fontcolor("ffffff")
element.content("Hello World!")
element.hidden(False)
element.onclick(test)
element.render()

gui.finish()