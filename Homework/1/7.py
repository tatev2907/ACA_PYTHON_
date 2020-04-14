
sentence = input("Input sentence: ")
words = sentence.split()
counts = {}
for word in words:
    if word.lower() not in counts:
        counts[word.lower()] = 0
    counts[word.lower()] += 1
print(counts)

print("".join((char if char.isalpha() else " ") for char in sentence).split())
