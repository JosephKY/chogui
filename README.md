# ChoGUI
ChoGUI is a Python GUI builder based on Tkinter.

## Getting Started

To get started, save the 'tkintergui' folder anywhere on your computer and import it properly

```
project
│   test.py  
│
└───tkintergui
    | ...
```

```py
# test.py
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
gui.renderall()

gui.finish()
```

## The 'finish' method

You must use the 'finish' method at the end of your code or your program will exit on its own

```py
import chogui as cgui

cgui.finish() # Very important!
```

## Default methods

**windowsize(*int*,*int*)**

Set the size of the window. The first argument is the width, the second argument is the height. It will either size in pixels or percentage of monitor size based on the option set for ``windowsizemethod()`` (by default it is pixels)

```py
chogui.windowsize(800,600)
```

**windowsizemethod(*int*)**

Define the method the window will resize. There are currently two options:
1. By pixels
2. By monitor percentage

```py
chogui.windowsizemethod(2)
chogui.windowsize(50,50)
```

**fullscreen(*bool*)**

Toggle fullscreen on or off. Fullscreen being enabled will overrule the window size and be automatically set to the max monitor size.

```py
chogui.fullscreen(True)
```

**borderless(*bool*)**

Toggle borderless mode on or off. If borderless mode is turned on, the window will have no border or title bar.

```py
chogui.borderless(True)
```

**title(*str*)**

Set the text displayed in the window's titlebar

```py
chogui.title("Made with ChoGUI")
```
**resizable(*bool*,*bool*)**

Set whether or not the window can be resized in the X or Y direction

```py
chogui.resizable(False, True) # Window can't be resized left or right, but can be resized up and down
```

**blockwindows()**, **blockmacos()**, **blocklinux()**

Block usage of your program in that respective operating system

```py
chogui.blocklinux() # Linux users will be forced to quit your program when they open it
```

## Classes

### 'Label'

A label is a widget that can contain text and has a color and border. It can be positioned anywhere on the screen and given any size, either based on pixels or percentage of window size. All labels start at the top-left of the screen and expand in the opposite directon when its size is changed.

```py
import chogui as cgui

label = cgui.Label()
```
**Methods**

**pos(*int*,*int*,*int*,*int*)**

Set the position of the label on the canvas.
The first argument is for the x location in pixels
The second argument is for the x location in percentage
The third argument is for the y location in pixels
The fourth argument is for the y location in percentage

```py
label.pos(100,7,300,20) # 100 pixels and 7% across the screen, 300 pixels and 20% down the screen
```

**size(*int*,*int*,*int*,*int*)**

Set the size of the element.
The first argument is for the width in pixels
The second argument is for the width in percentage
The third argument is for the height in pixels
The fourth argument is for the height in percentage

```py
label.pos(100,7,300,20) # 100 pixels and 7% in width, 300 pixels and 20% in height
```

**color(*(Hexadecimal Color Code)*)**

Set the color of the label with a hexadecimal color code

```py
label.color('FF00CC')
```

**content(*str*)**

Set the text the label contains. Text always appear at the center of a label

```py
label.content("Hello World!")
```

**bordercolor(*(Hexadecimal Color Code)*)**

Set the color of the label's border with a hexadecimal color code

```py
label.bordercolor('0000FF')
```

**bordersize(*int*)**

Set the thickness of the label's border in pixels

```py
label.bordersize(3)
```

**fontsize(*int*)**

Set the size of the label's text with an integer

```py
label.fontsize(21)
```

**fontfamily(*str*)**

Set the font family the label's text will be displayed in by the font family's name
*Do not include spaces!* If there are multiple words in the fony family's name, merge the words together.

```py
label.fontfamily("ComicSansMS")
```

**fontcolor(*(Hexadecimal Color Code)*)**

Set the color of the label's text with a hexadecimal color code

```py
label.fontcolor('FFFF00')
```

**hidden(*bool*)**

Toggle whether or not the label is hidden. Hidden labels cannot be interacted with in any way (hovering, clicking, etc), nor can they be seen at all

```py
label.hidden(False)
```

**onclick(*func*)**

Append a function to the label which it will perform when it is clicked

```py
def test(data):
    print(data, "Hello World!")

label.onclick(test)
```

**onhoverin(*func*)**

Append a function to the label when the mouse cursor hovers into it

```py
def test(data):
    print(data, "Hello, mouse cursor")

label.onhoverin(test)
```

**onhoverout(*func*)**

Append a function to the label when the mouse cursor hovers away from it, after hovering in

```py
def test(data):
    print(data, "Goodbye, mouse cursor")

label.onhoverout(test)
```



