d = {1:11, 2:22, 3:33}
k = list(d.keys ())
v = list(d.values ())
i = 0
while i< len(k): d[v[i]]=k[i]; del d[k[i]]; i = i+1
