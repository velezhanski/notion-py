from flask import Flask
from flask_restful import Api

from api import Todo

app = Flask(__name__)
api = Api(app)

api.add_resource(Todo, "/todo/<string:id>")

if __name__ == "__main__":
  app.run()