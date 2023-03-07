import pickle
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity
import bz2
import _pickle as cPickle

def recommend(anime_name):
#     try:
#         index = data.index[data['Title'] == anime_name][0]
#     except:
#         print("Anime Doesn't Exist")

    index = data.index[data['Title'] == anime_name][0]

    sim = cosine_similarity(vectors, vectors[index].reshape((1, -1)))

    data['Similarity'] = sim

    data.sort_values(by=['Similarity'], ascending=False, inplace=True)

    recommendations = data['Title'][1:6].values
    
    return recommendations


def decompress_pickle(file):
    vec = bz2.BZ2File(file, 'rb')
    vec = cPickle.load(vec)
    return vec


data = pickle.load(open('https://github.com/WaqarMakki/AnimeRecommendationSystem/blob/main/data.pkl','rb'))
# vectors = pickle.load(open('vectors.pkl','rb'))
vectors = decompress_pickle('https://github.com/WaqarMakki/AnimeRecommendationSystem/blob/main/vectors.pbz2')

st.header('Anime Recommender System')

anime_list = data['Title'].values
selected_anime = st.selectbox(
    "Type or select a movie from the dropdown",
    anime_list
)

if st.button('Show Recommendation'):
    recommended_anime_names = recommend(selected_anime)
    col1, col2, col3, col4, col5 = st.columns(5, gap='large')
    
    with col1:
        title = recommended_anime_names[0]
        idx = data[data['Title'] == title].index[0]
        st.image(data['Image_Source'][idx], width=150, caption=title)
    with col2:
        title = recommended_anime_names[1]
        idx = data[data['Title'] == title].index[0]
        st.image(data['Image_Source'][idx], width=150, caption=title)
    with col3:
        title = recommended_anime_names[2]
        idx = data[data['Title'] == title].index[0]
        st.image(data['Image_Source'][idx], width=150, caption=title)
    with col4:
        title = recommended_anime_names[3]
        idx = data[data['Title'] == title].index[0]
        st.image(data['Image_Source'][idx], width=150, caption=title)
    with col5:
        title = recommended_anime_names[4]
        idx = data[data['Title'] == title].index[0]
        st.image(data['Image_Source'][idx], width=150, caption=title)
