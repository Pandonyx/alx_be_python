shopping_list = []

def display_menu():
    print("Shopping List Manager")
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
        print("Shopping List:")
        for item in shopping_list:
            print(item)
    else:
        print("Shopping list is empty.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(item)
        elif choice == '2':
            item = input("Enter the item to remove: ")
            remove_item(item)
        elif choice == '3':
            view_list()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
