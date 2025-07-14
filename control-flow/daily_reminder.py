task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

reminder = f"'{task}' is a {priority} priority task"

match priority:
    case "high":
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += "."
    case "medium":
        if time_bound == "yes":
            reminder += " that should be completed soon."
        else:
            reminder += ". Try to get it done today."
    case "low":
        if time_bound == "yes":
            reminder += " that you should try to do today."
        else:
            reminder += ". Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority level entered."

print("Reminder:", reminder)
