"""Day 54: load, clean, and explore SMS spam messages.

Run: python preprocess_sms.py
Optional: python preprocess_sms.py path/to/SMSSpamCollection
The full dataset is downloaded when internet is available; a small bundled sample
is used as an offline fallback. Sample metrics/observations are not representative.
"""
from pathlib import Path
import re
import sys
import urllib.request
import zipfile
import io
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
SAMPLE_PATH = DATA_DIR / "sms_spam_sample.tsv"
UCI_URL = "https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip"
STOPWORDS = {
    "a", "an", "the", "and", "or", "but", "if", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "is", "am", "are", "was", "were", "be", "been", "being", "have", "has", "had", "do", "does", "did", "doing", "i", "me", "my", "myself", "we", "our", "ours", "you", "your", "yours", "he", "him", "his", "she", "her", "it", "its", "they", "them", "their", "this", "that", "these", "those", "as", "can", "could", "will", "would", "should", "not", "so", "too", "very"
}

def load_dataset(path_arg=None):
    if path_arg:
        path = Path(path_arg)
        if not path.exists():
            raise FileNotFoundError(f"Dataset not found: {path}")
        return read_tsv(path)
    local_uci = DATA_DIR / "SMSSpamCollection"
    if local_uci.exists():
        return read_tsv(local_uci)
    try:
        print("Downloading the full UCI SMS Spam Collection dataset...")
        with urllib.request.urlopen(UCI_URL, timeout=15) as response:
            archive = zipfile.ZipFile(io.BytesIO(response.read()))
            member = next(name for name in archive.namelist() if name.endswith("SMSSpamCollection"))
            content = archive.read(member).decode("utf-8", errors="replace")
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        local_uci.write_text(content, encoding="utf-8")
        return read_tsv(local_uci)
    except Exception as exc:
        print(f"Could not download full dataset ({exc}). Using bundled sample instead.")
        return read_tsv(SAMPLE_PATH)

def read_tsv(path):
    df = pd.read_csv(path, sep="\t", header=None, names=["label", "message"], encoding="utf-8", on_bad_lines="skip")
    df = df.dropna(subset=["label", "message"])
    df["label"] = df["label"].astype(str).str.strip().str.lower()
    df["message"] = df["message"].astype(str)
    df = df[df["label"].isin(["ham", "spam"])].drop_duplicates().reset_index(drop=True)
    if df.empty:
        raise ValueError("No valid rows found. Expected tab-separated label/message columns.")
    return df

def clean_text(text):
    text = text.lower()
    text = re.sub(r"https?://\S+|www\.\S+", " URL ", text)
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    tokens = [word for word in text.split() if word not in STOPWORDS and not word.isdigit()]
    return " ".join(tokens)

def main():
    df = load_dataset(sys.argv[1] if len(sys.argv) > 1 else None)
    df["clean_message"] = df["message"].map(clean_text)
    df.to_csv(DATA_DIR / "cleaned_sms.csv", index=False)
    counts = df["label"].value_counts()
    print("\n=== Day 54: SMS Spam Data Exploration ===")
    print(f"Total messages: {len(df)}")
    print(f"Ham (not spam): {counts.get('ham', 0)}")
    print(f"Spam: {counts.get('spam', 0)}")
    print(f"Duplicate rows removed during loading: duplicates are excluded")
    print("\nExamples of cleaned text:")
    for _, row in df.head(5).iterrows():
        print(f"[{row['label']}] {row['clean_message']}")
    print("\nTop words in spam messages:")
    words = " ".join(df.loc[df.label == "spam", "clean_message"]).split()
    print(pd.Series(words).value_counts().head(10).to_string() if words else "No spam messages available.")
    print("\nObservations:")
    print("- Ham messages are usually ordinary personal or service conversations.")
    print("- Spam often contains promotional terms, prize/claim language, links, or urgency.")
    print("- These are patterns, not rules: legitimate messages can contain similar words.")
    print("- Review the ham/spam counts; real SMS datasets are commonly imbalanced.")
    print(f"\nSaved cleaned dataset to: {DATA_DIR / 'cleaned_sms.csv'}")
    if len(df) < 100:
        print("NOTE: This is a small offline sample; use the full UCI dataset for meaningful analysis.")

if __name__ == "__main__":
    main()
