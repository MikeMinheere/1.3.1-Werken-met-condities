
Vraag = input('is uw kaas geel? ')
if(Vraag == 'ja'):
    A = input('zitten er gaten in? ')
    if (A == 'ja'):
        d = input('is de kaas belachelijk duur? ')
        if(d == 'ja'):
            print('uw kaas is Emmenthaler')
        elif(d == 'nee'):
            print('uw kaas is leerdammer')
    elif (A == 'nee'):
        D = input('is de kaas hard als steen? ')
        if (D == 'ja'):
            print('uw kaas is Panmigiano')
        elif (D == 'nee'):
            print("uw kaas is goudse kaas")

else: B = input('heeft de kaas blauwe schimmels? ')

if (B == 'ja'):
    b = input('heeft de kaas een korst? ')
    if(b == 'ja'):
        print('uw kaas is de bleu de rochbaron')
    elif(b == 'nee'):
        print("uw kaas is defoume d'ambert")
elif (B == 'nee'):
    C = input ('heeft de kaas een korst ')
    if (C == 'ja'):
        print('uw kaas is de Camembert')
    elif (C == 'nee'): 
        print('uw kaas is de Mozzarella')
