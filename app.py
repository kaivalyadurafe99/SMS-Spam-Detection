import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import nltk
nltk.download('punkt')
nltk.download('stopwords')

ps=PorterStemmer()

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
        if i not in stopwords.words("english") and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


cv=pickle.load(open("vectorizor.pkl","rb"))
model=pickle.load(open("model.pkl","rb"))

st.title("SMS Spam Detection")

sms=st.text_area("Enter the SMS")
if st.button("Detect Spam or Not"):

    transform_sms=transform_text(sms)
    vector_input=cv.transform([transform_sms])

    result=model.predict(vector_input)[0]

    if result==1:
        st.header("SMS is Spam")
    else:
        st.header("SMS is Not Spam")