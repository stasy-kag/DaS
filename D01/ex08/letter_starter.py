import sys


def main():

    if len(sys.argv) != 2:
        raise Exception("Неверное количество аргументов.")

    email_search = sys.argv[1]
    found = False

    with open("employees.tsv", "r", encoding="utf-8") as tsv:
        next(tsv)
        for line in tsv:
            name, surname, email = line.strip().split("\t")

            if email_search == email:
                print(
                    f"Dear {name}, welcome to our team! We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires."
                )
                found = True
    if not found:
        print("Email not found.")


if __name__ == "__main__":
    main()
