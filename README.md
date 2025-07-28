
# Fake News Detection System

An end-to-end machine learning project with a Flask web interface to detect fake news using natural language processing.

## Features
- Preprocesses news articles
- Trains an ML model (Logistic Regression)
- Flask web app for real-time predictions
- Simple, responsive UI

## How to Run

1. Install requirements:
```
pip install -r requirements.txt
```

2. Train the model:
```
python train_model.py
```

3. Run the web app:
```
python app.py
```

## Dataset
Use the [Kaggle Fake News dataset](https://www.kaggle.com/c/fake-news/data) and place `train.csv` in the root directory.
