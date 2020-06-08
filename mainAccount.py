#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 21:10:44 2020

@author: rain
"""
import tkinter as tk
#from PIL import ImageTk, Image

window = tk.Tk()

class newUser():
    print("punk'd")
    
class balance():
#    TODO: Implement this function
    print("punk'd")
    
class deposit():
#    TODO: Implement this function
    print("punk'd")
    
class withdraw():
#    TODO: Implement this function
    print("punk'd")
    
class checking():
#    TODO: Implement this function
    print("punk'd")
    
class savings():
#    TODO: Implement this function
    print("punk'd")

class mainGUI():
    window.title('Maze Bank of Los Santos')
    
    canvas = tk.Canvas(window, height=60, width=720)
    canvas.pack()
    
    #img = ImageTk.PhotoImage(Image.open("LSBank-GTAV.png"))  
    #l=tk.Label(image=img)
    #l.pack()
    
    path = "maze-bank-logo.png"
    logo_width = 320
    logo_height = 320
    
    ##Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
    #img = ImageTk.PhotoImage(Image.open(path))
    #
    #scale_w = 320/40
    #scale_h = 320/40
    #img._PhotoImage__photo.zoom(scale_w, scale_h)
    #
    ##The Label widget is a standard Tkinter widget used to display a text or image on the screen.
    #panel = tk.Label(window, image = img)
    #
    ##The Pack geometry manager packs widgets in rows or columns.
    #panel.pack(side = "bottom", fill = "both", expand = "yes")
    
    # Gets the requested values of the height and widht.
    windowWidth = window.winfo_reqwidth()
    windowHeight = window.winfo_reqheight()
    
    # Gets both half the screen width/height and window width/height
    positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(window.winfo_screenheight()/2 - windowHeight/2)
    
    #window.geometry("720x480+10+20")
    window.geometry("720x480+{}+{}".format(positionRight, positionDown))
    window.resizable(0,0)
    
    #When user clicks the buttons
    entbtn=tk.Button(window, text="SIGN IN", fg='blue', font=("Avenir", 16))
    entbtn.place(x=328, y=290)
    entbtn=tk.Button(window, text="CREATE NEW ACCOUNT", fg='blue', 
                     font=("Avenir", 16))
    entbtn.place(x=268, y=330)
    extbtn=tk.Button(window, text="EXIT", fg='blue', font=("Avenir", 16), 
                     command=window.quit)
    extbtn.place(x=338, y=370)
    lbl=tk.Label(window, text="Welcome to the Maze Bank of Los Santos", 
              fg='red', font=("Avenir", 24))
    lbl.place(x=140, y=50)
    
    #Input validation
    usrent=tk.Entry(window, text="Access ID", fg='red', font=("Avenir", 16))
    usrent.place(x=260, y=130)
    passent=tk.Entry(window, text="Password", fg='red', font=("Avenir", 16))
    passent.place(x=260, y=210)
    
    
    cpylbl=tk.Label(window, text="© 2020 Maze Bank Inc. All Rights Reserved.", 
                 fg='red', font=("Avenir", 10))
    cpylbl.place(x=250, y=420)
    window.mainloop()
    
mainGUI()






















#import tkinter as tk
#
#class App(tk.Frame):
#    def __init__(self, master):
#        tk.Frame.__init__(self, master)
#        self.pack()
#        self.master.title("Hello World")
#        
#        tk.Label(self, text="This is your first GUI.(Duck)").pack()
#        
#if __name__ == '__main__' :
#    root = tk.Tk()
#    app = App(root)
#    app.mainLoop

#from tkinter import Tk, Label, Entry, Canvas, Button, PhotoImage
#from PIL import ImageTk, Image
