#Write a function to find the area of a circle.The value of the radius must be entered by the user.#
'''def area(r):
    area=(22/7)*r*r
    print("The area of circle is",area)
radius=int(input("Enter the value of radius "))
area(radius)'''

#Write a function pow(a,b).The function should return the value a raised to the powr of . (a^b)
'''def pow(a,b):
    return a**b
a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
new=pow(a,b)
print("The new value of a is",new)'''

#Write a function to test if a number entered by the user is Armstrong or not.#
'''def arm(a):
    sum=0
    while a>0:
        num=a%10
        sum=sum+num**3
        a//=10
    return sum
arms=int(input("Enter the armstrong number"))
Number=arm(arms)
if Number==arms:
    print("Armstrong number")
else:
    print("Not Armstrong")'''

#Write s function to check if a number is reverse of the number i.e. Palindrome#

def palindrome(n):
    rev_number=0
    while n>0:
        num = n%10
        rev_number = rev_number*10+num
        n=n//10
    return rev_number
num=int(input("Enter the number to be checked"))
check=palindrome(num)
if check==num:
    print("Palindrome ")
else:
    print("Non-palindrome")


















