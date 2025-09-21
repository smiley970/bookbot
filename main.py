from stats import splitter
from stats import number
from stats import list_dict
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
      
    text = get_book_text(sys.argv[1])
    count = splitter(text)
    char_dict = number(text)
    sorted_chars = list_dict(char_dict)
    
    print("============ BOOKBOT ============")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    
    for item in sorted_chars:
        ch = item["char"]
        if not ch.isalpha():
            continue
        print(f"{ch}: {item['num']}")
    
    print("============= END ===============")

if __name__ == "__main__":
    def fix():
        if len(sys.argv) == 1:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
        else:
            return main()
    fix()        


