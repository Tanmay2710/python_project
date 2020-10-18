import streamlit as st
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
 
x = df.iloc[:,0].values # Review column as input
y = df.iloc[:,1].values # Sentiment column as output
st.title("Sentiment Analysis")
st.subheader('TFIFD Vectorizer')
st.write('')
 
text_model = Pipeline([('tfidf',TfidfVectorizer()),('model',MultinomialNB())])
text_model.fit(x,y)
message = st.text_area("Enter Text","Type Here ..")
op = text_model.predict([message])
if st.button("Predict"):
  st.title(op)
