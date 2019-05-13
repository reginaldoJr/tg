import csv
from itertools import islice
from imdb import IMDb,IMDbError
import pandas as pd
import numpy as np

data1 = pd.read_csv('teste.csv')
data2 = pd.read_csv('./dt_small/movies.csv')
df1 = data1[['movieId','synopsis']]
df2 = data2[['movieId','title']]
dfm = pd.merge(df1, df2, left_on='movieId', right_on='movieId')
print(dfm.head())
exit()

# create an instance of the IMDb class
ia = IMDb()

data = []
with open('./dt_small/movies.csv', mode='r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		with open('teste.csv', mode='w') as csv_file_write:
			fieldnames = ['movieID', 'synopsis']
			writer = csv.DictWriter(csv_file_write, fieldnames=fieldnames)
			writer.writeheader()
			for row in csv_reader:
				print(f"{row['movieId']} : {row['title']}")
				try:
					movie = ia.search_movie(row["title"])
					mvId = movie[0].movieID
					movie = ia.get_movie(mvId)
					if 'synopsis' in movie.keys():
						synopsis = movie['synopsis'][0]
					elif 'plot outline' in movie.keys():
						synopsis = movie['plot outline']
					writer.writerow({'movieID':row['movieId'],'synopsis':synopsis})
				except Exception as e:
					print("Error:",e)

#Descomentar para parar
#				if row['movieId'] == '5':
#					break
