import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import quote_plus
# def extract_last_page(url):
#     result=requests.get(url)
#     soup=BeautifulSoup(result.text,"html.parser")
#     pages=soup.find("div",{"class":"tablet computer large screen widescreen only"}).find_all("a")
#     print(pages)
#     last_page=pages[-1].string
#     return last_page
driver=webdriver.Chrome('C:\\Users\\김범준\\Desktop\\Git\\WebScaping\\ITJobs\\WebScraper_ITJobs\\chromedriver.exe')
driver.implicitly_wait(5)
def extract_job(url):
    
    driver.get(url)
    driver.implicitly_wait(5)
    html=driver.page_source
    soup=BeautifulSoup(html,"html.parser")
    #print(soup)
    #items=soup.find_all('div',{'class':'job-detail'})
    items=soup.select(".ui job items segment")
    print(items)
    # for item in items:
    #     #title=item.select('.job-detail')
    #     print(item)
    driver.close()
def get_rp_jobs(word):
    url=f"https://www.rocketpunch.com/jobs?keywords={word}"
    jobs=extract_job(url)
    return jobs    