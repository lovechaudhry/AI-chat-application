from fastapi import FastAPI, UploadFile, File
from modules.chatbot import handle_query

app = FastAPI()

@app.post("/query/")
async def query_endpoint(question: str, files: list[UploadFile] = File(...)):
    response = handle_query(question, files)
    return {"response": response}
