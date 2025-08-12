# Find whether a given year is a century leap year

# Input: year
year = int(input("Enter a year: "))

# Check if it's a century leap year
if year % 100 == 0 and year % 400 == 0:
    print(f"{year} is a Century Leap Year")
else:
    print(f"{year} is NOT a Century Leap Year")
