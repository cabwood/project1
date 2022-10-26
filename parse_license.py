import re

RE_WORD = re.compile(r"[a-zA-Z-]+")

find_words = [
    "copyright",
    "the",
    "a",
]

word_counts = {}

for word in find_words:
    word_counts[word] = 0

copyright_count = 0

def parse(ln):
    global copyright_count
    words = RE_WORD.findall(ln)
    for word in words:
        try:
            num = int(word)
        except:
            pass
        else:
            print(" There was a number: ", num)
        lword = word.lower()
        for search_word in find_words:
            if search_word == lword:
                word_counts[search_word] += 1

f = open("LICENSE", "r")
try:
    lines = f.readlines()
    for line in lines:
        parse(line)
finally:
    f.close()

for word, count in word_counts.items():
    print(f'There were {count} occurrences of the word {word}')
