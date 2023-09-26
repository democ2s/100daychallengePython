

"""
Project Title: 100 days of code in Python
File Title: Day 2
Date: 26/Sep/2023
"""

"""
Concepts
1. Data types
2. Mathematical operations and helper functions
3. Fstring
"""
# Data types

"""
String, Integer, Float and Boolean
"""
var_str = "Apples"
var_bool = True
var_float = 1234.56
var_int = 4534

print("**** Variables *****")
print("'" + var_str + "' is of " + str(type(var_str)) + " data type")
print("'" + str(var_bool) + "' is of " + str(type(var_bool)) + " data type")
print("'" + str(var_int) + "' is of " + str(type(var_int)) + " data type")
print("'" + str(var_float) + "' is of " + str(type(var_float)) + " data type")
print("\n")

# Mathematical Operations
var_a = 10
var_b = 19
var_sum = var_a  + var_b
var_rem = var_a -var_b
var_prod = var_a * var_b
var_div = var_a / var_b
var_div_floor = var_a // var_b
var_pow = var_a **3
var_div_round = round(var_a / var_b,2)

print("**** Mathematical operations ****")
print(f"Addition operation of {var_a} + {var_b} is: {var_sum}")
print(f"Subtraction operation of {var_a} - {var_b} is: {var_rem}")
print(f"Multiplication operation of {var_a} * {var_b} is: {var_prod}")
print(f"Power operation of {var_a} ** 3 is: {var_pow}")
print(f"Division operation of {var_a} / {var_b} is: {var_div}")
print(f"Division with rounding upto 2 digits of {var_a} / {var_b} is: {var_div_round}")
print(f"Floor division operation of {var_a} // {var_b} is: {var_div_floor}")
print("\n")

# helper functions
# type(), str() Float(), int(), round(x) OR round(x,y)
print("**** Helper Methods *****")

print("type()" + " is a method used to check the data type of the variable")
print("str()" + " is a method used to convert values / variables of other data type into string data type")
print("float()" + " is a method used to convert values / variables of number / string data type into float data type")
print("int()" + " is a method used to convert values / variables of number / string data type into integer data type")
print(f"round() is a method used to roundoff the decimal number. We can also pass second argument to specify number of decimals after rounding off.")
print("\n")
print("***Casting from one type to another***")
print("casting from int (" + str(var_int )+") to float")
print(float(var_int))
print("casting from float (" + str(var_float )+") to int")
print(int(var_float))
var_round = round(28.7867,3)
print(f"round(28.7867,3) -- > {var_round}")
var_div_quotient = 35/4
print(f"35/4 -- > {var_div_quotient}. This is normal division and hence displaying the decimal numbers as well")
var_div_round = round(35/4,3)
print(f"round(35/4,3) -- > {var_div_round}. This is normal division and also rounding off result with upto 3 decimal")
var_div_floor_quotient = 35//4
print(f"35//4 -- > {var_div_floor_quotient}. This is floor division where result is rounded to nearest least integer")
print(round(36/4,3))

print("Example programs using the above concepts")

print("Welcome to the tip calculator")
total_bill = input("What was the total bill? $")
tip_percent = input("What percentage tip would you like to give? 10, 12, or 15? ")
split_count = input("How many people to split the bill? ")

gross = float(total_bill) + (100 * (float(tip_percent)/float(total_bill)))
per_cost = gross / int(split_count)
per_cost_str = round(per_cost,2)
result_str = "$" + str(per_cost_str)

print(f"Each person should pay: {result_str}")