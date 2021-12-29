from GUI import *
from ErrorHandling import *
from plot import *
from parse import *



class Actions():
    """
        perform all operations (get data, parse it, check errors, plot)
    """
    @staticmethod
    def plot():

        # get data
        str_function = function.variable.get()
        min_value = minX.variable.get()
        max_value = maxX.variable.get()

        # edit data 
        edited_function = Parse(str_function).parse()
        print(f"edited function:{edited_function}")
        
        # pass data to error handling
        error_object = ErrorHandling(edited_function)
        error_object.checkXvalues(min_value, max_value)
        
        print(f"detedcted errors: {error_object.detected_errors}")

        # check reported errors
        error = error_object.retrieveError()
        if error != None:
            ErrorBox.display(error)
        else:
            # plot data
            plot_object = Plot(edited_function)
            plot_object.plotFunction(int(min_value), int(max_value))
    
    """
        exit the all open windows and terminate the program
    """
    @staticmethod
    def exit():
        plt.close() # close matplotlib windows
        app.exit()  # close app window




app = App()

#----------------- Design of the GUI

label_info = Label(app.mainWindow,"Plot Polynomial Functions",27,'Helvetica 18 bold',"grey","blue")#1
label_info.labelObj.place(x=0,y=0)


label_function = Label(app.mainWindow,"The Function",10,"Arial","grey", "black")#1
label_function.labelObj.place(x=0,y=0+40)
label_minValue = Label(app.mainWindow,"Min Value of X",11,"Arial","grey", "black")#3
label_minValue.labelObj.place(x=0,y=30+40)
label_maxValue = Label(app.mainWindow,"Max Value of X",11,"Arial","grey","black")#5
label_maxValue.labelObj.place(x=238,y=30+40)



function = Entry(app.mainWindow,32,"Arial","white","black")#2
function.entryObj.place(x=100, y=1+40)
minX = Entry(app.mainWindow,4,"Arial","white","black")#4
minX.entryObj.place(x=110,y=30+40)
maxX = Entry(app.mainWindow,4,"Arial","white","black")#6
maxX.entryObj.place(x=352,y=30+40)



plot = Button(app.mainWindow,"Plot",56,1,Actions.plot,"black","green")
plot.buttonObj.place(x=0,y=70+40)
exit = Button(app.mainWindow,"Exit",56,1,Actions.exit,"black","red")
exit.buttonObj.place(x=0,y=95+40)


app.run()