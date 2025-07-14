# Personal Finance Advisor 💸

**An AI-powered personal finance assistant that helps you understand and optimize your spending — running locally with LLaMA3 via Ollama.**

Upload your bank statement (PDF) and get instant, actionable insights, categorized spending, and personalized advice — all through an interactive dashboard with rich visualizations.


## 🔍 How It Works

| Step | Description                                   |
|-------|----------------------------------------------|
| 1. 🧾 Upload   | Upload your bank statement PDF file         |
| 2. 🔍 Extract  | Extract transactions with a PDF parser       |
| 3. 🧠 Cluster  | Group transactions into categories via KMeans|
| 4. 📊 Visualize| Explore your spending with charts (pie/bar) |
| 5. 🤖 Advise   | Receive personalized finance advice powered by LLaMA3 |



## 🛠️ Technology Stack

- **Frontend:** Streamlit for interactive UI  
- **LLM:** Ollama with `llama3` for local language modeling  
- **Orchestration:** LangChain (`langchain-ollama` package)  
- **ML:** `scikit-learn` (KMeans clustering, TF-IDF vectorization)  
- **PDF Parsing:** `PyMuPDF` or `pdfplumber`  
- **Visualization:** Matplotlib and Streamlit native charts  


## 📂 Project Structure
    LLM-project/
    │
    ├── app.py # Main Streamlit application
    ├── advisor.py # LLM integration & advice generation
    ├── clusterer.py # Transaction clustering logic
    ├── pdf_parser.py # Extract transactions from PDFs
    ├── utils.py # Plotting functions (charts)
    ├── requirements.txt # Python dependencies
    └── sample.pdf # (Optional) Sample bank statement


## 🧪 Setup Instructions

### 1. Clone & Setup Environment

```bash
git clone https://github.com/your-username/finance-advisor.git
cd finance-advisor
python -m venv .venv

# Activate virtual environment:
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```
### 2. Install and Run Ollama
Download and install Ollama from https://ollama.com/download

Pull the LLaMA3 model and start the Ollama server:
```bash
ollama pull llama3
ollama serve
```
### 3. Run the Streamlit App
```bash
streamlit run app.py
```

## 📊 What You’ll Get
- Detailed transaction table categorized by spending type

- Interactive pie and bar charts showing spending distribution

- Personalized AI-driven financial advice, e.g.:

“You’re spending heavily on dining and subscriptions. Consider reviewing or bundling these services to save money.”

## 🚀 Future Enhancements
- 🔄 Switch between models like llama3, mistral, or phi via UI dropdown

- 📄 Export personalized advice reports as PDF

- 🌍 Multilingual support for global users

- 🪄 Integration with LangGraph for advanced agent workflows

- 🔐 User authentication with Streamlit Auth or Supabase

## 📄 License
MIT License – free to use, modify, and distribute.