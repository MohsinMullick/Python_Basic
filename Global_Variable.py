"""
A global variable is a variable that is declared outside
of all functions and can be used anywhere in the program
"""

x="awesome"#x is defined outside the function
def myfunc():#just creating the function not running yet
    print("python is "+x)#no local x exist just ony global
myfunc()#my function run and print

x="awesome"#x is defined outside the function
def myfun():#just create the function not running yet
    x="fantastic"#x is define inside the function
    print("python is "+x)#local variable x
myfun()#call the function
print("Python is "+x )#global variable




#global variable many function
name="Mohsin"#global variable
def hello():#define function
    print("Hello " + name)#global variable
def bye():#just create the function
        print("Goodbye " + name)#global variable
hello()#call the function
bye()#call the function


