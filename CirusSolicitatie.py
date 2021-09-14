man = 0
haar = 0
print()
print('--------------------------------------------------------------------')
print('hallo, u bent uitgekozen om een paar vragen te beantwoorden')
print('over de baan "circusdirecteur". nadat u deze vragen heeft')
print("beantwoord, krijgt u te horen of u op gesprek mag komen.")
print('--------------------------------------------------------------------')

input('wat is uw volledige naam? ')
praktijkErvaring = input('hoeveel jaren ervaring heeft u met dieren-dresuur? ')
diploma = input("bent u in bezit van een MBO 4 diploma? (j/n) ")
vrachtwagen = input ('bent u in het bezit van een vrachtwagen rijbewijs? (j/n) ')
hoed = input("heeft u een hoge hoed in bezit? (j/n) ")
gender = input("bent u een man of vrouw? ")
if (gender == 'man'):
    man = input('hoe breed is uw snor in cm? ')
elif (gender == 'vrouw'):
    vrouw = input('heeft u oranje krulhaar? (j/n) ')
    if (vrouw == 'j'):
        haar = input('hoelang is uw haar in cm? ')
lengte = input('wat is uw lengte in cm? ')
gewicht = input('hoeveel weegt u in kg? ')
certificaat = input('bent u in het bezit van de "overleven met gevaarlijk personeel" certificaat? (j/n) ')
input('hoevel mensen heeft u gestoken? ')

if int(praktijkErvaring) >= 4 and diploma == 'j' and vrachtwagen == 'j' and hoed == 'j' and (int(man) > 10 or int(haar) > 20) and int(lengte) > 150 and int(gewicht) > 90 and certificaat == 'j':
    print()
    print('gefeliciteerd! u bent uitgenodigt om op solicitatiegesprek te komen!')
else:print('sorry, u voldoet niet aan de eisen voor deze baan')



