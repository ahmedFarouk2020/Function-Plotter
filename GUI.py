'''
    This module contains all gui classes needed
'''

import tkinter as GUI
from tkinter import messagebox


class Button():
    def __init__(self,main_window,text,width,height,function,bg,fg) -> None:
        self.buttonObj = GUI.Button(main_window,text=text,command=function,
            width=width,height=height,background=bg,fg=fg)
        # self.buttonObj = GUI.Button(main_window,text="text",command=function,
        # activebackground=activebackground,background=background,font=font,
        # textvariable=self.variable, width=width, height=height)

        

class Entry():
    def __init__(self,main_window,width,font,background, foreground) -> None:
        self.variable = GUI.StringVar()
        self.entryObj = GUI.Entry(main_window,width=width,font=font,background=background, 
        foreground=foreground, textvariable=self.variable)
        print(self.entryObj.configure()['font'])

        
        


class Label():
    def __init__(self,main_window,text,width,background,font, foreground) -> None:
        self.labelObj = GUI.Label(main_window,width=width,text=text,background=background
        , foreground=foreground, font=font)
        



class ErrorBox():

    @staticmethod
    def display(message: str):
        if message is None:
            return
        # split the string
        splitted_msg = message.split(': ')
        # display error
        messagebox.showerror(splitted_msg[0],splitted_msg[1])
        print(splitted_msg[0],splitted_msg[1])
        


    
   



class App():
    def __init__(self) -> None:
        self.mainWindow = GUI.Tk()
        # customize the main window
        self.mainWindow.title("Function Plotter")
        self.mainWindow.geometry("400x180+400+300")
        self.mainWindow.resizable(False,False)
        self.mainWindow.configure(background="grey")
        self.mainWindow.configure()['cursor']='Cursor'
  
    def run(self):
        self.mainWindow.mainloop()
    
    def exit(self):
        self.mainWindow.destroy()


