# Check if a person is eligible to vote (age >= 18).

#Get Age From The User

age=int(input("Enter Your Age:"))

if age>=18:
    print("You Are Eligible For Vote")
elif age<1:
    print("You Entered Invalid Age")
else:
    print("You Are Not Eligible for Vote")