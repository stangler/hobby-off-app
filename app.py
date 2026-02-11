from flask import Flask

app = Flask(__name__)

@app.get("/")
def hello():
    return "Hello, uv + Flask!"

if __name__ == "__main__":
    # デバッグ用の簡易サーバーを起動します。
    app.run(debug=True, host="127.0.0.1", port=5000)