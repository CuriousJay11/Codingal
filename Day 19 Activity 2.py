def match_words(words):
    ctr = 0
    lst = []
    for i in words:
        if len(i) > 1 and i[0] == i[-1]:
            ctr += 1
            lst.append(i)

    print("List of words with first and last character same:\n", lst)
    return ctr

# Test list of words
words = ['abc', 'cfc', 'xyz', 'aba', '1221', '3883', '7654']

result = match_words(words)
print("Number of words having first and last character same:", result)