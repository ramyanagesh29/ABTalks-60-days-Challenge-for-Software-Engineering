import streamlit as st
from spam_model import train_model, predict_message

st.set_page_config(page_title="Smart Spam Detector — Day 57", page_icon="⚡", layout="centered")
st.title("⚡ Smart Spam Detector — Optimized")
st.caption("Day 57 — Faster model reuse, confidence, and better feedback")
st.info("Demo only: the included dataset is small and is not suitable for production security decisions.")

@st.cache_resource(show_spinner="Training model once...")
def get_model():
    return train_model()

model = get_model()
message = st.text_area("Message to analyze", max_chars=5000, height=140,
                       placeholder="Type or paste a message here...")
if st.button("Analyze message", type="primary", use_container_width=True):
    if not message.strip():
        st.warning("Enter a non-empty message before analyzing.")
    elif len(message) > 5000:
        st.error("Message is too long. Use 5,000 characters or fewer.")
    else:
        result = predict_message(model, message)
        if result["label"] == "spam":
            st.error("🚨 Likely SPAM")
        else:
            st.success("✅ Likely NOT SPAM")
        st.metric("Prediction confidence", f"{result['confidence']:.1%}")
        st.caption("Confidence is not a guarantee of correctness.")
with st.expander("Optimization details"):
    st.markdown("""
    - `st.cache_resource` reuses the model instead of retraining it on every Streamlit rerun.
    - TF-IDF and Naive Bayes are kept in one scikit-learn pipeline.
    - Empty input is validated before prediction.
    - Confidence and limitations are shown clearly.
    """)
