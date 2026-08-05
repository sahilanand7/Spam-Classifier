# Email-Spam-Classifier

A Machine Learning web application that classifies Email and SMS messages as **Spam** or **Not Spam** using **Natural Language Processing (NLP)** and the **Multinomial Naive Bayes** algorithm. The application is built with **Streamlit** and provides an interactive interface for real-time spam detection.

## Features

- Classifies messages as **Spam** or **Not Spam**
- Text preprocessing using NLTK
- TF-IDF Vectorization
- Multinomial Naive Bayes Classifier
- Simple and interactive Streamlit web interface
- Displays prediction results instantly


## Technologies Used

- Python
- Streamlit
- Scikit-learn
- NLTK
- Pandas
- NumPy
- Pickle

## 📂 Dataset

This project uses the **SMS Spam Collection Dataset**, a publicly available dataset containing thousands of labeled SMS messages categorized as either **Spam** or **Ham (Not Spam)**.

## Text Preprocessing

The following preprocessing steps are applied before prediction:

- Convert text to lowercase
- Tokenize the text
- Remove non-alphanumeric characters
- Remove English stopwords
- Apply Porter Stemming
- Convert text into numerical features using TF-IDF Vectorization

## Machine Learning Model

**Algorithm Used:** Multinomial Naive Bayes

### Model Performance

- **Accuracy:** 97%
- **Precision:** 1.00

---

## 📁 Project Structure

```
Spam-Classifier/
│── app.py
│── Spam_Classifier.ipynb
│── model.pkl
│── vectorizer.pkl
│── requirements.txt
│── README.md
```


## Author

**Sahil Anand**

- GitHub: https://github.com/sahilanand7
- B.Tech (Data Science & AI)

---

## ⭐ If you found this project useful, consider giving it a star!
