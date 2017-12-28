from bs4 import BeautifulSoup

def options(soup, id):
    option_values = []
    carrier_list = soup.find(id=id)
    for option in carrier_list.find_all('option'):
        option_values.append(option['value'])
    return option_values

def print_list(label, codes):
    print '\n%s:' % label
    for c in codes:
        print c
        
def main():
    #soup = BeautifulSoup(open('./data/page_source.html'))
    html_page = "E:/Google Drive/Backpack/Udacity DAND/04 Data Wrangling/american_and_orlando.html"
    soup = BeautifulSoup(open(html_page), "html5lib")
        
    airports = options(soup, 'AirportList')
    carriers = options(soup, 'CarrierList')
    
    print_list('Airports', airports)
    print_list('Carriers', carriers)
    
main()