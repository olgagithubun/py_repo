i = 1
f = [1,1]
while i<100000:
    i = i+1
    f.append (f[i-1]+f[i-2])
print(len(str(f[i-1])))
