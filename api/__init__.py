from flask_restful import Api
from .resources import Blog


api = Api(prefix='/api/blogs')
api.add_resource(Blog, '/')
