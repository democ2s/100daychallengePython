

"""
Project Title: 100 days of code in Python
File Title: Day 3
Date: 26/Sep/2023
"""
"""
Concepts
1. If else statement
2. Relational operators
3. Modulo Operator
4. https://ascii.co.uk/art/abacus
"""


# Exercise 1 : Check number is EVEN / ODD
user_input = int(input("Enter a number to check whether it is Even / Odd: "))
if (user_input % 2) == 0:
    print("The entered number is EVEN")
else:
    print("The entered number is ODD")

# Exercise 2: Demonstration of multiple If/Else conditions

bill = 0
height = float(input("What is your height in cms? "))
if height >=120:
    print("You can ride the rollercoaster")
    age = float(input("What is your age? "))
    if age < 12:
        bill = 5
    elif age <18:
        bill = 7
    elif age >=45 and age <=55:
        bill = 0
        print("You are having free ride")    
    if age >=45 and age <=55:
        bill = 0
    else:
        bill = 12    
    want_photo = input("Want photos? Y or N")
    if want_photo == "Y":
        bill+=3
    print(f"The total bill is ${bill} for your ride")    
else:
    print("Sorry, you cannot ride rollercoaster!")

# Excercise 3: BMI Calculator

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = weight / (height **2)
bmi = round(weight / (height **2))
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi <25:
        print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi <30:
        print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi <35:
        print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")


# Exercise 4: Check whether user entered year is Leap year / not.

user_year = int(input("Enter a year"))

if (user_year % 4) == 0:
    if user_year % 100 ==0:
        if user_year % 400 ==0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("leap year.")    
else:
        print("Not leap year.")

# Exercise 5: Another example for multiple If/Else conditions
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
pep = input("Do you want Pepporini? Y or N ")
cheese = input("Do you want extra cheese? Y or N ")
bill = 0

if size == "S":
    bill +=15    
elif size == "M":
    bill +=20    
elif size == "L":
    bill +=25
if(pep == "Y"):
    if size == "S":
        bill +=2
    else:
        bill+=3
if cheese == "Y":
    bill +=1
print(f"Your final bill is: ${bill}")

# Exercise 6: Another example for multple If /Else conditions

person_one_name = input("Enter first person name: ")
person_two_name = input("Enter second person name: ")
person_one_name = person_one_name.lower()
person_two_name = person_two_name.lower()
combined_name = person_one_name + person_two_name

# true
# love

count_t1 = combined_name.count('t') 
count_r1 = combined_name.count('r') 
count_u1 = combined_name.count('u') 
count_e1 = combined_name.count('e') 

count_l2 = combined_name.count('l') 
count_o2 = combined_name.count('o') 
count_v2 = combined_name.count('v') 
count_e2 = combined_name.count('e') 

index1 = count_t1 + count_r1 + count_u1 + count_e1
index2 = count_l2 + count_o2 + count_v2 + count_e2
score_str = str(index1) + str(index2)
score = int(score_str)

if (score <10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >=40) and (score <=50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

# Exercise 7: Simple Game using If/Else conditions

# Tressur Island
print('''
          /|                        /|
                          | \           __ _ _     / ;
                    ___    \ \   _.-"-" `~"\  `"--' /
                _.-'   ""-._\ ""   ._,"  ; "\"--._./
            _.-'       \./    "-""", )  ~"  |
           / ,- .'          ,     '  `o.  ;  )
           \ ;/       '                 ;   /
            |/        '      |      \   '   |
            /        |             J."\  ,  |
           "         :       \   .'  : | ,. _)
           |         |     /     f |  |`--"--'
            \_        \    \    / _/  |
             \ "-._  _.|   (   j/; -'/
              \  | "/  (   |   /,    |
               | \  |  /\  |\_///   /
               \ /   \ | \  \  /   /
                ||    \ \|  |  |  |
                ||     \ \  |  | /
                |\      |_|/   ||
                L \       ||   ||
                `"'       |\   |\
    [nabis]               ( \. \ `.
                          |_ _\|_ _\
                            "    "
      
      ''')





print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("You are at a crossroad. Where do you want to go? Type 'left' or 'right' ").lower()

if choice1 == "left":
    choice2 = input("You came to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.").lower()    
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?").lower()        
        if choice3 == "yellow":
            print("You Win!")
        elif choice3 == "red":
            print("Bummed by fire. Game Over.")
        elif choice3 == "blue":
            print("Eaten by beasts, Game Over.")
        else:
            print("You have chosen door that doesn't exits, Game over.")
    else:
        print("Attacked during swimming, Game Over.")
else:
    print("You fell into a hole, Game Over.")






