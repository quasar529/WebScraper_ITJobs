import requests
from bs4 import BeautifulSoup
from selenium import webdriver
def extract_jobs(url):
    jobs=[]
    driver=webdriver.Chrome('C:\\Users\\김범준\\Desktop\\Git\\WebScaping\\ITJobs\\WebScraper_ITJobs\\chromedriver.exe')
    driver.get(url)
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    b=soup.select('._3D4OeuZHyGXN7wwibRM5BJ')
    #print(b)
    for i in b:
        title=i.select_one('dt').text
        link="https://www.wanted.co.kr/"+i.a.get('href')
        name=i.select_one('div[class=body]>dl>dd')
        job={
            'title':title,
            'link':link,
            'name':name.text
        }
        #print(job)
        jobs.append(job)
    driver.close()
    return jobs

def get_wanted_jobs(word):
    url=f"https://www.wanted.co.kr/search?query={word}"
    jobs=extract_jobs(url)
    return jobs
