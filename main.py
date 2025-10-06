from stats import separation_of_words, number_of_words, number_of_characters, sort_on, character_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    words = separation_of_words(text)
    num_words = number_of_words(words)
    count = number_of_characters(text)
    pairs = character_list(count)
    print(f"Found {num_words} total words")
    for item in pairs:
        ch = item["cha"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")

if __name__ == "__main__":
    main()