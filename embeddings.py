from langchain.embeddings import OpenAIEmbeddings
import numpy as np

def create_embeddings(courses):
    texts = [course['description'] for course in courses]
    embeddings = OpenAIEmbeddings(openai_api_key="My_secret_key")
    vectors = embeddings.embed_documents(texts)
    return vectors

def create_user_embedding(user_input):
    embeddings = OpenAIEmbeddings(openai_api_key="My_secret_key")
    return np.array(embeddings.embed_documents([user_input]))