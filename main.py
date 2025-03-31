import stats
import sys


def print_section_name(name, fill_char="-", width=33):
    content = name.center(len(name) + 2, " ")
    print(f"{content:{fill_char}^{width}}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    print_section_name("BOOKBOT", "=")
    print(f"Analyzing book found at {filepath}...")

    text = stats.read_book(filepath)

    print_section_name("Word Count")
    print(f"Found {stats.count_words(text)} total words")

    print_section_name("Character Count")
    letters_count = stats.count_letters(text)

    for letter in letters_count:
        print(f"{letter['char']}: {letter['count']}")

    print_section_name("END", "=")


main()
