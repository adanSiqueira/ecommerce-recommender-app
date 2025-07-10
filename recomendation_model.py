
import os
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_data(path=os.path.join(os.path.dirname(__file__),'products.csv')):
    df = pd.read_csv(path)
    df.drop('image', axis=1, inplace=True)
    df['features'] = df[['name','category', 'gender', 'age_group', 'color', 'season', 'type']].fillna('').apply(
        lambda row: ' '.join([str(item) if not isinstance(item, list) else ' '.join(map(str, item)) for item in row]), axis=1)
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df['features'])
    return df, tfidf_matrix

def get_user_vector(log_data, df, tfidf_matrix):
    # Define os pesos das ações
    ACTION_WEIGHTS = {
        'view': 0.2,
        'add_to_cart': 0.7,
        'purchase': 1.0,
        'remove_from_cart': -0.3  # pode ignorar se não usar
    }

    vectors = []
    weights = []

    for entry in log_data:
        action = entry.get('action')
        product_id = entry.get('product_id')

        if action not in ACTION_WEIGHTS:
            continue

        weight = ACTION_WEIGHTS[action]
        index = df[df['id'] == product_id].index

        if not index.empty:
            vec = tfidf_matrix[index[0]].toarray()[0]
            vectors.append(vec * weight)
            weights.append(abs(weight))  # valor absoluto para média ponderada

    if not vectors:
        return np.zeros(tfidf_matrix.shape[1])

    user_vector = np.sum(vectors, axis=0) / np.sum(weights)
    return user_vector


def get_recommendations_from_vector(user_vector, df, tfidf_matrix, top_n=5):
    similarities = cosine_similarity([user_vector], tfidf_matrix).flatten()
    df_copy = df.copy()
    df_copy['similarity'] = similarities
    return df_copy.sort_values('similarity', ascending=False).head(top_n)