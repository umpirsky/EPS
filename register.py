import string
import random
import requests

url = 'http://www.jugoistok.com/prikazracuna/index.php/registracija_korisnika'

# adjust range as needed
for x in xrange(100,500):
    name = ''.join(random.choice(string.ascii_letters) for _ in range(10))
    lastname = ''.join(random.choice(string.ascii_letters) for _ in range(10))
    phone = ''.join(random.choice(string.digits) for _ in range(10))
    email = 'pera'+str(random.randint(1,10000000))+'@ueiuwnf.com'
    password = '1234'
    payload = {'ime': name, 'prezime':lastname, 'telefon':phone, 'email':email, 'user_password':password, 'user_password_potvrda':password, 'uslovi_koriscenja':'da','submit':'register'}
    result = requests.post(url, data=payload)
    print(email)
