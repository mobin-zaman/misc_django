
class Config(object):
    SQLALCHEMY_DATABASE_URI='mysql://root:amarsql@localhost/joke'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ...
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'app.db')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False