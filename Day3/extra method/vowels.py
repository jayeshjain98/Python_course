new = []
x = ''
name = ['adsd','evfhgi']
vowels = ['a','e','i','o','u']
for i in name:
    for j in i:
        if j in vowels:
            continue
        else:
            x = x+j
    new.append(x)
    x = ''
print(new)
