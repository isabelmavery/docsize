from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from bs4 import BeautifulSoup
import requests

#Get Src from Fanatics
def Get_Source(url):
     agent = {"User-Agent":"Mozilla/5.0"}
     source=requests.get(url, headers=agent).text
     return source

#Gets Size of a html element
def Get_Len(elem):
    return len(str(elem))

def Get_Script_Info(script):
    if not (script):
        return ''
    if (script.string):
        return str(script.string).lstrip()[0:40] 
    elif (script.attrs):
        return script.attrs
    return script.id

def Get_Scripts(soup):
    sizes = []
    scriptIds = []
    for num, script in enumerate(soup.find_all('script'), start=1):
        sizes.append(len(str(script)))
        scriptIds.append(str(Get_Script_Info(script)))
        # print(len(str(script)), Get_Script_Info(script))
    return sizes, scriptIds

def Parse_HTML(url):
    # url="https://www.mlsstore.com/columbus-crew-sc/t-25897955+z-9594207-1542318430"
    soup=BeautifulSoup(Get_Source(url), 'html.parser')
    
    docSize = Get_Len(soup)
    headSize = Get_Len(soup.html.head)
    bodySize = Get_Len(soup.html.body)
    allScriptSizes = Get_Len(soup.find_all('script'))

    print('Successfully Parsed Document')
    print('Doc Size -', docSize)
    print('Head Size -',headSize, str(soup.html.head).lstrip()[0:25])
    print('Body Size -',bodySize, str(soup.html.body).lstrip()[0:25])
    print('Scripts Total Size -', allScriptSizes)
 
    scriptSizes, scriptIds = Get_Scripts(soup)
    return docSize, headSize, bodySize, scriptSizes, scriptIds, allScriptSizes
