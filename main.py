import stats


def print_section_name(name, fill_char="-", width=33):
    content = name.center(len(name) + 2, " ")
    print(f"{content:{fill_char}^{width}}")


def main():
    print_section_name("BOOKBOT", "=")
    print("Analyzing book found at books/frankenstein.txt...")

    filename = "./books/frankenstein.txt"
    text = stats.read_book(filename)

    print_section_name("Word Count")
    print(f"Found {stats.count_words(text)} total words")

    print_section_name("Character Count")
    letters_count = stats.count_letters(text)

    for letter in letters_count:
        print(f"{letter['char']}: {letter['count']}")

    print_section_name("END", "=")


main()
