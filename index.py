import bs4
import pandas
import requests

url = 'https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating%27' # các bạn thay link của trang mình cần lấy dữ liệu tại đây
def get_page_content(url):
   page = requests.get(url,headers={"Accept-Language":"en-US"})
   return bs4.BeautifulSoup(page.text,"html.parser")
soup = get_page_content(url)

certificate = []
runtime = []
genre = []

print(soup.prettify)

for movie in soup.findAll('p',class_='text-muted'):
  if ((not movie.findAll('span',class_='certificate')) &
    (not movie.findAll('span',class_='runtime')) &
    (not movie.findAll('span',class_='genre'))):
    continue
  certificate.append('' if not [ce.text for ce in movie.findAll('span',class_='certificate')] else
    [ce.text for ce in movie.findAll('span',class_='certificate')][0])
  runtime.append('' if not [rt.text for rt in movie.findAll('span',class_='runtime')] else
    [rt.text for rt in movie.findAll('span',class_='runtime')][0])
  genre.append('' if not [gr.text for gr in movie.findAll('span',class_="genre")] else
    [rt.text for rt in movie.findAll('span',class_='genre')][0])

print('123123123123123', genre)

import csv
with open('something.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Certificate", "Runtime", "Genre"])
    for i in range(len(certificate)):
      writer.writerow([certificate[i], runtime[i], genre[i].strip()])

###################################################################################################
