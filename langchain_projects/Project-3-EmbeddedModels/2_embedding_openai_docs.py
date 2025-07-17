from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=32
)

docs = [
    "What is the capital of India?",
    "The capital of France is Paris.",
    "The capital of Japan is Tokyo."
]

embedding_result = embeddings.embed_documents(docs)

for i, doc in enumerate(docs):
    print(f"Document {i+1}: {doc}")
    print(f"Embedding: {embedding_result[i]}")
# Output: Embedding vectors for each document
# This will print the embedding vectors for the documents.