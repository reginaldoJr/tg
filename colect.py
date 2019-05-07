import csv
from itertools import islice
from imdb import IMDb,IMDbError

# create an instance of the IMDb class
ia = IMDb()

# get a movie
movie = ia.search_movie('Grumpier Old Men (1995)')
movie = ia.get_movie(movie[0].movieID)
print(movie.data)


exit()
import csv
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
					synopsis = movie['synopsis'][0]
					writer.writerow({'movieID':row['movieId'],'synopsis':synopsis})
#		    	data.append((row['movieId'],synopsis))
				except Exception as e:
					print("Error:",e)
				if row['movieId'] == '5':
					break
