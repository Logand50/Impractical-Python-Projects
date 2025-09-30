"""Pig Latin Translator - Logan Dye"""

import sys

VOWELS = ('A', 'E', 'I', 'O', 'U')

def main():
    """Translate input to pig latin."""
    print("Welcome to the pig latin translator!")
    while True:
        original_word = input("Please enter a word to be translated: ")

        for vowel in VOWELS:
            if original_word.upper().startswith(vowel):
                translated_word = original_word + "way"
            else:
                translated_word = original_word[1:] + original_word[0] + "ay"
        print(f"{translated_word}", file=sys.stderr)

        try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
        if try_again.lower() == 'n':
            break

    input("\nPress Enter to exit.")

if __name__ == "__main__":
    main()
