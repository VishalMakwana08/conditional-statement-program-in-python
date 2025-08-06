#  Find the largest of two numbers.

#Get Number From The User

num1=int(input("Enter First Integer Number:"))
num2=int(input("Enter Seconf Integer Number:"))


if num1>num2:
    print(f"{num1} is largest")
elif num2>num1:
    print(f"{num2} is largest")
else:
    print("Both Are Equal")