from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    return 'Hello Sam Beckett - Rapid Prototyping 2014'

@app.route('/find', methods=['POST', 'GET'])
def find():
	searchword = request.args.get('course', '')
	print("["+searchword+"]")
	searchword.rstrip()
	if searchword == 'csci1300':
		return 'Find the classroom for CSCI1300 ... ATLAS 100'
	if searchword == 'csci2240':
		return 'Find the classroom for CSCI2240 ... ITLL 1B50'
	else:
		return 'Find the classroom for ' + searchword + ' ...  Sorry no result for ' + searchword +'.'
	
	

@app.route('/notification')
def notification():
	return 'Get notification - to be implemented'

if __name__ == '__main__':
    app.run()