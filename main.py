from stats import separation_of_words, number_of_words, number_of_characters, sort_on, character_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    
    filepath = sys.argv[1]
    text = get_book_text(filepath)
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


