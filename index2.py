num = int(input("Enter number to double check: "))

if num>50:
    print("Your number is greater than 50! ")
elif num==50:
    print("Your number is equal to 50! ")
    if num%2==0:
        print("And ur number is even")
    else:
        print("And ur number is odd")
else:
    print("Number is less than 50! ")