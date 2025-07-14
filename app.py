import streamlit as st
from pdf_parser import extract_transactions
from clusterer import cluster_transactions
from advisor import generate_advice
from utils import plot_spending_pie, plot_spending_bar

st.set_page_config(page_title="Finance Advisor", layout="wide")
st.title("💸 LLM-Powered Personal Finance Advisor")

uploaded_file = st.file_uploader("📄 Upload your bank statement (PDF)", type="pdf")

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())
    
    df = extract_transactions("temp.pdf")
    if df.empty:
        st.warning("No transactions detected. Please upload a different PDF.")
    else:
        df = cluster_transactions(df)

        st.subheader("🔍 Extracted Transactions")
        st.dataframe(df)

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📊 Pie Chart")
            plot_spending_pie(df)
        with col2:
            st.subheader("📈 Bar Chart")
            plot_spending_bar(df)

        st.subheader("💡 AI Advice")
        with st.spinner("Analyzing your spending..."):
            advice = generate_advice(df)
            st.markdown(advice)
