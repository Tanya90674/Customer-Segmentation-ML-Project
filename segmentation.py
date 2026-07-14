import streamlit as st
import numpy as np
import pandas as pd
import joblib

kmeans = joblib.load("kmeans_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Customer Personality Segmentation using Machine Learning")
st.write("Enter customer details to predict the segment.")

age = st.number_input("Age", min_value=18,max_value=100,value=30 )
income = st.number_input("Income",min_value=0,max_value=500000,value=50000)
amount_spent = st.number_input("Amount_Spent", min_value= 0,max_value=500000,value=1000)
num_web_purchases = st.number_input("Number of WEB Purchases",min_value = 0,max_value=100,value= 10)
num_store_purchases = st.number_input("Number of Store Purchases", min_value = 0, max_value=100,value= 10)
num_web_visits_month = st.number_input("Number of Web Visits per Month",min_value=0,max_value=50,value=3)
recency = st.number_input("Recency (days since last purchase)", min_value=0,max_value=365,value=30)


input_data = pd.DataFrame({
    "Age": [age],
    "Income": [income],
    "Amount_Spent": [amount_spent],
    "NumWebPurchases": [num_web_purchases],
    "NumStorePurchases": [num_store_purchases],
    "NumWebVisitsMonth": [num_web_visits_month],
    "Recency": [recency]
})

input_scaled = scaler.transform(input_data)

segment_info = {
    0: {
        "name": "🟡 Regular Customers",
        "description": "Customers with moderate income and average purchasing behavior.",
        "recommendation": "Offer seasonal discounts, reward points, and personalized promotions to increase engagement."
    },

    1: {
        "name": "🟢 Premium Customers",
        "description": "High-income customers with the highest spending habits.",
        "recommendation": "Provide VIP membership, exclusive offers, premium services, and loyalty rewards."
    },

    2: {
        "name": "🔴 Budget Customers",
        "description": "Customers with low income and minimal spending.",
        "recommendation": "Promote affordable products, discount campaigns, and value-for-money offers."
    },

    3: {
        "name": "🔵 Loyal Online Customers",
        "description": "Customers who frequently purchase online and spend significantly.",
        "recommendation": "Recommend products based on purchase history and provide exclusive online deals."
    },

    4: {
        "name": "🟣 High Value Customers",
        "description": "Active customers with high income and strong purchasing behavior.",
        "recommendation": "Maintain long-term relationships through loyalty programs and early access to new products."
    },

    5: {
        "name": "⚫ Inactive Customers",
        "description": "Customers with low spending who have not purchased recently.",
        "recommendation": "Launch re-engagement campaigns using special discounts and personalized email offers."
    }
}

if st.button("Predict Segment"):

    cluster = kmeans.predict(input_scaled)[0]
    st.success(f"Predicted Segment: {segment_info[cluster]['name']}")

    st.subheader("📋 Customer Characteristics")
    st.write(segment_info[cluster]["description"])

    st.subheader("💡 Business Recommendation")
    st.info(segment_info[cluster]["recommendation"])
