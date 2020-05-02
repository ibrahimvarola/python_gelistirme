from bs4 import BeautifulSoup
import requests

#imdb top 10

url = "https://www.imdb.com/chart/top"
r = requests.get(url)
soap = BeautifulSoup(r.content , "html.parser")


def search(edge) :
    a = soap.find_all("table" , {"class" : "chart full-width"})
    body = a[0].contents[len(a[0].contents)-2]
    body = body.find_all("tr",limit=int(edge))
    return body

def finding () :
    limit = input("İlk kaç sıralamayı görmek istiyorsunuz : ")
    
    for film in search(limit) : 
        filmname = film.find_all("td" , {"class" : "titleColumn"})
        point = film.find_all("td" , {"class" : "ratingColumn imdbRating"})
        point = point[0].get_text(strip = True)
        filmnames = filmname[0].get_text(strip=True)
        print(filmnames , " "*6 , "IMDb : {}".format(point)) 
        print("*"*25)

finding()


