import pandas as pd
import numpy as np
from imdb import IMDb
from tqdm.auto import tqdm

tqdm.pandas()
ia = IMDb()

#data = ia.get_movie('114709')
#print(type(data.get('plot')))

movies = pd.read_csv("./movies.csv")
links = pd.read_csv("./links.csv")
#movies.head(5)

movies = pd.merge(movies,links, on='movieId')

movies['year'] = 0
movies['rating'] = 0
#movies['plot'] = [[]]
movies['synopsis'] = ''
movies['description'] = ''
movies['text'] = ''


for index, row in tqdm(movies.iterrows(), total=movies.shape[0]):
    m = ia.get_movie(movies.loc[index,'imdbId'])
    movies.loc[index,'year'] = m.get('year')
    movies.loc[index,'rating'] = m.get('rating')
    movies.loc[index,'plot'] = m.get('plot')
    movies.loc[index,'description'] = m.get('plot outline')
    movies.loc[index,'synopsis'] = m.get('synopsis')
    #movies.loc[index,'text'] = movies.loc[index,'description']+''+movies.loc[index,'synopsis']
movies.to_csv("./ResultadoCompleto.csv")
