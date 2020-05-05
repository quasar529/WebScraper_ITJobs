from flask import Flask,render_template, redirect
#from rocket import get_rp_jobs
from wanted import get_wanted_jobs
from saramin import get_saramin_jobs
from save import save_to_file
#wanted_jobs=get_wanted_jobs("산업기능요원")
saramin_jobs=get_saramin_jobs("산업기능요원")
save_to_file(saramin_jobs)
# driver=webdriver.Chrome('C:\\Users\\김범준\\Desktop\\Git\\WebScaping\\ITJobs\\WebScraper_ITJobs\\chromedriver.exe')
# driver.implicitly_wait(5)
# driver.get('https://www.rocketpunch.com/jobs?keywords=산업기능요원')
# driver.implicitly_wait(5)

# html=driver.page_source
# soup=BeautifulSoup(html)

# items=soup.select('.job-detail')
# print(items)
#pagination=soup.select('.pagination')
#last_page=pagination[0]
#for p in pagination:
    #print(p.a.attrs['page'])
#driver.close()
# jobs=[]
# for item in items:
#     title=item.select_one('a').text
#     link='http://www.saramin.co.kr/'+item.select_one('a').get('href')
#     job={
#         'title':title,
#         'link':link
#     }
#     jobs.append(job)
