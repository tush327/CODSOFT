import pickle as p, streamlit as s, requests as r

def a(x):
    u=f"https://api.themoviedb.org/3/movie/{x}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    d=r.get(u).json()
    p=d.get('poster_path')
    return f"https://image.tmdb.org/t/p/w500/{p}" if p else "https://via.placeholder.com/500x750?text=No+Image"

def b(z):
    i=c[c['title']==z].index[0]
    d=sorted(list(enumerate(e[i])), reverse=True, key=lambda x:x[1])
    n,p=[],[]
    for j in d[1:6]:
        m_id=c.iloc[j[0]].movie_id
        p.append(a(m_id))
        n.append(c.iloc[j[0]].title)
    return n,p

s.header('🎬 Recommender')
c=p.load(open('model/movie_list.pkl','rb'))
e=p.load(open('model/similarity.pkl','rb'))
m=c['title'].values
x=s.selectbox("Pick a movie",m)
if s.button('Go'):
    n,p=b(x)
    y=s.columns(5)
    for i,j in enumerate(y):
        with j:
            s.text(n[i]); s.image(p[i])
