from flask import Flask,request, jsonify
app = Flask(__name__)

@app.route('/fib')
def get_request():

    n = int(request.args.get('n', ''))
    a, b = 0, 1
    fib_l=[]
    
    while n:
         n-=1
         fib_l.append(b)
         a, b = b, a+b
    
    fib_sum = sum(fib_l)

    body = { "results" : fib_sum}
    
    return body

# @app.errorhandler(BadRequest)
# @app.errorhandler(NotFound)
# @app.errorhandler(InternalServerError)
# def error_handler(e):
#   res = jsonify({   
#                   "status": e.name, 
#                   "message": e.name 
#                  })
#   return res, e.code


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=80, debug=True)
#  app.run()





