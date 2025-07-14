import streamlit as st
from pdf_parser import extract_transactions
from clusterer import cluster_transactions
from advisor import generate_advice
from utils import plot_spending_pie, plot_spending_bar

st.set_page_config(page_title="Finance Advisor", layout="wide")
st.title("💸 LLM-Powered Personal Finance Advisor")

st.markdown("""
Upload your **bank statement PDF**, and this app will:
- 🔍 Extract transactions
- 🧠 Cluster them by type
- 📊 Visualize spending
- 🤖 Suggest personalized financial tips using **local LLM (Ollama)**
""")

uploaded_file = st.file_uploader("📄 Upload PDF", type="pdf")

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    df = extract_transactions("temp.pdf")

    if df.empty or len(df) < 2:
        st.warning("⚠️ Not enough transactions detected. Please upload a longer or clearer statement.")
    else:
        df = cluster_transactions(df)

        st.subheader("🔍 Extracted Transactions")
        st.dataframe(df, use_container_width=True)

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📊 Spending Breakdown (Pie)")
            plot_spending_pie(df)
        with col2:
            st.subheader("📈 Spending Overview (Bar)")
            plot_spending_bar(df)

        st.subheader("💡 AI-Powered Financial Advice")
        with st.spinner("Analyzing your spending..."):
            advice = generate_advice(df)
            st.markdown(advice)
