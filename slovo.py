def longest_word(file):
    f = open(file, encoding="utf-8")
    words = f.read().split()
    max_lenght = len(max(words, key=len))
    longest_words = []
    wordslen = len(words)
    for i in range(wordslen):
        long_word = min(words, key=len)
        longest_words.append(long_word)
        words.remove(long_word)
        longlen = len(longest_words)
    for i in range (longlen):
        word_len = len(longest_words[i])
        if word_len == max_lenght:
            print(longest_words[i])

longest_word('article.txt')