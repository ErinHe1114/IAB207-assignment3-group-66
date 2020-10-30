from flask_sqlalchemy import SQLAlchemy

from . import db

import datetime


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(16),nullable=False)
    password = db.Column(db.String(16),nullable=False)
    email = db.Column(db.String(16),nullable=False)
    is_active=db.Column(db.Boolean,default=True)
    is_authenticated=db.Column(db.Boolean,default=True)
    is_anonymous=db.Column(db.Boolean,default=True)
    createtime=db.Column(db.DateTime,default=datetime.datetime.now())
    def __init__(self,username,password,email):
        self.username=username
        self.password=password
        self.email=email
    def get_id(self):
        return self.id
    def savebyadd(self): 
        try:
            db.session.add(self)
            db.session.commit()
        except BaseException:
            db.session.rollback()


# class Categort(db.Model):
#     __tablename__="watchs"
#     id=db.Column(db.Integer,primary_key=True,autoincrement=True)
#     categort=db.Column(db.String(16),nullable=False)

class Watch(db.Model):
    __tablename__="watchs"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    categortid=db.Column(db.String(16),nullable=False)
    name=db.Column(db.String(36),nullable=False)
    brand=db.Column(db.String(16),nullable=False)
    size=db.Column(db.String(16),nullable=False)
    price=db.Column(db.String(16),nullable=False)
    condition=db.Column(db.String(16),nullable=False)
    quantity=db.Column(db.Integer,nullable=False)
    goline=db.Column(db.Boolean,default=False)
    description=db.Column(db.Text)
    fileurl=db.Column(db.String(36))
    createtime=db.Column(db.DateTime,default=datetime.datetime.now())
    status=db.Column(db.String(16),default='Bidding')
    def __init__(self,categortid,name,brand,size,price,condition,quantity,goline,description,fileurl):
        self.categortid=categortid
        self.name=name
        self.brand=brand
        self.size=size
        self.price=price
        self.condition=condition
        self.quantity=quantity
        self.goline=goline
        self.description=description
        self.fileurl=fileurl
    def get_id(self):
        return self.id
    def updatestatus(self,status):
        self.status=status
        return self.status
    def savebyadd(self):
        try:
            db.session.add(self)
            db.session.commit()
        except BaseException:
            db.session.rollback()



class WatchList(db.Model):
    __tablename__="watchlist"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    watchid=db.Column(db.Integer,db.ForeignKey('watchs.id'))
    userid=db.Column(db.Integer,db.ForeignKey('users.id'))
    createtime=db.Column(db.DateTime,default=datetime.datetime.now())
    def __init__(self,watchid,userid):
        self.watchid=watchid
        self.userid=userid
    def get_id(self):
        return self.id
    def savebyadd(self):
        try:
            db.session.add(self)
            db.session.commit()
        except BaseException:
            db.session.rollback()

class Cart(db.Model):
    __tablename__="cart"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    watchid=db.Column(db.Integer,db.ForeignKey('watchs.id'))
    userid=db.Column(db.Integer,db.ForeignKey('users.id'))
    createtime=db.Column(db.DateTime,default=datetime.datetime.now())
    def __init__(self,watchid,userid):
        self.watchid=watchid
        self.userid=userid
    def get_id(self):
        return self.id
    def savebyadd(self):
        try:
            db.session.add(self)
            db.session.commit()
        except BaseException:
            db.session.rollback()

class BidRecord(db.Model):
    __tablename__="bidrecord"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    watchid=db.Column(db.Integer,db.ForeignKey('watchs.id'))
    userid=db.Column(db.Integer,db.ForeignKey('users.id'))
    price=db.Column(db.String(16),nullable=False)
    createtime=db.Column(db.DateTime,default=datetime.datetime.now())
    def __init__(self,watchid,userid,price):
        self.watchid=watchid
        self.userid=userid
        self.price=price
    def get_id(self):
        return self.id
    def savebyadd(self):
        try:
            db.session.add(self)
            db.session.commit()
        except BaseException:
            db.session.rollback()

class Reviews(db.Model):
    __tablename__="reviews"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    watchid=db.Column(db.Integer,db.ForeignKey('watchs.id'))
    userid=db.Column(db.Integer,db.ForeignKey('users.id'))
    comment=db.Column(db.String(200),nullable=False)
    createtime=db.Column(db.DateTime,default=datetime.datetime.now())
    def __init__(self,watchid,userid,comment):
        self.watchid=watchid
        self.userid=userid
        self.comment=comment
    def get_id(self):
        return self.id
    def savebyadd(self):
        try:
            db.session.add(self)
            db.session.commit()
        except BaseException:
            db.session.rollback()

