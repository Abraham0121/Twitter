from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.model):
    __tablename__ = "users"

    username = db.Column(db.String(30), primary_key=True)
    password = db.Column(db.String(30), nullable=False)
    bio = db.Column(db.String(500))


class Tweet(db.model):
    __tablename__ = "tweets"

    id = db.Column(db.Integer, primary=True)
    text = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    from_username = db.Column(db.String, db.ForeignKey("users.username"))


class Comment(db.model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary=True)
    text = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    tweet_id = db.Column(db.Integer, db.ForeignKey("tweets.id"))


class Follow(db.model):
    __tablename__ = "follows"

    id = db.Column(db.Integer, primary=True)
    from_username = db.Column(db.String, db.ForeignKey("users.username"))
    to_username = db.Column(db.String, db.ForeignKey("users.username"))


class Like(db.model):
    __tablename__ = "likes"

    id = db.Column(db.Integer, primary=True)

    username = db.Column(db.String, db.ForeignKey("users.username"))
    tweet_id = db.Column(db.Integer, db.ForeignKey("tweets.id"))


class Bookmark(db.model):
    __tablename__ = "bookmarks"

    id = db.Column(db.Integer, primary=True)

    username = db.Column(db.String, db.ForeignKey("users.username"))
    tweet_id = db.Column(db.Integer, db.ForeignKey("tweets.id"))





