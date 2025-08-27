import sys
from stats import count_words, count_characters, sort_characters

def get_book_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        return f.read()

def main():
    # ✅ Step 1: Check for correct usage
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # ✅ Step 2: Take book path from CLI
    book_path = sys.argv[1]

    # ✅ Step 3: Read text
    text = get_book_text(book_path)

    # ✅ Step 4: Word count
    num_words = count_words(text)

    # ✅ Step 5: Character counts (sorted)
    char_counts = count_characters(text)
    sorted_chars = sort_characters(char_counts)

    # ✅ Step 6: Print report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        ch = item["char"]
        if ch.isalpha():  # skip non-letters
            print(f"{ch}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()

