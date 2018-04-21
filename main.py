import requests
import time


def main():
    print '*****main is starting*****'
    _get('https://www.ebay.com/sch/i.html?_odkw=batman+%22new+52%22+variant+1%3A100+-%28Detective%2Csuperman%2Caquaman%2Cflash%2Cwonderwoman%2Crobin%2Clot%2Ccgc%2Ccbcs%2Cbatgirl%29&LH_Complete=1&LH_Sold=1&_osacat=0&_ipg=200&_from=R40&_trksid=p2045573.m570.l1313.TR0.TRC0.H0.Xbatman+%22new+52%22+variant+1%3A100+-%28talon%2CDetective%2Csuperman%2Caquaman%2Cflash%2Cwonderwo.TRS0&_nkw=batman+%22new+52%22+variant+1%3A100+-%28talon%2CDetective%2Csuperman%2Caquaman%2Cflash%2Cwonderwoman%2Crobin%2Clot%2Ccgc%2Ccbcs%2Cbatgirl%29&_sacat=0')
    print '*****main is done*****'

def _get(url):
    try:
        r = requests.get(url)
        file = open("xml.txt","w")
        file.write(r.content)
            
    except Exception as e:
        print 'ERROR:' + str(e)
        
if __name__ == '__main__':
  main()