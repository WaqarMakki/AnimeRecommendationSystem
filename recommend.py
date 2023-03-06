import pickle
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity
from pyunpack import Archive

def recommend(anime_name):
    try:
        index = data.index[data['Title'] == anime_name][0]
    except:
        print("Anime Doesn't Exist")

    sim = cosine_similarity(vectors, vectors[index].reshape((1, -1)))

    data['Similarity'] = sim

    data.sort_values(by=['Similarity'], ascending=False, inplace=True)

    recommendations = data['Title'][1:6].values

    
    return recommendations

src = r"C:\Users\Waqar Makki\OneDrive\Desktop\ARS\AnimeRecommendationSystem\vectors.zip"
dest = r'C:\Users\Waqar Makki\PycharmProjects\AnimeRecommendationSystem'
Archive(src).extractall(dest)

data = pickle.load(open('/home/waqarmakki/Desktop/ars/data.pkl','rb'))
vectors = pickle.load(open('/home/waqarmakki/Desktop/ars/vectors.pkl','rb'))

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
