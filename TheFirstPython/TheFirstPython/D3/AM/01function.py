"""
A function is a block of organized, reusable code that is used to perform a single,
related action. Functions provide better modularity for your application and a high degree of code reusing.

Python gives you many built-in functions like print(), etc. but you can also create your owon
functions. There functions are called user-defined functions
"""



"""
Definding a Function

you can define functions to provide the required functionality. Here are simple rules to define a function in Python

- Function blocks begin with keyword def followed by the function name and parentheses (()).

- Any input parameters or arguments should be placed within there parentheses. You can also define parameters inside there parenthese.

- The first statement of a function can be an optional statement - the documentation string of the function or docstring.

- The code block within every function starts with a colon (:) and s indented.

- The statement return[rexpression] exsits a functino, optionally passing back an expression to the caller. A return statement with no arguments is the same as return NON


"""

### Syntax

#def functionname(parameters) :
#    "function_docstring"
#    function_suite
#    return [expression]

# By default, parameters have a positional behavior and you need to inform them in the same order that they were defined.


def printme(str): 
    "This prints a passed string into this function"
    print(str)
    return;

#Now you can call printme function
printme("abc")
printme("def")




"""
Pass by reference vs value
All parameters (arguments) in the Python 
language are passed by reference. 
It means if you change what a parameter 
refers to within a function, 
the change also reflects back in the calling
function. For example −
"""
def changeme(mylist):
    "This changes a passed list into this function"
    mylist.append([1,2,3,4]);
    print ("Values inside the function: " ,mylist)
    return

mylist = [10,20,30]

changeme(mylist)

print(mylist)


"""
There is one more example where argument 
is being passed by reference 
and the reference is being overwritten 
inside the called function.

"""

def changeme (mylist):
    "This changes a passed list into this function"
    mylist = [1,2,3,4]
    print("Values inside the function", mylist)
    return

mylist = [10, 20, 30];
changeme(mylist);
print(mylist)


"""
Variable-length arguments

You may need to process a function for more arguments that you specified while definding the function.
These arguments are called variable-length arguments and are not named in the functino definition, unlike required and default arguments.

"""


def printinfo( arg1, *vartuple):
    "This prints a variable passed arguments"
    print (arg1)
    for var in vartuple:
        print (var)
    return;


printinfo(10)
printinfo(70,60)
printinfo(70,60,50,40)



def sumAll(arg1, *arg2):
    "This sums all varialbe passed arguments"
   
    for var in arg2:
        arg1 += var             
    
    return arg1

print("*"*50)

print(sumAll(5,4,3,2,1))
print(sumAll(5,-4,-4,2,1))


print("*"*50)

def addAll(*arg1):
    result = 0
    for var in arg1:
        result += var
    return result

print("*"*50)
print(addAll(5,-4,-4,2,1,1,2,3))





"""
The Anonymous Functions

These functions are called anonymous because they are not declared
in the standrad mannger by susing the def keyword. You can use the lambda keyword to create small anonymous functions.

- Lambda forms can take any number of arguments but return just one value in the form of an expression.
- An anonymous function cannt be a direct callt o print because lambda required an expression
- Lambda functions have thier own local namespace and cannot access variables other than those in thier parameter list and those in the global namespace
- Alothough it appears that lambda's are a one-like version of a function, they are not equivalent to inline statements in C or C++,
  whose purpose is by passing function stack allocation during invodation for performance reasons.
"""


sum = lambda arg1, arg2: arg1 + arg2;


print("Value of Total :" , sum(10,20))



"""
The return Statement

The statement return [expression] exiss a function, optionally passing back an expression to the caller. A return 

"""



def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "multiply":
         result = 1
         for i in args:
             result *= i
    return result

result = add_mul("add", 8,4)
print(result) # 12

result = add_mul("multiply", 8,4)
print(result) #32


#Keyword parameter

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)

print_kwargs(name="foo", age=3)
