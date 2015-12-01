d = {}
for index, element in enumerate('abcdefgijhklmnopqrstuvwxyz'):
    d[index] = element
w = list(raw_input('Enter word: '))
k = int(raw_input('Enter shift: '))
for i in xrange(len(w)):
    for j in xrange(len(d.keys())):
        if w[i] == d[d.keys()[j]]:
            if j+k>=len(d.keys()):
                w[i]=d[d.keys()[j+k-len(d.keys())]]
            else:
                w[i]=d[d.keys()[j+k]]
            break              
print(''.join(w))
