from langchain_ollama import ChatOllama  # ✅ OFFICIAL
from langchain.prompts import ChatPromptTemplate

def generate_advice(df):
    summary = df.groupby('Category')['Amount'].sum().to_string()
    model = ChatOllama(model="qwen3:1.7b")  # Ensure llama3 is pulled
    prompt = ChatPromptTemplate.from_template(
        "Analyze this user spending breakdown by category:\n{summary}\n\n"
        "Give detailed, personalized financial tips for better savings."
    )
    chain = prompt | model
    return chain.invoke({"summary": summary}).content
