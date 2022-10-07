def is_substring(s1, s2) -> bool:
    return s1 in s2


def main() -> None:
    s1 = "waterbottle"
    s2 = "erbottlewat"

    result = is_substring(s1, s2 + s2)
    print(result)


if __name__ == "__main__":
    main()
