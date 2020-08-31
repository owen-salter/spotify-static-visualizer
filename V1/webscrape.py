import requests
from bs4 import BeautifulSoup
search_prefix = "https://pitchfork.com/search/?query="
def scrape(search):
    #initialize query & search for album/news images
    session = requests.Session()
    page = session.get(search_prefix + search)
    pitchfork = BeautifulSoup(page.content, "lxml")
    albumreviews = pitchfork.find(id="result-albumreviews")
    albums = albumreviews.find_all(class_='result-item')
    newsstories = pitchfork.find(id="result-news")
    thumbnails = newsstories.find_all(class_='result-item')

    #combine relevent info from scrape
    results = []
    for img in albums:
        results.append(img.find('img').get('src'))
    for img in thumbnails:
        results.append(img.find('img').get('src'))
    return(results)


print(scrape("bottomless pit"))