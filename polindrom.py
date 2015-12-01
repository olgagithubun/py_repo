text = raw_input('enter word ')
t = list(text)
r = t[::-1]
if t == r:
    print('word is polindrom')
else: print ('word is not polindrom')
