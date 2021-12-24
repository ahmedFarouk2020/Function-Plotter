'''
    plot the function
'''

import numpy as np
import matplotlib.pyplot as plt


class Plot():
    def __init__(self, function: str) -> None:
        
        self.__function = function
        self.__originalFunction = self.__function.replace("**","^")

    

    def plotFunction(self, min_value: str, max_value: str):
        X = [i for i in range(int(min_value),int(max_value)+1,1)]
        y = [eval(self.__function) for x in range(int(min_value),int(max_value)+1,1)]
        # fig, ax = plt.subplots()
        # ax.plot(X, y)

        # # customize the plot
        # ax.set(title="Function",
        #     xlabel="X-axis",
        #     ylabel="Y-axis",
        #     )
        
        # ax.set_xlim(min_value,max_value)
        # plt.title(f"The Function: {self.__originalFunction}")
        # plt.show()

        plt.plot(X,y)
        plt.title(f"The Function: {self.__originalFunction}")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.show()



        


#========= Debugging ================
# p = Plot("x+x**2")

# p.plotFunction(0, 10)

# close()