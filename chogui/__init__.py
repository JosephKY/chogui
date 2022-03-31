from ctypes import alignment
from email.mime import image
import tkinter
from typing import Callable 
from PIL import ImageTk
from PIL import Image as PImage
elements = []
userconfig = {
    "SCREENSIZE":[600,480],
    "SCREENMETHOD":[1,"Pixels","Percent"],
    "BGCOLOR":"FFFFFF",
    "FULLSCREEN":False,
    "BORDERLESS":False,
    "WINDOWS_BLOCKED":False,
    "MAC_BLOCKED":False,
    "LINUX_BLOCKED":False,
    "TITLE":"Made with ChoGUI",
    "RESIZABLE_X":False,
    "RESIZABLE_Y":False
}

hideref = {
    True:"hidden",
    False:"normal"
}

def valCol(color):
  for _,i in enumerate(color):
    our = ord(i)
    if(our < 48 or our > 102):
      return 1
      break

configd = False

from tkinter import ANCHOR, CENTER, messagebox as msg
from turtle import back, color 
import platform
win = tkinter.Tk()
canvas = tkinter.Canvas(win,width=userconfig["SCREENSIZE"][0],height=userconfig["SCREENSIZE"][1])
canvas.pack(fill="both",expand=True)

screenDimensions = [win.winfo_screenwidth(),win.winfo_screenheight()]
canvasDimensions = []
def applyConfig():
    global configd
    global canvasDimensions
    scmethod = userconfig["SCREENMETHOD"][userconfig["SCREENMETHOD"][0]]
    canvasDimensions = []
    if(scmethod == "Pixels"):
        canvasDimensions = userconfig["SCREENSIZE"]
    else:
        canvasDimensions = [ (userconfig["SCREENSIZE"][0] / 100) * screenDimensions[0] , (userconfig["SCREENSIZE"][1] / 100) * screenDimensions[1] ]
    

    sys = platform.system()
    if(sys == "Darwin"):
        sys = "MacOS" # darwin?
    if(sys == "Windows" and userconfig["WINDOWS_BLOCKED"] == True) or (sys == "MacOS" and userconfig["MAC_BLOCKED"] == True) or (sys == "Linux" and userconfig["LINUX_BLOCKED"] == True):
        msg.showerror("Operating System Not Supported","The developers have disabled usage of this application on your operating system, " + sys + ", and the program must now quit. Sorry for any inconvenience.")
        win.quit()
        win.destroy()

    win.winfo_toplevel().title(userconfig["TITLE"])

    if(userconfig["FULLSCREEN"] == True):
        win.attributes("-fullscreen",True)
        canvasDimensions = screenDimensions

    if(userconfig["BORDERLESS"] == True):
        win.overrideredirect(True)

    win.resizable(userconfig["RESIZABLE_X"],userconfig["RESIZABLE_Y"])
    
    canvas.config(width=canvasDimensions[0],height=canvasDimensions[1],bg=("#" + userconfig["BGCOLOR"]))

    configd = True

applyConfig()

def windowsize(x: int,y: int):
    """
    Define the size of the window by x and y dimensions, or percentage (0 to 100), depending on the set window size method
    """
    if not all(isinstance(i,int) for i in [x,y]) or not all(i > 0 for i in [x,y]):
        raise TypeError("Dimensions must be integers and above zero for screensize")
    userconfig["SCREENSIZE"] = [x,y]
    applyConfig()

def windowsizemethod(index: int):
    """
    Define the method which the window is resized. Available options:\n
    1 - By pixels (default)\n
    2 - By percentage 
    """
    if not isinstance(index, int):
        raise TypeError("Argument for window size method must be an integer")
    if not index in range(1,len(userconfig["SCREENMETHOD"])):
        raise Exception("Specified window size method " + str(index) + " is not in range")
    userconfig["SCREENMETHOD"][0] = index
    applyConfig()

def fullscreen(boolean: bool):
    """
    Specify whether or not fullscreen is enabled with a boolean
    """
    if not isinstance(boolean, bool):
        raise TypeError("Argument must be a boolean for fullscreen")
    userconfig["FULLSCREEN"] = boolean
    applyConfig()

def borderless(boolean: bool):
    """
    Specify whether or not the window has no border or titlebar with a boolean
    """
    if not isinstance(boolean, bool):
        raise TypeError("Argument must be a boolean for borderless")
    userconfig["BORDERLESS"] = boolean
    applyConfig()

def title(title: str):
    """
    Specify the title for the window
    """
    if not isinstance(title, str):
        raise TypeError("Argument must be a string for title")
    userconfig["TITLE"] = title
    applyConfig()

def resizable(boolx: bool,booly: bool):
    """
    Specify for x and y whether or not each is resizable for the window with a boolean
    """
    if not all(isinstance(i,int) for i in [boolx,booly]):
        raise TypeError("Arguments must be a boolean for resizable")
    userconfig["RESIZABLE_X"] = boolx
    userconfig["RESIZABLE_Y"] = booly
    applyConfig()

def blockwindows():
    userconfig["WINDOWS_BLOCKED"] = True
    applyConfig()

def blockmacos():
    userconfig["MAC_BLOCKED"] = True
    applyConfig()

def blocklinux():
    userconfig["LINUX_BLOCKED"] = True
    applyConfig()


def placeholder(data):
    pass

class Label:
    def render(self):
        """
        Confirm visual adaptations and render the element onto the screen
        """
        posx = self.__pos[0][0] + (self.__pos[0][1] / 100) * canvasDimensions[0]
        posy = self.__pos[1][0] + (self.__pos[1][1] / 100) * canvasDimensions[1]
        width = self.__size[0][0] + (self.__size[0][1] / 100) * canvasDimensions[0]
        height = self.__size[1][0] + (self.__size[1][1] / 100) * canvasDimensions[1]
        self.curpos = [posx,posy]
        self.cursize = [width,height]
        self.__borderframe.place(width=width,height=height,x=posx,y=posy)
        self.__borderframe.configure(bg="#" + self.__bordercolor)
        self.__widget.place(width=width - self.__borderwidth * 2,height=height - self.__borderwidth * 2,x=self.__borderwidth,y=self.__borderwidth)
        self.__widget.configure(
            background="#" + self.__color,
            font=(self.__fontfamily,self.__fontsize),
            text=self.__content,
            fg="#" + self.__fontcolor
        )

        if(self.__hidden == True):
            self.__borderframe.place(x=-9999,y=-9999)
            # listen, i know what youre thinking, but trust me, you would have done it too...
        
        canvas.pack()

    def __init__(self) -> None:
        self.test = "Hello World!"
        self.__size = [[0,0],[0,0]]
        self.__pos = [[0,0],[0,0]]
        self.curpos = [0,0]
        self.cursize = [0,0]
        self.__color = "FFFFFF"
        self.__content = ""
        self.__fontfamily = "Segoe"
        self.__fontcolor = "000000"
        self.__fontsize = 16
        self.__hidden = False
        self.__onclickfunc = placeholder
        self.__onhoverinfunc = placeholder 
        self.__onhoveroutfunc = placeholder
        self.__bordercolor = "000000"
        self.__borderwidth = 1
        self.__borderframe = tkinter.Frame(win,bg="#" + self.__bordercolor)
        self.__widget = tkinter.Label(
        self.__borderframe,
        bg="#" + self.__color,
        bd=0,
        font=(self.__fontfamily,self.__fontsize),
        fg="#" + self.__fontcolor,
        text=self.__content,
        width=0,
        height=0
        )
        self.__borderframe.place(x=0,y=0)
        self.data = None

        self.__widget.bind("<Button-1>",self.__perf__)
        self.__widget.bind("<Enter>",self.__perfhvin__)
        self.__widget.bind("<Leave>",self.__perfhvout__)

        elements.append(self)

    def __perf__(self, ddata):
        data = [ddata.x,ddata.y,self]
        self.__onclickfunc(data)

    def __perfhvin__(self, ddata):
        data = [ddata.x,ddata.y,self]
        self.__onhoverinfunc(data)

    def __perfhvout__(self, ddata):
        data = [ddata.x,ddata.y,self]
        self.__onhoveroutfunc(data)
        

    def size(self,x: int, xpercent: int,y: int,ypercent: int):
        """
        Change the size of the element by the following arguments:\n
        X size in pixels\n
        X size in percentage of the window size (0 to 100)\n
        Y size in pixels\n
        Y size in percentage of the window size (0 to 100)
        """
        if not all(isinstance(i, int) for i in [x, xpercent, y, ypercent]) or not all(i > -1 for i in [x, xpercent, y, ypercent]):
            raise TypeError("All arguments must be a positive integer for size")
        self.__size = [[x,xpercent],[y,ypercent]]

    def pos(self,x: int, xpercent: int,y: int,ypercent: int):
        """
        Change the position of the element by the following arguments:\n
        X position in pixels\n
        X position in percentage of the window size (0 to 100)\n
        Y position in pixels\n
        Y position in percentage of the window size (0 to 100)
        """
        if not all(isinstance(i, int) for i in [x, xpercent, y, ypercent]) or not all(i > -1 for i in [x, xpercent, y, ypercent]):
            raise TypeError("All arguments must be a positive integer for pos")
        self.__pos = [[x,xpercent],[y,ypercent]]

    def content(self,content: str):
        """
        Change the text content the element will render at its center
        """
        if not(isinstance(content, str)):
            raise TypeError("Argument must be a string for content")
        self.__content = content

    def color(self,color: str):
        """
        Change the color of the element by a hexadecimal color code
        """
        if(not(isinstance(color,str))):
            raise TypeError("Argument must be a string for color")
        if(valCol(color.lower()) != 1):
            self.__color = color
        else:
            raise Exception("Invalid color argument '" + color + "', color must be a hexadecimal color code")

    def bordercolor(self,color: str):
        """
        Change the color of the element's surrounding border by a hexadecimal color code
        """
        if(not(isinstance(color,str))):
            raise TypeError("Argument must be a string for bordercolor")
        if(valCol(color.lower()) != 1):
            self.__bordercolor = color
        else:
            raise Exception("Invalid color argument '" + color + "', color must be a hexadecimal color code")

    def bordersize(self,size: int):
        """
        Change the thickness of the element's surrounding border in pixels
        """
        if not(isinstance(size, int)):
            raise TypeError("Argument must be an integer for bordersize")
        if not size > 0:
            raise Exception("bordersize needs to be greater than zero")
        self.__borderwidth = size

    def fontsize(self,size: int):
        """
        Change the font size of the element's text content
        """
        if not(isinstance(size, int)):
            raise TypeError("Argument must be an integer for fontsize")
        if not size > 0:
            raise Exception("fontsize needs to be greater than zero")
        self.__fontsize = size

    def fontfamily(self,family: str):
        """
        Change the font family the element's text content will render in
        """
        if not(isinstance(family, str)):
            raise TypeError("Argument must be a string for fontfamily")
        if len(family.split(" ")) != 1:
            raise Exception("Do not include spaces in the font family name, merge words together instead")
        self.__fontfamily = family

    def fontcolor(self,color: str):
        """
        Change the color of the element's rendered text content
        """
        if(not(isinstance(color,str))):
            raise TypeError("Argument must be a string for fontcolor")
        if(valCol(color.lower()) != 1):
            self.__fontcolor = color
        else:
            raise Exception("Invalid fontcolor argument '" + color + "', color must be a hexadecimal color code")

    def hidden(self,boolean: bool):
        """
        Toggle whether or not the element and it's text is hidden. Hiding also disables the onclick function
        """
        if not isinstance(boolean,bool):
            raise TypeError("Argument must be a boolean (True/False) for hidden")
        self.__hidden = boolean

    def onclick(self,fun):
        """
        Append a function to the element which it will perform whenever it was clicked. Always include exactly 1 argument in your function, as the module will always return data about the click event. Enter a False boolean to disable
        """
        if(fun == False):
            self.__onclickfunc = placeholder
            return
        if(fun == True):
            self.__onclickfunc(self)
            return
        if (not callable(fun)):
            raise TypeError("Argument must be a function for onclick or False to disable")
        else:
            self.__onclickfunc = fun

    def onhoverin(self,fun):
        """
        Append a function to the element which it will perform whenever the mouse cursor hovers into it. Always include exactly 1 argument in your function, as the module will always return data about the click event. Enter a False boolean to disable
        """
        if(fun == False):
            self.__onhoverinfunc = placeholder
            return
        if(fun == True):
            self.__onhoverinfunc(self)
            return
        if (not callable(fun)):
            raise TypeError("Argument must be a function for onclick or False to disable")
        else:
            self.__onhoverinfunc = fun

    def onhoverout(self,fun):
        """
        Append a function to the element which it will perform whenever the mouse cursor hovers out of it after hovering into it (onhoverin function is not required). Always include exactly 1 argument in your function, as the module will always return data about the click event. Enter a False boolean to disable
        """
        if(fun == False):
            self.__onhoveroutfunc = placeholder
            return
        if(fun == True):
            self.__onhoveroutfunc(self)
            return
        if (not callable(fun)):
            raise TypeError("Argument must be a function for onclick or False to disable")
        else:
            self.__onhoveroutfunc = fun

    def getpos(self):
        return self.__pos

    def getsize(self):
        return self.__size

class Image:
    def render(self):
        """
        Confirm visual adaptations and render the element onto the screen
        """
        posx = self.__pos[0][0] + (self.__pos[0][1] / 100) * canvasDimensions[0]
        posy = self.__pos[1][0] + (self.__pos[1][1] / 100) * canvasDimensions[1]
        width = self.__size[0][0] + (self.__size[0][1] / 100) * canvasDimensions[0]
        height = self.__size[1][0] + (self.__size[1][1] / 100) * canvasDimensions[1]
        self.curpos = [posx,posy]
        self.cursize = [width,height]
        self.__borderframe.place(width=width,height=height,x=posx,y=posy)
        self.__borderframe.configure(bg="#" + self.__bordercolor)
        self.__load = (PImage.open(self.__filename).convert('RGB')).resize((int(width - self.__borderwidth * 2),int(height - self.__borderwidth * 2)),PImage.BICUBIC)
        self.__render = ImageTk.PhotoImage(self.__load)
        self.__widget.configure(image=self.__render)
        self.__widget.image = self.__render

        if(self.__hidden == True):
            self.__borderframe.place(x=-9999,y=-9999)
            # listen, i know what youre thinking, but trust me, you would have done it too...
        
        canvas.pack()

    def __init__(self, file) -> None:
        self.test = "Hello World!"
        self.__filename = file
        self.__size = [[0,0],[0,0]]
        self.__pos = [[0,0],[0,0]]
        self.curpos = [0,0]
        self.cursize = [0,0]
        self.__hidden = False
        self.__onclickfunc = placeholder
        self.__onhoverinfunc = placeholder 
        self.__onhoveroutfunc = placeholder
        self.__bordercolor = "000000"
        self.__borderwidth = 1
        self.__borderframe = tkinter.Frame(win,bg="#" + self.__bordercolor)
        self.__load = PImage.open(file)
        self.__render = ImageTk.PhotoImage(self.__load)
        self.__widget = tkinter.Label(self.__borderframe,image=self.__render,borderwidth=0)
        self.__widget.image = self.__render
        self.__widget.pack(expand=True)
        self.__borderframe.place(x=0,y=0)
        self.data = None

        self.__widget.bind("<Button-1>",self.__perf__)
        self.__widget.bind("<Enter>",self.__perfhvin__)
        self.__widget.bind("<Leave>",self.__perfhvout__)

        elements.append(self)

    def __perf__(self, ddata):
        data = [ddata.x,ddata.y,self]
        self.__onclickfunc(data)

    def __perfhvin__(self, ddata):
        data = [ddata.x,ddata.y,self]
        self.__onhoverinfunc(data)

    def __perfhvout__(self, ddata):
        data = [ddata.x,ddata.y,self]
        self.__onhoveroutfunc(data)
        

    def size(self,x: int, xpercent: int,y: int,ypercent: int):
        """
        Change the size of the element by the following arguments:\n
        X size in pixels\n
        X size in percentage of the window size (0 to 100)\n
        Y size in pixels\n
        Y size in percentage of the window size (0 to 100)
        """
        if not all(isinstance(i, int) for i in [x, xpercent, y, ypercent]) or not all(i > -1 for i in [x, xpercent, y, ypercent]):
            raise TypeError("All arguments must be a positive integer for size")
        self.__size = [[x,xpercent],[y,ypercent]]

    def pos(self,x: int, xpercent: int,y: int,ypercent: int):
        """
        Change the position of the element by the following arguments:\n
        X position in pixels\n
        X position in percentage of the window size (0 to 100)\n
        Y position in pixels\n
        Y position in percentage of the window size (0 to 100)
        """
        if not all(isinstance(i, int) for i in [x, xpercent, y, ypercent]) or not all(i > -1 for i in [x, xpercent, y, ypercent]):
            raise TypeError("All arguments must be a positive integer for pos")
        self.__pos = [[x,xpercent],[y,ypercent]]

    def bordercolor(self,color: str):
        """
        Change the color of the element's surrounding border by a hexadecimal color code
        """
        if(not(isinstance(color,str))):
            raise TypeError("Argument must be a string for bordercolor")
        if(valCol(color.lower()) != 1):
            self.__bordercolor = color
        else:
            raise Exception("Invalid color argument '" + color + "', color must be a hexadecimal color code")

    def bordersize(self,size: int):
        """
        Change the thickness of the element's surrounding border in pixels
        """
        if not(isinstance(size, int)):
            raise TypeError("Argument must be an integer for bordersize")
        if not size > 0:
            raise Exception("bordersize needs to be greater than zero")
        self.__borderwidth = size

    def hidden(self,boolean: bool):
        """
        Toggle whether or not the element and it's text is hidden. Hiding also disables the onclick function
        """
        if not isinstance(boolean,bool):
            raise TypeError("Argument must be a boolean (True/False) for hidden")
        self.__hidden = boolean

    def onclick(self,fun):
        """
        Append a function to the element which it will perform whenever it was clicked. Always include exactly 1 argument in your function, as the module will always return data about the click event. Enter a False boolean to disable
        """
        if(fun == False):
            self.__onclickfunc = placeholder
            return
        if(fun == True):
            self.__onclickfunc(self)
            return
        if (not callable(fun)):
            raise TypeError("Argument must be a function for onclick or False to disable")
        else:
            self.__onclickfunc = fun

    def onhoverin(self,fun):
        """
        Append a function to the element which it will perform whenever the mouse cursor hovers into it. Always include exactly 1 argument in your function, as the module will always return data about the click event. Enter a False boolean to disable
        """
        if(fun == False):
            self.__onhoverinfunc = placeholder
            return
        if(fun == True):
            self.__onhoverinfunc(self)
            return
        if (not callable(fun)):
            raise TypeError("Argument must be a function for onclick or False to disable")
        else:
            self.__onhoverinfunc = fun

    def onhoverout(self,fun):
        """
        Append a function to the element which it will perform whenever the mouse cursor hovers out of it after hovering into it (onhoverin function is not required). Always include exactly 1 argument in your function, as the module will always return data about the click event. Enter a False boolean to disable
        """
        if(fun == False):
            self.__onhoveroutfunc = placeholder
            return
        if(fun == True):
            self.__onhoveroutfunc(self)
            return
        if (not callable(fun)):
            raise TypeError("Argument must be a function for onclick or False to disable")
        else:
            self.__onhoveroutfunc = fun

    def getpos(self):
        return self.__pos

    def getsize(self):
        return self.__size


            
def finish():
    """
    Always call this function at the very end of your application to prevent it from closing
    """
    win.mainloop()

def __adjust__(data):
    #if configd == True:
    global canvasDimensions
    canvasDimensions = [win.winfo_width(),win.winfo_height()]
    #    canvas.configure(width=win.winfo_width() - 6,height=win.winfo_height() - 6,bg=("#" + userconfig["BGCOLOR"]))
    for _,obj in enumerate(elements):
        obj.render()

def masterclick(data):
    print(data)

def renderall():
    canvas.pack()

win.bind("<Configure>",__adjust__)

canvas.pack()