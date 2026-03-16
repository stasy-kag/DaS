def data_types():
    a, b, c, d, e, f, g, h = (
        7,
        "error",
        3.14,
        False,
        [1, 2, 3],
        {"Python": "Гвидо ван Россум"},
        (4, 5, 1),
        {4, 6, 8},
    )

    my_list = [a, b, c, d, e, f, g, h]

    l = [type(i).__name__ for i in my_list]
    print(f"[{', '.join(l)}]")


if __name__ == "__main__":
    data_types()
