#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 18:41:36 2023

@author: waqarmakki
"""

from bs4 import BeautifulSoup
import pandas as pd
# import numpy as np
import requests
import time
# import concurrent.futures
from openpyxl import Workbook
## Data_Extraction Single Page

def extract_data(link):
    
    # headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
    headers={'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
    r = requests.get(link, headers=headers)
    
    title, description, producers, studios, licensors, source, genre, demographic, rating, theme = '-', '-', '-', '-', '-', '-', '-','-','-','-'
    src = '-'
    if r.status_code != 200:
        print("waiting...")
        time.sleep(2)
        r = requests.get(link, headers=headers)
    
    if r.status_code == 200:
        print("fetching data")
        soup = BeautifulSoup(r.text, 'lxml')

        title = soup.find('div', {'itemprop': 'name'}).text.strip()
        description = soup.find('p', {'itemprop': 'description'}).text.strip()

        data = soup.find_all('div', {'class': ['spaceit_pad']})

        for d in data:
            ds = d.text.strip().split(':')
            if ds[0].lower() == 'producers':
                producers = ds[1]
            elif ds[0].lower() == 'genres':
                genre = ds[1]
            elif ds[0].lower() == 'demographic':
                demographic = ds[1]
            elif ds[0].lower() == 'rating':
                rating = ds[1]
            elif ds[0].lower() == 'licensors':
                licensors = ds[1]
            elif ds[0].lower() == 'studios':
                studios = ds[1]
            elif ds[0].lower() == 'source':
                source = ds[1]
            elif ds[0].lower() == 'theme':
                theme = ds[1]
                
        ## fetching image source
        try:
            src = soup.find('div', class_='leftside').find('img')['data-src']
        except:
            pass
        
    return pd.DataFrame({
        'Id': link.split('/')[-2],
        'Title': title,
        'Description': description,
        'Genre': genre,
        'Demographic': demographic,
        'Rating': rating,
        'Producers': producers,
        'Licensors': licensors,
        'Studios': studios,
        'Source': source,
        'Theme': theme,
        'Image_Source': src,
    }, index=[0])
    

## loading the links

all_links = list(pd.read_csv('myAnimeList_allLinks.csv')['Links'])[15815:]

# extract_data(all_links[0])

dataset = pd.DataFrame()
wb = Workbook()
ws =  wb.active
ws.title = "Changed Sheet"
wb.save(filename = 'all_data_anime_15815+.xlsx')
with pd.ExcelWriter("/home/waqarmakki/Desktop/Anime_Recommendation_System/all_data_anime_15815+.xlsx", mode="a", engine="openpyxl",if_sheet_exists='new') as writer:
    for idx in range(len(all_links)):
        d = pd.DataFrame(extract_data(all_links[idx]), index=[0])
        dataset = pd.concat([dataset, d], ignore_index=True)
        # time.sleep(0.1)
        print(idx+1, all_links[idx])
        if idx%1000 == 0:
            dataset.to_excel(writer, sheet_name="Sheet1")
            dataset = pd.DataFrame()
        
writer.close()
dataset.to_excel('/home/waqarmakki/Desktop/Anime_Recommendation_System/all_data_anime_last_few.xlsx', index=False)

# all_data = pd.read_excel('C/home/waqarmakki/Desktop/Anime_Recommendation_System/all_data_anime_15815+.xlsx')

# with pd.ExcelWriter("C:\\Users\\Waqar Makki\\OneDrive\\Desktop\\Anime_Recommendation_System\\all_data_anime_4000_+_.xlsx", mode="a", engine="openpyxl",if_sheets_exists='overlay') as writer:
#     df.to_excel(writer, sheet_name="Sheet1")
#     writer.close
