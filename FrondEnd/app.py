import streamlit as st
import pickle
import pandas as pd

similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(article):
    article_index = articles[articles['article'] == article].index[0]
    distances = similarity[article_index]
    article_list = sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:11]

    recommended_articles=[]


    for i in article_list:
        recommended_articles.append(articles.iloc[i[0]].article)

    return recommended_articles


article_list= pickle.load(open('scholar.pkl', 'rb'))
articles= pd.DataFrame(article_list)
article_list= article_list['article'].values

st.title('Scholarly Article Recommender')

selected_article_name = st.selectbox('Article Name', article_list)
if st.button('Recommend'):
    recommendations = recommend(selected_article_name)
    for i in recommendations:
        st.write(i)
