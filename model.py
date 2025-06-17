import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer

# Load dataset
df = pd.read_csv("app_business_features.csv")

# NLP vectorization for business_type
tfidf = TfidfVectorizer()
business_type_vec = tfidf.fit_transform(df["business_type"])

# Normalize budget
scaler = StandardScaler()
budget_scaled = scaler.fit_transform(df[["budget"]])

# Combine all features
from scipy.sparse import hstack
X = hstack([business_type_vec, budget_scaled])

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=5, random_state=42)
df["cluster"] = kmeans.fit_predict(X)

# Function to get recommended features based on similar businesses
def recommend_features(business_type, budget):
    vec = tfidf.transform([business_type])
    scaled_budget = scaler.transform([[budget]])
    user_input = hstack([vec, scaled_budget])
    
    cluster = kmeans.predict(user_input)[0]
    
    similar = df[df["cluster"] == cluster]
    
    all_features = similar["features_used"].str.split(", ").explode()
    top_features = all_features.value_counts().head(5)
    
    return top_features.index.tolist()
