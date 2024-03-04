from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import numpy as np

app = Flask(__name__)

# Load models
lstm_model = load_model('lstm_model.h5')
w2v_model = Word2Vec.load("word2vec_model.bin")

def preprocess_text(text, model):
    """Preprocess text by tokenizing and converting to embeddings."""
    tokenized_text = word_tokenize(text.lower())  # Convert to lowercase
    embeddings = [model.wv[word] for word in tokenized_text if word in model.wv]
    if embeddings:
        document_embedding = np.mean(embeddings, axis=0)
    else:
        document_embedding = np.zeros(model.vector_size)
    return np.expand_dims(document_embedding, axis=-1).reshape(1, -1, 1)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    text = data['text']
    preprocessed_text = preprocess_text(text, w2v_model)
    prediction = lstm_model.predict(preprocessed_text)
    pred_class = 'No' if prediction[0][0] < 0.5 else 'Yes'
    return jsonify({'dispute': pred_class})

if __name__ == '__main__':
    app.run(debug=True)
