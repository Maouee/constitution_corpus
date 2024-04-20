##__IMPORTS__##
from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup


##__DATACLASSES__##
@dataclass
class Drama : 
    auteur : str
    titre : str
    date : str
    genre : str
    contenu : str   
    url : str
    
class Corpus : 
    items : list[Drama]


##__FONCTIONS__##  
def get_all_plays(url): 
    """
    Récupération de toutes les urls utiles et transformation de toutes les urls en urls absolues.
    """
    data = []
    html = url

    table = html.find("table", {"id": "table_AA", "class": "TF"}) # recherche tous les liens dans le tableau 
    rows = table.find_all("tr") #récupérer les lignes du tableau  

    for row in rows[1:]:  # ignorer l'en-tête
        case = row.find_all("td") #récupérer les cellules
    
        auteur_cell = case[0]
        titre_cell = case[1]
        date_cell = case[2]
        genre_cell = case[3]
        contenu_cell = case[4].find('a')['href']

        if contenu_cell.startswith("http"): # si http alors url absolue donc ok on append
            contenu_abs_url = contenu_cell
        else : # si non on concatène l'url de base avec l'url relative récupérée pour avoir que des urls absolues
            base_url = "https://www.theatre-classique.fr/pages/programmes/"
            contenu_abs_url = base_url + contenu_cell.lstrip("/")
            
        auteur = auteur_cell.text.strip()
        titre = titre_cell.text.strip()
        date = date_cell.text.strip()
        genre = genre_cell.text.strip()
        contenu_final = extract_contenu(contenu_abs_url)

        drama_items = Drama(auteur=auteur, titre=titre, date=date, genre=genre, contenu=contenu_final, url=url)
        data.append(drama_items)
          
    return data

def extract_contenu(contenu_abs_url): 
    contenu = []
    r = requests.get(contenu_abs_url)
    if r.status_code == 200:
        html_content = r.content
        soup = BeautifulSoup(html_content, 'html.parser')
        texte = soup.find('div', {'id' : 'texteTheatre'})
        contenu.append(texte) 
    else : 
        print("Une erreur s'est produite lors de la récupération du contenu.")

    return contenu


##__MAIN__##
def main(): 
    url = "https://www.theatre-classique.fr/pages/programmes/PageEdition.php"
    result = get_all_plays(url)
    print(result)

if __name__ == "__main__":
    main()
