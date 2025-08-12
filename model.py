# train_model.py

import pandas as pd
import os
import pickle
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import linkage, dendrogram

# Paths
DATA_PATH = os.path.join("dataset", "gdp_health_data.csv")
MODEL_DIR = "model"
LINKAGE_MATRIX_PATH = os.path.join(MODEL_DIR, "linkage_matrix.pkl")
DENDROGRAM_PATH = os.path.join("static", "dendrogram.png")

# Create directories if they don't exist
os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs("static", exist_ok=True)

print("Loading data...")
try:
    df = pd.read_csv(DATA_PATH)
except FileNotFoundError:
    print(f"Error: Dataset file not found at {DATA_PATH}")
    exit()

print("Standardizing features...")
features = ['GDP', 'Literacy_Rate', 'Life_Expectancy']
X = df[features]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Performing hierarchical clustering and saving linkage matrix...")
# The linkage matrix is the core output of hierarchical clustering, representing the merges
linked = linkage(X_scaled, method='ward')

# Save the linkage matrix to a pkl file
with open(LINKAGE_MATRIX_PATH, "wb") as f:
    pickle.dump(linked, f)

print(f"Linkage matrix saved to {LINKAGE_MATRIX_PATH}")

print("Generating and saving the dendrogram...")
plt.figure(figsize=(15, 8))
dendrogram(linked,
           orientation='top',
           labels=df['Country'].values,
           distance_sort='descending',
           show_leaf_counts=True)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Country')
plt.ylabel('Euclidean Distance')
plt.tight_layout() # Adjust plot to ensure all labels fit
plt.savefig(DENDROGRAM_PATH)
plt.close() # Close the plot to avoid displaying it in the terminal

print(f"Dendrogram saved to {DENDROGRAM_PATH}")

# Save the original dataframe to be used by the app.py
df.to_csv(os.path.join(MODEL_DIR, "original_data.csv"), index=False)
