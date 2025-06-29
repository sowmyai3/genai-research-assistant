# genai-research-assistant

This project is a smart document-aware assistant built using Generative AI. It allows users to upload research papers, legal docs, or technical manuals and interact with them through summarization, question answering, and logic-based challenges.

---

##  Objective

To build an AI-powered tool that goes beyond basic keyword search or static summarization. The assistant must:

- Understand uploaded documents contextually
- Answer complex user questions
- Generate logic-based questions for user engagement
- Justify every response with evidence from the original document

---

##  Features

-  **PDF/TXT Upload**: Supports up to 150MB file size
-  **Auto-Summary**: Concise summary (≤150 words) shown on upload
-  **Ask Anything**: Ask free-form questions; AI responds using only document content
-  **Challenge Me**: Generates reasoning-based questions; evaluates your answers
-  **Justifications**: Every answer is grounded in document references
-  **No Hallucinations**: Answers are never fabricated—strictly document-based

---

##  Tech Stack

- **Frontend**: Streamlit (UI + interaction modes)
- **Backend**:
  - HuggingFace Transformers (BART, GPT-2, Roberta)
  - FAISS for document chunk retrieval
  - LangChain for embedding pipeline
  - pdfminer.six for PDF parsing

---
##  Quick Start

```bash
git clone https://github.com/sowmyai3/genai-research-assistant.git
cd genai-research-assistant

python -m venv assistant_env
assistant_env\Scripts\activate       # Windows
# source assistant_env/bin/activate  # Mac/Linux

pip install -r requirements.txt
streamlit run app.py
---
## Testing
pip install pytest
pytest tests/
---


