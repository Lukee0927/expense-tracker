# Laboratory 2 Installment 2: Talking to the User, Author: Joshua Luke G. Raterta
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

item1 = input("\nFirst expense?: ")
amount1 = float(input("Enter the amount: "))

item2 = input("Second expense?: ")
amount2 = float(input("Enter the amount: "))

total = amount1 + amount2
average = total / 2

print("-" * 40)

print("\nSUMMARY")
print(f" - {item1}:\t${amount1}")
print(f" - {item2}:\t${amount2}")
print(f"Total spent:\t${total}")
print(f"Average:\t${average}\n")

print("-" * 40)
print("Made by: Joshua Luke G. Raterta | Installment 2")
