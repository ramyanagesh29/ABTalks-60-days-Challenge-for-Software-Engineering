import streamlit as st
from spam_model import train_model, predict_message

st.set_page_config(page_title="Smart Spam Detector — Day 56", page_icon="🛡️")
st.title("🛡️ Smart Spam Detector")
st.caption("Day 56 — Interactive spam prediction app")
st.info("This is a learning demo trained on a small sample dataset. Do not use it for real-world security decisions.")

@st.cache_resource
def get_model():
    return train_model()

model = get_model()
message = st.text_area("Enter an SMS message", height=140, max_chars=5000,
                       placeholder="Example: Congratulations! Claim your free prize now...")
if st.button("Check message", type="primary", use_container_width=True):
    if not message.strip():
        st.warning("Please enter a message first.")
    else:
        result = predict_message(model, message)
        if result["label"] == "spam":
            st.error("🚨 Prediction: Likely SPAM")
        else:
            st.success("✅ Prediction: Likely NOT SPAM")
        st.metric("Model confidence", f"{result['confidence']:.1%}")
        st.caption("Confidence is a probability estimate, not a guarantee.")
with st.expander("How it works"):
    st.write("TF-IDF converts text into numerical features. Multinomial Naive Bayes predicts spam or ham.")
