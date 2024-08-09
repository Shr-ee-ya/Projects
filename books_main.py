import requests 
from bs4 import BeautifulSoup
import pandas as pd
#url="https://books.toscrape.com/catalogue/page-1.html"

#page= requests.get(url)

#soup= BeautifulSoup(page.text,"html.parser")

#print(soup.title.text)
current_page =1
data = []
#to stop scraping at the first empty page
proceed = True
while(proceed==True):
    print("currently scraping page:" +str(current_page))

    url="https://books.toscrape.com/catalogue/page-"+str(current_page)+".html"
    page= requests.get(url)
    soup= BeautifulSoup(page.text,"html.parser")

    if soup.title.text== "404 Not Found":
        proceed=False
    else:
        #main data extraction
        all_books=soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
        for book in all_books:
            item={}
            item['Title']=book.find("img").attrs["alt"]
            item["Link"] =book.find("a").attrs["href"] #add the url link then+ wtever is there for a working link
            item["Price"]=book.find("p", class_="price_color").text[2:]
            item['Stock']=book.find("p",class_="instock availability").text.strip()
            data.append(item)

    current_page+=1  
       
#to save the data 
df=pd.DataFrame(data)
df.to_excel("books.xlsx")
#df.to_csv("book.csv")