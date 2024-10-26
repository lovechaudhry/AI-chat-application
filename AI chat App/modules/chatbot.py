from .llm_integration import query_llm
from .rag import process_pdfs, retrieve_relevant_text

def handle_query(question, files):
    index, texts, model = process_pdfs(files)
    relevant_text = retrieve_relevant_text(question, index, texts, model)
    response = query_llm(question, relevant_text)
    return response
