from random import randint
x = randint(1,1000)
#y = int(raw_input('Vvedit chuslo '))
vuk = True
while vuk:
    y = int(raw_input('Vvedit chuslo '))
    if y == x:
        print('chuslo vhadano!!!')
        vuk = False
    elif y<x:
        print('vvedene chuslo menshe zahadanoho')
    else:
        print('vvedene chuslo bilshe zahadanoho')
else:
    print(x)
    
		
	
		
			
    
