# Clustering Project

This project demonstrates **unsupervised learning** using clustering techniques.  
It includes both a **Jupyter Notebook** for analysis and a **Streamlit app** for deployment.

---

## 📂 Project Structure

Clustering/
│
├── notebooks/ # Jupyter notebooks (exploration & model building)
│ └── Clustering_DS_Portfolio.ipynb
│
├── app/ # Streamlit app for deployment
│ └── app.py
│
├── model/ # Serialized pipeline(s)
│ └── pipeline.pkl
│
├── data/ # CSV files (if applicable)
│ └── CountryAidAllocation.csv
│
├── requirements.txt # Python dependencies for deployment
├── .gitignore # Ignore virtual env, cache, etc.
└── README.md # Project documentation

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/clustering-project.git
cd clustering-project

2️⃣ Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate # On macOS/Linux

3️⃣ Install dependencies
pip install -r requirements.txt

Running the Streamlit App
streamlit run app/app.py

📊 Notebook

The notebooks/Clustering_DS_Portfolio.ipynb contains:
Data exploration
Feature preprocessing
Clustering pipeline (AgglomerativeClustering)
Cluster evaluation & visualization

📌 Notes
Agglomerative Clustering doesn’t support .predict(), so production usage is limited.
Virtual environments (e.g., capsule/) are excluded from GitHub via .gitignore.

🛠️ Built With

Python 3.11
Numpy 
Pandas
Seaborn
Scikit-Learn
Streamlit
Matplotlib

