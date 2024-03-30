#!/usr/bin/env python
# coding: utf-8

#  
#  Question 1: 
#  
# Let's break down the elements into values and expressions:
# 
# Values:
# 
# 1. 'hello' (string)
# 2. -87. (floating-point number)
# 
# 
# Expressions:
# 
# 1. ')' (operator)
# 2. o (variable or identifier)
# 3. lu (variable or identifier)
# 4. alu (variable or identifier)
# 5. ssion)'(Value))str" (expression)
# 6. (Value) (expression)
# 
# Explanation:
# 
# -> Values represent data, such as strings or numbers, and they do not involve any operations or computations.
# 
# -> Expressions involve operations or computations and can include variables, identifiers, and operators.

# 
# Question 2 :
# 
# 
# --String:
# 
# -> A string is a data type used to represent text data in programming.
# 
# -> It consists of a sequence of characters, such as letters, digits, symbols, or spaces, enclosed within single (' ') or double (" ") quotation marks.
# 
# -> Examples of strings: "Hello, World!", '12345', "Data Science", etc.
# 
# -> Strings are immutable in many programming languages, meaning that their values cannot be changed after they are created. However, you can create new strings based on existing ones through operations like concatenation.
# 
# 
# --Variable:
# 
# -> A variable is a named storage location in a computer's memory that holds a value.
# 
# -> It serves as a symbolic representation of data that can vary or change during the execution of a program.
# 
# -> Variables are used to store different types of data, including strings, numbers, boolean values, and more.
# 
# -> Before using a variable in a program, you need to declare it by specifying its name and data type (although some dynamically typed languages may not require explicit data type declaration).
# 
# -> Examples of variables: name, age, total_amount, etc.
# 
# -> Unlike strings, variables can hold various types of data, and their values can be modified or reassigned throughout the execution of a program.

# 
# 
# 
# Question 3: 
# 
# 1.Integer (int):
# 
# -> The integer data type represents whole numbers without any decimal or fractional parts.
# 
# -> Integers can be both positive and negative, including zero.
# 
# -> Examples of integers: -10, 0, 42, 100, etc.
# 
# -> Integer data types typically have a finite range determined by the number of bits used to represent them (e.g., 32-bit 
# integers, 64-bit integers).
# 
# 
# 2.String(str):
# 
# -> The string data type represents a sequence of characters, such as letters, digits, symbols, or spaces.
# 
# -> Strings are commonly used to store textual data in programming.
# 
# -> Strings are enclosed within single (' ') or double (" ") quotation marks.
# 
# -> Examples of strings: "Hello, World!", 'Data Science', "12345", etc.
# 
# -> String some built-in function like upper(),lower(),and split() etc.
# 
# 
# 3.Boolean (bool):
# 
# -> The boolean data type represents logical values, typically denoted as either true or false.
# 
# -> Booleans are used to evaluate logical conditions and control the flow of execution in programs.
# 
# -> They are commonly used in conditional statements (e.g., if statements, while loops) and logical operations (e.g., AND, OR, NOT).
# 
# -> Examples of boolean values: true, false.
# 
# -> Booleans are essential for decision-making and controlling program behavior based on specific conditions.
# 

# 
# Question 4:
# 
# 
# 
# * An expression in programming is made up of one or more operands and operators and may also include function calls and other expressions. Here's a breakdown:
# 
# 1.Operands: These are the values or variables on which the operators act. For example, in the expression x + 5, x and 5 are operands.
# 
# 2.Operators: These are symbols that represent actions or computations to be performed on the operands. For example, + is the addition operator in the expression x + 5.
# 
# 3.Function calls: Expressions may also include function calls, where a function is invoked with certain arguments. For example, sin(x) or max(10, 20).
# 
# 4.Other expressions: Expressions can also include other expressions nested within them. For example, (x + y) * z.
# 
# * The general purpose of expressions in programming is to compute values based on the operations and data provided. They are used extensively in writing algorithms, defining conditions, performing calculations, and manipulating data. Here are some common use cases and purposes of expressions:
# 
# I.Arithmetic calculations: Expressions are commonly used to perform arithmetic operations such as addition, subtraction, multiplication, and division.
# 
# II.Logical operations: Expressions are used to evaluate logical conditions and perform logical operations such as AND, OR, and NOT.
# 
# III.Control flow: Expressions are often used in conditional statements (e.g., if-else statements, switch-case statements) and loops (e.g., for loops, while loops) to control the flow of execution based on certain conditions.
# 
# IV.Function evaluation: Expressions can include function calls, where functions are invoked with certain arguments to perform specific tasks or calculations.
# 
# V.Data manipulation: Expressions can be used to manipulate and transform data in various ways, such as filtering, sorting, aggregating, and transforming data sets.
# 
# 

# Qquestion 5:
# 
# --Expression:
# 
# -> An expression is a combination of values, variables, operators, and function calls that evaluates to a single value.
# 
# -> Expressions can be used to perform calculations, evaluate conditions, and create data structures.
# 
# Example:
# 

# In[7]:


x = 5
y = 10
result = x + y * 2  # This is an expression


# In this example, x + y * 2 is an expression that computes a value (25) based on the variables x and y.

# --Statement:
# 
# -> A statement is a complete line of code that performs an action, makes a decision, or controls the flow of execution.
# 
# -> Statements can include expressions but are not limited to them; they can also include keywords, control structures, and other elements that perform specific tasks.
# 
# Example:

# In[8]:


if result > 20:  # This is a statement
    print("The result is greater than 20")


# In this example, if result > 20: is a statement that controls the flow of execution based on the condition specified by the expression result > 20.

# In[20]:


#Question 6:
bacon = 22
bacon +1

#output:
# 23


# In[19]:


#question 7:
'spam' + 'spamspam'
'spam'*3

#output
#spamspamspam


# Question 8:
# 
# --eggs:
# 
#          "eggs" are valid variable name  becasue it start with letter (e) and the variable name should be start with a letter (a to z or A to Z) or an  underscore(_).
#          
#          After the first character , variable names can contain letters ,digits ,or underscore.
#          "eggs".
#          
#          Therefore "eggs" is valid variable name.
#         
# -- 100: 
# 
#         "100" is start with digit and the variable name cannot start with digit(0-9).
#         
#         Therefore "100" is invalid variable name.

# Question 9:
# 
# 1.int() function:
# 
# -> The int() function converts a value to an integer.
# 
# ->If the value is a string representation of an integer, it returns the corresponding integer.
# 
# -> If the value is a floating-point number, it truncates the decimal part and returns the integer part.
# 
# Examples:

# In[12]:


int_value = int("10")  # Converts string "10" to integer 10


# 2.float() function:
# 
# -> The float() function converts a value to a floating-point number.
# 
# -> If the value is an integer, it adds a decimal point and returns the corresponding floating-point number.
# 
# -> If the value is a string representation of a floating-point number, it returns the corresponding floating-point number.
# 
# Examples:

# In[13]:


float_value = float(10)  # Converts integer 10 to floating-point number 10.0


# 3.str() function:
# 
# -> The str() function converts a value to a string.
# 
# -> It returns the string representation of the value.
# 
# Examples:

# In[14]:


str_value = str(10)  # Converts integer 10 to string "10"


# Question 10: 
# 
# The expression 'I have eaten ' + 99 + ' burritos.' causes an error because it attempts to concatenate a string ('I have eaten ') with an integer (99) without converting the integer to a string first. In Python, the + operator is used for string concatenation when applied to strings, but it cannot concatenate strings with integers or other data types directly.
# 
# To fix the error, you need to convert the integer 99 to a string before concatenating it with the other strings. You can achieve this by using the str() function to convert the integer to its string representation:
# 

# In[17]:


'I have eaten ' + str(99) + ' burritos.'


# With this modification, the integer 99 will be converted to the string '99', allowing the expression to concatenate three strings ('I have eaten ', '99', and ' burritos.') together successfully.
# 
# 
# 
# 
# 
# 

# In[18]:


# Question 11:
# Function to calculate the sum of two numbers

def calculate_sum(num1, num2):
    return num1 + num2

# Input the numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate the sum
sum_result = calculate_sum(num1, num2)

# Print the result
print("The sum of", num1, "and", num2, "is:", sum_result)


#output
#Enter the first number: 12.5
#Enter the second number: 10.00
#The sum of 12.5 and 10.00 is : 22.5

# In[21]:


# Question 12
# Take user's name as input
name = input("Enter your name: ")

# Print greeting message
print("Hello,", name + "! Welcome to our program.")


#output
#Enter your name : Ravi
#Hello Ravi! Welcome to our program



# In[22]:


#Question 13
# Take input for length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the area
area = length * width

# Print the result
print("The area of the rectangle with length", length, "and width", width, "is:", area)

#output 
#Enter the length of the rectangle: 10
#Enter the width of the rectangle: 5
#The area of the rectangle with length 10 and width  5 is: 50

# In[23]:


#Question 14
# Take input for age
age = int(input("Enter your age: "))

# Check age category and print message
if age < 0:
    print("Invalid age entered.")
elif age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")

#output
#Enter your age: 25
#You are an adult.


# In[24]:


#Question 15
# Take input for Celsius temperature
celsius = float(input("Enter the temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Print the result
print("Temperature in Fahrenheit:", fahrenheit)

#output
#Enter the temperature in Celsius: 36
#Temperature in Fahrenheit: 96.800


# In[25]:


#Question 16
# Define the value of pi
pi = 3.14

# Take input for radius
radius = float(input("Enter the radius of the circle: "))

# Calculate the area
area = pi * (radius ** 2)

# Print the result
print("The area of the circle with radius", radius, "is:", area)

#output
#Enter the radius of the circle: 5
#The area of the circle with radius 5 is : 78.53


# In[26]:


#Question 17
# Take input for the first number
num1 = float(input("Enter the first number: "))

# Take input for the second number
num2 = float(input("Enter the second number: "))

# Find the maximum of the two numbers
maximum = max(num1, num2)

# Print the result
print("The maximum of", num1, "and", num2, "is:", maximum)

#output
#Enter the first number: 20
#Enter the second number: 18
#The maximum of 20 and 18 is : 20


# In[27]:


#Question 18
# Take input for the first number
num1 = float(input("Enter the first number: "))

# Take input for the second number
num2 = float(input("Enter the second number: "))

# Calculate the product
product = num1 * num2

# Print the result
print("The product of", num1, "and", num2, "is:", product)

#output
#Enter the first number: 11
#Enter the second number: 11
#The product of 11 and 11 is : 121



# In[28]:


#Question 19
# Take input for the number
number = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if number > 0:
    print("The number entered is positive.")
elif number < 0:
    print("The number entered is negative.")
else:
    print("The number entered is zero.")

#output
#Enter a number: 00
#The number entered is zero

    


# In[ ]:




