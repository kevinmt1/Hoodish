from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    address = db.Column(db.String(300))
    cart = db.relationship('Cart', backref='user', uselist=False)
    transaction_header = db.relationship('Transactionheader')

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    price = db.Column(db.Integer)
    stock = db.Column(db.Integer)
    discount = db.Column(db.Integer)
    img = db.Column(db.String)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    cart_items = db.relationship('CartItem')

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    size = db.Column(db.String(30))
    qty = db.Column(db.Integer)

class Transactionheader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    total_price = db.Column(db.Integer)
    transactions = db.relationship('TransactionItem')

class TransactionItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    qty = db.Column(db.Integer)
    size = db.Column(db.String(30))
    transaction_header_id = db.Column(db.Integer, db.ForeignKey('transactionheader.id'))

class PaymentDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transaction_header_id = db.Column(db.Integer, db.ForeignKey('transactionheader.id'))
    status = db.Column(db.String(20))
    method = db.Column(db.String(30))
    total_price = db.Column(db.Integer)
