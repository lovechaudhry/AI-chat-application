from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from huggingface_hub import InferenceApi

def query_llm(question, context):
    api = InferenceApi("facebook/opt-125m", token="YOUR_HUGGING_FACE_TOKEN")
    response = api(inputs=question + "\n" + context)
    return response[0]["generated_text"]
