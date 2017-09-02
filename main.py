from flask import Flask, render_template, jsonify, request
from os import environ
from crawler import ptt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ptt')
def beauty():
    url = request.args.get('url')
    if url is None:
        url = 'https://www.ptt.cc/bbs/Beauty/index.html'
    next_url, results = ptt.start(url)

    return jsonify({
        'url': next_url,
        'articles': results
    })

if __name__ == '__main__':
    app.run(port = int(environ.get("PORT", 5000)))