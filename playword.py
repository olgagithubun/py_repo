vuk = True
y = str(raw_input('Vvedit slovo: '))
x = str(raw_input('Vvedit nastupne slovo: '))
while vuk:
    if x == ' ':
        vuk = False
        print('Hru zakincheno')
    elif y[len(y)-1] == x[0]:
        y = x
        x = str(raw_input('Vvedit nastupne slovo: '))
    else:
        print('Vashe slovo povunno pochunatus z literu  '+str(y[len(y)-1]).upper())
        x = str(raw_input('Vvedit nastupne slovo: '))

