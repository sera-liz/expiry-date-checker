### 📦 Expiry Date Tracker System
 ___
 
 A simple Python-based command-line tool to help users keep track of items and their expiry dates. This system allows users to add items with expiry dates, view all stored items, and get alerts for items that are expiring within 7 days.

### 🚀 Features
___
✅ Add items with expiry dates

🔔 Get notified about items expiring within the next 7 days

📋 View a list of all items

💾 Data persistence using a JSON file (expiry_database.json)

### 🛠️ Requirements  
Python 3.x

No external libraries required — uses only built-in Python modules (json, datetime).

### 📁 File Structure

expiry_tracker.py          # Main Python script
expiry_database.json       # JSON file that stores item data (auto-created if not present)
README.md                  # This file

### 🧑‍💻 How to Use
Clone the Repository or Download the script.

Run the script using:


python expiry_tracker.py
Follow the menu options:
   

### 📦 Welcome to the Expiry Date Tracker System
MENU
1. Add item with expiry date
2. View items nearing expiry (within 7 days)
3. View all items
4. Exit
   ____
🧾 Example
Adding an Item:

<p>Enter item name: Milk
<p>Enter expiry date (YYYY-MM-DD): 2025-06-10

<p>✅ 'Milk' added with expiry date 2025-06-10
<p>Viewing Near-Expiry Items:
 ___
<p>⚠ Items nearing expiry (within 7 days):
<p>- Milk (Expires: 2025-06-10)

 
 ### 💡 Future Improvements (Suggestions)
 ____
GUI interface using Tkinter or PyQt

Notification support (email or local alert)

Batch import/export feature for large inventories

Expired items cleanup option


