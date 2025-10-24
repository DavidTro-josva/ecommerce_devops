from flask import Blueprint, render_template, session, redirect, url_for
from app.products import PRODUCTS

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html', products=PRODUCTS)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    return render_template('cart.html', cart=cart_items)

@main.route('/add/<int:product_id>')
def add_to_cart(product_id):
    cart = session.get('cart', [])
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if product:
        cart.append(product)
        session['cart'] = cart
    return redirect(url_for('main.cart'))

