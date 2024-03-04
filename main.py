def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, SyntaxError):
            return "Give me name and phone please."
        except IndentationError:
            return "Please use spaces to separate your command, name and phone"

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} changed."


@input_error
def get_phone(args, contacts):
    name = args[0]
    phone = contacts[name]
    return f"Phone number of contact '{name}' is {phone}."


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

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(get_phone(args, contacts))

        elif command == "all":
            [print(f"{key}: {value},") for key, value in contacts.items()]

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
