from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


def cluster_transactions(df, max_clusters=5):
    n_clusters = min(max_clusters, df.shape[0])
    
    if n_clusters < 2:
        df['Category'] = 0
        return df

    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(df['Description'])

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['Category'] = kmeans.fit_predict(X)

    return df
