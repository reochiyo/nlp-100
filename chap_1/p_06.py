str1= "paraparaparadise"
str2= "paragraph"
X=set()
Y=set()

for i in range(len(str1)):
    X.add(str1[i:i+2])
for i in range(len(str2)):
    Y.add(str2[i:i+2])

print(X)
print(Y)
print(X|Y)
print(X&Y)
print(X-Y)
print('se' in X)
print('se' in Y)
