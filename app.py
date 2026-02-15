from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/components')
def components():
    return render_template('components.html')

@app.route('/admission')
def admission():
    return render_template("admission.html")

@app.route('/gallary')
def gallary():
    return render_template("gallery.html")

@app.route('/newsLetter')
def newsLetter():
    return render_template("newsLetter.html")

@app.route('/notice')
def notice():
    return render_template("notice.html")


if __name__ == '__main__':
    app.run(debug=True, port=8000)