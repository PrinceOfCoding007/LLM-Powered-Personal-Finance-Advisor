import pdfplumber
import pandas as pd

def extract_transactions(pdf_path):
    transactions = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            lines = page.extract_text().split('\n')
            for line in lines:
                parts = line.split()
                if len(parts) >= 3 and any(char.isdigit() for char in parts[-1]):
                    try:
                        date = parts[0]
                        amount = float(parts[-1].replace(",", "").replace("₹", "").replace("$", ""))
                        description = " ".join(parts[1:-1])
                        transactions.append({"Date": date, "Description": description, "Amount": amount})
                    except:
                        pass
    return pd.DataFrame(transactions)
