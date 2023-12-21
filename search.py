from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#Définition de recherche de produit
def search_Product(req):
    #Initialisation du navigateur Chrome et de son Driver
    service = Service(executable_path='chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    #Mise en place de l'URL de recherche
    form_req = req.replace(' ', '+')
    driver.get(f'https://www.google.fr/search?q={form_req}&source=lnms&tbm=shop')
    sleep(2)

    #Refus des cookies
    driver.find_element('xpath', "//span[text()='Tout refuser']").click()
    sleep(2)

    #Scrapping des éléments des éléments
    global list_product
    list_product = []
    for product in driver.find_elements(By.CLASS_NAME, 'i0X6df')[:20]:
        result_image = product.find_element(By.TAG_NAME, 'img')
        try:
            image = result_image.get_attribute('src')
        except:
            image = "-"
        description = product.find_element(By.CLASS_NAME, 'tAxDx')
        prix = product.find_element(By.CLASS_NAME, 'a8Pemb')
        seller = product.find_element(By.CLASS_NAME, 'aULzUe')
        livraison = product.find_element(By.CLASS_NAME, 'vEjMR')
        div_result_link = product.find_element(By.CLASS_NAME, 'shntl')
        result_link = div_result_link.find_element(By.TAG_NAME, 'a')
        try: 
            link = result_link.get_attribute('href')
        except:
            link = '-'
        list_product.append({"image": image, "description": description.text, "prix": prix.text.replace('\u202f', ''), "seller": seller.text, "livraison": livraison.text, "link":link})
    driver.close()
    return sort_Product(list_product)


#Fonction de tri de résultats
def sort_Product(list_product):
    global sorted_list
    sorted_list = sorted(list_product, key=lambda x: float(x["prix"].replace('€', '').replace(',', '.').replace('\u202f', '').replace('&nbsp;', '')))
    return sorted_list

