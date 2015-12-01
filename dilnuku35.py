dilnuku = []
i = 3
while len(dilnuku)<100:
    if ((i%3 == 0) and (i%5 <> 0)) or ((i%3 <> 0) and (i%5 ==0)):
        dilnuku.append (i)
        i = i+1
    elif (i%3 == 0) and (i%5 ==0):
        i = i+1
    else:
        i = i+1
	
print(dilnuku)
	
