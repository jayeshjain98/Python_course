import string
alpha = string.ascii_lowercase
str1 = raw_input("enter any string:").lower()
str2 = str1.lower()
empty_str = ''
c = 0
for i in str1:
    for j in alpha:
        if i == j and i not in empty_str:
            empty_str += i
for i in empty_str:
    for j in alpha:
        if i == j:
            c += 1

if c ==26:
    print 'Pangram'
else:
    print 'NotPangram'
        

    
    
