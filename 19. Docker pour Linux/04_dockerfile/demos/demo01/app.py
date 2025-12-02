from flask import Flask

app = Flask(__name__)

@app.route("/test") # localhost:5000/test
def home():
    return "Hello depuis le container"

@app.route("/hello")  # localhost:5000/hello
def hello():
    return "Hello world"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)