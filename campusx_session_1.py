#****************python output***********
print("hello world")

#Print("hello world") ----> python is a case sensitive language

print("salman khan")    #string
print(7)      #integer
print(7.7)    #float
print(True)    #boolean
print("rajnish",7,False,45)   #many datatypes print at a time

print('Hello',1,4.5,True,sep='/')   #here seperator is /, not ''
print("hello",end='-')
print("world")

#***************Data Types***************
#integer
print(8)
print(1e308)    #1*10^308

#float/Decimal
print(7.3)
print(1.7e308)    #1.7*10^308

# Boolean
print(True)
print(False)

# Text/String
print('Hello World')

# complex
print(5+6j)

# List-> C-> Array
print([1,2,3,4,5])

# Tuple
print((1,2,3,4,5))

# Sets
print({1,2,3,4,5})

# Dictionary
print({'name':'Rajnish','gender':'Male','weight':70})

# Type Function -----> they tell me the type of variable
print(type('rajnish'))

'''******************* Static Vs Dynamic Typing   **********
********************** Static Vs Dynamic Binding   **********
********************** stylish declaration techniques   **********'''
# in c/c++ we use static typing but in pyhon we use dynamic typing
# int a=4 ----> this is static typing becuse in this we define the type(int)
# a= 4 ----->  this is dynamic typing because in this we donot define the type like int,str

# Dynamic Binding
a = 5
print(a)
a = 'rajnish'
print(a)

# Static Binding
# int a = 5

# stylish declaration techniques
# first method
a = 1
b = 2
c = 3
print(a,b,c)

# second method
a,b,c = 1,2,3
print(a,b,c)

# third methodd
a=b=c= 5
print(a,b,c)

#***************Comments****************
# this is a comment
# second line
a = 4
b = 6 # like this
# second comment
print(a+b)

#************Identifiers*********

# You can't start with a digit
name1 = 'Rajnish'
print(name1)
# You can only use special chars -> _
_ = 'Rajnish'
print(_)
# identiers can not be keyword

# *************Keywords*********
# keywords are nothing but reserve word which cannot use like a identifiers (print,true,type,false,and more)

# ***********User Input*********
input1 = input("enter a number")       # here the type of input1 is string

# *********TYpe Conversion ***********
input1 = int(input("enter a number"))   # here the type of input1 is integer

# Implicit  -----> in implicit the computer already know the datatype and perform operation
print(5+5.6)
print(type(5),type(5.6))

# Explicit ------> in Explicit when we add two opertion then computer donot know the datatype of both variable and throw error
# print(4 + '4')


# ***********Literals***************
# (a = 5) in this code 5 are literals
a = 0b1010 #Binary Literals
b = 100 #Decimal Literal
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5
float_2 = 1.5e2 # 1.5 * 10^2
float_3 = 1.5e-3 # 1.5 * 10^-3

#Complex Literal
x = 3.14j

print(a, b, c, d)
print(float_1, float_2,float_3)
print(x, x.imag, x.real)

string = 'This is Python'
strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\U0001f600\U0001F606\U0001F923"
raw_str = r"raw \n string"

print(string)
print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

