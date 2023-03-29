import json
import uuid
import random
import string

def random_char(char_num):
       return ''.join(random.choice(string.ascii_lowercase) for _ in range(char_num))

mesta = ['Praha', 'Brno', 'Plzen', 'Rumburk', 'Varnsdorf', 'Most', 'Ostava', 'Tábor']
ulice = ['Západní', 'Krymská', 'Veletržní', 'Milady Horákové', 'Vítězná', 'U hradu', 'Letenská', 'Horní']
jmena = ['Pavel', 'Jan', 'Tomáš', 'Karel', 'Hynek', 'Donald', 'Jiří', 'Klára', 'Michal', 'David', 'Markéta', 'Martin', 'Joe', 'Petr']
prijmeni = ['Nový', 'Trump', 'Biden', 'Marek', 'Mikeš', 'Jiřinský', 'Pavel', 'Zeman', 'Novotný', 'Janoušek', 'Bajtoš']

fixtures = []
for i in range(1,201):
    pojistenec = {
                'model': 'pojisteniapp.pojistenec',
                'pk': i,
                'fields':{
                'jmeno': random.choice(jmena),
                'prijmeni': random.choice(prijmeni),
                'email': f"{random_char(random.randint(5,8))}@gmail.com",
                'telefon': int(f"2123456{random.randint(10,99)}"),
                'ulice': random.choice(ulice),
                'cislo_popisne': random.randint(1,999),
                'mesto': random.choice(mesta),
                'psc': random.randint(10000,99999)
                }
                }
    fixtures.append(pojistenec)

for i in range (1,401):
    pojisteni = {
        'model': 'pojisteniapp.pojisteni',
        'pk': f'{uuid.uuid4()}',
        'fields':{
        'mesicni_pojistne': random.randint(100,2000),
        'pojistenec_id': random.randint(1,200),
        'typ_pojisteni_id': random.randint(1,5),
        'castka': random.randint(1000,1000000),
        'platnost_od': f'{random.randint(2022,2023)}-{random.randint(1,6)}-{random.randint(1,28)}',
        'platnost_do': f'{random.randint(2023,2024)}-{random.randint(7,12)}-{random.randint(1,28)}'
        }
        }
    fixtures.append(pojisteni)
     
with open("fixtures.json", "w") as outfile:
    json.dump(fixtures, outfile, indent= 4)