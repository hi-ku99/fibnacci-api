from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError

app = Flask(__name__)

@app.route("/fib")
def get_request():

    n = request.args.get("n",type=int)
    a, b = 0, 1
    
    while n:
         n-=1
         a, b = b, a+b
    
    return jsonify({"results" : b})

# URLの構文エラー
@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return jsonify({"status":400, "message":"Bad request."})

# 間違ったURLにアクセス
@app.errorhandler(NotFound)
def handle_bad_request(e):
    return jsonify({"status":404, "message":"Not found."})

# サーバー内部で何らかのエラーが発生し、HTTPの要求を完了できなかった
@app.errorhandler(InternalServerError)
def handle_bad_request(e):
    return jsonify({"status":500, "message":"Internal server error."})

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=80, debug=True)

