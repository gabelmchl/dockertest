# import main Flask class and request object
from flask import Flask, request
from flask_cors import CORS, cross_origin

# create the Flask app
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/query-example')
def query_example():
    # if key doesn't exist, returns None
    number = request.args.get('number')

    return str(2 * int(number))

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)