# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 03:09:06 2020

@author: Bui Thang
"""


from bs4 import BeautifulSoup
import requests 
import pandas as pd

apis_dict = {}
api_no = 0
url = "https://www.programmableweb.com/category/all/apis"
while url_tag != None:
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data,'html.parser')
    odd_apis = soup.find_all('tr',{'class':'odd'})
    even_apis = soup.find_all('tr',{'class':'even'})


    for api in (even_apis + odd_apis):
        api_td = api.find_all('td')
        name = api_td[0].text
        desc = api_td[1].text
        cat = api_td[2].text
        link = 'https://www.programmableweb.com'+api.find('a').get('href')
        #print('Name: ',name,'\n','Category: ',cat,'\n','URL link: ',link,'\n','Description: ',desc,'\n','----------')
        api_no +=1
        apis_dict[api_no] = [name,cat,link,desc]
        print(api_no,': ', name)

    url_tag = soup.find('a',{'title':'Go to next page'})
    if url_tag is None:
        break
    if url_tag.get('href'):
        url = 'https://www.programmableweb.com'+url_tag.get('href')
    else:
        break
    
apis_dict_df = pd.DataFrame.from_dict(apis_dict, orient = 'index', columns = ['Name','Category','URL Link', 'Description'])

apis_dict_df.head()

apis_dict_df.to_csv('APIs.csv')
