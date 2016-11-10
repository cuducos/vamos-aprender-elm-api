import json
from datetime import datetime

from flask import Flask, request
from flask_cors import CORS
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
api = Api(app)
db = SQLAlchemy(app)
CORS(app)


class Comment(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(32))
    content = db.Column(db.Text())
    date = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return 'Comment by {} on {}'.format(self.author, self.date)

    @property
    def as_dict(self):
        return {
            'id': self.id,
            'author': self.author,
            'content': self.content,
            'date': self.date.isoformat()
        }


class CommentsApi(Resource):

    def get(self):
        comments = [comment.as_dict for comment in Comment.query.all()]
        return dict(comments=comments)

    def post(self):
        form = json.loads(request.data.decode('utf-8'))
        comment = Comment(
            author=form.get('author'),
            content=form.get('content'),
            date=form.get('date')
        )
        db.session.add(comment)
        db.session.commit()
        return comment.as_dict, 201


class CommentApi(Resource):

    def get(self, comment_id):
        comment = Comment.query.get(comment_id)
        if comment:
            return comment.as_dict, 200
        return 'Comment not found', 404

    def delete(self, comment_id):
        comment = Comment.query.get(comment_id)
        if comment:
            db.session.delete(comment)
            db.session.commit()
            return comment.as_dict, 204
        return 'Comment not found', 404

api.add_resource(CommentsApi, '/api/comments/')
api.add_resource(CommentApi, '/api/comment/<comment_id>/')

db.create_all()
comments = (
    dict(author='John Doe', content="Ahoy, cap'n"),
    dict(author='Joane Doe', content="What be happenin', matey?"),
    dict(author='Buccaneer', content="What say ye, ya scurvy dog"),
)
[db.session.add(Comment(**comment)) for comment in comments]
db.session.commit()
