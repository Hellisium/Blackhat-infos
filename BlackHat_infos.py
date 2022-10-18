import requests
from bs4 import BeautifulSoup

def infoblackhats():
    #Appel de la page recherchée
    r = requests.get('https://www.blackhat.com/html/archives.html')
    soup = BeautifulSoup(r.content, 'html.parser')

    #Récupération des différents évenements
    events = []
    archives = soup.findAll("h3")
    for archive in archives:
        countries = archive.text
        events.append(countries)
    print (events)


infoblackhats()