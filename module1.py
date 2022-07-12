#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hp1
#
# Created:     27-05-2022
# Copyright:   (c) hp1 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#even odd
##num = (1,2,3,4,5,6,7,8,9)
##count_even=0
##count_odd=0
##for i in num:
##    if not i%2:
##        count_even += 1
##    else:
##        count_odd += 1
##print ('number of even number', count_even)
##print ('number of odd number', count_odd)
###new problem
##num in range (1,50)
##Buzz = 0
##Fizz = 0
##BuzzFizz = 0
##for i in num:
##    if i%3==0:
##        Buzz = 1
##    elif i%5==0:
##        Fizz = 1
##    else:
##        i%3==0 and i%5==0
##        BuzzFizz = 1
##print('Buzz','Fizz','BuzzFizz')
##


##no = 20
##print(id(no))
##no = 30
##print (id(no))
##0

##na = 1000.2
##print (id(na))
##na1 = 1000.2
##print (id(na1))

##name = input("Enter your name :")
##print(name)

##num1 = int(input("enter the 1st number:"))
##num2 = int(input("enter the 2nd number:"))
##add = num1 + num2
##print('Addition:', add)


##num1 = input("enter the 1st number:")
##num2 = input("enter the 2nd number:")
##add = int(num1) + int(num2)
##print('Addition:', add)


##num1 = int(input("enter the 1st number:"))
##num2 = int(input("enter the 2nd number:"))
##sub = num1 - num2
##print('Substraction:', sub)

##num1 = input('enter the 1st number :')
##num2 = input('enter the 2nd number :')
##print(num1==num2)

##num1 = input('enter the 1st number :')
##num2 = input('enter the 2nd number :')
##print (not(num1==num2 or num1<num2))

##num1 = 20
##num2 = 30
##print(not(num1<num2 or num1==num2))

### ord function
##num = "r"
##print(ord(num))

###Format inbuilt function
##name = "Suraj"
##greetings = "Good morning"
###print 'Good morning Suraj' by format function
##print (format,greetings,name,"What is your age?")

###id inbuilt function
##name = "Suraj"
##print(id(name))
##
##num = 25
##print(id(num))
##num = 300
##print(id(num))#intigers are immutable in nature
##
##num1 = 55
##num2 = 55
##print(id(num1))
##print(id(num2))#in python -5 to 256 values are predefined so the id of numbers in the range will be same.

##name= "Suraj"
##name = "Rohan"
##print(id(name), type(name))#type function is used to find the data ttype of variable
##print(id(name))
##
##w = "a"
##print(ord(w))#ASCII value function

#input inbuilt function
##name1 = input("Enter the first name")
##name2 = input("Enter the second name")
##add = name1 and name2
##print("There was a fight between :", add)

##num1 = int(input("Enter the 1st number :"))
##num2 = int(input("Enter the 2nd number :"))
##multi = num1 * num2
##print ("The multiplication of num1 & num2 is :", multi, type(multi))

##lst = [1,2.5,True,"Suraj",5+2j]
##print(lst)
##print(type(lst))
##print(lst[3])
##lst[3]="Rohan"
##print (lst)

##set_demo = {1,2.5,True,"Suraj",5+2j}
##print (set_demo)

##tup_demo = (1,2.5,True,"Suraj",5+2j)
##print(tup_demo)
##print(tup_demo[3])
##print(type(tup_demo[2]))

##dict_demo = {"one":"Bharati","two":"Mohit","three":"Deepak","four":"Bharati"}
##print(dict_demo)
##print(type(dict_demo))
##print(dict_demo["one"])
##dict_demo["one"] = "Rohan"
##print(dict_demo["one"])

#Type casting
##name = 'Suraj'
###print("string into int : ",int(name),type(nmae)) #can not convert str into int if it got alphabets
###print("string into float", float(name), type(name)) #can not convert str into float if it got alphabets
##print("string into bool", bool(name), type(name))

##num = 55
##print("int into srting", str(num),type(num))
##print("int into float", float(num), type(num))
##print("int into bool", bool(num), type(num))
##
##num = 55.0
##print("float into srting", str(num),type(num))
##print("float into int", int(num), type(num))
##print("float into bool", bool(num), type(num))

##num = True
##print("bool into srting", str(num),type(num))
##print("bool into float", float(num), type(num))
##print("bool into int", int(num), type(num))

##num = False
##print("bool into srting", str(num),type(num))
##print("bool into float", float(num), type(num))
##print("bool into int", int(num), type(num))

#operators
#arythmatic operators
##num1 = int(input("enter 1st number :"))
##num2 = int(input("enter 2nd number :"))
###+operator
##print(num1+num2)
###-operator
##print(num1-num2)
###*operator
##print(num1*num2)
###%operator
##print(num1%num2)
###//operator(floor_division)
##print(num1//num2)
###**operator(exponential)
##print(num1**3)

#comparision operator, #Always returns boolean value
##num1 = int(input("enter 1st number :"))
##num2 = int(input("enter 2nd number :"))
### == operator
##print(num1==num2)
### != oprator
##print(num1!=num2)
### < operator
##print(num1<num2)
### > operator
##print(num1>num2)
### <= operator
##print(num1<=num2)
### >= operator
##print(num1>=num2)

# logical operator, #Always returns boolean value, #used for checking multiple conditions

# and operator
##num1 = int(input("enter 1st number :"))
##num2 = int(input("enter 2nd number :"))
##
##print(num1==num2 and num1<num2)
##print(num1!=num2 and num1>num2)
##
### or oprator
##print(num1==num2 or num1<num2)
##print(num1!=num2 or num1>num2)
##
###not operator
##print(not(num1==num2 and num1<num2))
##print(not(num1!=num2 and num1>num2))

#Assignment
#operator
##num1 = int(input("Enter 1st number : "))
##num2 = int(input("Enter 2nd number : "))
##add = num1+num2
##print("The result is : ", add)

#Area of a triangle
##height = int(input("Height of triangle = "))
##base = int(input("Base of triangle ="))
##area = 1/2*base*height
##print("Area of triangle is :",int(area))

#Swap two numbers
##num1 = 5
##num2 = 9
#creat a temporary variable to swap the values
##temp = num1
##num1=num2
##num2=temp
##print(num1,num2)

#convert KM to Miles
##distance_km = float(input("Enter the distance in kilometer :"))
##distance_miles = 0.621*distance_km
##print("The given distance in miles =", float(distance_miles))

##import math
###Square root of a given number
##x = 8
##print(sqrt(x))

# Largest among three numbers
##num1 = int(input("Enter the 1st number :"))
##num2 = int(input("Enter the 2nd number :"))
##num3 = int(input("Enter the 3rd number :"))
##if num1>num2>num3:
##    print("num1 is greater than num2 & num3")
##elif num2>num3>num1:
##    print("num2 is greater than num3 & num1")
##else:
##    print("num3 is gretest")


#identity operator



#Assignment operator
##num1 = int(input('enter 1st number'))
##num2 = int(input('enter 2nd number'))
##num1 += num2
##print(num1)
##num1**=num2
##print(num1)
##num1//=num2
##print(num1)

#condition statements
#find a given number is odd or even
##num = int(input("Enter a number :"))
##if num%2==0:
##    print("num is even")
##else:
##    print("num is odd")

#given number is divisible or not by 7
##num = int(input("Enter a number :"))
##if num/7==0:
##    print("num is divisible by 7")
##else:
##    print("num is not divisible by 7")


#display "Hello" if a number entered by user is a multiple of five, otherwise print "Bye"
##num = int(input("Enter a number :"))
##if num%5==0:
##    print("Hello")
##else:
##    print("Bye")

#Write a program to display the last digit of a number.
##num = 89624624566
##print("Last digit of the number is :", num%10)

#identity operator
##no1 = int(input("Enter a number :"))
##no2 = int(input("Enter another number :"))
##is_demo = no1 is no2
##print(is_demo)
##is_not_demo = no1 is not no2
##print(is_not_demo)


#membership operator
##lst1 = [25,35,65,55,85,45,75,95]
##in_demo = 25 in lst1
##print(in_demo)

#nestd if statement
##age = int(input("Enter your age :"))
##if age>=18:
##    print("Your age is ",age,"you are eligible to do job")
##    qualification = int(input("Enter your highest qualification :"))
##    if qualification>=12:
##        print("Congratualation you have the right qualification for the job role")
##    else:
##        print("you are not eligible")
##    internships = int(input("Enter the ps you have done :"))
##    if internships>=5:
##        print("Congratulation you are hired!!!")
##    else:
##        print("Sorry we would like to consider another candidate")
##else:
##    print("Your age is ",age, "you are not eligible to do a job")

#Write a program to check whether the last digit of a number( entered by user ) is divisible by 3 or not
##num = int(input("Enter a number :"))
##num1 = num%10
##if num1%3==0:
##    print(True)
##else:
##    print(False)

# Write a program to accept percentage from the user and display the grade according to the following criteria:
##  Marks                        Grade
##  > 90                           A
##  > 80 and <= 90                 B
##  >= 60 and <= 80                C
##  below 60                       D
#Laddes if statement
##marks = int(input("Enter the marks obtained in percentage :"))
##if marks>90:
##    print("Grade A")
##if marks>80 and marks<=90:
##    print("Grade B")
##if marks>=60 and marks<=80:
##    print("Grade C")
##if marks<60:
##    print("Grade D")


#Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria :
##  Cost price (in Rs)                 Tax
##  > 100000                           15 %
##  > 50000 and <= 100000              10%
##  <= 50000                           5%
#Laddes if statement
##cost = int(input("Enter the cost of the bike in rupees :"))
##if cost>100000:
##    print("Tax is to be paid is 15%")
##if cost>50000 and cost<=100000:
##    print("Tax is to be paid is 10%")
##if cost<=50000:
##    print("Tax is to be paid is 5%")


#Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
#      Unit                      Price
# First 100 units               no charge
# Next 100 units              Rs 5 per unit
# After 200 units             Rs 10 per unit
#(For example if input unit is 350 than total bill amount is Rs2000)

##unit = int(input("Enter number of units consumed :"))
##pri = 0
##if unit == 100:
##    pri = 0
##if unit>100 and unit<200:
##    pri = (unit-100)*5
##if unit>200:
##    pri = 500+(unit-200)*10
##print("Amaount to pay",pri)


# Write a program to check whether the last digit of a number( entered by user ) is divisible by 3 or not.
##no_1 = int(input("Enter a number :"))
##no = no_1%10
##if no%3 ==0:
##    print("number is divisible by 3")
##else:
##    print("numnber is not divisible by 3")


# Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday , 2 for Monday and so on.
##num = int(input("Enter a number between 1 to 7 : "))
##if num == 1:
##    print("It is Sunday")
##if num == 2:
##    print("Itis Monday")
##if num == 3:
##    print("it is Tuesday")
##if num == 4:
##    print("it is Wednesday")
##if num == 5:
##    print("it is Thursday")
##if num == 6:
##    print("it is Saturday")
##if num == 7:
##    print("it is Saturday")



# Accept any city from the user and display monument of that city.
# City                   Monument
# Delhi                  Red Fort
# Agra                  Taj Mahal
# Jaipur                Jal Mahal
##city = input("Enter the city name : ")
##if city == "Delhi":
##    print("The monument is : ", "Red Fort")
##elif city == "Agra":
##    print("The monument is : ", "Taj Mahal")
##elif city == "Jal Mahal":
##    print("The monument is : ", "Jala Mahal")
##else:
##    print("Enter a valid city name!!!")


# Write a program to check whether a number entered is three digit number or not.
##num = int(input("Enter a number : "))
##if num>99 and num<=999:
##    print("num is a three digit number")
##else:
##    print("num is not a three digit number")


# Write a program to check whether a person is eligible for voting or not.(voting age >=18)
##age = int(input("Enter your age : "))
##if age>=18:
##    print("You'r eligible to vote!!!")
##else:
##    print("You'r not eligible to vote, Sorry")


# Write a program to find the lowest number out of two numbers excepted from user.
##num1 = 155
##num2 = 20
##if num1<num2:
##    print("num1 is lower than num2")
##else:
##    print("num2 is lower than num1")


# Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.
##num = int(input("Enter a number : "))
##if num%2==0 and num%3==0:
##    print("Given number is divisible by 2 & 3")
##else:
##    print("Given no is not divisible by 2 & 3")


# Write a program to find the largest number out of three numbers excepted from user.
##num1 = int(input("Enter 1st number : "))
##num2 = int(input("Enter 2nd number : "))
##num3 = int(input("Enter 3rd number : "))
##if num1>num2 and num1>num3:
##    print("Largest number is : ",num1)
##if num2>num1 and num2>num3:
##    print("Largest number is : ",num2)
##if num3>num1 and num3>num2:
##    print("Largest number is : ",num3)


# Accept the temperature in degree Celsius of water and check whether it is boiling or not (boiling point of water in 100 oC.
##temp = int(input("Enter the temperature of water in degree Celsius : "))
##if temp>=100:
##    print("The water is boiling !!!")
##else:
##    print("The water is not boiling...")




#Questions & Answer
##num = int(input("Enter a number : "))
##if num/2 == num//2:
##    print("even")

##length = int(input("Enter the length : "))
##breadth = int(input("Enter the breadth : "))
##if length == breadth:
##    print("It is a Square")
##else:
##    print("It is a Rectangle ")


##age1 = int(input("Enter age : "))
##age2 = int(input("Enter age : "))
##age3 = int(input("Enter age : "))
##if age1>age2 and age1>age3:
##    print("The oldest is ", age1)
##elif age2>age1 and age2>age3:
##    print("The oldest is ", age2)
##else:
##    print("The oldest is ", age3)
##if age1<age2 and age1<age3:
##    print("The youngest is ", age1)
##elif age2<age1 and age2<age3:
##    print("The youngest is ", age2)
##else:
##    print("The youngest is ", age3)



##name = input("Enter your name : ")
##roll_number = int(input("Enter your roll number : "))
##eng = int(input("Enter English marks : "))
##math = int(input("Enter Math marks : "))
##sci = int(input("Enter Science marks : "))
##Total = eng+math+sci
##perc = (Total//300)*100
##if perc>=90:
##    print("Grade A")
##if perc<90 and perc>=80:
##    print("Grade B")
##if perc<80 and perc>=70:
##    print("Grade c")
##if perc<70 and perc>=40:
##    print ("Grade D")
##else:
##    print("Fail")
##print (name, roll_number, perc)


num = int(input("Enter a number"))
for i in range (1,11,1):
    multi = num*i
    print(multi, end=" " )

































































































