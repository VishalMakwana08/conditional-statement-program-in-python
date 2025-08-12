# Electricity bill calculator:

# Up to 100 units: ₹1.5/unit

# 101–200: ₹2/unit

# 201–300: ₹3/unit

# Above 300: ₹5/unit + ₹100 fixed charge

units=int(input("Enter Used Units:"))
fixed_charge=100


if units>0:
    if units<=100:
        total_bill=units*1.5+fixed_charge
    elif units<=200:
        total_bill=units*2+fixed_charge
    elif units<=300:
        total_bill=units*3+fixed_charge
    else:
        total_bill=units*5+fixed_charge
    print(f"Your Total Electricity Bill Is {total_bill}$")

        

else:
    print("Negative Units Are Not Allowed")