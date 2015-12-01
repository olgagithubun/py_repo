li = []
integer = int(raw_input('Vvedit kilkist trijok Pifagora: '))
for i in xrange(1, 100):
	for j in xrange(i,100):
		for k in xrange(1, 100):
			if (i**2+j**2 == k**2) and (len(li)<integer):
				li.append ((i,j,k))
print(li)
		 
				
