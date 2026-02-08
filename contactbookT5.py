# ---------------- Contact Book Application ----------------

GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

contacts = []

def print_box(message, color=GREEN):
    print(f"{color}{BOLD}")
    print("+" + "-" * (len(message) + 2) + "+")
    print(f"| {message} |")
    print("+" + "-" * (len(message) + 2) + "+")
    print(RESET)

def add_contact():
    print_box("ADD NEW CONTACT", CYAN)
    name = input("Enter Name    : ")
    phone = input("Enter Phone   : ")
    email = input("Enter Email   : ")
    address = input("Enter Address : ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    print_box("Contact Added Successfully ✔", GREEN)

def view_contacts():
    print_box("CONTACT LIST", BLUE)

    if not contacts:
        print(f"{RED}No contacts available.{RESET}")
        return

    for i, c in enumerate(contacts, start=1):
        print(f"\n{YELLOW}Contact {i}{RESET}")
        print("Name    :", c["name"])
        print("Phone   :", c["phone"])
        print("Email   :", c["email"])
        print("Address :", c["address"])

def search_contact():
    print_box("SEARCH CONTACT", CYAN)
    key = input("Enter name or phone: ")

    for c in contacts:
        if key.lower() in c["name"].lower() or key in c["phone"]:
            print_box("Contact Found ✔", GREEN)
            print("Name    :", c["name"])
            print("Phone   :", c["phone"])
            print("Email   :", c["email"])
            print("Address :", c["address"])
            return

    print_box("Contact Not Found ✖", RED)

def update_contact():
    print_box("UPDATE CONTACT", CYAN)
    phone = input("Enter phone number to update: ")

    for c in contacts:
        if c["phone"] == phone:
            name = input("New Name (leave blank to skip): ")
            email = input("New Email (leave blank to skip): ")
            address = input("New Address (leave blank to skip): ")

            if name:
                c["name"] = name
            if email:
                c["email"] = email
            if address:
                c["address"] = address

            print_box("Contact Updated Successfully ✔", GREEN)
            return

    print_box("Contact Not Found ✖", RED)

def delete_contact():
    print_box("DELETE CONTACT", CYAN)
    phone = input("Enter phone number to delete: ")

    for c in contacts:
        if c["phone"] == phone:
            contacts.remove(c)
            print_box("Contact Deleted Successfully ✔", GREEN)
            return

    print_box("Contact Not Found ✖", RED)

# ---------------- Main Menu ----------------
while True:
    print(f"""
{GREEN}{BOLD}
╔════════════════════════════╗
║        CONTACT BOOK        ║
╚════════════════════════════╝
{RESET}
{CYAN}{BOLD}1.{RESET} Add Contact
{BLUE}{BOLD}2.{RESET} View Contacts
{YELLOW}{BOLD}3.{RESET} Search Contact
{GREEN}{BOLD}4.{RESET} Update Contact
{RED}{BOLD}5.{RESET} Delete Contact
{BOLD}6.{RESET} Exit
""")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print_box("Thank you for using Contact Book ✔", GREEN)
        break
    else:
        print_box("Invalid Choice! Try Again ✖", RED)
