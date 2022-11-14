import pandas as pd
import bs4
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

url = 'https://www.vivino.com/explore?e=eJzLLbI1VMvNzLM1UMtNrLA1MjUwUEuutHXxVksGEt5qBUDp9DTbssSizNSSxBy1_KIU25TU4mS1_KRK26LEksy89OL45PzSvBIAZGAZAw%3D%3D'

options = Options()
options.headless = True

# browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
browser = webdriver.Firefox(options=options)

print('Opening webpage...')
browser.get(url)

print('Webpage loading...')
time.sleep(5)

# a = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[4]/div/div/div[2]/div[2]/div[1]/div[1]/div')))
# a = browser.find_elements(By.XPATH, '/html/body/div[2]/div[4]/div/div/div[2]/div[2]/div[1]/div[1]/div')

print('Scraping...')
soup = bs4.BeautifulSoup(browser.page_source, 'lxml')
browser.close()

result_div = soup.findAll('div', {'class': 'explorerPage__results--3wqLw'})[0]

wine_data = []
a = 0
for ele in result_div.findNext('div'):
    if str(ele) == '<span data-testid="sentinel"></span>':
        continue

    grape_div = ele.findNext('div', {'class': 'wineInfoVintage__vintage--VvWlU wineInfoVintage__truncate--3QAtw'})
    region_country_div = ele.findNext('div', {'class': 'wineInfoLocation__regionAndCountry--1nEJz'})
    winery_div = ele.findNext('div', {'class': 'wineInfoVintage__truncate--3QAtw'})
    rating_div = ele.findNext('div', {'class': 'vivinoRating_averageValue__uDdPM'})

    # grape = ''
    # if grape_div.text.endswith('N.V.'):
    #     grape = 'Blend'

    split_country_region = region_country_div.text.split(', ')

    wine_dict = {
        'grape': grape_div.text,
        'region': split_country_region[0],
        'country': split_country_region[1],
        'winery': winery_div.text,
        'rating': rating_div.text
    }

    wine_data.append(wine_dict)
    a += 1

print("Number of wines scraped: " + str(a))

print(wine_data)
