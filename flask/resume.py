from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/resume/')
@app.route('/resume/<name>')
def hello(name=None):
    return render_template('ResumeLanding.html', name=name)

if __name__ == '__main__':

    app.run()