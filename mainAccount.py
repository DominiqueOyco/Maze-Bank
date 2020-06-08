#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 21:10:44 2020

@author: rain
"""

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

from tkinter import Tk, Label, Entry, Frame, Button, PhotoImage
from PIL import ImageTk, Image

window = Tk()

#canvas=Canvas(window, width=720, height=480)
#mzebnkImg=Image.open('')
#photo=ImageTk.PhotoImage(mzebnkImg)
#label=Label(window, image=photo)
#label.pack()

#bgImage = PhotoImage(file = r"LSBank-GTAV.png")
#Label(window, image = bgImage).place(relwidth = 1, relheight = 1)

img = ImageTk.PhotoImage(Image.open("LSBank-GTAV.png"))  
l=Label(image=img)
l.pack()

window.title('Maze Bank of Los Santos')
window.geometry("720x480+10+20")
entbtn=Button(window, text="SIGN IN", fg='blue')
entbtn.place(x=330, y=290)
extbtn=Button(window, text="EXIT", fg='blue', command=window.quit)
extbtn.place(x=338, y=330)
lbl=Label(window, text="Welcome to the Maze Bank of Los Santos", 
          fg='red', font=("Avenir", 16))
lbl.place(x=210, y=50)
usrent=Entry(window, text="Access ID", fg='red', font=("Avenir", 16))
usrent.place(x=260, y=130)
passent=Entry(window, text="Password", fg='red', font=("Avenir", 16))
passent.place(x=260, y=210)
cpylbl=Label(window, text="© 2020 Maze Bank Inc. All Rights Reserved.", 
             fg='red', font=("Avenir", 10))
cpylbl.place(x=250, y=400)
window.mainloop()
