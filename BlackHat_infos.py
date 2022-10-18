import requests
from bs4 import BeautifulSoup

def infoblackhats():
    #Appel de la page recherchée
    r = requests.get('https://www.blackhat.com/html/archives.html')
    soup = BeautifulSoup(r.content, 'html.parser')

    #Définir le périmètre de scraping
    #Div partivulière
    perimeter = soup.find(class_='col-lg-7 mb-3')

    #Récupère tout les titres évènements et liens du périmètre
    events = perimeter.find_all("h3")
    links = perimeter.find_all("p")

    l_Events = []
    l_Links = []

    #Parcourir la liste des évènements pour push les noms dans la liste l_Events
    for event in events:
        name = event.text
        l_Events.append(name)

    #Parcourir la liste des liens pour les push les années dans la liste l_Links
    for link in links:
        years = links

    # Récupérer les liens des années et les associés à leurs texte 
    # Faire le rapprochement entre les 2 listes l_Events[1] possède tout les liens l_Links[1] (USA : 2022 -> 1997)

infoblackhats()