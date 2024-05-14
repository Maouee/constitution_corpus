##__IMPORTS__##
from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


##__DATACLASSES__##
@dataclass
class Drama : 
    auteur : str
    titre : str
    date : str
    genre : str
    style : str
    contenu : str   
    
class Corpus : 
    items : list[Drama]


##__FONCTIONS__##  
def verif_valid_url(url):
    """
    Cette fonction permet de vérifier si le lien est valide. Il ne récupère que les status 200. 
    Argument : une url (str) correspondant à l'url à vérifier. L'url est à préciser dans le main.
    Sorties : Seuls les liens valides seront transformés en outils "BeautifulSoup". Sinon renvoie None.
    """
    r = requests.get(url)
    if r.status_code == 200 : 
        print(r.status_code)
        soup = BeautifulSoup(r.content, "html.parser")
        return soup
    else : 
        print(f"Erreur {r.status_code}.")
        return None
    

def get_all_plays(url): 
    """
    Récupération de toutes les urls utiles et transformation de toutes les urls en urls absolues.
    Argument : url (str): Une chaîne de caractères représentant l'URL de la page principale.
    Sortie : list: Une liste d'objets Drama contenant les informations sur chaque pièce de théâtre.
    """
    data = []
    html = verif_valid_url(url)

    table = html.find("table", {"id": "table_AA", "class": "TF"}) # recherche tous les liens dans le tableau 
    rows = table.find_all("tr") #récupérer les lignes du tableau  

    for row in tqdm(rows[1:], desc="Traitement des différentes pièces"):  # barre d'avancement + ignorer l'en-tête
        case = row.find_all("td") #récupérer les cellules
    
        auteur_cell = case[0]
        titre_cell = case[1]
        date_cell = case[2]
        genre_cell = case[3]
        contenu_cell = case[6].find('a')['href']

        if contenu_cell.startswith("http"): # si commence par http alors url absolue donc ok on append
            contenu_abs_url = contenu_cell
        else : # si non on concatène l'url de base avec l'url relative récupérée pour avoir que des urls absolues
            base_url = "https://www.theatre-classique.fr/pages/programmes/"
            contenu_abs_url = base_url + contenu_cell.lstrip("/")
            
        auteur = auteur_cell.text.strip()
        titre = titre_cell.text.strip()
        date = date_cell.text.strip()
        genre = genre_cell.text.strip()
        style, contenu_final = extract_content(contenu_abs_url)

        drama_items = Drama(auteur=auteur, titre=titre, date=date, genre=genre, style=style, contenu=contenu_final)
        data.append(drama_items)
        print(f"Pièce ajoutée: {titre}")

    return data

def extract_content(contenu_abs_url): 
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
