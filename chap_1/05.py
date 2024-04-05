def n_gram(n, text):
    char = text.replace(' ', '')
    word = text.split(' ')
    ans_char = []
    ans_word = []
    for i in range(len(char)):
        ans_char.append(char[i:i+n])
    for i in range(len(word)):
        ans_word.append(word[i:i+n])
    return ans_char, ans_word

str = "I am an NLPer"
char, word = n_gram(2, str)
print(char)
print(word)



