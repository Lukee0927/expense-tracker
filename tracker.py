# Laboratory 3 Installment 3: The Tracker Does Math, Author: Joshua Luke G. Raterta
print("=" * 40)
print("\t   EXPENSE TRACKER")
print("\tyour money, your rules")
print("=" * 40)

print("MAIN MENU:")
print("\t[1] Add an expense\t(coming soon)")
print("\t[2] View all expenses\t(coming soon)")
print("\t[3] Show total spent\t(coming soon)")
print("\t[4] Exit\t\t(coming soon)")

name = input("\nWhat is your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

subtotal = 0

item1 = input("\nFirst expense?: ")
amount1 = float(input("Enter the amount: "))
subtotal += amount1

item2 = input("Second expense?: ")
amount2 = float(input("Enter the amount: "))
subtotal += amount2

average = subtotal / 2

tax_percent = int(input("Enter the tax rate %: "))
tax = subtotal * (tax_percent / 100)
total = tax + subtotal

budget = float(input("Enter your budget amount: "))
over_budget = total > budget
left = budget - total

print("-" * 40)

print("\nSUMMARY")
print(f" - {item1}:\t${amount1}")
print(f" - {item2}:\t${amount2}")
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent}%):\t${tax}")
print(f"Grand total:\t${total}")
print(f"Over budget?:\t{over_budget}")
print(f"Left in budget:\t${left}\n")

print("-" * 40)
print("Made by: Joshua Luke G. Raterta | Installment 3")
