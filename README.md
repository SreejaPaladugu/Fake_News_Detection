# Fake_News_Detection_System



An end-to-end machine learning project that uses Natural Language Processing (NLP) to detect whether a news article is **Real** or **Fake**, with a user-friendly web interface built using Flask.

---

## 📌 Features

- ✅ Trained ML model using logistic regression and TF-IDF
- ✅ Accepts news content input via a web form
- ✅ Predicts and displays whether news is fake or real
- ✅ Clean UI using HTML/CSS
- ✅ Ready to deploy on platforms like Render or Railway

---

## 🧠 Machine Learning Details

- Dataset: Combined [Fake.csv](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset) and [True.csv] datasets from Kaggle
- Model: Logistic Regression
- Vectorizer: TfidfVectorizer (stop words + max_df tuning)
- Accuracy: **~99%** on test data
- Libraries: `pandas`, `scikit-learn`, `nltk`, `pickle`

---

## 🗂️ Project Structure

```

FakeNewsDetection/
├── app.py                 # Flask web app
├── train\_model.py         # ML training script
├── prepare\_dataset.py     # Dataset combiner
├── requirements.txt       # Required packages
├── model/
│   ├── fake\_news\_model.pkl
│   └── tfidf\_vectorizer.pkl
├── static/
│   └── style.css          # Styling for the web UI
├── templates/
│   └── index.html         # Frontend form
├── train.csv              # Combined dataset
└── README.md

````

---

## 🚀 Getting Started

### 1️⃣ Clone the repo
```bash
git clone https://github.com/your-username/FakeNewsDetection.git
cd FakeNewsDetection
````

### 2️⃣ Install requirements

```bash
pip install -r requirements.txt
```

### 3️⃣ Prepare the dataset

Place `Fake.csv` and `True.csv` in the root, then:

```bash
python prepare_dataset.py
```

### 4️⃣ Train the model

```bash
python train_model.py
```

### 5️⃣ Run the web app

```bash
python app.py
```

Then visit: `http://127.0.0.1:5000/`

---

## 🧪 Example

Enter a news article or headline in the text box.
Click **"Check"** — and the model will respond with **"Real"** or **"Fake"**.

---

## 🌐 Deployment (Optional)

You can deploy this to:

* [Render](https://render.com/)
* [Railway](https://railway.app/)
* [Heroku](https://heroku.com/)


---


