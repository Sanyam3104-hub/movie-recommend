import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=bb16f0aa2ca178a126d377ecd35e70f5".format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movie=[]
    rec_poster=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommend_movie.append(movies.iloc[i[0]].title)
        rec_poster.append(fetch_poster(movie_id))
    return recommend_movie,rec_poster



movie_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
st.title('MOVIE RECOMMEND SYSTEM')
select_movie_name = st.selectbox(
"SELECT THE MOVIE FOR RECOMMENDATION",
movies['title'].values)
if st.button("Recommend"):
    recommended_movie_names,recommended_movie_posters = recommend(select_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
