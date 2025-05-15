# 📄 OCR Translator & Semantic Search App (Python + .NET MAUI)
Project in early phase of develpoment.
End goal is to create a tool that extracts text from PDFs using OCR, translates it into English, generates semantic embeddings, and allows question-answering via a chatbot interface. .NET MAUI version in development.

## 🧩 Planned Features

- 📑 **PDF OCR** – Extracts images from PDF pages and uses Tesseract to detect text
- 🌍 **Translation** – Automatically translates Czech text into English using Google Translate
- 🧠 **Embeddings** – Generates vector representations using SentenceTransformers
- 🔍 **Semantic Search** – Finds the most relevant text chunks for user questions using ChromaDB
- 🧵 **Chat Interface** – Console chatbot that answers questions based on document content

## ⚙️ Requirements

- Python 3.8+
- [`PyMuPDF`](https://pypi.org/project/PyMuPDF/)
- `pytesseract` (with system-level Tesseract installed)
- `Pillow`
- `googletrans`
- `sentence-transformers`
- `chromadb`
