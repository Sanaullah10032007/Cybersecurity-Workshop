
users = {
    "016": {"name": "sanaullah", "age": 21, "department": "CSE", "email": "sana@example.com"},
    "007": {"name": "Muhammad Ahmed", "age": 21, "department": "CSE", "email": "ahmed@example.com"},
    "024": {"name": "ekta", "age": 20, "department": "CSE", "email": "ekta@example.com"},
    "017": {"name": "mahnoor", "age": 19, "department": "CSE", "email": "mahnoor@example.com"},
}


user_id = input("Enter User ID: ")


if user_id in users:
    print("\n--- User Profile ---")
    for key, value in users[user_id].items():
        print(f"{key.capitalize()}: {value}")
else:
    print("Invalid User ID! Please try again.")
