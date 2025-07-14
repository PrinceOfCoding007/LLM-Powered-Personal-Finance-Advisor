import matplotlib.pyplot as plt
import streamlit as st

def plot_spending_pie(df):
    grouped = df.groupby('Category')['Amount'].sum()
    fig, ax = plt.subplots()
    ax.pie(grouped, labels=grouped.index, autopct='%1.1f%%')
    ax.set_title("Spending by Category")
    st.pyplot(fig)

def plot_spending_bar(df):
    grouped = df.groupby('Category')['Amount'].sum().sort_values()
    st.bar_chart(grouped)
