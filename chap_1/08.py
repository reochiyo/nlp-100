def cipher(text):
    return ''.join([chr(219 - ord(c)) if c.islower() else c for c in text])

str = "I am an NLPer"
ans = cipher(str)
ans_back = cipher(ans)
print(ans)
print(ans_back)