str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
ans = {}
for i, word in enumerate(str.split(), 1):
    if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        ans[word[0]] = i
    else:
        ans[word[:2]] = i
print(ans)