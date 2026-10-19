# Day 54 — The Smart Spam Detector, Part 1

## Goal
Load SMS messages, clean and preprocess text, remove punctuation/stopwords, and explore differences between spam and non-spam (ham).

## Setup
```bash
python -m pip install pandas
python preprocess_sms.py
```
The script attempts to download the full UCI SMS Spam Collection dataset. If internet access is unavailable, it uses the bundled small sample. For full analysis, download the UCI dataset and place the extracted `SMSSpamCollection` file in `data/`.

## What the script does
- Loads tab-separated `label` and `message` fields.
- Normalizes labels and removes invalid/duplicate rows.
- Lowercases text, replaces URLs with a marker, removes punctuation and common stopwords.
- Saves `data/cleaned_sms.csv` and prints label counts, examples, and frequent spam words.

## Observations
Spam may use urgency, prize/claim language, promotional wording, and links. Ham tends to contain personal or service-related conversation. These are tendencies, not guaranteed rules. Check class counts because spam datasets are often imbalanced.

## Limitations
The bundled sample is only an offline fallback and is too small for reliable conclusions. Use the full UCI dataset for meaningful exploration.
