# 📊 CORD-19 Sample Data Explorer

This project explores COVID-19 research metadata from the CORD-19 dataset.  
A smaller **sample** is used for demonstration because the full dataset is too large for GitHub.

---

## 🎯 Objectives
- Load, clean, and explore metadata
- Create visualizations and word cloud
- Build an interactive Streamlit app
- Prepare a sample dataset suitable for GitHub submission

---

## 📂 Project Structure

Frameworks_Assignment/
│── CORD19_Analysis.ipynb # Notebook with analysis & visualizations
│── app.py # Streamlit application
│── metadata_sample.csv # Sample dataset (~5000 rows)
│── cord19_cleaned.csv # Cleaned dataset for Streamlit
│── README.md


---

## 🛠️ Tools & Libraries
- Python 3.7+
- pandas
- matplotlib
- seaborn
- wordcloud
- streamlit

Install with:

```bash
pip install pandas matplotlib seaborn wordcloud streamlit

📊 How to Run
Jupyter Notebook

Open CORD19_Analysis.ipynb

Run cells in order

Uses metadata_sample.csv for demonstration

Streamlit App

streamlit run app.py

Interactive filtering by year and journal

Shows charts and word cloud

Displays a sample of the data

📄 Note

The full CORD-19 metadata.csv is too large to push to GitHub.
Use metadata_sample.csv (included) for running the notebook and app.
Full dataset download: Kaggle CORD-19 Dataset

📝 Reflection

Learned real-world data cleaning & visualization

Managed missing data and text preprocessing

Built a simple interactive Streamlit app

Learned to work with a dataset sample for GitHub

