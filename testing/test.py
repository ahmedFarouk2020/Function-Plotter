"""
                TEST CODE
    The test cases exist in test_case(plot).csv

    The other file `test_case(exit).csv` test `exit` button functionalities
        and contains test cases and the result of each test case `all are passed`
"""
import sys

# append parent directory to the sys.path so that i can import the files
sys.path.append('./..')

from ErrorHandling import *
from plot import *
from parse import *




def plot(str_function='', min_value='', max_value=''):

    # edit data 
    edited_function = Parse(str_function).parse()
    
    # pass data to error handling
    error_object = ErrorHandling(edited_function)
    error_object.checkXvalues(min_value, max_value)
    

    # check reported errors
    error = error_object.retrieveError()
    if error != None:
        print(error)
    else:
        # plot data
        print('Plotted Successfully')


with open("test_case(plot).csv",'r') as file:
    file.readline() # read header of the file

    # read line from csv file
    line = file.readline()
    testcaseId = 1
    # loop untill the end of file
    while(line != ''):
        print(f"Test Case: {testcaseId}")

        function, min_value, max_value, output = line.split(', ')
        
        
        output.replace('\n','')
        print(f"Expected Output: {output}")

        print("Actual Output: ", end='')
        plot(str_function=function, min_value=min_value, max_value=max_value)
        
        # read line from csv file
        line = file.readline()
        testcaseId +=1
        print("--------------------------------\n")
    file.close()