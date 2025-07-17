from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=32
)

embedding_result = embeddings.embed_query("What is the capital of India?"
                                          )
print(str(embedding_result))
# Output: [0.123, -0.456, ...] (example output, actual values will vary)
# This will print the embedding vector for the query.