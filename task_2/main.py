def parse_input(user_input):
    norm_str = user_input.strip().lower()
    if norm_str.startswith("phone username"):
        cmd = "phone username"
        user_input_res = user_input[14:].strip()
    elif norm_str.startswith("add username phone"):
        cmd = "add username phone"
        user_input_res = user_input[18:].strip()
    elif norm_str.startswith("change username phone"):
        cmd = "change username phone"
        user_input_res = user_input[21:].strip()
    else:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args
    *args , = user_input_res.split()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return "Contact already exists"
    else:
        contacts[name] = phone
        return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else:
        return "Contact does not exists"

def get_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact does not exists"

def get_all(contacts):
    res = ""
    if len(contacts) == 0:
         res = "no contacts"
    else:
        i = 1
        for name, number in contacts.items():
            if i < len(contacts):
                res += f"{name}: {number}\n"
                i += 1
            else:
                res += f"{name}: {number}"
    return res

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add username phone":
            print(add_contact(args, contacts))

        elif command == "change username phone":
            print(change_contact(args, contacts))

        elif command == "phone username":
            print(get_phone(args, contacts))

        elif command == "all":
            print(get_all(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()