import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)


stop_words = set(stopwords.words('english'))


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stop_words and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# st.title('Email/SMS Spam Classifier')
#
# input_sms = st.text_area('Enter the Message')
# if st.button('Predict'):
#
#     # 1 . preprocessing
#     transformed_sms = transform_text(input_sms)
#
#     # 2. vectorize
#     vector_input = tfidf.transform([transformed_sms])
#
#     # 3. Predict
#     result = model.predict(vector_input)[0]
#
#     # 4. Result
#     if result == 1:
#         st.header('Spam Detected')
#     else:
#         st.header('Not Spam Detected')


st.set_page_config(
    page_title="Spam Classifier",
    page_icon="📩"
)

st.title("📩 Email / SMS Spam Classifier")
st.write("Enter a message below and click **Predict**.")

input_sms = st.text_area("Enter the Message")

if st.button("Predict"):

    if input_sms.strip() == "":
        st.warning("Please enter a message.")
    else:
        # Preprocess
        transformed_sms = transform_text(input_sms)

        # Vectorize
        vector_input = tfidf.transform([transformed_sms])

        # Predict
        prediction = model.predict(vector_input)[0]

        # Probability (works for Naive Bayes)
        if hasattr(model, "predict_proba"):
            probability = model.predict_proba(vector_input)[0]

        st.divider()

        if prediction == 1:
            st.error("🚨 Spam Detected")
        else:
            st.success("✅ Not Spam")