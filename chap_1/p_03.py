str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
ans = []
for i in str.split():
    if i[-1] in [",", "."]:
        ans.append(len(i)-1)
    else:
        ans.append(len(i))
print(ans)