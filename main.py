from flask import Flask,render_template, redirect,request
from rocket import get_rp_jobs
from wanted import get_wanted_jobs
from saramin import get_saramin_jobs
from save import save_to_file
#wanted_jobs=get_wanted_jobs("산업기능요원")
#saramin_jobs=get_saramin_jobs("산업기능요원")
#rocketpunch_jobs=get_rp_jobs("산업기능요원")
#print(rocketpunch_jobs)
app=Flask('esc_scraper')
@app.route('/quasar529.github.io/WebScraper_ITJobs/')
def home():
    return render_template('index.html')

@app.route('/quasar529.github.io/WebScraper_ITJobs/report')
def report():
    word=request.args.get('word')
    if word:
        word=word.lower()
        jobs=get_saramin_jobs(word)
    return render_template('report.html',
    searchingBy=word,jobs=jobs,resultNum=len(jobs))

app.run(host='127.0.0.1')
