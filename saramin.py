import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import quote_plus
def extract_last_page(word):
    url=f"http://www.saramin.co.kr/zf_user/search/recruit?searchType=search&loc_mcd=101000,102000&company_cd=0,1,2,3,4,5,6,7,9&searchword={word}&panel_type=&search_optional_item=y&search_done=y&panel_count=y&recruitPage=1&recruitSort=relation&recruitPageCount=40&inner_com_type="
    driver=webdriver.Chrome('C:\\Users\\김범준\\Desktop\\Git\\WebScaping\\ITJobs\\WebScraper_ITJobs\\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get(url)
    driver.implicitly_wait(5)
    
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    last_page=soup.select_one('.pagination').select('a')[-1].get('page')
    return last_page

def extract_jobs(url):
    jobs=[]
    driver=webdriver.Chrome('C:\\Users\\김범준\\Desktop\\Git\\WebScaping\\ITJobs\\WebScraper_ITJobs\\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get(url)
    driver.implicitly_wait(5)
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    items=soup.select('.item_recruit')
    pagination=soup.select_one('.pagination').select('a')[-1].get('page')
    print(pagination)
    for item in items:
        title=(item.select_one('a').get('title'))
        link="http://www.saramin.co.kr"+item.select_one('a').get('href')
        name=item.select_one('.area_corp').select_one('span').text
        job={
            'title':title,
            'link':link,
            'name':name
        }
        jobs.append(job)
    return jobs 

def get_saramin_jobs(word):
    url=f"http://www.saramin.co.kr/zf_user/search/recruit?searchType=search&loc_mcd=101000,102000&company_cd=0,1,2,3,4,5,6,7,9&searchword={word}&panel_type=&search_optional_item=y&search_done=y&panel_count=y&recruitPage=1&recruitSort=relation&recruitPageCount=40&inner_com_type="
    last_page=extract_last_page(word)
    for i in range(last_page):
        jobs=extract_jobs(url)
    return jobs