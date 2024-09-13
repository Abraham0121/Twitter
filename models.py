from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    username = db.Column(db.String(30), primary_key=True)
    password = db.Column(db.String(30), nullable=False)
    bio = db.Column(db.String(500))

    def has_tweet(self):
        return db.session.query(Tweet).filter_by(from_username=self.username).count() > 0

class Tweet(db.Model):
    __tablename__ = "tweets"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    from_username = db.Column(db.String, db.ForeignKey("users.username"))

    def get_tweets(self):
        return Tweet.query.filter_by(from_username=self.username).all()

class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    tweet_id = db.Column(db.Integer, db.ForeignKey("tweets.id"))


class Follow(db.Model):
    __tablename__ = "follows"

    id = db.Column(db.Integer, primary_key=True)
    from_username = db.Column(db.String, db.ForeignKey("users.username"))
    to_username = db.Column(db.String, db.ForeignKey("users.username"))


class Like(db.Model):
    __tablename__ = "likes"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String, db.ForeignKey("users.username"))
    tweet_id = db.Column(db.Integer, db.ForeignKey("tweets.id"))


class Bookmark(db.Model):
    __tablename__ = "bookmarks"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String, db.ForeignKey("users.username"))
    tweet_id = db.Column(db.Integer, db.ForeignKey("tweets.id"))





