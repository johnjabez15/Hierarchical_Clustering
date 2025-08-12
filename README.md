# Hierarchical Clustering Project – Country Grouping

## Overview

This project implements a **Hierarchical Clustering** algorithm to group a set of fictional countries based on socioeconomic and health indicators.

The model is trained using a custom dataset, and the results are visualized and deployed through a **Flask** web application. The application allows users to explore the clustering by selecting a desired number of clusters.

## Project Structure
```
DataScience/
│
├── Hierarchical Clustering/
│   ├── data/
│   │   └── gdp_health_data.csv
│   ├── model/
│   │   └── linkage_matrix.pkl
│   │   └── original_data.csv
│   ├── static/
│   │   └── style.css
│   │   └── dendrogram.png
│   ├── templates/
│   │   ├── index.html
│   │   └── result.html
│   ├── train_model.py
│   ├── app.py
│   └── requirements.txt
```

## Installation & Setup

1.  **Clone the repository**

    ```
    git clone <your-repo-url>
    cd "DataScience/Hierarchical Clustering"
    ```

2.  **Create a virtual environment (recommended)**

    ```
    python -m venv venv
    source venv/bin/activate  # For Linux/Mac
    venv\Scripts\activate     # For Windows
    ```

3.  **Install dependencies**

    ```
    pip install -r requirements.txt
    ```

## Dataset

The `gdp_health_data.csv` dataset contains socioeconomic and health data for 100 fictional countries, including the following features:

* **GDP** (numeric): Gross Domestic Product
* **Literacy_Rate** (numeric): Percentage of the population that can read and write
* **Life_Expectancy** (numeric): Average number of years a person is expected to live

## Problem Statement

Instead of predicting an outcome, this project aims to discover underlying patterns and structures within the data. By applying hierarchical clustering, we can group countries with similar characteristics, which can be useful for policymakers, researchers, and economic analysts to identify country archetypes.

## Why Hierarchical Clustering?

* **Hierarchical Structure:** It creates a tree-like hierarchy of clusters called a dendrogram, which visually shows the relationships between data points and clusters at different levels.
* **No Pre-defined Number of Clusters:** You do not need to specify the number of clusters in advance. The dendrogram helps in deciding the optimal number of clusters by observing the longest distances between merges.
* **Informative Visualization:** The dendrogram is a powerful tool for interpreting the clustering results, providing insights into how clusters are formed and which data points are most similar.

## How to Run

1.  **Train the Model**

    ```
    python train_model.py
    ```

    This will create:
    * `linkage_matrix.pkl` (the core clustering result)
    * `dendrogram.png` (a visual representation of the hierarchy)
    * `original_data.csv` (a copy of the dataset for the app)

2.  **Run the Flask App**

    ```
    python app.py
    ```

    Visit `http://127.0.0.1:5000/` in your browser.

## Frontend Input Example

The application will prompt you to select the number of clusters you want to see.

Select Number of Clusters (2-10): [Input field, e.g., 3]
## Prediction Goal

The application will not provide a single prediction but rather a cluster assignment for each country, for example: `Country_5 is in Cluster 2`.

## Tech Stack

* **Python** – Core programming language
* **Pandas** – Data manipulation
* **Scikit-learn** – Data standardization
* **SciPy & Matplotlib** – Clustering and visualization
* **Flask** – Web framework for deployment
* **HTML/CSS** – Frontend UI design

## Future Scope

* Add an interactive feature where a user can hover over a point on the dendrogram to see the country details.
* Implement other clustering methods (e.g., K-Means) for comparison.
* Allow users to choose different linkage methods (e.g., 'single', 'complete') to see how the clustering changes.

## Screenshots

**Home Page:**<img width="1920" height="1080" alt="Screenshot (49)" src="https://github.com/user-attachments/assets/24f64b2d-a9db-4a3a-bcb0-59b48e409cf4" />


**Result Page:**<img width="1920" height="1080" alt="Screenshot (50)" src="https://github.com/user-attachments/assets/948061a7-ff01-4994-9202-41dd45811b08" />

