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

    USA = events[1]
    Europe = events[2]
    Asia = events[3]
    Abu_Dhabi = events[5]
    London = events[8]
    Sao_Paulo = events[9]

    countries = [USA, Europe, Asia, Abu_Dhabi, London, Sao_Paulo]
    print(countries)


infoblackhats()