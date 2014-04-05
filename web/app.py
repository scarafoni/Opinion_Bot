from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hel():
    return "Hello World!"

@app.route("/layout")
def layout():
    render_template('layout.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
	app.run(debug=True)
