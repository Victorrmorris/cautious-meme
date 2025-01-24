import streamlit as st
import pandas as pd
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="Financial Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="📊",  # Added a favicon
)

# Sample Data
balance = "$25,580.75 (€24,526.50)"
budget_data = {
    "Germany Budget": {
        "Total": "$3,200.00",
        "Spent": "$3,166.19 (€3,036.30)",
        "Categories": {
            "Transportation": "$62.80",
            "Rent": "$1,800.00",
            "Entertainment": "$154.67",
            "Education": "$123.54",
            "Utilities": "$179.20",
            "Groceries": "$845.98",
        },
    },
    "US Budget": {
        "Total": "$3,000.00",
        "Spent": "$2,801.97 (€2,687.30)",
        "Categories": {
            "Transportation": "$113.67",
            "Mortgage": "$1,502.16",
            "Home maintenance": "$312.43",
            "Utilities": "$416.82",
            "Groceries": "$456.89",
        },
    },
}
bills = [
    {"Name": "Germany Rent Payment", "Amount": "$1,800.00 (Monthly)", "Due Date": "1st June"},
    {"Name": "O2 - Internet", "Amount": "$39.99 (Monthly)", "Due Date": "1st June"},
    {"Name": "REWAG - Utilities", "Amount": "$30.00 (Monthly)", "Due Date": "1st June"},
]

credit_cards = {
    "Total Credit Card Debt": "$5,420.10",
    "Star Card": "$1,645.98",
    "USAA": "$3,774.12",
    "Recommendation": "You're slightly over the recommended 30% (36.13%) utilization rate. Paying down $1,020 would bring your overall rate to 30% or below.",
}

investments = {
    "Total Investments": "$53,926.44",
    "Breakdown": {
        "Schwab": "$7,890.32",
        "Fidelity": "$12,487.23",
        "Thrift Savings Plan": "$33,548.89",
    },
}

ai_insight = "You have $231.84 (€222.33) remaining for both of your May 2024 household budgets."

# Main Content
st.title("Financial Dashboard")
st.markdown("---")

# Balance Section
st.header("Balance (All Linked Accounts)")
st.subheader(balance)

# Budget Section
st.header("My Monthly Spending Analysis")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Germany Budget")
    st.metric(label="Total Budget", value=budget_data["Germany Budget"]["Total"], delta=f"Spent: {budget_data['Germany Budget']['Spent']}")  # Ensuring string formatting
    st.write("Category Breakdown:")
    if isinstance(budget_data["Germany Budget"]["Categories"], dict):  # Validating the Categories key
        for category, amount in budget_data["Germany Budget"]["Categories"].items():
            st.write(f"{category}: {amount}")

with col2:
    st.subheader("US Budget")
    st.metric(label="Total Budget", value=budget_data["US Budget"]["Total"], delta=f"Spent: {budget_data['US Budget']['Spent']}")  # Ensuring string formatting
    st.write("Category Breakdown:")
    if isinstance(budget_data["US Budget"]["Categories"], dict):  # Validating the Categories key
        for category, amount in budget_data["US Budget"]["Categories"].items():
            st.write(f"{category}: {amount}")

# AI Financial Insights
st.markdown("---")
st.header("AI Financial Analyst Insights")
st.info(ai_insight)

# Bills Section
st.header("My Bills")
try:
    total_due = sum(float(bill['Amount'].split('$')[1].split()[0]) for bill in bills)
    st.write(f"Total Due in Next 7 Days: ${total_due:.2f}")  # Added currency symbol
except (IndexError, ValueError, KeyError):
    st.error("Error calculating total due. Please check bill formats.")

for bill in bills:
    st.write(f"{bill['Name']}: {bill['Amount']} (Due: {bill['Due Date']})")

# Credit Card Section
st.header("My Credit Cards")
st.subheader(credit_cards["Total Credit Card Debt"])
st.write(credit_cards["Recommendation"])

# Investments Section
st.header("My Investments")
st.subheader(investments["Total Investments"])
st.write("Breakdown:")
for account, value in investments["Breakdown"].items():
    st.write(f"{account}: {value}")
