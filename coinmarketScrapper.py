# -*- coding: utf-8 -*-
"""
@author: Mohammadreza Ashouri
Created in May 2020
"""
from selenium import webdriver
import requests
import bs4
import csv


dateList=[]
highList=[]
marketCapList=[]

r = requests.get('https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20130428&end=20190423')
soup = bs4.BeautifulSoup(r.text,"lxml")

tr = soup.find_all('tr',{'class':'text-right'})
for item in tr:

    dateList.append(item.find('td',{'class':'text-left'}).text)
    highList.append(item.find_all('td')[2].text)
    marketCapList.append(item.find_all('td')[6].text)


row0=['date','high','market cap']
rows=zip(dateList,highList,marketCapList)
with open('coinmarket.csv','w',encoding='utf-8',newline='')as csvfile:
    links_writer=csv.writer(csvfile)
    links_writer.writerow(row0)
    for item in rows:
        links_writer.writerow(item)
