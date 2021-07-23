from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup as BS
import re
import string
import pandas as pd

driver = webdriver.Chrome('chromedriver.exe')
searchAddress = "https://tgstat.ru/search"
driver.get(searchAddress)
time.sleep(3)


driver.find_element_by_id('q').send_keys("cloud.mail.ru")

time.sleep(2)
# driver.find_element_by_id("termsconditions").click()
# driver.find_element_by_xpath('//*[@id="Искать"]').click()

# class="btn btn-primary search-button"
driver.find_element_by_css_selector('[class="btn btn-primary search-button"]').click()
time.sleep(2)
html = driver.page_source.encode('utf-8')
#html = BS(html, 'html.parser')
html = BS(html, 'lxml')

items = html.find_all('figure', {'class': 'post-container'})
print(items)
forum = []
for item in items:
        dostupno = ''
        # item.find('h3', class_='title').find('a', 'prefixLink').find('span', class_='prefix prefixSecondary')
        # title = item.find('div', class_='channel-post-title').get_text(strip=True)
        # title = item.find('div', class_='float-right').find('a','title')
        # title = item.find('div', class_='float-left').find('a').get('title')
        title = item.find('a', class_='channel-post-title').string
        link = item.find('div', class_='post-body')
        # link = link.replace('<mark>', '')
        # link = link.replace('</mark>', '')

        # pattern = r'<\/mark>\s*"(.*?)"'
        pattern = r'\/mark&gt;\s*(.*?)"'
        m = ''
        try:
             m = re.search(pattern, str(link))
             print(m.group(1))
        except:
             m = ''
        cloud_link = 'https://cloud.mail.ru' +  m.group(1)
        forum.append(
            {
                'title_post': title,
                'link': cloud_link
#                'date_time': date_time,
#               'dostupno_sklad': item.find('h3', class_='title').find('a', 'prefixLink').find('span',  class_='prefix prefixSecondary')
#                'dostupno_sklad': dostupno
            }
        )


print(forum)


