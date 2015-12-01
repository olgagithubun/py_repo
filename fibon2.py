i = 1
f = [1,1]
while len(str(f[i]))<1000:
    i = i+1
    f.append (f[i-1]+f[i-2])
print(f[len(f)-1])
