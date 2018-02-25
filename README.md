# Crawler API

## Available

- [Beauty - Ptt BBS](https://www.ptt.cc/bbs/Beauty/index.html)
- [clock face emoji](https://apps.timwhitlock.info/emoji/tables/unicode)
- [Daily activities of the President of the ROC](http://www.president.gov.tw/Page/37)
- [Announcements of NCU CSIE](http://www.csie.ncu.edu.tw/announcement)

## Development

```shell
pip3 install virtualenv # global
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
export PORT=5000 # optional
export FLASK_DEBUG=1 # optional
python main.py
```

## Packages

- Python 3.6
- Flask
- requests
- beautifulsoup4
- gunicorn

## Notes

```shell
# Deploy using Heroku Git
git remote add heroku https://git.heroku.com/q86.git # or heroku git:remote -a q86
git push heroku master
```

