print("Which ride would you like to select: ")
print("1-Bike")
print("2-Car")
choice = int(input("Enter 1 or 2"))
if choice == 1:
    print("Would you like a: ")
    print("1-scooty")
    print("2-scooter")
    choice_2 = int(input("Enter 1 or 2"))
    if choice_2 == 1:
        print("Enjoy your scooty")
    else:
        print("Enjoy your scooter")
elif choice == 2:
    print("Would you like a: ")
    print("1- Sedan")
    print("2- SUV")
    choice_3 = int(input("Enter 1 or 2"))
    if choice_3 == 1:
        print("Enjoy your sedan")
    else:
        print("Enjoy your SUV")
else:
    print("Wrong Choice!")
