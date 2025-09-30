"""Finding Palingram Spells"""
import sys

WORDS_FILE = "2) Finding Palingram Spells/words.txt"

def transform(file):
    

    return [x.lower() for x in transformed_text]


def load(file):
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError Opening {}. Terminating program.".format(e, WORDS_FILE), file=sys.stderr)
        sys.exit(1)


def main():
    words = load(WORDS_FILE)
    for word in words:
        if len(word) > 1 and word == word[::-1]:
            print(word)
    q=0
    for word in words:
        if len(word) > 1:
            for i in range(len(words)):
                if word + words[i] == words[i][::-1] + word[::-1] and len(words[i]) > 1:
                    q+=1
                    print(str(q) + ") " + word + " " + words[i])

if __name__ == "__main__":
    main()
