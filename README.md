# 🛒 eCard AI Customer Support Chatbot (RAG + Memory + LangGraph)

An **AI-powered customer support chatbot** built using **LangGraph, LangChain, and Streamlit** that can intelligently handle:

* 📦 Order tracking (from CSV data)
* 📄 Company policies & FAQs (from PDF using RAG)
* 🧠 Context-aware conversations (memory-enabled)

---

## 🚀 Features

* 🔍 **Multi-Source Retrieval**

  * Structured data (CSV for orders)
  * Unstructured data (PDF for policies)

* 🧠 **Memory-Aware Chatbot**

  * Handles follow-up questions
  * No need to repeat order ID

* 🔀 **Intent-Based Routing**

  * Automatically decides:

    * Order query → CSV
    * Policy query → PDF

* 🤖 **LangGraph Workflow**

  * Modular node-based architecture
  * Stateful execution

* 🖥️ **Streamlit UI**

  * ChatGPT-like interface
  * Real-time responses

---

## 🏗️ Project Architecture

```
                    START
                      ↓
                  User Query
                      ↓
        Intent Detection (order OR policy)
                      ↓
      ┌───────────────┬───────────────┐
      ↓                               ↓
  Extract Order ID             Use Query Directly
      ↓                               ↓
  Fetch from CSV               Fetch from PDF (Vector DB)
      ↓                               ↓
      └───────  Combine Context───────┘
                       ↓
              LLM Generates Answer
                       ↓
              Update Chat Memory
                       ↓
                      END
```

## ⚙️ Tech Stack

* 🧠 **LangGraph** – Workflow orchestration
* 🔗 **LangChain** – LLM + RAG integration
* 🤖 **OpenAI / Groq** – LLMs
* 📊 **Pandas** – CSV handling
* 📚 **FAISS** – Vector database
* 🖥️ **Streamlit** – UI

---

## 📊 Example Use Cases

### ✅ Order Query

```
User: Where is my order 1001?
Bot: Your order is shipped and will arrive on 25 March.
```

---

### ✅ Follow-up (Memory)

```
User: When will it arrive?
Bot: It will arrive on 25 March.
```

---

### ✅ Policy Query

```
User: What is your refund policy?
Bot: Refunds are processed within 5–7 days...
```

---

## 🧠 Key Concepts Used

* Retrieval-Augmented Generation (RAG)
* Stateful AI systems (LangGraph)
* Conversational memory
* Multi-source data retrieval
* Prompt engineering

---

## ⚡ Installation

```bash
git clone <your-repo-link>
cd ecard-ai-support

pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📌 Environment Variables

Create a `.env` file and add:

```
OPENAI_API_KEY=your_api_key_here
```

---


## 📜 License

This project is for educational and portfolio purposes.

---

## 👨‍💻 Author

**RAM**
Aspiring AI / GenAI / Agentic AI Engineer 🚀
