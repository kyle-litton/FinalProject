from flask import Flask
		
app = Flask(__name__)
		
@app.route('/')
def index():
	return 'this is a test for the local host'
		
if __name__ == '__main__':
	app.run(debug=True)