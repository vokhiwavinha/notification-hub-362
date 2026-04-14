from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return {"status": "ok", "version": "2.5"}

if __name__ == "__main__":
    app.run(debug=True, port=6777)
