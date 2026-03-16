def csv_to_tsv(input="ds.csv", output="ds.tsv"):
    with open(input, "r", encoding="utf-8") as csv, open(
        output, "w", encoding="utf-8"
    ) as tsv:
        for line in csv:
            tsv.write(parse(line))


def parse(line):
    result = []
    quot = False

    for ch in line:
        if ch == '"':
            quot = not quot
            result.append(ch)
        elif ch == "," and not quot:
            result.append("\t")
        else:
            result.append(ch)
    return "".join(result)


if __name__ == "__main__":
    csv_to_tsv()
