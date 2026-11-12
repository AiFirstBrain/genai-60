sentence = input("Enter the sentence: ")
words = sentence.split()
print(len(words))
for word in words:
    print(word, len(word))