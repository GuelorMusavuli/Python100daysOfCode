
print("Welcome to the tip calculator.")

# prompt the user's total bill
bill = float(input("what was the total bill ?  $"))
tip = int(input("What percentage tip would you like to give ? 10, 12, or 15 ?"))
people = int(input("How many people to split the bill ?"))

# if the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12. The result needs to be
# rounded to 2 decimal places e.g 33.60
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
# bill_with_tip = round(bill_per_person, 2)
bill_with_tip = "{:.2f}".format(bill_per_person) # round format in string

# Similarly, the above can be shorten as follows
# bill_with_tip = tip / 100 * bill + bill    or  bill * (1 + tip /100)

print(f"Each person should pay : ${bill_with_tip}")
