"""Day 55: train and evaluate an SMS spam classifier.

Run: python spam_classifier.py
The full UCI dataset is downloaded when possible; a small bundled sample is
used offline. Accuracy on the sample is only a smoke test, not a benchmark.
"""
from pathlib import Path
import io
import zipfile
import urllib.request
import re
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
SAMPLE_PATH = DATA_DIR / "sms_spam_sample.tsv"
UCI_URL = "https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip"

def load_data():
    local = DATA_DIR / "SMSSpamCollection"
    if local.exists():
        return read_tsv(local)
    try:
        print("Downloading the full UCI SMS Spam Collection dataset...")
        with urllib.request.urlopen(UCI_URL, timeout=15) as response:
            archive = zipfile.ZipFile(io.BytesIO(response.read()))
            member = next(name for name in archive.namelist() if name.endswith("SMSSpamCollection"))
            content = archive.read(member).decode("utf-8", errors="replace")
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        local.write_text(content, encoding="utf-8")
        return read_tsv(local)
    except Exception as exc:
        print(f"Could not download full dataset ({exc}). Using bundled sample instead.")
        return read_tsv(SAMPLE_PATH)

def read_tsv(path):
    df = pd.read_csv(path, sep="\t", header=None, names=["label", "message"], encoding="utf-8", on_bad_lines="skip")
    df = df.dropna(subset=["label", "message"])
    df["label"] = df["label"].astype(str).str.strip().str.lower()
    df["message"] = df["message"].astype(str)
    df = df[df.label.isin(["ham", "spam"])].drop_duplicates().reset_index(drop=True)
    if df["label"].nunique() < 2:
        raise ValueError("Training requires examples from both ham and spam classes.")
    return df

def clean_text(text):
    text = text.lower()
    text = re.sub(r"https?://\S+|www\.\S+", " URL ", text)
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()

def main():
    df = load_data()
    df["clean_message"] = df.message.map(clean_text)
    # Stratification keeps the ham/spam ratio similar in train and test sets.
    X_train, X_test, y_train, y_test = train_test_split(
        df["clean_message"], df["label"], test_size=0.20, random_state=42,
        stratify=df["label"]
    )
    model = Pipeline([
        ("tfidf", TfidfVectorizer(stop_words="english", ngram_range=(1, 2), min_df=1)),
        ("classifier", MultinomialNB())
    ])
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print("\n=== Day 55: Smart Spam Detector ===")
    print(f"Dataset rows: {len(df)} | Training rows: {len(X_train)} | Test rows: {len(X_test)}")
    print(f"Accuracy: {accuracy:.2%}")
    print("\nClassification report:")
    print(classification_report(y_test, predictions, labels=["ham", "spam"], zero_division=0))
    print("Confusion matrix (rows=actual [ham, spam], columns=predicted [ham, spam]):")
    print(confusion_matrix(y_test, predictions, labels=["ham", "spam"]))
    custom_messages = [
        "Hey, are we still meeting after class?",
        "Congratulations! You won a free prize. Call now to claim!",
        "Your appointment is confirmed for tomorrow morning.",
        "URGENT! Claim your cash reward by clicking this link."
    ]
    print("\nCustom predictions:")
    for message, prediction in zip(custom_messages, model.predict([clean_text(m) for m in custom_messages])):
        print(f"{prediction.upper():4} | {message}")
    print("\nInterpretation: accuracy is the share of correct predictions, but also inspect spam precision/recall and the confusion matrix.")
    if len(df) < 100:
        print("WARNING: Small fallback sample detected. This evaluation is only a smoke test; rerun with the full UCI dataset for meaningful metrics.")

if __name__ == "__main__":
    main()
