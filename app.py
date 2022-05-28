from flask import Flask, render_template 
import os

app = Flask(__name__)

@app.route('/')
def hello():
    user = os.environ['USER_NAME'] if 'USER_NAME' in os.environ else 'World'
    return render_template('hello.html', user=user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)