from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
import json
from .models import Product, Cart, CartItem, Transactionheader, TransactionItem
from . import db

views = Blueprint('views', __name__)

@views.route('/')

def home():
    return render_template("home.html", user=current_user, products=Product.query.all())


@views.route('/edit-profile')
def editProfile():
    return render_template("edit-profile.html", user=current_user)

@views.route('/display/<filename>')
def display_image(filename):
    print(filename)
    return redirect(url_for('static', filename = filename), code=301)


@views.route('/product/<product>', methods=['GET'])
def show_product(product):
    _product = Product.query.get(product)
    return render_template("product.html", user=current_user, product=_product)

@views.route('/cart')
def cart():
    user = current_user
    cart = Cart.query.filter_by(user_id = user.id).first()
    p_id = []
    cart_length = 0
    for cart_items in cart.cart_items:
        cart_length  += 1
        p_id.append(cart_items.product_id)
    products = []
    for id in p_id:
        product = Product.query.filter_by(id = id).first()
        products.append(product)
    return render_template("cart.html", user=user, products=products, cart_items = cart.cart_items)

@views.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    print("Function called")
    product = json.loads(request.data)
    cart_id = current_user.cart.id
    new_cart_item = CartItem(cart_id = cart_id, product_id = product['productId'], size = product['size'], qty=product['qty'])
    db.session.add(new_cart_item)
    db.session.commit()

    return jsonify({})

@views.route('/confirm_transaction', methods=['POST'])
def confirm_transaction():
    _json = json.loads(request.data)
    cart = current_user.cart
    print(cart)

    transaction_header = Transactionheader(user_id=current_user.id, total_price=_json['total_price'])
    db.session.add(transaction_header)
    db.session.commit()

    for cart_items in cart.cart_items:
        p_id = cart_items.product_id
        qty = cart_items.qty
        size = cart_items.size
        transaction_item = TransactionItem(product_id = p_id, qty = qty, size = size, transaction_header_id = transaction_header.id)
        db.session.add(transaction_item)
        db.session.delete(cart_items)
        db.session.commit()

    return jsonify({})

@views.route('/transaction')
def show_transaction():
    t_header = current_user.transaction_header
    products = []
    transactions = []
    print(t_header)
    for t in t_header:
        dict = {}
        dict["header"] = t
        dict["transactions"] = []
        ti_list = []
        products_list = []
        t_items = t.transactions
        for ti in t_items:
            product = Product.query.filter_by(id=ti.product_id).first()
            products.append(product)
            ti_list.append(ti)
            products_list.append(product)
        dict['transactions'].append(zip(ti_list, products_list))
        print(ti_list)
        print(products_list)
        transactions.append(dict)
    print(transactions)

    return render_template("transaction.html", user=current_user, transactions=transactions)