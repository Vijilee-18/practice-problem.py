total_amount=int(input("enter the total amount for the order:"))
if total_amount>=500:
    print("shipping is free:")
    total=total_amount+0
    print(f"Total for the shopping is\t{total}""$")
elif total_amount<50 or total_amount>=20:
    print("shipping charge cost's $5:")
    total=total_amount+5
    print(f"Total for the shopping is\t{total}""$")
elif total_amount<20:
    print("shipping charge cost's $10:")
    total=total_amount+10
    print(f"Total for the shopping is\t{total}""$")

