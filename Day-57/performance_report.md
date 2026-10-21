# Day 57 — Performance Comparison Report

## Optimizations
- Cached the trained model using `st.cache_resource`.
- Bundled TF-IDF and Multinomial Naive Bayes in one pipeline.
- Added input validation and clearer UI feedback.
- Added a repeatable local benchmark for latency and throughput.

## Measurements
Run `python benchmark.py` and fill in the actual output:
- Python version / computer:
- Messages tested:
- Model training time:
- Average prediction latency:
- Median prediction latency:
- Approximate throughput:

Do not claim a numerical speedup unless you compare an earlier version and this version under the same conditions. This local benchmark is not a server load test. The sample dataset is for demonstration only.
