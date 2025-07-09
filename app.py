from flask import Flask, render_template, request, redirect, url_for, session
import os
import csv
from datetime import datetime
from collections import defaultdict
import pandas as pd

app = Flask(__name__)
app.secret_key = 'chave-secreta-simples'

LOG_FILE = 'logs/user_interactions.csv'
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

def log_interaction(event_type, product_id):
    with open(LOG_FILE, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([datetime.now(), session.get('session_id', 'anonymous'), event_type, product_id])

@app.before_request
def create_session():
    if 'session_id' not in session:
        session['session_id'] = str(datetime.now().timestamp())

# Lista realista de produtos conforme modelagem
df = pd.read_csv('products.csv')
products = df.to_dict(orient='records')

@app.route('/')
def home():
    selected_category = request.args.get('category')
    filtered_products = [p for p in products if not selected_category or p['category'] == selected_category]

    categorized = defaultdict(list)
    for p in filtered_products:
        categorized[p['category']].append(p)

    available_categories = sorted(set(p['category'] for p in products))

    return render_template('home.html', categorized_products=categorized, available_categories=available_categories)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product is None:
        return "Produto não encontrado", 404
    log_interaction('view', product_id)
    return render_template('product.html', product=product)

@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    grouped_cart = defaultdict(lambda: {'product': None, 'quantity': 0})
    for item in cart_items:
        pid = item['id']
        grouped_cart[pid]['product'] = item
        grouped_cart[pid]['quantity'] += 1
    cart_display = list(grouped_cart.values())
    return render_template('cart.html', cart_items=cart_display)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    cart = session.get('cart', [])
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        cart.append(product)
        session['cart'] = cart
        log_interaction('add_to_cart', product_id)
    return redirect(url_for('cart'))

@app.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    cart = session.get('cart', [])
    for i, item in enumerate(cart):
        if item['id'] == product_id:
            del cart[i]
            break
    session['cart'] = cart
    return redirect(url_for('cart'))

@app.route('/clear_cart')
def clear_cart():
    session['cart'] = []
    return redirect(url_for('cart'))

if __name__ == '__main__':
    app.run(debug=True)