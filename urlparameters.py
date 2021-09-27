from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def default():
    return render_template('index.html')

@app.route('/<username>/<int:post_id>')
def new(username=None,post_id=None):
    return render_template('index.html',name=username,id=post_id)

