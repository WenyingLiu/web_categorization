import urllib2
import bs4
import requests
import pandas as pd

URL_list = ['buzzlamp.com', 'mediatakeout.com', 'viraldips.com', 
           'webmaila.juno.com', 'cafemom.com', 'www.mangahere.co', 'm.mangahere.co',
           'www.pof.com', 'm.mangahere.co', 'www.astrologyzone.com']

for u in URL_list:
    response = requests.get('http://www.alexa.com/siteinfo/{}'.format(u))
    soup = bs4.BeautifulSoup(response.text)
    global_rank = int(soup.findAll('img', {'class':'img-inline', 'title':'Global rank icon'})[0].text.split()[0].replace(',', ''))
    category = filter(None, soup.findAll('table', {'id':'category_link_table'})[0].text.split('\n'))[-1].split('>')[0].strip()
    print u, '\t', global_rank, category
