import openpyxl
from selenium import webdriver
import urllib.request
import urllib.parse
from urllib.request import urlopen
from bs4 import BeautifulSoup as soups

def search_selenium(search_name, search_limit) :
    search_url = "https://www.google.com/search?q=" + urllib.parse.quote_plus(search_name) + "&hl=ko&tbm=isch"
    
    browser = webdriver.Chrome('C:/Users/home/chromedriver.exe')
    browser.get(search_url)
    
    image_count = len(browser.find_elements_by_tag_name("img"))
    
    print(search_name + "로드된 이미지 개수 : ", image_count)

    browser.implicitly_wait(2)
    

    for i in range( image_count ) :
        image = browser.find_elements_by_tag_name("img")[i]
        image.screenshot("C:/Users/home/milk/" + str(search_name) + str(i) + ".png")

    browser.close()
    
    
filename = "milk.xlsx"
milk = openpyxl.load_workbook(filename)
sheet = milk.worksheets[0]


if __name__ == "__main__" :
    for row in sheet.rows:
        brand = row[0].value
        print(brand)
        check=0
        for i in row:
            if check == 0:
                check=1
            elif i.value == None:
                break
            else:
                search_limit=10
                search_name = brand + " " + (i.value)
                #print(plusUrl)
                search_selenium(search_name, search_limit)
                
                
