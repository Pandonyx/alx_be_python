shopping_list = []
def add_item(item):
    shopping_list.append(item)
    return f"Item '{item}' added to the shopping list."

def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        return f"Item '{item}' removed from the shopping list."
    else:
        return f"Item '{item}' not found in the shopping list."

def view_list():
    if shopping_list:
        return "Shopping List:\n" + "\n".join(shopping_list)
    else:
        return "Shopping list is empty."

