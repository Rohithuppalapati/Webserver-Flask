from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def new():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return 'this is my blog'

@app.route('/about')
def about():
    return 'about the webpage.html'
