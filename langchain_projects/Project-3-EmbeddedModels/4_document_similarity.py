from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity 

load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=300
)

multiple_docs = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = "Who is known for virat in Indian cricket?"

docs_embedding = embeddings.embed_documents(multiple_docs)
query_embedding = embeddings.embed_query(query)

similarity_scores = cosine_similarity([query_embedding], docs_embedding)[0]

index, score  = sorted(list(enumerate(similarity_scores)), key=lambda x:x[1])[-1]

print(multiple_docs[index])
print("similarity score is:", score)