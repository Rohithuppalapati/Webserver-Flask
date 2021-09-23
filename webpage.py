from flask import Flask
app=Flask(__name__)

@app.route('/')
def new():
    return 'Hello World'

@app.route('/blog')
def blog():
    return 'this is my blog'

@app.route('/about')
def about():
    return 'about the webpage.html'
