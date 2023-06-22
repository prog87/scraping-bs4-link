import requests
from bs4 import BeautifulSoup

root = 'https://subslikescript.com'
website = f'{root}/movies'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())

box = soup.find('article', class_='main-article') # find() to get element

links = []
for link in box.find_all('a', href=True):
    links.append(link['href'])

print(links)

# for link in links:
#     website = f'{root}/{link}'
#     result = requests.get(website)
#     content = result.text
#     soup = BeautifulSoup(content, 'lxml')
#
#     box = soup.find('article', class_='main-article')
#
#     title = box.find('h1').get_text()
#     title = ''.join(title.split('/'))
#     transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
#
#     with open(f'{title}.txt', 'w',encoding="utf-8") as file:
#         file.write(transcript)

for link in links:
    result = requests.get(f'{root}/{link}')
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    # Locate the box that contains title and transcript
    box = soup.find('article', class_='main-article')
    # Locate title and transcript
    title = box
    transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

    # Exporting data in a text file with the "title" name
    with open(f'{title}.txt', 'w') as file:
        file.write(transcript)