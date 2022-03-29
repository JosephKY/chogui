from ctypes import alignment
import tkinter 
userconfig = {
    "SCREENSIZE":[60,60],
    "SCREENMETHOD":[2,"Pixels","Percent"],
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

applyConfig()

def placeholder(element):
    pass

class Box:
    def render(self):
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
        if not all(isinstance(i, int) for i in [x, xpercent, y, ypercent]) or not all(i > -1 for i in [x, xpercent, y, ypercent]):
            raise TypeError("All arguments must be a positive integer")

def finish():
    win.mainloop()

canvas.pack()