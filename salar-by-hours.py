# Write a program that takes hours worked and wage per hour and calculates salary:

# If hours > 40, pay overtime (1.5×).


# Input: hours worked and wage per hour
hours = float(input("Enter total hours worked: "))
wage_per_hour = float(input("Enter wage per hour: "))

# Normal and overtime calculation
if hours > 40:
    # First 40 hours at normal rate
    normal_pay = 40 * wage_per_hour
    # Overtime hours at 1.5× rate
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * wage_per_hour * 1.5
    total_salary = normal_pay + overtime_pay
else:
    # No overtime
    total_salary = hours * wage_per_hour

# Output
print(f"Total salary: ₹{total_salary:.2f}")
