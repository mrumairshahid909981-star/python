inventory = {
}
while True:
    print("\n1. Add items")
    print("2. item quantity")
    print("3. Exit")
    print("4. Display items")
    choice = input("Enter your choice: ")
    if choice == "1":
        item =input("enter item name: ")
        quality = int(input("enetr item quality: "))
        inventory[item] = quality
        again= input("Do you want to add another item? (6/0): ")
        if again != "6":
            break
    elif choice == "2":
        print(inventory)
    elif choice == "3":
        print("Exiting...")
        break
    elif choice == "4":
        if not inventory:
            print("Inventory is empty.")
        else:
            print("Items in inventory:")
            for item, quality in inventory.items():
                print(f"{item}: {quality}")
    else: 
        print ("Invalid choice. Please try again.")
    