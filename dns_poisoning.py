# dns poising in website mitigation example 
from flask import Flask, request, make_response


app = Flask(__name__)
@app.after_request
def set_secure_headers(response):
    response.headers['Cache-control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response

@app.route('/')
def index():
    resp = make_response("Welcome to the secure website!")
    return resp
if __name__ == '__main__':
    app.run(debug=True)

    