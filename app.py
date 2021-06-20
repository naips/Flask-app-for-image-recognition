from flask import Flask

UPLOAD_FOLDER = '/mnt/ubuntu/naips/anaconda_files/webApp/display_image/uploads/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024