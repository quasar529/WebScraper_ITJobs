from flask import Flask,render_template, redirect
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
    return render_template('home.html')

app.run()
