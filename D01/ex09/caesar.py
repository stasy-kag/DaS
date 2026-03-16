import sys


def main():

    if len(sys.argv) != 4:
        raise Exception("Неверное количество аргументов.")

    func = sys.argv[1]
    text = sys.argv[2]
    shift = sys.argv[3]

    for i in text:
        if i.isalpha() and ord(i.lower()) not in range(97, 123):
            print("The script does not support your language yet.")

    try:
        shift = int(shift)
    except ValueError:
        raise Exception("Shift must be integer.")

    if func in ("decode", "encode"):
        print(decode_encode(text, shift, func))
    else:
        raise Exception("Invalid function (encode/decode)")


def decode_encode(text, shift, func):
    char_en = [chr(i) for i in range(97, 123)]
    out = ""
    for i in text:
        if i.isalpha() and i.islower():
            if func == "encode":
                out += char_en[(char_en.index(i) + shift) % 26]
            elif func == "decode":
                out += char_en[(char_en.index(i) - shift) % 26]
        elif i.isalpha() and i.isupper():
            if func == "encode":
                out += char_en[(char_en.index(i.lower()) + shift) % 26].upper()
            elif func == "decode":
                out += char_en[(char_en.index(i.lower()) - shift) % 26].upper()
        else:
            out += i
    return out


if __name__ == "__main__":
    main()
