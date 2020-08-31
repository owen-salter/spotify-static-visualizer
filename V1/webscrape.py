import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageFilter
import io, os

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
    #return(results)
    # if a search hasn't already been made, create a folder and save results
    if not os.path.exists('C:/Users/owens/PycharmProjects/spotify-static-visualizer/results/' + search):
        os.makedirs('C:/Users/owens/PycharmProjects/spotify-static-visualizer/results/' + search)
        for i in range (len(results)):
            image = Image.open(io.BytesIO(requests.get(results[i]).content)).convert('RGB')
            image.save('C:/Users/owens/PycharmProjects/spotify-static-visualizer/results/' + search + '/' + str(i) + '.jpeg', 'JPEG')
