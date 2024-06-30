from flask import request, jsonify
from app import app
from app.embeddings import create_user_embedding
from app.vector_store import load_vector_store, courses

index = load_vector_store()

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('question')
    if not user_input:
        return jsonify({'error': 'No question provided'}), 400

    user_vector = create_user_embedding(user_input)
    distances, indices = index.search(user_vector, k=1)
    closest_course = courses[indices[0][0]]

    return jsonify({'course': closest_course})