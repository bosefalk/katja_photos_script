from flask import Flask, send_file

app = Flask(__name__)
app.config.from_object('config')



@app.route('/brains/test1', methods=['GET', 'POST'])
def test1():
	return send_file('photos/test1/katerina_falk_photos.zip', as_attachment=True)

@app.route('/brains/fuckup', methods=['GET', 'POST'])
def fuckup():
	return send_file('photos/fuckup/katerina_falk_photos.zip', as_attachment=True)