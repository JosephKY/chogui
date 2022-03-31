import chogui as gui
gui.resizable(True, True)
gui.bgcolor("000000")

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

image = gui.Image("alphatest.png")
image.pos(0,50,0,50)
image.size(0,50,0,50)
image.bordercolor("ff0000")
image.bordersize(3)
image.render()

gui.renderall()

gui.finish()