from bs4 import BeautifulSoup
import requests
import csv
import lxml

csv_file=open('ebay-data.csv','w')
csv_w=csv.writer(csv_file)
csv_w.writerow(['title','price','ratings'])
def get_details(url):
    response = requests.get(url)
    
    if not response.ok:
        print('Server responded: ', response. status_code)
    else:
        tags = BeautifulSoup(response.text, 'lxml')
        try:
            title=tags.find("h1",{"class":"product-title"}).text
        
        except:
            title = ''
        try:
            price=tags.find("div",{"class":"display-price"}).text
        
        except:
            price = ''            
        try:
            rate=tags.find("span",{"class":"num-of-rewiews reviews-aggregated-pt"}).a.text
        
        except:
            rate = ''  
        csv_w.writerow([title,price,rate])          
 


def get_page(url):
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
    response = requests.get(url, headers=headers, timeout=2)
    if not response.ok:
        print('Server responded: ', response. status_code)
    else:
        soup = BeautifulSoup(response.text, 'lxml')
    
        for div in soup.findAll("div",{"class":"s-item__image s-item__image--prettify"}):
            link=div.a.get('href')
            get_details(link)
        next=soup.findAll("a",{"class":"ebayui-pagination__control"})
  
        link=next[1].get('href')
        print(link)
        get_page(link)
        
    


def main():
    print("hey")
    #url='https://www.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094?rt=nc&_pgn=5'
    url='http://www.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094'
    get_page(url)

if __name__ == '__main__':
    main()