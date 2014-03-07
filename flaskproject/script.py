from flask import render_template
from flask import request
from flask import Flask
app = Flask(__name__)

@app.route('/home', methods=['POST', 'GET'])
def home():
	if request.method == 'POST':
		a = request.form['user']
		b = request.form['email']
		print 'User:'+ a
		print 'Email:'+ b
		return render_template('p52.html', u=a, s=b)
	else:
		return render_template('Project5.html')


if __name__ == '__main__':

    app.run()