import os
from flask import Flask, url_for, send_from_directory, render_template, abort, session, redirect, request, flash

app = Flask(__name__, static_url_path='/static')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


@app.route('/static/css/<path:path>')
def send_static_css(path):
    return send_from_directory('static/css', path)


@app.route('/static/js/<path:path>')
def send_static_js(path):
    return send_from_directory('static/js', path)
    

@app.route('/')
def root():
    return render_template('main.html')
  
  
@app.errorhandler(401)
def unauthorized_page(error):
    return render_template('401.html'), 401   
        
        
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.config
    app.debug = True
    app.run(host='0.0.0.0')