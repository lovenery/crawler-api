# Crawler API

## Available

- [Beauty - Ptt BBS](https://www.ptt.cc/bbs/Beauty/index.html)

## Development

```shell
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