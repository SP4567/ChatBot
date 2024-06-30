import faiss
from app.extract_data import fetch_course_data
from app.embeddings import create_embeddings

url = "https://brainlox.com/courses/category/technical"
courses = fetch_course_data(url)
vectors = create_embeddings(courses)

def create_vector_store():
    vector_store = faiss.IndexFlatL2(vectors.shape[1])
    vector_store.add(vectors)
    faiss.write_index(vector_store, "vector_store.faiss")

def load_vector_store():
    return faiss.read_index("vector_store.faiss")