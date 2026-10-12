text = "apple banana apple cherry banana apple"
words = text.split()

word_counts = {}

for word in words:
    # .get(word, 0) checks if the word exists, or defaults to 0
    word_counts[word] = word_counts.get(word, 0) + 1

print("Word Breakdown:")
print(word_counts)
