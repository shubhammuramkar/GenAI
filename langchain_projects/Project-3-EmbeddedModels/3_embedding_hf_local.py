from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
import os

# Load environment variables
load_dotenv() 

# 1. Initialize the local Sentence Transformer model using HuggingFaceEmbeddings
# This class from langchain_community is designed to work with sentence-transformers models locally.
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 2. Prepare some text data
raw_documents = [
    "The quick brown fox jumps over the lazy dog.",
    "Artificial intelligence is rapidly advancing.",
    "Machine learning is a subset of AI.",
    "Dogs are often kept as pets.",
    "Technology is transforming our lives.",
    "The fox is a cunning animal."
]

vector = embeddings.embed_documents(raw_documents)
print("Creating vector store and generating embeddings...")
print(str(vector))

# # 3. Split documents into chunks (optional but good practice for large texts)
# text_splitter = CharacterTextSplitter(
#     separator="\n\n",
#     chunk_size=200,
#     chunk_overlap=0,
#     length_function=len,
#     is_separator_regex=False,
# )
# docs = text_splitter.create_documents(raw_documents)
# print(docs)

# # 4. Create a vector store from the documents
# # This step uses the initialized HuggingFaceEmbeddings to generate embeddings.
# print("Creating vector store and generating embeddings...")
# vectorstore = FAISS.from_documents(docs, embeddings)
# print("Vector store created successfully!")

# # 5. Perform a similarity search
# query = "What do we know about canines?"
# results = vectorstore.similarity_search(query)

# print(f"\nQuery: '{query}'")
# print("\nMost similar documents:")
# for i, doc in enumerate(results):
#     print(f"{i+1}. Content: '{doc.page_content}' (Score: {doc.metadata['score']:.4f})")

# # 6. (Optional) Save and load the vector store
# save_path = "faiss_index_all_minilm"
# vectorstore.save_local(save_path)
# print(f"\nVector store saved to '{save_path}'")

# loaded_vectorstore = FAISS.load_local(save_path, embeddings, allow_dangerous_deserialization=True)
# print(f"Vector store loaded from '{save_path}'")

# query_loaded = "Tell me about animals."
# results_loaded = loaded_vectorstore.similarity_search(query_loaded)

# print(f"\nQuery (loaded store): '{query_loaded}'")
# print("\nMost similar documents from loaded store:")
# for i, doc in enumerate(results_loaded):
#     print(f"{i+1}. Content: '{doc.page_content}' (Score: {doc.metadata['score']:.4f})")