import json

USERS_FILE = "users.json"


def load_users():
    """Load all users from the JSON file."""
    with open(USERS_FILE, "r", encoding="utf-8") as file:
        users = json.load(file)
    return users


def filter_users_by_name(name):
    """Filter users by name (case-insensitive) and print matches."""
    users = load_users()

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_users_by_age(age):
    """Filter users by age and print matches."""
    users = load_users()

    filtered_users = [user for user in users if str(user["age"]) == age]

    for user in filtered_users:
        print(user)


def filter_users_by_email(email):
    """Filter users by email (case-insensitive) and print matches."""
    users = load_users()

    filtered_users = [user for user in users if user["email"].lower() == email.lower()]

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    filter_option = (
        input(
            "What would you like to filter by? "
            "('name', 'age' and 'email' is supported): ").strip().lower())

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = input("Enter a age to filter users: ").strip()
        filter_users_by_age(age_to_search)
    elif filter_option == "email":
        email_to_search = input("Enter a email to filter users: ").strip()
        filter_users_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")
