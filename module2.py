#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hp1
#
# Created:     15-07-2022
# Copyright:   (c) hp1 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#  WHILE & FOR LOOP QUESTION PRACTICE:
# Q1. Write a program to print the following using while loop
# a. First 10 Even numbers
# b. First 10 Odd numbers
# c. First 10 Natural numbers
# d. First 10 Whole numbers

#a
##num=2
##while num<=20:
##    print(num, end=" ")
##    num+=2
#b
##num=1
##while num<=19:
##    print(num, end= " ")
##    num+=2
#c
##num=0
##while num<=9:
##    num+=1
##    print(num,end=" ")
#d
##num=0
##while num<10:
##    num+=1
##    print(num, end=" ")

# Write a program to print first 10 integers and their squares using while loop.
##num=1
##print("Number","  ","Square")
##while num<10:
##    num+=1
##    print(num,"      ",num**2)

# Write for loop statement to print the following series: 10, 20, 30 … … 300
##num = 0
##for num in range(10,310,10):
##    print(num, end=",")

##num = 10
##while num<=300:
##    print(num, end=",")
##    num+=10

# Write a while loop statement to print the following series: 105, 98, 91 ………7.
##num = 105
##while num==7:
##    num-=7
##    print(num,end=",")

# Write a program to print first 10 natural number in reverse order using while loop.
##num = 10
##while num>0:
##    print(num)
##    num-=1

# Write a program to print sum of first 10 Natural numbers.
##num = 10
##sum = 0
##while num >= 1:
##   sum = sum + num
##   num= num - 1
##print(sum)

##num = 1
##sum = 0
##while num <= 10:
##   sum = sum + num
##   num= num + 1
##print(sum)

# Write a program to print sum of first 10 Even numbers.
##num = 2
##sum = 0
##while num<=20:
##    sum+=num
##    num+=2
##    print(sum)

# Write a program to print table of a number entered from the user.
##num = int(input("Enter a number : "))
##i = 1
##while i<=10:
##    print(num*i, end=" ")
##    i+=1

# Write a program to find the sum of all even numbers that falls between two numbers (exclusive both numbers) entered from the user using while loop.
##num1 = int(input("Enter the 1st number : "))
##num2 = int(input("Enter the 2nd number : "))
##if num1<num2:
##    while num1<num2:
##        if num1%2==0:
##            print(num1)
##        num1+=1
##else:
##    while num1<num2:
##        if num2%2==0:
##            print(num2)
##        num2+=1

##num1 = int(input("Enter first number  : "))
##num2 = int(input("Enter second number  : "))
##if num1 > num2:
##   while(num1>num2):
##     if num2 % 2 == 0:
##       print(num2)
##     num2 = num2 + 1
##else:
##   while(num1<num2):
##     if num1 % 2 == 0:
##       print(num1)
##     num1 = num1 + 1

# Write a program to check whether a number is prime or not using while loop.
##num = int(input("Enter the number  : "))
##i = 0
##while i in range(2,num):
##    if num%i!=0:
##        print("prime")
##        break
##    else:
##        print("not prime")


# take a value from user and reverse it by while loop?
##num = int(input("Enter the number : "))
##number= num
##reverse = 0
##while(num > 0):
##    reminder = num %10
##    reverse = (reverse *10) + reminder
##    num = num //10
##print("Reverse of", number, "is", reverse)


# Write a program to find the sum of the digits of a number accepted from the user.
##num = int(input("Enter the number : "))
##number = num
##sum = 0
##while num!=0:
##    rem = num%10
##    sum = sum+rem
##    num = num//10
##print("Sum of all the digit of", number, "is", sum)


# Write a program to find the product of the digits of a number accepted from the user.
##num = int(input("Enter the number : "))
##number = num
##mul = 1
##rem = 1
##while num!=0:
##    if rem>0:
##        rem = num%10
##        mul = mul*rem
##        num = num//10
##print(mul)


# Write a program to reverse the number accepted from user using while loop.
##num = int(input("Enter the number : "))
##rev = 0
##while num!=0:
##    rem = num%10
##    rev = (rev*10)+rem
##    num = num//10
##print(rev)

# Write a program to know thye length of a intiger given by user
##num = int(input("Enter the number : "))
##count = 0
##while num!=0:
##    rem = num%10
##    num = num//10
##    count = count+1
##print(count)

# Write a program to display the number names of the digits of a number entered by user, for example if the number is 231 then output should be Two Three One



# Write a program to print the factorial of a number accepted from user.
##num = int(input("Enter the number : "))
##fact = 1
##i = 1
##while i<=num:
##    fact = fact*i
##    i = i+1
##print(fact)

#  Write a program to check whether a number is Armstrong or not. (Armstrong number is a number that is equal to the sum of cubes of its digits for example : 153 = 1^3 + 5^3 + 3^3.)
##num = input("Enter any number : ")
##num1=num
##lst = list(num)
##length = len(num)
##i = 0
##mult = 1
##while i<length:
##    mult = mult+int(lst[i])**3
##    i = i+1
##if num1 == mult:
##    print("armstrong")
##else:
##    print("not a armstrong")

##num1 = input("Enter any number : ")
##p=0
##L = len(num1)
##L1 = list(num1)
##i = 0
##while(i < L):
##   p = p + int(L1[i])**3
##   i = i + 1
##if int(num1) == p:
##    print("Number is Armstrong")
##else:
##   print("Number is not Armstrong")


# Nestd For Loop
# Home Work

for i in range(1, 5):
    for j in range(1):
        print(1,2,3,4, end=' ')
    print()


