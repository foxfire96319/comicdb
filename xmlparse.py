import requests
import time
from bs4 import BeautifulSoup
import re


def main():
    print '*****MAIN IS STARTING*****'
    result = _get('https://www.ebay.com/sch/i.html?_odkw=batman+%22new+52%22+variant+1%3A100+-%28Detective%2Csuperman%2Caquaman%2Cflash%2Cwonderwoman%2Crobin%2Clot%2Ccgc%2Ccbcs%2Cbatgirl%29&LH_Complete=1&LH_Sold=1&_osacat=0&_ipg=200&_from=R40&_trksid=p2045573.m570.l1313.TR0.TRC0.H0.Xbatman+%22new+52%22+variant+1%3A100+-%28talon%2CDetective%2Csuperman%2Caquaman%2Cflash%2Cwonderwo.TRS0&_nkw=batman+%22new+52%22+variant+1%3A100+-%28talon%2CDetective%2Csuperman%2Caquaman%2Cflash%2Cwonderwoman%2Crobin%2Clot%2Ccgc%2Ccbcs%2Cbatgirl%29&_sacat=0')

    soup = BeautifulSoup(result.content,'lxml')
    #list_data = soup.find_all("ul", {"id":"ListViewInner"})
    list_data = soup.find_all("li",{"id":re.compile('item')})
    for data in list_data:
        temp = data.contents[3].text
        temp = re.sub('New 52', 'New52', temp)
        issue = re.search(r'#\d+',temp)
        print "Title : %s" % (temp)
        if issue:
            print "Issue : %s" % (issue.group()[1:])
        else:
            print "Issue :"
        print "Price : %s" % (data.contents[5].find_all("span",{"class":"bold bidsold"})[0].text.strip())
        try:
            print data.contents[5].find_all("span",{"class":"fee"})[0].text.strip()
        except:
            pass
        print '******************************'
    print '*****MAIN IS DONE*****'

def _get(url):
    try:
        r = requests.get(url)
        return r;
            
    except Exception as e:
        print 'ERROR:' + str(e)
        
def print_result(response):
    print response.content
    
if __name__ == '__main__':
  main()