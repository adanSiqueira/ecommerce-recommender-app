from flask import Flask, render_template, request, redirect, url_for, session
import numpy as np
import os
import csv
from datetime import datetime
from collections import defaultdict
import pandas as pd
from recomendation_model import load_data, get_user_vector, get_recommendations_from_vector

#Instancing app
app = Flask(__name__)
app.secret_key = 'chave-secreta-simples'

#Creating Log Registering
LOG_FILE = 'logs/user_interactions.csv'
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

def log_interaction(event_type, product_id):
    with open(LOG_FILE, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([datetime.now(), session.get('session_id', 'anonymous'), event_type, product_id])

df = pd.read_csv('products.csv')
products = df.to_dict(orient='records')
df_r, tfidf_matrix = load_data()

@app.before_request
def create_session():
    if 'session_id' not in session:
        session['session_id'] = str(datetime.now().timestamp())

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
    # Pega o produto atual
    product = df[df['id'] == product_id].to_dict(orient='records')
    if not product:
        return "Produto não encontrado", 404
    product = product[0]

    # Simulação do log do usuário (idealmente, viria da sessão ou banco)
    log_data = [
        {'action': 'view', 'product_id': product_id},
        # Aqui você pode adicionar outras interações anteriores do usuário
    ]

    # Geração do vetor e recomendações
    user_vector = get_user_vector(log_data, df_r, tfidf_matrix)
    recommended_df = get_recommendations_from_vector(user_vector, df, tfidf_matrix, top_n=4)

    # Converte para lista de dicionários para o template
    recommended_products = recommended_df.to_dict(orient='records')

    return render_template(
        'product.html',
        product=product,
        recommended_products=recommended_products
    )

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

@app.route('/recommendations')
def recommendations():
    cart = session.get('cart', [])
    product_ids = [p['id'] for p in cart]
    if not product_ids:
        return render_template('recommendations.html', products=[])
    user_vector = np.array(tfidf_matrix[df_r[df_r['id'].isin(product_ids)].index].mean(axis=0)).flatten()
    recommendations = get_recommendations_from_vector(user_vector, df, tfidf_matrix, top_n=15)
    recommendations = recommendations[~recommendations['id'].isin(product_ids)]

    return render_template('recommendations.html', products=recommendations.to_dict(orient="records"))


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