# Day 55 — The Smart Spam Detector, Part 2

## Goal
Convert SMS text into numeric features, train a machine-learning classifier, evaluate it, and predict custom messages.

## Setup
```bash
python -m pip install pandas scikit-learn
python spam_classifier.py
```
The script downloads the full UCI SMS Spam Collection when internet is available. Otherwise, it uses the bundled sample for a basic smoke test. For meaningful evaluation, place the full extracted `SMSSpamCollection` file in `data/` or run with internet access.

## Model pipeline
1. Clean and normalize the message text.
2. Split the data into 80% training and 20% test sets, using stratification.
3. Convert text to TF-IDF vectors, including unigrams and bigrams.
4. Train a Multinomial Naive Bayes classifier.
5. Report accuracy, per-class precision/recall/F1, and confusion matrix.
6. Predict labels for four custom example messages.

## Evaluation
The script prints actual metrics from the dataset it loads. Do not copy a fixed accuracy number into a report: results can vary with dataset contents and split. The small bundled sample is for verifying that the program runs, not for claiming model quality.

## Limitations
- Text patterns can change over time and models can make false positives/negatives.
- Accuracy alone can be misleading if the classes are imbalanced; inspect spam precision and recall.
- This demo is educational and should not be used as a production spam filter without broader testing.
