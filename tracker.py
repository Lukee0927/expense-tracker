# Laboratory 5 Installment 5: The Menu Comes Alive, Author: Joshua Luke G. Raterta
print("=" * 40)
print("\t   EXPENSE TRACKER")
print("\tyour money, your rules")
print("=" * 40)

name = input("\nWhat is your name? ")
tax_percent = int(input("Enter the tax rate %: "))
budget = float(input("Enter your budget amount: "))
print(f"\nWelcome, {name}!")

subtotal = 0
count = 0

while True:
    print("\nMAIN MENU:")
    print("\t[1] Add an expense")
    print("\t[2] View all expenses\t(coming soon)")
    print("\t[3] Show total spent")
    print("\t[4] Exit")
    choice = input("\nChoose 1-4: ")

    if choice == "1":
        amount = float(input("\nEnter the amount: "))
        subtotal += amount
        count += 1
        
        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")
    
    elif choice == "2":
        print("  Coming soon: the tracker can't remember each item yet.")
   
    elif choice == "3":
        tax = subtotal * (tax_percent / 100)
        total = subtotal + tax
        over_budget = total > budget
        left = budget - total

        print("-" * 40)
        print("SUMMARY")
        print(f"Expenses:\t{count}")
        print(f"Subtotal:\t${subtotal}")
        print(f"Tax ({tax_percent}%):\t${tax}")
        print(f"Grand total:\t${total}")

        if over_budget:
            print(f"Over budget by ${total - budget}!")
        elif total > budget * 0.9:
            print(f"Careful: only ${left} left.")
        else:
            print(f"Within budget. ${left} left.")
        print("-" * 40)
    
    elif choice == "4":
        print(f"Goodbye, {name}!\n")
        print("-" * 40)
        print("Made by: Joshua Luke G. Raterta | Installment 5")
        break
    
    else:
        print("  Please choose 1, 2, 3 or 4.")