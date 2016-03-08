import os
from flask import Flask, url_for, send_from_directory, render_template, abort, session, redirect, request, flash

app = Flask(__name__, static_url_path='/static')

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'JustinSiebert.db'),
    SECRET_KEY='BobNewhart',
    USERNAME='Just.Sieb',
    PASSWORD='TempPass'
))

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


@app.route('/static/css/<path:path>')
def send_static_css(path):
    return send_from_directory('static/css', path)


@app.route('/static/fonts/<path:path>')
def send_static_fonts(path):
    return send_from_directory('static/fonts', path)


@app.route('/static/html/<path:path>')
def send_static_html(path):
    return send_from_directory('static/html', path)


@app.route('/static/js/<path:path>')
def send_static_js(path):
    return send_from_directory('static/js', path)


@app.route('/')
def root():
    return render_template('main.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/contact/')
def contact():
    return render_template('contact.html')


@app.route('/LEGO/')
def lego():
    return render_template('lego.html')


@app.route('/LEGO/<build>/')
def build(build):
    return "Player %s" % build


@app.route('/programming/')
def programming():
    return render_template('programming.html')


@app.route('/programming/<program>')
def program(program_name):
    return "Program %s" % program_name

       
@app.route('/admin/')
def admin():
    if not session.get('logged_in'):
        print("Mission Abort")
        return redirect(url_for('login'))
    return render_template('admin.html')
  
  
@app.route('/login/', methods=['get', 'post'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid Username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid Password'
        else:
            session['logged_in'] = True
            flash('Your quantum state was changed to being logged in.') 
            return redirect(url_for('admin'))
    return render_template('login.html')
  
  
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Signed Out')
    return redirect(url_for('root'))
  
  
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