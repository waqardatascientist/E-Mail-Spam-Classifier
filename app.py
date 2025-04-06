import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
ps= PorterStemmer()
# now we convert all the sentences into lower case
def text_transform(text):
    text=text.lower()
    text=nltk.word_tokenize(text)
    #this will extrect the alpha numeric values like a20 20%
    y=[]
    for i in text:
        if i.isalnum():  #this is shows all numbers in the list
            y.append(i)   #this will append the values in the y
    #return text
    text=y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text=y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    return  ' '.join(y)
model=pickle.load(open('model.pkl','rb'))
vector=pickle.load(open('vector.pkl','rb'))

st.title('Email spam classifier')
input_msg=st.text_input('Enter the Email')
if st.button('Prediction'):
    #preprocess
    processed=text_transform(input_msg)
    #transform the data
    vectorise=vector.transform([processed])
    #predication
    guess=model.predict(vectorise)[0]
    if guess == 0:
        st.write('Not Spam')
    else:
        st.write('Email is Spam')

