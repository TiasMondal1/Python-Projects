print("Hello, world!")

# variable = contains any value that we assign

#string = single or double quotes

name = "Tias"
print(name)
print("Hello " + name)

#type = data type of variable

print(type(name))

age = 21
age += 1
print(age)
print(type(age))

#type casting = changes the datatype of one variable to another

#str(variable) changes the variable into string

#float = stores integer with decimal number 

height = 123.23
print(height)
print(type(height))

# This prints the length of string inside the two quotes
print(len('This is how i ride')) 

str() #Converts anything into a string
int() #Converts anything into an integer
float() #Converts anything into float/decimal

# When we use input() function, it returns a string by default

# String and integer value cant be same
# Integer and floating point value can be same

# This means that we compare between them using == operator

#round()  rounds off the numbers to nearest whole number

weight = 75.64
print(round(weight))

# abs() gives us the absolute value of any number

num = -9
print(abs(num))

#pow(base, exponent) calculates base raised to power of exponent

result = pow(2,3)
print(result)

# The modulus % operator gives the remainder when divided by something else

a = 10
b = 3
c = a%b
print(c)

# Booleans -> can be stored in a variable, but they cant be used as Variable names