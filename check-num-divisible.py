# Check whether a number is divisible by 5 or not.

#get a number from the user

num=int(input("Enter Any Integer Number:"))

if num%5==0:
    print(f"Yes {num} is divisible by 5")
else:
    print(f"No {num} is not divisible by 5")