 ##inputs we need from the user
# total rent
# total food ordered for snacking
# electricity units spend
# charge per unit
# persons

## output
# toatal amount you've to pay is

rent = int(input("Enter the rent of flat: "))
food = int(input("Enter the spend on food: "))
electricity_spend = int(input("Enter electricity units: "))
charge_per_unit = int(input("Enter the charge per unit: "))
person = int(input("Enter the no. of personds in flat: "))

total_bill = electricity_spend*charge_per_unit

output = (food+rent+total_bill)//person

print("Each person will pay: ",output)