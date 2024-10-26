from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from huggingface_hub import InferenceApi

def query_llm(question, context):
    api = InferenceApi("facebook/opt-125m", token="YOUR_HUGGING_FACE_TOKEN")
    try:
        response = api(inputs=question + "\n" + context)
        print("LLM Response:", response)  # Print the response to check its structure
        if response and isinstance(response, list) and "generated_text" in response[0]:
            return response[0]["generated_text"]
        else:
            print("Unexpected response format:", response)
            return "Sorry, an error occurred while generating a response."
    except Exception as e:
        print("Error while querying the LLM:", str(e))
        return "Sorry, an error occurred while generating a response."
