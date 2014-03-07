from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/planets', methods=['POST', 'GET'])
def planets():
	searchword = request.args.get('search', '')
	if (searchword == 'Mars'):
		return render_template('deathstarcustom2.html')
	else:
		return render_template('deathstarcustom.html')


if __name__ == '__main__':
    app.run()