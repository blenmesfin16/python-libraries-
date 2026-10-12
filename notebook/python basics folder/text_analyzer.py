# Preset paragraph to analyze
sentence = "python is a powerful programming language that is easy to learn and fun to write"

# Splitting the string into a list of individual words
all_words = sentence.split()
long_words = []

# Loop to filter and sort text data
for word in all_words:
    if len(word) >= 4:
        long_words.append(word)

# Output summary data
print("--- Text Summary Report ---")
print(f"Original text: '{sentence}'")
print(f"Total word count: {len(all_words)}")
print(f"Words with 4+ letters: {len(long_words)}")
print(f"Filtered word list: {long_words}")
