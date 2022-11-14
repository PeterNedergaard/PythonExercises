import time

import bs4
import requests
import re

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


url = "https://en.wikipedia.org/wiki/Alan_Turing"

r = requests.get(url)
r.raise_for_status()
soup = bs4.BeautifulSoup(r.text, 'html.parser')

title = soup.select('title')[0]
# print(title.string)

p_tags = soup.select('p')
for p_tag in p_tags:
    if len(p_tag.text.strip()) > 0:
        # print(p_tag.text)
        break


toc = soup.select('div[id=toc]')
a_tags_outer = soup.select('.toc > ul > li > a')
a_tags_inner = soup.select('.toc > ul > li > ul > li > a')
toc_dict = {}

for tag in a_tags_outer:
    toc_dict[tag.text.lstrip('0123456789.- ')] = tag.get('href')

for tag in a_tags_inner:
    toc_dict[tag.text.lstrip('0123456789.- ')] = tag.get('href')


def search_in_dict(word):
    text = ""
    content = soup.select(f'span[id={word}]')[0]

    for ele in content.find_all_next(['p', 'h3']):
        if str(ele).startswith("<h3>"):
            break
        else:
            text += ele.text

    return text


# print(search_in_dict("Family"))


##########################################


turing_reg = re.compile('Turing')
match_turing = turing_reg.findall(str(soup.select('#mw-content-text')))
# print(len(match_turing))

match_text = ""
for el in soup.select('#mw-content-text'):
    match_text += el.text

year_reg = re.compile(r'([A-Z][^.!?]*\d{4}[^.!?]*[.!?])')
match_year = year_reg.findall(match_text)
# print(match_year)


##########################################


options = Options()
# options.headless = True
browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

browser.get("https://amazon.com")
browser.implicitly_wait(50)

search_field = browser.find_element(By.ID, 'twotabsearchtextbox')
search_field.send_keys('Pet Shower Cap - Waterproof Reusable Bath Ear Covers')
search_field.submit()


# Amount of shower caps
amount_tag = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/span/div/h1/div/div[1]/div/div/span[1]')
amount = ""

if amount_tag.text.startswith('1-'):
    amount = amount_tag.text.removesuffix(' results for')[-2:]
else:
    amount = amount_tag.text.removesuffix(' results for')

print("Amount of 'Pet shower caps': " + amount)
print("------------------------------------------")


# Cheapest shower cap
dropdown_element = browser.find_element(By.ID, 'a-autoid-0')
time.sleep(1)
dropdown_element.click()

sort = browser.find_element(By.ID, 's-result-sort-select_1')
sort.click()

time.sleep(2)
scrape_sort = browser.page_source
soup_sort = bs4.BeautifulSoup(scrape_sort, 'html.parser')

first_product = soup_sort.select('div[data-index="1"]')[0]
product_split = first_product.text.split('  ', 1)

name = product_split[0]
price = soup_sort.select('span[class="a-offscreen"]')[0].text

print(name)
print(price)
print("------------------------------------------")


# Most expensive shower cap
# dropdown_element = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/span/div/h1/div/div[2]/div/div/form/span/span')
# time.sleep(1)
# dropdown_element.click()
#
# sort = browser.find_element(By.ID, 's-result-sort-select_2')
# sort.click()
#
# time.sleep(2)
# scrape_sort = browser.page_source
# soup_sort = bs4.BeautifulSoup(scrape_sort, 'html.parser')
#
# first_product = soup_sort.select('div[data-index="1"]')[0]
# product_split = first_product.text.split('  ', 1)
#
# name = product_split[0]
# price = soup_sort.select('span[class="a-offscreen"]')[0].text
#
# print(name)
# print(price)
# print("------------------------------------------")

browser.close()
