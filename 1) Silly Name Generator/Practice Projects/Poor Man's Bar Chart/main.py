"""Bar chart showing letters used in a sentence"""
import pprint
from collections import defaultdict

def main():
    """Ask a sentence and add it to a defaultdict then print."""
    print("Poor Man's Bar Chart.")

    while True:
        d = defaultdict(list)
        sentence = input("Please enter a sentence to be displayed.\n")
        for letter in sentence:
            d[letter].append(letter)

        pprint.pprint(d)

        try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
        if try_again.lower() == 'n':
            break

    input("\nPress Enter to exit.")

if __name__ == "__main__":
    main()
