import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import quote_plus
# def extract_last_page(url):
#     driver=webdriver.Chrome('C:\\Users\\김범준\\Desktop\\Git\\WebScaping\\ITJobs\\WebScraper_ITJobs\\chromedriver.exe')
#     driver.implicitly_wait(5)
#     driver.get(url)
#     driver.implicitly_wait(5)
#     html=driver.page_source
#     soup=BeautifulSoup(html,"html.parser")
#     pagination=soup.select('.pagination')
#     last_page=pagination[0]
#     for p in pagination:
#         print(p.a.attrs['page'])
#     return 

def extract_job(url):
    jobs=[]
    driver=webdriver.Chrome('C:\\Users\\김범준\\Desktop\\Git\\WebScaping\\ITJobs\\WebScraper_ITJobs\\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get(url)
    driver.implicitly_wait(5)
    html=driver.page_source
    soup=BeautifulSoup(html,"html.parser")
    
    items=soup.select('div.job-detail')
    #names=soup.find_all('h4',{'class':'header name'})
    # tmp=driver.find_element_by_xpath('//*[@id="company-list"]/div[3]/div[2]/div[2]/a[1]/h4/strong')
    # driver.implicitly_wait(3)
    # print(tmp)
    # names=tmp.find_elements_by_tag_name('strong')
    # driver.implicitly_wait(3)
    #names=soup.select('div.content > div.company-name')
    tmp=driver.find_element_by_xpath('//*[@id="company-list"]')
    names=tmp.find_elements_by_tag_name('strong')
    
    #print(tmp.get_attribute('text'))
    for n in names:
        print(n.get_attribute('text'))
    for item in items:

        title=item.select_one('a').text
        link='https://www.rocketpunch.com'+item.select_one('a').get('href')
        #name=n
        job={
            'title':title,
            #'name':n,
            'link':link
        }
        jobs.append(job)
    return jobs

def get_rp_jobs(word):
    #jobs=[]
    url=f"https://www.rocketpunch.com/jobs?keywords={word}"
    jobs=extract_job(url)
    return jobs    