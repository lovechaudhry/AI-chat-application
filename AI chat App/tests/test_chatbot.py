import unittest
from modules.rag import process_pdfs, retrieve_relevant_text
from modules.llm_integration import query_llm

class TestChatbot(unittest.TestCase):

    def test_process_pdfs(self):
        # Example test to check if process_pdfs correctly processes a sample PDF
        sample_pdf_path = "path/to/sample.pdf"
        processed_text = process_pdfs([sample_pdf_path])  
        
        # Basic assertion to check if output is not empty
        self.assertIsInstance(processed_text, list)
        self.assertGreater(len(processed_text), 0, "Processed text should not be empty")
    
    def test_retrieve_relevant_text(self):
        # Example test for retrieve_relevant_text functionality
        sample_texts = ["This is a sample document.", "Another document text."]
        question = "What is the content of the sample document?"
        relevant_text = retrieve_relevant_text(question, sample_texts)
        
        # Basic assertion to check if output contains relevant text
        self.assertIsInstance(relevant_text, str)
        self.assertIn("sample document", relevant_text, "Relevant text should mention 'sample document'")
    
    def test_query_llm(self):
        # Example test to check if query_llm returns a plausible response
        question = "What is AI?"
        response = query_llm(question)
        
        # Basic assertion to check if LLM response is a non-empty string
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0, "LLM response should not be empty")
        self.assertIn("intelligence", response.lower(), "Response should contain a relevant keyword")

 