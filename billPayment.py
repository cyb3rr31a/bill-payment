# Get user input for total bill amount, tip percentage and number of people splitting the bill
total_bill = float(input("What is the total bill amount? "))
tip_percentage = int(input("What percentage tip would you like to give? (10, 12, or 15) "))
num_people = int(input("How many people are splitting the bill? "))

# Calculate tip amount and total bill with tip
tip_amount = total_bill * (tip_percentage / 100)
total_bill_with_tip = total_bill + tip_amount

# Calculate amount each person should pay
amount_per_person = total_bill_with_tip / num_people

# Display the answer rounded to two decimal points
print("Each person should pay: $%.2f" % amount_per_person)
