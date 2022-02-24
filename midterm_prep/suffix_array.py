s = 'banana'
a = sorted(range(len(s)), key=lambda i: s[i:])
print(a)