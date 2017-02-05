#!/usr/bin/python

'''

forloop-statement.
laajentaa if esimerkkia

'''

#asetaan arvo

a=3
b=7
xmin=0
xmax=10



print ( ' vertaa x : a,b')

for x in range(xmin, xmax):
    if x < a: # jos x on pienempi kuin a, huom loppuun :
        print ('{0} < {1}'.format(x,a))
    elif x > a and x < b: # jos x on suurempi kuin a ja pienempi kuin b :
        print ('{0} > {1} ja  {0} < {2}'.format(x,a,b))
    elif x > b:
        print ('{0} > {1}'.format(x,b))
    else: #muutoin
        print ('{0} <= {1} tai {0} <= {2}'.format(x,a,b))
