# Laboratory 4 Installment 4: The Tracker Makes Decisions, Author: Joshua Luke G. Raterta
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
if amount1 > 200:
    print(" Huge expense - are you sure?")
elif amount1 > 100:
    print(" Big expense.")
elif amount1 > 50:
    print(" Moderate expense.")
else:
    print(" Small expense.")

item2 = input("Second expense?: ")
amount2 = float(input("Enter the amount: "))
subtotal += amount2
if amount2 > 200:
    print(" Huge expense - are you sure?")
elif amount2 > 100:
    print(" Big expense.")
elif amount2 > 50:
    print(" Moderate expense.")
else:
    print(" Small expense.")

if amount1 > 100 and amount2 > 100:
    print("Two big expenses in a row - slow down!")

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

if over_budget:
    print(f"Over budget by ${total - budget}!\n")
elif total > budget * 0.9:
    print(f"Careful: only ${left} left.\n")
else:
    print(f"Within budget. ${left} left.\n")

print("-" * 40)
print("Made by: Joshua Luke G. Raterta | Installment 4")