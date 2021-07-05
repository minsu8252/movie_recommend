import requests
from bs4 import BeautifulSoup
import re

def get_movie_link(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html5lib')

    movie_links = soup.select('a[href]')

    movie_links_list = []

    for link in movie_links:
        if re.search(r'st=mcode&sword' and r'&target=after', link['href']):
            target_url = url + str(link['href'])
            movie_links_list.append(target_url)

    return movie_links_list

# url = "https://movie.naver.com/movie/point/af/list.nhn"
# movie_links = get_movie_link(url)
# print(movie_links)



def genre_list(url):
    movie_links_list = get_movie_link(url)
    genre_list =[]
    for movie_url in movie_links_list:
        res = requests.get(movie_url)
        content = res.text
        soup = BeautifulSoup(content, 'html5lib')
        genre = soup.find_all('table', class_ = 'info_area')

        for genre in genre:
            genre_list.append(genre.a.get_text())
    
    return genre_list

url = "https://movie.naver.com/movie/point/af/list.nhn"
genre_list_data = genre_list(url)
print(genre_list_data)