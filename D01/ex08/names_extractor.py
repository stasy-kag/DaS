import sys


def main():

    if len(sys.argv) != 2:
        raise Exception("Неверное количество аргументов.")

    path = sys.argv[1]

    l = list()

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            email = line.strip()
            parts = email.split("@")[0].split(".")
            name, last = parts[0], parts[1]
            l.append((name.capitalize(), last.capitalize(), email))

    with open("employees.tsv", "w", encoding="utf-8") as tsv:
        tsv.write(f"Name\tSurname\tEmail\n")
        for i in l:
            tsv.write(f"{i[0]}\t{i[1]}\t{i[2]}\n")


if __name__ == "__main__":
    main()
