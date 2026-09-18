from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloApi(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloApi, '/helloworld')

@app.route("/")
def helloWorld():
    return "<p>Hello world!</p>"

if __name__ == '__main__':
    app.run(debug=True)