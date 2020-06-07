from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return """
        Welcome to my website!<br /><br />
        <a href="/hello">Go to hello world</a>"""

@app.route("/hello")
def hello():
    return """
        Hello World!<br /><br />
        <a href="/">Back to index</a>"""

if __name__ == '__main__':
    app.run(host='0.0.0.0')