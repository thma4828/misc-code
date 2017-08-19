import bs4
from bs4 import BeautifulSoup
import requests
import csv
import glob
import pandas
from urllib.request import Request, urlopen

def main():
    url = 'http://abcnews.go.com/xmlLatestStories'
    request = Request(url, headers={'User-Agent':'Mozilla/5.0'})
    source = urlopen(request).read()
    soup = bs4.BeautifulSoup(source, 'xml')
    #print(soup)
    URLS = []
    for url1 in soup.find_all('loc'):
        URLS.append(url1.string)
    
    trumpArt = []
    russiaArt = []
    putinArt = []
    ciaArt = []
    bernieArt = []
    syriaArt = []
    saudiArt = []
    nsaArt = []
    crimeArt = []
    afghArt = []
    
    for loc in URLS:
        itru = loc.find('trump')
        irus = loc.find('russia')
        iput = loc.find('putin')
        icia = loc.find('cia')
        iber =loc.find('bernie-sanders')
        isyr = loc.find('syria')
        isau = loc.find('saudi')
        insa = loc.find('nsa')
        icrm = loc.find('crime')
        iafg = loc.find('afghanistan')
        
        if itru != -1:
            trumpArt.append(loc)
        if irus != -1:
            russiaArt.append(loc)
        if iput != -1:
            putinArt.append(loc)
        if icia != -1:
            ciaArt.append(loc)
        if iber != -1:
            bernieArt.append(loc)
        if isyr != -1:
            syriaArt.append(loc)
        if isau != -1:
            saudiArt.append(loc)
        if insa != -1:
            nsaArt.append(loc)
        if icrm != -1:
            crimeArt.append(loc)
        if iafg != -1:
            afghArt.append(loc)
            
    print("trump articles: ", len(trumpArt))
    print("russia articles: ", len(russiaArt))
    print("putin articles: ", len(putinArt))
    print("CIA articles: ", len(ciaArt))
    print("bernie articles: ", len(bernieArt))
    print("syria articles: ", len(syriaArt))
    print("saudi articles: ", len(saudiArt))
    print("nsa articles: ", len(nsaArt))
    print("crime articles: ", len(crimeArt))
    print("afghanistan articles: ", len(afghArt))
    
main()