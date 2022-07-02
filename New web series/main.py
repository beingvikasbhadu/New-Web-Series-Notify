import requests
import os
from bs4 import BeautifulSoup
import plyer
def saveImage(url):
        with open('img1.ico','wb') as f:
            response=requests.get(url)
            f.write(response.content)
response=requests.get('https://gadgets.ndtv.com/entertainment/new-web-series')
html_doc=response.text

soup=BeautifulSoup(html_doc,'html.parser')
tags=soup.find_all(attrs={'class':'_mvbx _flx'})
url=tags[0].img['src']
saveImage(url)
title=tags[0].find_all(attrs={'class':'_mvinfo'})[0].find_all('a')[0]['title']
release_date=tags[0].find_all(attrs={'class':'_mvrldt'})[0].div.get_text().strip()
genre=tags[0].find_all(attrs={'class':'_mvgenre'})[1].get_text().strip()
episodes=genre=tags[0].find_all(attrs={'class':'_mvgenre'})[0].get_text().split(',')[1].strip()
cast=tags[0].find_all(attrs={'class':'lclamp'})[0].get_text().split(',')
cast=cast[0]+','+cast[1]
director=tags[0].find_all(attrs={'class':'lclamp'})[1].get_text()
platform=tags[0].span.img['alt']
print("Title:",title)
print("Release Date:",release_date)
print("Number Of Episodes:",episodes)
print("Watch on:",platform)
plyer.notification.notify(title="New Web Series",message=f"Title: {title}\nRelease Date: {release_date}\n{episodes}\nWatch on: {platform}\n",timeout=10)
