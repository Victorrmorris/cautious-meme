import streamlit as st
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(
    page_title="Split Household Spending Insights",
    layout="wide",
    page_icon="💰",
)

# Sample Data
spending_data = {
    "Germany": {
        "Total Budget": "$3,200.00",
        "Spent": "$3,166.19 (€3,036.30)",
        "Categories": {
            "Transportation": 62.80,
            "Rent": 1800.00,
            "Entertainment": 154.67,
            "Education": 123.54,
            "Utilities": 179.20,
            "Groceries": 845.98,
        },
    },
    "US": {
        "Total Budget": "$3,000.00",
        "Spent": "$2,801.97 (€2,687.30)",
        "Categories": {
            "Transportation": 113.67,
            "Mortgage": 1502.16,
            "Home maintenance": 312.43,
            "Utilities": 416.82,
            "Groceries": 456.89,
        },
    },
}

ai_insight = (
    "Based on your current spending patterns, you may want to focus on reducing "
    "utility costs in both Germany and the US. In Germany, cutting utility costs "
    "by €30 can free up funds for unexpected expenses. In the US, consider reallocating "
    "home maintenance costs to savings for long-term goals."
)

# Utility: Create a bar chart for spending categories
def create_spending_chart(categories, title):
    labels = list(categories.keys())
    values = list(categories.values())

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.barh(labels, values, color="skyblue")
    ax.set_xlabel("Amount ($)")
    ax.set_title(title)
    st.pyplot(fig)

# Main Application
st.title("💰 Split Household Spending Insights")
st.markdown("This dashboard provides an overview of spending insights for households in Germany and the US.")
st.markdown("---")

# Insights Section
st.header("LLM Spending Insights")
st.info(ai_insight)

# Spending Analysis for Germany
col1, col2 = st.columns(2)
with col1:
    st.subheader("Germany Household Spending")
    st.metric(
        label="Total Budget",
        value=spending_data["Germany"]["Total Budget"],
        delta=f"Spent: {spending_data['Germany']['Spent']}"
    )
    create_spending_chart(spending_data["Germany"]["Categories"], "Germany Spending Breakdown")

# Spending Analysis for US
with col2:
    st.subheader("US Household Spending")
    st.metric(
        label="Total Budget",
        value=spending_data["US"]["Total Budget"],
        delta=f"Spent: {spending_data['US']['Spent']}"
    )
    create_spending_chart(spending_data["US"]["Categories"], "US Spending Breakdown")

# User Interaction for Insights
st.markdown("---")
st.subheader("Ask Your Financial AI Assistant")
user_query = st.text_input("Type your question about spending insights or budgeting:")
if user_query:
    st.write(f"**Your Question:** {user_query}")
    with st.spinner("Processing your query..."):
        # Simulated AI response for demo purposes
        st.success("AI Insight: Consider adjusting grocery budgets in both households to align better with inflation trends.")
else:
    st.write("Awaiting your question. Get tailored insights for your finances!")

# Footer
st.markdown("---")
st.caption("Developed for households managing cross-border spending.")
