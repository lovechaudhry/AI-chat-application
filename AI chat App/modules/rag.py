import pdfplumber
from sentence_transformers import SentenceTransformer
import faiss

def process_pdfs(files):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    texts = []

    for file in files:
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    texts.append(text)
    
    embeddings = model.encode(texts)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    return index, texts, model

def retrieve_relevant_text(query, index, texts, model):
    query_embedding = model.encode([query])
    _, closest_indices = index.search(query_embedding, k=5)
    return " ".join([texts[idx] for idx in closest_indices[0]])
