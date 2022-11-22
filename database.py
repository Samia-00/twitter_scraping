from sqlalchemy import create_engine, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, String, Integer, Date

engine = create_engine('sqlite:///twitter.db', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

posts_comments_association = Table(
    'posts_comments', Base.metadata,
    Column('post_id', Integer, ForeignKey('posts.id')),
    Column('comment_id', Integer, ForeignKey('comments.id'))
)
posts_retweets_association = Table(
    'posts_retweets', Base.metadata,
    Column('post_id', Integer, ForeignKey('posts.id')),
    Column('retweet_id', Integer, ForeignKey('retweets.id'))
)

class Posts(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    n_comments = Column(Integer)
    n_retweets = Column(Integer)
    n_like = Column(Integer)
    post_url = Column(String)
    post_time = Column(String)
    post_text = Column(String)
    comments = relationship("Comments", secondary=posts_comments_association)
    retweets = relationship("Retweets", secondary=posts_retweets_association)

    def __init__(self, n_comments, n_retweets, n_like, post_url, post_time, post_text):
        self.n_comments = n_comments
        self.n_retweets = n_retweets
        self.n_like = n_like
        self.post_url = post_url
        self.post_time = post_time
        self.post_text = post_text


class Comments(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    profile_url = Column(String)
    commenter_name = Column(String)
    comment_time = Column(String)
    comment_text = Column(String)

    def __init__(self, profile_url, commenter_name, comment_time, comment_text):
        self.profile_url = profile_url
        self.commenter_name = commenter_name
        self.comment_time = comment_time
        self.comment_text = comment_text

class Retweets(Base):
    __tablename__ = 'retweets'

    id = Column(Integer, primary_key=True)
    retweeter_profile_url = Column(String)
    retweeter_name = Column(String)
    retweet_text = Column(String)

    def __init__(self, retweeter_profile_url, retweeter_name, retweet_text):
        self.retweeter_profile_url = retweeter_profile_url
        self.retweeter_name = retweeter_name
        self.retweet_text = retweet_text

