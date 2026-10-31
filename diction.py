sentence = "Python is easy and Python is powerful"

# Split the sentence into words and ignore case
words = sentence.lower().split()

# Count how many times each word occurs
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

# Find the longest word
longest_word = max(words, key=len)

# Display the results
print("Number of Words :", len(words))
print("Longest Word :", longest_word)

print("\nWord Frequency:")
for word, count in frequency.items():
    print(f"{word} : {count}")

print("\nRepeated Words:")
for word, count in frequency.items():
    if count > 1:
        print(word)