from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/list')
def list():
	return render_template('list.html', names = ['ben', 'harry', 'bob', 'jay', 'matt', 'bill'])

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)
	
