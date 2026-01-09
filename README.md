# 🚁 Drone Intelligence System

An AI-powered **Drone Intelligence System** built using **Retrieval-Augmented Generation (RAG)**, **FastAPI**, and **Streamlit**.  
The system provides drone-related information, ROI analysis, flight time estimation, and DGCA compliance checking using structured data and domain knowledge.

---

## 📌 Features

- **Drone Knowledge Chat (RAG)**
  - Answers drone-related questions using ingested documents
  - Retrieves information from DGCA rules, market data, and industry reports

- **ROI Calculator**
  - Calculates agriculture drone cost savings
  - Uses interpolation for accurate estimates

- **Flight Time Estimator**
  - Estimates flight duration based on battery parameters

- **DGCA Compliance Checker**
  - Determines drone classification and airspace permissions

- **Interactive Frontend**
  - Built with Streamlit
  - Communicates with backend APIs

---

## 📁 Project Structure
 internship/  
 
 │  
 |── api/ # FastAPI backend  
 │ ├── main.py  
 │ ├── schemas.py  
 │  
 ├── frontend/ # Streamlit frontend  
 │ └── app.py  
 │  
 ├── rag/ # RAG pipeline  
 │ ├── ingest.py  
 │ ├── retriever.py
 │ ├── vectorstore.py  
 │  
 ├── mcp_server/ # MCP tools  
 │ ├── roi_calculator.py  
 │ ├── flight_time_estimator.py  
 │ ├── compliance_checker.py  
 │  
 ├── data/  
 │ ├── raw/ # Knowledge base (.txt files)  
 | └── processed/ # CSV datasets  
 │  
 ├── test_mcp.py # MCP testing script  
 ├── .gitignore  
 └── README.md


---

## 🧠 RAG (Retrieval-Augmented Generation)

- All `.txt` files inside `data/raw/` are treated as **separate knowledge documents**
- Files are vectorized using **TF-IDF**
- Vector embeddings and metadata are stored locally
- User queries retrieve the most relevant document content

---

## ⚙️ Generating Vector Files

The following files are **generated automatically** and should **not be committed**:
- `tfidf.pkl`
- `vectorstore.pkl`

### Generate them using:
```bash
py -3.12 -m rag.ingest
```

### Start the Backend (FastAPI):

From the project root directory:

```bash

py -3.12 -m uvicorn api.main:app --reload            
```


## Backend URL:
http://127.0.0.1:8000

## API Docs (Swagger):
http://127.0.0.1:8000/docs

## Available API Endpoints
| Endpoint          | Description                 |
| ----------------- | --------------------------- |
| /chat             | Drone knowledge Q&A (RAG)   |
| /roi              | Agriculture ROI calculation | 
| /flight-time      | Flight time estimation      |
| /compliance       | DGCA compliance check       | 

## Start the frontend(Streamlit)
Open new terminal and run

``bash
 streamlit run frontend/app.py 
 ``
 ## frontend URL
 http://localhost:8501
