'''
    This module contains all gui classes needed
'''

import tkinter as GUI
from tkinter import messagebox


"""
    create a button with specifier collection of features
"""
class Button():
    def __init__(self,main_window,text,width,height,function,bg=None,fg=None) -> None:
        self.buttonObj = GUI.Button(main_window,text=text,command=function,
            width=width,height=height,background=bg,fg=fg)


        

"""
    create an entry (text field) with specifier collection of features
"""
class Entry():
    def __init__(self,main_window,width,font=None,bg=None, fg=None) -> None:
        self.variable = GUI.StringVar()
        self.entryObj = GUI.Entry(main_window,width=width,font=font,background=bg, 
        foreground=fg, textvariable=self.variable)
        

        
        

"""
    create a label with specifier collection of features
"""
class Label():
    def __init__(self,main_window,text,width,font=None,bg=None, fg=None) -> None:
        self.labelObj = GUI.Label(main_window,width=width,text=text,background=bg
        , foreground=fg, font=font)
        


"""
    Display an error message in small independent window 
"""
class ErrorBox():

    """
        Display an error message (split it to header and body then display)

        args:
            message(str)
            
        return: None
    """
    @staticmethod
    def display(message: str):

        if message is None:
            return

        # split the string
        splitted_msg = message.split(': ')

        # display error
        messagebox.showerror(splitted_msg[0],splitted_msg[1])

        


    
   



class App():

    # define the shape of the main window of the application
    def __init__(self) -> None:
        self.mainWindow = GUI.Tk()
        # customize the main window
        self.mainWindow.title("Function Plotter")
        self.mainWindow.geometry("400x180+400+300")
        self.mainWindow.resizable(False,False)

        photo = GUI.PhotoImage(file="./icon/plotter.PNG")
        self.mainWindow.iconphoto(False, photo)

        self.mainWindow.configure(background="grey")
        
  

    def run(self):
        self.mainWindow.mainloop()
    

    def exit(self):
        self.mainWindow.destroy()