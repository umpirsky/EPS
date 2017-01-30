import string
import random
import requests

url = 'http://www.jugoistok.com/prikazracuna/index.php/registracija_korisnika'

# adjust range as needed
for x in xrange(100,500):
    name = 'Ivan'
    lastname = 'Golubovic'
    phone = '1234567'
    email = 'golub+'+str(x)+'@jugoistok.com'
    password = 'opaaa'
    payload = {'ime': name, 'prezime':lastname, 'telefon':phone, 'email':email, 'user_password':password, 'user_password_potvrda':password, 'uslovi_koriscenja':'da','submit':'register'}
    result = requests.post(url, data=payload)
    print(email)