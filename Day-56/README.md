# Day 56 — Smart Spam Detector Part 3

## Goal
Build an interactive application that lets a user enter a message and see a live spam prediction.

## Features
- Streamlit UI for custom SMS messages.
- Spam / not-spam prediction.
- Confidence estimate.
- Cached model initialization.
- Input validation.

## Run locally
```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

## Deployment
Push this folder to GitHub. On Streamlit Community Cloud, create a new app, select the repository and set `app.py` as the main file. Deploy and add the actual public URL here only after it works.

## Limitation
The bundled sample dataset is small and only demonstrates the workflow. Use a larger, appropriate dataset and held-out evaluation before relying on model predictions.
