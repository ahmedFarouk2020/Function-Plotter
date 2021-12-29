'''
    plot user functions
'''

import matplotlib.pyplot as plt

"""
    This class is used to plot the function the user enters
"""

class Plot():

    def __init__(self, function: str) -> None:
        
        self.__function = function

        # extract the original function in case of using `^`
        # EX: 
        #   (X^2) --parser--> (X**2) --plot--> (X^2) --> Display
        self.__originalFunction = self.__function.replace("**","^")

    
    """
        plot the function with defined range

        args:
            min_value(str)
            max_value(str)

        return: None
    """
    def plotFunction(self, min_value: str, max_value: str):
        X = [i for i in range(int(min_value),int(max_value)+1,1)]
        y = [eval(self.__function) for x in range(int(min_value),int(max_value)+1,1)]

        plt.plot(X,y)
        plt.title(f"The Function: {self.__originalFunction}")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.show()



        


#========= Debugging ================
# p = Plot("x+x**2")

# p.plotFunction(0, 10)

# close()