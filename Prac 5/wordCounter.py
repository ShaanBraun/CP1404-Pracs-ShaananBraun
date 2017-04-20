sentence = input("Your sentence: ")

wordCounts = {}
words = sentence.split()

for word in words:
    if word in wordCounts:
        wordCounts[word] += 1
    else:
        wordCounts[word] = 1

max_word_length = max(len(x) for x in wordCounts)
for word in sorted(wordCounts.keys()):
    print("{:{}} : {}".format(word, max_word_length, wordCounts[word]))
