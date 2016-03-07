from flask import Flask, url_for, send_from_directory, render_template

app = Flask(__name__, static_url_path='/static')


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


@app.route('/')
def root():
    return render_template('main.html')


@app.route('/about/')
def about():
    return "about"


@app.route('/contact/')
def contact():
    return "contact"


@app.route('/LEGO/')
def lego():
    return "LEGO"


@app.route('/LEGO/<build>/')
def build(build):
    return "Player %s" % build


@app.route('/programming/')
def programming():
    return "programming"


@app.route('/programming/<program>')
def program(program_name):
    return "Program %s" % program_name
        

@app.route('/fail/')
def fail():
    abort(404)

        
@app.errorhandler(404)
def page_not_found(error):
    return "This page does not exist in any known quantum state", 404


if __name__ == '__main__':
        app.debug = True
        app.run()