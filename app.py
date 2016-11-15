from flask import render_template, Flask, request
import sys
import exifTags

UPLOAD_FOLDER = './temp'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/upload_file', methods=['POST'])
def upload_file():
    metaData = exifTags.getMetaData(request.files['file'], None)
    body = '<table><tr><th>EXIF Data</th><th></th></tr>'
    if metaData:
        for key, value in metaData.iteritems():
            body += '<tr><td><b>{0}</b></td><td>{1}</td></tr>'.format(
                key, value
            )
        body += '</table>'
    return body


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
    try:
        appPort = int(sys.argv[1])
    except IndexError:
        appPort = 80
    app.run(
        debug=True,
        host='0.0.0.0',
        port=appPort
    )
