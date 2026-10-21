from pathlib import Path
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

DATA_PATH = Path(__file__).parent / "data" / "sms_sample.csv"

def load_data(path=DATA_PATH):
    df = pd.read_csv(path)
    if not {"label", "message"}.issubset(df.columns):
        raise ValueError("Dataset must have label and message columns.")
    df = df.dropna(subset=["label", "message"]).copy()
    df["label"] = df["label"].astype(str).str.strip().str.lower()
    df["message"] = df["message"].astype(str).str.strip()
    df = df[df["label"].isin(["ham", "spam"]) & df["message"].ne("")]
    if df["label"].nunique() < 2:
        raise ValueError("Dataset must contain both ham and spam labels.")
    return df

def build_pipeline():
    return Pipeline([
        ("tfidf", TfidfVectorizer(lowercase=True, strip_accents="unicode")),
        ("classifier", MultinomialNB()),
    ])

def train_model(path=DATA_PATH):
    df = load_data(path)
    model = build_pipeline()
    model.fit(df["message"], df["label"])
    return model

def predict_message(model, message):
    if not isinstance(message, str) or not message.strip():
        raise ValueError("Enter a non-empty message.")
    prediction = model.predict([message])[0]
    probabilities = model.predict_proba([message])[0]
    confidence = float(probabilities[list(model.classes_).index(prediction)])
    return {"label": prediction, "confidence": confidence}
