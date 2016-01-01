from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # index: 如果设为 True,为这列创建索引,提升查询效率
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    # backref: 在关系的另一个模型中添加反向引用
    # lazy: 指定如何加载相关记录。
    # 可选值有 select(首次访问时按需加载)、immediate(源对象加 载后就加载)、joined(加载记录,但使用联结)、subquery(立即加载,但使用子查询),
    # noload(永不加载)和 dynamic(不加载记录,但提供加载记录的查询)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.nickname)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)
