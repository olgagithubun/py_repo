i = 1
f = [1,1]
while f[i]<10000000:
    i = i+1
    f.append (f[i-1]+f[i-2])
print(f[len(f)-1])
