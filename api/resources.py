from flask_restful import Resource, marshal_with, fields
from models import Blog as blog_model

blog_resource = {
   "title": fields.String,
   "description": fields.String
}

class Blog(Resource):
    @marshal_with(blog_resource)
    def get(self):
        blogs = blog_model.query.all()
        return blogs