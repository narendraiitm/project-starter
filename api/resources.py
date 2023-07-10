from flask_restful import Resource, marshal_with, fields
from models import Blog as blog_model
from flask_security import auth_required

blog_resource = {
   "title": fields.String,
   "description": fields.String
}

class Blog(Resource):
    @marshal_with(blog_resource)
    @auth_required('token')
    def get(self):
        blogs = blog_model.query.all()
        return blogs