import time
import os
import requests


'''
A placer et exécuter dans le répertoire pd3f
'''

'''
il est possible de modifier les parametres tels que la langue
liste parametres :

- lang: options de langues (options: 'de', 'en', 'es', 'fr')
- fast: exécution plus rapide, on ne sait pas exactement lequel  (default: False)
- tables: option pour récupérer les tableaux  (default: False)
- experimental: option pour extraire le texte de façon expérimentales (footnotes to endnotes, depuplicate page header / footer) (default: False) /!\ pas utilisé
- check_ocr: Option pour vérifier que les pages du pdf sont bien OCR (default: True, cannot be modified in GUI)

'''

dir = os.getcwd() # la ou se trouve le pdf,
files = {'pdf': ('test.pdf', open('/'+dir+'/test.pdf', 'rb'))}
response = requests.post('http://localhost:1616', files=files, data={'lang': 'fr'})
id = response.json()['id']

while True:
    r = requests.get(f"http://localhost:1616/update/{id}")
    j = r.json()
    if 'text' in j:
        break
    print('waiting...')
    time.sleep(1)
print(j['text'])
