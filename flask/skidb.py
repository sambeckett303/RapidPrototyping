from flask import Flask
from flask import render_template
from flask import request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resorts.db'
db = SQLAlchemy(app)

app.debug = True

class Resorts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    base = db.Column(db.Integer)
    peak = db.Column(db.Integer)
    runs = db.Column(db.Integer)
    parks = db.Column(db.Integer)

    def __init__(self, name, base, peak, runs, parks):
        self.name = name
        self.base = base
        self.peak = peak
        self.runs = runs
        self.parks = parks

    def __repr__(self):
        return 'Name: %r' % str(self.name)

@app.route('/register', methods=['POST', 'GET'])
def register():
	return render_template('skiregister.html')

@app.route('/search', methods=['POST', 'GET'])
def search():
	if request.method == 'POST':
		name = request.form['resortname']
		base = request.form['base_elevation']
		peak = request.form['peak_elevation']
		runs = request.form['runs']
		tparks = request.form['terrainparks']
		newresort = Resorts(name, base, peak, runs, tparks)
		db.session.add(newresort)
		db.session.commit()
		print 'Name:'+name
		print 'Base:'+base
		print 'Peak:'+peak
		print 'Runs:'+runs
		print 'Parks:'+tparks
		return 'Yo data was added.'
	else: 
		resortData = Resorts.query.all()
		return render_template('skisearch.html', resorts = resortData)

if __name__ == '__main__':

	app.run()

