import bs4
import requests
import pandas as pd
import pyperclip
import webbrowser

#https://www.amazon.in/s?k=books

url=pyperclip.paste()
def getInfo(url):
    try:
        r=requests.get(url)
    except:
        print("Invalid url")
        return
    price=[]
    product=[]
    soup=bs4.BeautifulSoup(r.text,'html.parser')
    results = soup.find_all(class_='puisg-col-inner')

    for result in results:
        # Extract product name
        product_name = result.find(class_='a-size-medium a-color-base a-text-normal')
        if product_name:
            product_ = product_name.text.strip()
        else:
            continue

        # Extract product price
        price_tag = result.find(class_='a-price-whole')
        if price_tag:
            price_ = price_tag.text.strip()
        else:
            continue
        product.append(product_)
        price.append(price_)
    print(len(product))
    dict={'Product':product,'Price':price}
    df=pd.DataFrame(dict)
    df.to_csv('file.csv')

    
getInfo(url)
# webbrowser.open('https://www.amazon.in/s?k=books')

