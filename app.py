from flask import render_template, Flask, request, session, abort
from flask.ext.session import Session
import sys
import exifTags
# import re
import uuid

sess = Session()
UPLOAD_FOLDER = './temp'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.before_request
def csrf_protect():
    if request.method == "POST":
        token = session.pop('_csrf_token', None)
        if not token or token != request.form.get('_csrf_token'):
            abort(403)


def generate_random_string():
    return str(uuid.uuid4())


def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = generate_random_string()
    return session['_csrf_token']


app.jinja_env.globals['csrf_token'] = generate_csrf_token


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/upload_file', methods=['POST'])
def upload_file():
    metaData = exifTags.getMetaData(request.files['file'], None)
    return render_template('results.html', metaData=metaData)


# ERROR HANDLING
@app.errorhandler(405)
def methodNotAllowed(e):
    return '<h1>The method is not allowed for the requested URL.</h1>'


@app.errorhandler(404)
def notFound(e):
    return '<h1>The page you are looking for is not found</h1>'


@app.errorhandler(403)
def forbidden(e):
    return "<h1>"
"You don\'t have the required premissions to view this page"
"</h1>"


@app.errorhandler(503)
def serviceUnavailable(e):
    return "<h1>"
"You don\'t have the required premissions to view this page"
"</h1>"


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    sess.init_app(app)
    try:
        appPort = int(sys.argv[1])
    except IndexError:
        appPort = 80
    app.run(
        debug=True,
        host='0.0.0.0',
        port=appPort
    )
