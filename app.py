
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load model and vectorizer
with open('model/fake_news_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('model/tfidf_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        news = request.form['news']
        if news:
            news_vector = vectorizer.transform([news])
            result = model.predict(news_vector)[0]
            prediction = "Fake" if result == 1 else "Real"
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
