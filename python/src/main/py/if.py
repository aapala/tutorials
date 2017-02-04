#!/usr/bin/python

'''
Tassa esimerkissa esitellaan if-statement.
if  jos
elif , jos taas
else muutoin
'''

#asetaan arvo

x=10
a=50
b=5000

#erilliset if
print ('Vain if')
if x < a: # jos x on pienempi kuin a, huom loppuun :
    print ('{0} pienempi kuin {1}'.format(x,a))
if x > a: # jos x on suurempi kuin a, huom loppuun :
    print ('{0} suurempi kuin {1}'.format(x,a))

#Suositus on kayttaa elif
print ('elif')
if x < a: # jos x on pienempi kuin a, huom loppuun :
    print ('{0} pienempi kuin {1}'.format(x,a))
elif x > a: # jos x on suurempi kuin a, huom loppuun :
    print ('{0} suurempi kuin {1}'.format(x,a))

print ( ' vertaa x : a,b')
if x > a: # jos x on pienempi kuin a, huom loppuun :
    print ('{0} > {1}'.format(x,a))
elif x > a and x < b: # jos x on suurempi kuin a ja pienempi kuin b :
    print ('{0} < {1} < {2}'.format(x,a,b))
elif x > b:
    print ('{0} > {1}'.format(x,b))
else: #muutoin
    print ('{0} < {1} ja {0} < {2}'.format(x,a,b))
