from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post' method=['GET', 'POST'])
def post():
    if request.method == 'POST':
        word = request.form['search']
        return render_template('post.html')

if __name__ == '__main__':
    app.run()
