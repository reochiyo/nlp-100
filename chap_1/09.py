import random

def typoglycemia(text):
    words = text.split(' ')
    ans = []
    for word in words:
        if len(word) <= 4:
            ans.append(word)
        else:
            head = word[0]
            tail = word[-1]
            body = word[1:-1]
            body = random.sample(body, len(body))
            ans.append(head + ''.join(body) + tail)
    return ' '.join(ans)

str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
ans = typoglycemia(str)
print(ans)