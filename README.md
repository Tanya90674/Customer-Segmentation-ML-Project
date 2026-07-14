# Customer Personality Segmentation Using Machine Learning

## Project Overview

Customer segmentation is an important technique used by businesses to understand customer behavior and improve marketing strategies. This project groups customers into different segments based on their demographic details and purchasing patterns using the K-Means Clustering algorithm.

A Streamlit web application is also developed to allow users to enter customer information and predict the customer segment instantly.

---

## Problem Statement

Businesses often have a large customer base with different buying behaviors. Treating every customer in the same way can reduce marketing effectiveness. The objective of this project is to identify similar groups of customers so that businesses can provide personalized offers, improve customer satisfaction, and increase sales.

---

## Objectives

- Perform customer segmentation using Machine Learning.
- Analyze customer purchasing behavior.
- Build a clustering model using the K-Means algorithm.
- Develop an interactive Streamlit application for customer segment prediction.
- Provide business insights based on the predicted customer segment.

---

## Dataset

The project uses the **Marketing Campaign Dataset**, which contains customer demographic information and purchase history.

### Features Used

- Age
- Income
- Amount Spent
- Number of Web Purchases
- Number of Store Purchases
- Number of Web Visits per Month
- Recency

---

## Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib

---

## Machine Learning Algorithm

The K-Means Clustering algorithm is used to group customers with similar characteristics.

### Data Preprocessing

- Data Cleaning
- Feature Selection
- StandardScaler for Feature Scaling

The trained model and scaler are saved using Joblib for deployment in the Streamlit application.

---

## Project Workflow

1. Load the dataset.
2. Perform data cleaning and preprocessing.
3. Conduct Exploratory Data Analysis (EDA).
4. Select important features.
5. Scale the data using StandardScaler.
6. Apply the K-Means Clustering algorithm.
7. Save the trained model and scaler.
8. Build the Streamlit application.
9. Predict customer segments based on user input.

---

## Project Structure

```
Customer Personality Analysis/
│
├── Customer_Personality_Analysis.ipynb
├── segmentation.py
├── marketing_campaign.csv
├── kmeans_model.pkl
├── scaler.pkl
├── requirements.txt
└── README.md
```

---

## How to Run the Project

### Step 1

Install the required libraries.

```bash
pip install -r requirements.txt
```

### Step 2

Run the Streamlit application.

```bash
py -m streamlit run segmentation.py
```

---

## Output

The application predicts the customer segment based on the entered customer details.

The prediction can help businesses understand customer behavior and support better marketing decisions.

---

## Future Scope

- Compare K-Means with other clustering algorithms.
- Deploy the application on a cloud platform.
- Add data visualization dashboards.
- Improve customer recommendations using AI techniques.

---

## Conclusion

This project successfully demonstrates customer segmentation using the K-Means Clustering algorithm. The developed Streamlit application provides an easy-to-use interface for predicting customer segments based on user input. The project can help businesses understand customer behavior and improve decision-making through targeted marketing strategies.

---

## Developer

**Tanya Agarwal - 2400270120164,
  Raj Vardhan Singh - 2400270120124**

B.Tech (3rd Year)

Machine Learning Internship Project