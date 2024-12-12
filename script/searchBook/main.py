import os
import sys
import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# cache
os.environ["TRANSFORMERS_CACHE"] = "/Users/wys/transformers_cache"

def load_and_clean_data(file_path):
    try:
        df = pd.read_csv(file_path, on_bad_lines='skip', encoding='utf-8', low_memory=False, escapechar='\\', quoting=1)
        df['title'] = df['title'].fillna('').str.strip()
        df['authors'] = df['authors'].fillna('').str.strip()
        df['text_features'] = df['title'] + ' ' + df['authors']
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        sys.exit(1)

def recommend_based_on_query(query, df, tfidf):
    try:
        query_vector = tfidf.transform([query])
        tfidf_matrix = tfidf.transform(df['text_features'].fillna(''))
        similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()
        top_indices = similarities.argsort()[::-1][:5]
        return df.iloc[top_indices]['title'].tolist()
    except Exception as e:
        print(f"Error in TF-IDF recommendation: {e}")
        return []

def semantic_recommend_based_on_query(query, df):
    try:
        model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2', cache_folder="/Users/wys/transformers_cache")
        query_embedding = model.encode(query)
        book_embeddings = model.encode(df['text_features'].fillna(''))
        similarities = cosine_similarity([query_embedding], book_embeddings).flatten()
        top_indices = similarities.argsort()[::-1][:5]
        return df.iloc[top_indices]['title'].tolist()
    except Exception as e:
        print(f"Error in semantic recommendation: {e}")
        return []

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python recommend.py '<query>'")
        sys.exit(1)

    query = sys.argv[1]
    file_path = "books.csv"
    df = load_and_clean_data(file_path)

    # TF-IDF 
    tfidf = TfidfVectorizer(stop_words="english", max_features=5000, strip_accents='unicode', token_pattern=r'\w+')
    tfidf.fit(df["text_features"].fillna(''))
    tfidf_recommendations = recommend_based_on_query(query, df, tfidf)

    # semantic_recommendations
    semantic_recommendations = semantic_recommend_based_on_query(query, df)

    # result
    result = {
        "query": query,
        "tfidf_recommendations": tfidf_recommendations,
        "semantic_recommendations": semantic_recommendations
    }
    print(json.dumps(result, ensure_ascii=False))
