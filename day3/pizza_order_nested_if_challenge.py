# This is an automatic pizza order program.
# It will work out the user's final bill based on their order.
# S = $15, M = $20, L = $25, pepperoni for S = 2, pepperoni for M and L = $3, extra cheese for any size =$1

print("Welcome to Pizza Deliveries!")
size = input("What size of Pizza do you want ? S, M, or L")
add_pepperoni = input("Do you want pepperoni ? Y or N")
extra_cheese = input("Do you want extra cheese ? Y or N")
bill = 0

if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
    elif extra_cheese == "Y":
        bill += 1
    else:
        bill
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
    elif extra_cheese == "Y":
        bill += 1
    else:
        bill

else :
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
    elif extra_cheese == "Y":
        bill += 1
    else:
        bill


# OR the nested if could be done as follows
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is {bill}")





