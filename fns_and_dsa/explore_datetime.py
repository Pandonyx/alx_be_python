from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date():
    try:
        num_days = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=num_days)
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Invalid input. Please enter an integer for the number of days.")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
