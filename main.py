from flask import Flask, render_template, jsonify, request
from os import environ
from crawler import ptt
from helper.flask_cors import add_cors_headers
from helper import emoji

app = Flask(__name__)
app.after_request(add_cors_headers)

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

@app.route('/time')
def time():
    now, code = emoji.time()
    return jsonify({
        'unicode': code,
        'now': now.strftime("%Y-%m-%d %H:%M:%S"),
        'timezone': 'GMT+8',
    })

@app.route('/fruit')
def fruit():
    code = emoji.fruit()
    return jsonify({
        'unicode': code,
    })

if __name__ == '__main__':
    app.run(port = int(environ.get("PORT", 5000)))
