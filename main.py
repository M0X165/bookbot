def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def separation_of_words(text):
    return text.split()

def number_of_words(words):
    return len(words)

def main():
    text = get_book_text("books/frankenstein.txt")
    words = separation_of_words(text)
    num_words = number_of_words(words)
    print(f"Found {num_words} total words")

if __name__ == "__main__":
    main()