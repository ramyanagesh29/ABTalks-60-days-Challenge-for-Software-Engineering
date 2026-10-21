# Day 57 — Spam Detector Performance Optimization

This folder is the optimization stage, separate from Day 56.

## Improvements
- Cached model loading in the Streamlit app.
- One pipeline for TF-IDF and Naive Bayes.
- Prediction confidence and input validation.
- Local benchmark script and performance report.

## Run
```bash
python -m pip install -r requirements.txt
streamlit run app.py
python benchmark.py
python -m unittest discover -s tests -v
```

## Note
The sample dataset is intentionally small. Run the benchmark on your own computer and report actual values; do not invent speedup figures.
