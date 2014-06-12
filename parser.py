import urllib
from datetime import date
from pytesser import *
import os



def image_to_string(image):
    os.system("convert -flatten DomainList.png DomainList-white.png")
    os.system("convert DomainList-white.png DomainList-white.tiff")
    return image_file_to_string("DomainList-white.tiff")

def main():
    today=date.today()
    date_as_string=today.strftime('%d.%m.%Y')
    urllib.urlretrieve ("https://domain.fi/s/FI/GrantedDomains/DomainList?selectedDate="+date_as_string, "DomainList.png")
    print image_to_string('DomainList.png')

if __name__ == "__main__": main()