"""
Word Occurrences
Estimate: 30 minutes
Actual:   48 minutes
"""
word_to_count = {}

text = input("Text: ")
words = text.split()

for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
longest_word = max(len(word) for word in word_to_count)

for word, number in sorted(word_to_count.items()):
    # print(f"{word:<11}: {number}")
    print(f"{word:{longest_word}} : {number}")
