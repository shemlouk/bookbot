def read_book(filepath):
    with open(filepath) as book:
        return book.read()


def count_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    count_hash = {}

    for letter in text:
        if not letter.isalpha():
            continue

        char = letter.lower()
        count_hash[char] = 1 if char not in count_hash else count_hash[char] + 1

    letters = []

    for char in count_hash:
        letter = {"char": char, "count": count_hash[char]}
        letters.append(letter)

    letters.sort(key=lambda letter: letter["count"], reverse=True)
    return letters
