import json
from datetime import datetime, timedelta

database = "expiry_database.json"

def load_database():
    try:
        with open(database, "r") as file:                                                                                                                                                                       
            return json.load(file)
    except FileNotFoundError:
        return []

def save_database(data):
    with open(database, "w") as file:
        json.dump(data, file, indent=4)


def show_menu():
    print("\n📦 Welcome to the Expiry Date Tracker System")
    print("MENU")
    print("1. Add item with expiry date")
    print("2. View items nearing expiry (within 7 days)")
    print("3. View all items")
    print("4. Exit")


def add_item(data):
    item_name = input("Enter item name: ")
    expiry_str = input("Enter expiry date (YYYY-MM-DD): ")
    try:
        expiry_date = datetime.strptime(expiry_str, "%Y-%m-%d").date()
        data.append({
            "item": item_name,
            "expiry_date": expiry_str
        })
        save_database(data)
        print(f"✅ '{item_name}' added with expiry date {expiry_str}")
    except ValueError:
        print("❌ Invalid date format. Please use YYYY-MM-DD.")

def view_near_expiry_items(data):
    today = datetime.today().date()
    warning_date = today + timedelta(days=7)
    near_expiry_items = [
        item for item in data
        if today <= datetime.strptime(item["expiry_date"], "%Y-%m-%d").date() <= warning_date
    ]

    if near_expiry_items:
        print("\n⚠ Items nearing expiry (within 7 days):")
        for item in near_expiry_items:
            print(f"- {item['item']} (Expires: {item['expiry_date']})")
    else:
        print("\n✅ No items nearing expiry within 7 days.")

def view_all_items(data):
    if not data:
        print("📭 No items in the database.")
        return

    print("\n📋 All Items:")
    for item in data:
        print(f"- {item['item']} (Expiry Date: {item['expiry_date']})")

# Main loop
data = load_database()
user_input = ""

while user_input != "4":
    show_menu()
    user_input = input("Enter your choice: ")

    if user_input == "1":
        add_item(data)
    elif user_input == "2":
        view_near_expiry_items(data)
    elif user_input == "3":
        view_all_items(data)
    elif user_input == "4":
        print("👋 Exiting... Stay ahead of expiry dates!")
    else:
        print("❌ Invalid option. Please choose from the menu.")
