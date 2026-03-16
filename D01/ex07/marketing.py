import sys


def main():
    clients = [
        "andrew@gmail.com",
        "jessica@gmail.com",
        "ted@mosby.com",
        "john@snow.is",
        "bill_gates@live.com",
        "mark@facebook.com",
        "elon@paypal.com",
        "jessica@gmail.com",
    ]
    participants = [
        "walter@heisenberg.com",
        "vasily@mail.ru",
        "pinkman@yo.org",
        "jessica@gmail.com",
        "elon@paypal.com",
        "pinkman@yo.org",
        "mr@robot.gov",
        "eleven@yahoo.com",
    ]
    recipients = ["andrew@gmail.com", "jessica@gmail.com", "john@snow.is"]

    if len(sys.argv) != 2:
        raise Exception("Неверное количество аргументов.")

    clients = set(clients)
    participants = set(participants)
    recipients = set(recipients)

    if sys.argv[1] == "call_center":
        for email in sorted(clients - recipients):
            print(email)
    elif sys.argv[1] == "potential_clients":
        for email in sorted(participants - clients):
            print(email)
    elif sys.argv[1] == "loyalty_program":
        for email in sorted(clients - participants):
            print(email)
    else:
        raise Exception(f"Invalid task name: {sys.argv[1]}. ")


if __name__ == "__main__":
    main()
