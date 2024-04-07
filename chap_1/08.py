#Way1
def cipher(text):
    return ''.join([chr(219 - ord(c)) if c.islower() else c for c in text])

str = "I am an NLPer"
ans = cipher(str)
ans_back = cipher(ans)
print(ans)
print(ans_back)

#Way2
def cipher2(text):
    result = ''
    for c in text:
        if c.islower():
            result += chr(219 - ord(c))
        else:
            result += c
    return result

ans2 = cipher2(str)
ans2_back = cipher2(ans2)
print(ans2)
print(ans2_back)