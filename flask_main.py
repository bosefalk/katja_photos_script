from flask import Flask, send_file

app = Flask(__name__)
app.config.from_object('config')


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return send_file('photos/test1/katerina_falk_photos.zip', as_attachment=True)

@app.route('/brains/test1', methods=['GET', 'POST'])
def test1():
	return send_file('photos/test1/katerina_falk_photos.zip', as_attachment=True)