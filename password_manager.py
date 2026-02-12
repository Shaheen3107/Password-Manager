import json
import os

DATA_FILE = "password_manager.json"

# load and save json data 
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        text = f.read().strip()
        
        if text:
            return json.loads(text)
        else:
            return {}
        
def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def add_password():
    website = input("Enter website or app name : ").strip()
    if not website:
        print("Website cannot be empty")
        return
    
    username = input("Enter Username/Email : ").strip()
    password = input("Enter password : ").strip()

    data = load_data()

    if website in data:
        confirm = input(f"{website} already exist! Do you want to overwrite? yes or no : ").strip().lower()
        if confirm != "yes":
            print("Add cancelled")
            return
    data[website] = {"username" : username, "password" : password}
    save_data(data)
    print(f"saved entry for {website}")

def view_password():
    data = load_data()
    if not data:
        print("No password is saved.")
        return
    
    print("-----Saved Passwords----")
    for site,info in data.items():
        print(f"\n  website : {site}")
        print(f" username: {info['username']}")
        print(f" password : {info['password']}")

def search_password():
    site = input("Enter website or app name to search : ").strip()
    if not site:
        print("Site can not be empty")
        return
    
    data = load_data()
    entry = data.get(site)
    if entry:
        print(f"Fount entry for {site}")
        print(f"username : {entry['username']}")
        print(f"password : {entry['password']}")
    else:
        print("No entry found")

def update_password():
    site = input("Enter website or app name to update : ").strip()
    if not site:
        print("Website cannot be empty")    
        return
    
    data = load_data()
    if site not in data:
        print("No entry found for {site}")
        return
    
    current = data[site]
    new_username = input("Enter new username to update : ").strip()
    new_password = input("Enter new password to update : ").strip()

    if new_username:
        current['username'] = new_username
    if new_password:
        current['password'] = new_password

    data[site] = current
    save_data(data)
    print(f"Entry updated successfully for {site}")

def delete_password():
    site = input("Enter website or app name to delete : ").strip()
    if not site:
        print("Website cannot be empty")    
        return
    
    data = load_data()
    if site in data:
        entry = input(f"Are you sure you want to delete {site} ? yes or no : ").strip()
        if entry == "yes":
            del data[site]
            save_data(data)
            print(f"{site} Deleted")
        else:
            print("Delete cancelled.")
        
    else:
        print(f"No entry found for {site}")

def main():
    while True:
        print("--------Password Manager-------")
        print("1. Add Password")
        print("2. View Password")
        print("3. Search Password")
        print("4. Update Password")
        print("5. Delete Password")
        print("6. Exit")

        choice = input("Enter choice 1-6) : ")
        if choice == "1":
            add_password()
        elif choice == "2":
            view_password()
        elif choice == "3":
            search_password()
        elif choice == "4":
            update_password()
        elif choice == "5":
            delete_password()
        elif choice == "6":
            print("Exiting! GoodBye")
            break
        else:
            print("Invalid choice! enter (1-6)")

if __name__ == "__main__":
    main()      


    