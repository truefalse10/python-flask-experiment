from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    # execute julias function and return image url
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
