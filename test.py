import chogui as gui
gui.resizable(True, True)

def testClickFunc(data):
    print("Hello world!")

def testHoveringIn(data):
    print("Hi, mouse cursor")

def testHoveringOut(data):
    print("Bye, cursor")

label = gui.Label()
label.size(0,40,0,15)
label.pos(0,10,0,10)
label.fontfamily("Georgia")
label.fontsize(22)
label.bordersize(4)
label.bordercolor("0000ff")
label.content("Hello World!")
label.onclick(testClickFunc)
label.onhoverin(testHoveringIn)
label.onhoverout(testHoveringOut)
label.hidden(False)

image = gui.Image("testimage.gif")


gui.renderall()

gui.finish()