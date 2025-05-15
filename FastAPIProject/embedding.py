from sentence_transformers import SentenceTransformer
import chromadb

if "document_embeddings" in [col.name for col in client.list_collections()]:
    client.delete_collection(name="document_embeddings")

# Funkcja dzieląca tekst na fragmenty
def split_text_into_chunks(text, chunk_size=50):
    words = text.split()
    return [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

# Załaduj model
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Przekształć na embeddingi
embeddings = [embedding_model.encode(chunk).tolist() for chunk in split_text_into_chunks(" ".join(english_texts))]

# Inicjalizacja bazy wektorowej
client = chromadb.Client()
collection = client.create_collection(name="document_embeddings")

# Zapis do bazy
for idx, (chunk, embedding) in enumerate(zip(split_text_into_chunks(" ".join(english_texts)), embeddings)):
    collection.add(
        documents=[chunk],
        embeddings=[embedding],
        ids=[f"chunk_{idx}"]
    )
