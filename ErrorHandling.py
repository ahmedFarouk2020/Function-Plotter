'''
    This module is used to check the errors in data entered by user
    and respond to them (Error handling).

    These Errors are:
    1. Invalid operator (e.g. `x&4+5/a`)
    2. Invalid function (e.g. x++2 or *x+5)
'''


import re as regex


'''
    contains a DB of supported operators and variable that
    the other classes uses to check on errors
'''
class ErrorDB():

    valid_operators = ['+', '-', '*', '/', '^']
    valid_variable = 'x'


    Error_IDs = {
        "operator_error": 0,
        "variable_error": 1,
        "math_error": 2,
        "x_values_error":3,
        "str_value_error":4
    }

    # list of found errors
    # if any class detect an error it will be pushed here
    detected_errors = []

    Error_messages = [
        f"Invalid Operator: Supported operators are{valid_operators}",
        "Invalid variable: Use only one variable throughout the function",
        "Mathimatical Error: Invalid Function",
        "X value Error: Min value must be greater than max value",
        "X value Error: X Values must be integers"
    ]



'''
    Deal with error database (report error, retrieve error)
'''
class ErrorDBHandle(ErrorDB):

    '''
        append error in error list

        args:
            Error(str): error name in database

        return: 
            None
    '''
    def reportError(self, Error: str):
        if len(self.detected_errors) == 0:
            self.detected_errors.append(self.Error_IDs[Error])
        

    '''
        retrieve error from database

        args: 
            None

        return:
            Error_messages(str): if any 
            OR
            None (if no errors)
    '''
    def retrieveError(self):
        try:
            return self.Error_messages[self.detected_errors.pop()]
        except:
            return None


'''
    detect the operator errors
    EX: {`x/*9`,`c++5`}
'''
class OperatorErrors(ErrorDBHandle):
    def __init__(self, function: str ) -> None:
        
        ErrorDBHandle.__init__(self)

        '''those operators aren't supported in this app
            but python support them (`MethimaticalErrors` might not oppose)
            so i have to explicitly generate an error if any of them exist
        '''
        invalid_operators = r"[(!#%_&|.\)]"
        invalidOperatorsInFunction = regex.findall(invalid_operators, function)
        

        if len(invalidOperatorsInFunction) > 0:
            self.reportError("operator_error")
           




'''
    Detect mathimatical errors(function is mathimatically wrong) in function
    (e.g. "x$5", "X%5", "a/0")
'''
class MathematicalErrors(ErrorDBHandle):
    def __init__(self, function: str) -> None:
        ErrorDBHandle.__init__(self)

        # execute the function
        try:
            x = 0
            eval(function)
        except:
            self.reportError("math_error")

        


"""
    the main module in error handling
"""
class ErrorHandling(OperatorErrors,MathematicalErrors):
    def __init__(self, function: str) -> None:
        OperatorErrors.__init__(self,function)
        MathematicalErrors.__init__(self,function)
        


    """
        detech possible error that might happens in x values

        args:
            -min_value(str)
            -max_value(str)
    """
    def checkXvalues(self, min_value: str, max_value: str):
        try:
            if (int(min_value) >= int(max_value)):
                self.reportError("x_values_error")
        except:
            self.reportError("str_value_error")

