import bs4
import requests
import re

url = "https://en.wikisource.org/wiki/Portal:State_of_the_Union_Speeches_by_United_States_Presidents"
r = requests.get(url)
r.raise_for_status()
soup = bs4.BeautifulSoup(r.text, 'lxml')

year_reg = re.compile(r'\d{4}')

speechLinks = {}
ulElem = soup.select('ul')
for ul in ulElem:
    for li in ul.find_all('li'):
        if li.get_text().endswith(')') | li.get_text().endswith('Response') | li.get_text().endswith('Democratic'):
            match_year = year_reg.findall(li.get_text())
            if int(match_year[0]) >= 1900:
                link = li.findNext('a').get('href')
                speechLinks[match_year[0]] = link

for year in speechLinks:
    print('Scraping year: ' + year)

    speechUrl = "https://en.wikisource.org" + speechLinks.get('1900')
    speech = requests.get(speechUrl)
    speech.raise_for_status()
    speechSoup = bs4.BeautifulSoup(speech.text, 'lxml')

    speechDiv = speechSoup.select('div[class=ws-column-container]')
    pTags = speechSoup.select('p')
    text = ""
    for tag in pTags:
        text += tag.get_text()

    print('Writing to file')
    with open('speeches/' + year + '.txt', 'w') as f:
        f.write(text)
