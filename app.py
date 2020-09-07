from flask import Flask
from flask_restful import Api

from api import Category

app = Flask(__name__)
api = Api(app)

api.add_resource(Category, "/category/<string:id>")

if __name__ == "__main__":
  app.run()