import requests
from bs4 import BeautifulSoup
import random

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
webpage = response.text # to make the soup we have to get the HTML code for the website. 
# print(webpage)

soup = BeautifulSoup(webpage,"html.parser")

movie_tags = soup.find_all(name="h3",class_="title")
# print(movie_tags)

all_titles = [] # an empty list that will hold all the titles of the movies

for title in movie_tags:
    movie_title = title.getText()
    all_titles.append(movie_title)
    # print(movie_title)
    
# print(all_titles)
all_titles.reverse()
# print(all_titles)

with open('movies.txt','w',encoding='utf-8') as file:
    file.write('\n'.join(all_titles))
    
yes_no = input("Do you want to watch a movie?").lower()
if yes_no == "yes":
    random_movie = random.choice(all_titles)
    print(random_movie)
else:
    print("okay")
