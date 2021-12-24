'''
    parse string input

    `If An Error exist in error DB don't execute this module`
'''
import re as regex
from ErrorHandling import ErrorDBHandle
from ErrorHandling import OperatorErrors

NO_REPORT = 0
REPORT = 1
NO_VAR = 0

class Parse():
    def __init__(self, function: str) -> None:
        self.__function = function
        self.__support_variable = 'x'
        self.__exist_variables = None
        self.__reportFlag = NO_REPORT


    def __convert(self):
        variablesInFunction = regex.findall('[A-Z,a-z]', self.__function)
        print("+++++++++++++++++++++++++")
        print(variablesInFunction)
       
        print(type(len(variablesInFunction)))
        if variablesInFunction == []:
            self.__exist_variables = NO_VAR
        # len(list) = count of that variable in the list
        # so list contains only a repeated one variable
        elif variablesInFunction.count(variablesInFunction[0]) is len(variablesInFunction):

            self.__exist_variables = variablesInFunction[0] # variable exist in the function
            print("len(list) = count of that variable in the list")
        else:
            ErrorDBHandle().reportError("variable_error")
            self.__reportFlag = REPORT
            print("variable error reported")

    def parse(self) ->str :
        self.__convert()
        if self.__reportFlag == REPORT:
            return "/*x"
        # No variables exits `F(x)=5`
        if self.__exist_variables == NO_VAR:
            return self.__function

        self.__function = self.__function.replace('^',"**")

        # replace each variable with 'x'
        indexOfVariable = self.__function.find(self.__exist_variables)

        print(self.__function.replace(self.__function[indexOfVariable],self.__support_variable))

        return self.__function.replace(self.__function[indexOfVariable],self.__support_variable)



# invalid_operators = "[(! @ # $ % _)]"
# invalidOperatorsInFunction = regex.findall(invalid_operators, "2a+*")
# print(invalidOperatorsInFunction)

# OperatorErrors("s\a")

# l = [1,2,3,5]
# print(l.pop(2))