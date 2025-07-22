shopping_list = []

def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item(item):
    shopping_list.append(item)
    print(f"Item '{item}' added to the shopping list.")

def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"Item '{item}' removed from the shopping list.")
    else:
        print(f"Item '{item}' not found in the shopping list.")

def view_list():
    if shopping_list:
        print("\nShopping List:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")
    else:
        print("\nShopping list is empty.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item:  # only add non-empty item
                add_item(item)
            else:
                print("Item name cannot be empty.")
        elif choice == '2':
            item = input("Enter the item to remove: ").strip()
            if item:
                remove_item(item)
            else:
                print("Item name cannot be empty.")
        elif choice == '3':
            view_list()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
