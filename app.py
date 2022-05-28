from flask import Flask, render_template 
import os

app = Flask(__name__)

@app.route('/')
def hello():
    user = os.environ['USER_NAME'] if 'user_name' in os.environ else 'World'
    return render_template('hello.html', user=user)

app.run(port=8080, debug=True)