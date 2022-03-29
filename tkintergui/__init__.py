from ctypes import alignment
import tkinter
from typing import Callable 
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

from tkinter import CENTER, messagebox as msg
from turtle import color 
import platform
win = tkinter.Tk()
canvas = tkinter.Canvas(win,width=userconfig["SCREENSIZE"][0],height=userconfig["SCREENSIZE"][1])
screenDimensions = [win.winfo_screenwidth(),win.winfo_screenheight()]
canvasDimensions = []
def applyConfig():
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

    win.title = userconfig["TITLE"]

    if(userconfig["FULLSCREEN"] == True):
        win.attributes("-fullscreen",True)
        canvasDimensions = screenDimensions

    if(userconfig["BORDERLESS"] == True):
        win.overrideredirect(True)

    win.resizable(userconfig["RESIZABLE_X"],userconfig["RESIZABLE_Y"])
    
    canvas.config(width=canvasDimensions[0],height=canvasDimensions[1],bg=("#" + userconfig["BGCOLOR"]))

    print(canvasDimensions)

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


def placeholder(element):
    pass

class Box:
    def render(self):
        """
        Confirm visual adaptations and render the element onto the screen
        """
        posx = self.__pos[0][0] + (self.__pos[0][1] / 100) * canvasDimensions[0]
        posy = self.__pos[1][0] + (self.__pos[1][1] / 100) * canvasDimensions[1]
        width = self.__size[0][0] + (self.__size[0][1] / 100) * canvasDimensions[0]
        height = self.__size[1][0] + (self.__size[1][1] / 100) * canvasDimensions[1]
        canvas.coords(self.__box,0,0,width,height)
        canvas.move(self.__box,posx,posy) 
        canvas.moveto(self.__label,posx + (width / 2),posy + (height/2) - self.__fontsize / 2) #WHY U USE TWO DIFFERENT METHODS??? ?????? ???????? 
        canvas.itemconfigure(self.__box,fill=("#" + self.__color),state=(hideref[self.__hidden]))
        canvas.itemconfigure(self.__label,text=self.__content, fill=("#" + self.__fontcolor),state=(hideref[self.__hidden]))
        try:
            canvas.itemconfigure(self.__label,font=(self.__fontfamily,self.__fontsize))
        except: # tkinter HATES invalid font names... AND SPACES IN SAID NAMES.
            canvas.itemconfigure(self.__label,font=("Georgia",self.__fontsize))
        canvas.pack()

    def __init__(self) -> None:
        self.__box = canvas.create_rectangle(0,0,0,0)
        self.__fontsize = 16
        self.__fontfamily = "Segoe"
        self.__fontcolor = "000000"
        self.__label = canvas.create_text(200,200,justify="center",fill=("#" + self.__fontcolor),font=(self.__fontfamily,self.__fontsize), )
        self.__pos = [[0,0],[0,0]] # X: pixel,perc Y: pixel,perc
        self.__size = [[0,0],[0,0]]
        self.__color = "FF0000"
        self.__content = ""
        self.__hidden = False
        self.__onclickfunc = placeholder

    def size(self,x: int, xpercent: int,y: int,ypercent: int):
        """
        Change the size of the element by the following arguments:
        X size in pixels
        X size in percentage of the window size (0 to 100)
        Y size in pixels
        Y size in percentage of the window size (0 to 100)
        """
        if not all(isinstance(i, int) for i in [x, xpercent, y, ypercent]) or not all(i > -1 for i in [x, xpercent, y, ypercent]):
            raise TypeError("All arguments must be a positive integer for size")
        self.__size = [[x,xpercent],[y,ypercent]]

    def pos(self,x: int, xpercent: int,y: int,ypercent: int):
        """
        Change the position of the element by the following arguments:
        X position in pixels
        X position in percentage of the window size (0 to 100)
        Y position in pixels
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
        Append a function to the element which it will perform whenever it was clicked. Always include exactly 1 argument in your function, as the module will always return the object that was clicked to the onclick function. Enter a False boolean to disable
        """
        if(fun == False):
            self.__onclickfunc = placeholder
            return
        if (not callable(fun)):
            raise TypeError("Argument must be a function for onclick or False to disable")
        self.__onclickfunc = fun
            
def finish():
    win.mainloop()

def click(data):
    print(data.x,data.y)

win.bind("<Button-1>",click)

canvas.pack()