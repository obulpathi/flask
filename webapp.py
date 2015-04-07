import os

from flask import Flask, render_template
from flask import send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/debug')
def debug():
    x = "hi"
    y = 2

    return x + y

@app.route('/user/<username>')
def user(username):
    return username

@app.route('/post/<int:post_id>')
def post(post_id):
    return 'Post {0}'.format(post_id)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/login', methods = ['GET'])
def get_login():
    return 'Get credentials'

@app.route('/login', methods = ['POST'])
def post_login():
    return 'Check credentials'

if __name__ == '__main__':
  app.run(debug=True)
